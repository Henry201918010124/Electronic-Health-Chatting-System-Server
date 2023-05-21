"""
coding:utf-8
file: comments.py
@time: 2023/5/20 10:33
@desc:
"""
from flask import Blueprint, request, jsonify
from hospital.database import Message, Contact, ContactStatus, User
from flask_jwt_extended import current_user, jwt_required
from hospital.extensions import db
from sqlalchemy.sql.expression import or_, and_
from hospital.setting import basedir
import os
IMG_DIR = os.path.join(basedir, 'assets', 'image')
message = Blueprint('message', __name__, url_prefix='/message')


def get_contact_list(user_id):
    subquery = db.session.query(
        db.case([(Message.sender == user_id, Message.receiver)], else_=Message.sender).label('contact_id'),
        db.func.max(Message.id).label('last_message_id')
    ).filter((Message.sender == user_id) | (Message.receiver == user_id)).group_by('contact_id').subquery()

    query = db.session.query(User.id, User.username, User.avatar, Message.content, Message.create_time, Message.type).join(
        subquery, User.id == subquery.c.contact_id
    ).join(Message, Message.id == subquery.c.last_message_id).order_by(Message.id.desc())

    result = query.all()
    # 处理查询结果
    contact_list = []
    for row in result:
        contact = {
            'id': row.id,
            'displayName': row.username,
            'avatar': 'http://127.0.0.1:5000'+row.avatar,
            'lastContent': row.content,
            'lastSendTime': row.create_time,
            'type': row.type
        }
        contact_list.append(contact)

    return contact_list


@message.route('/contact/list')
@jwt_required()
def contact_list():
    result = get_contact_list(current_user.id)
    return jsonify(
        code=200,
        data=result
    )


@message.route('/pay/list')
@jwt_required()
def pay_list():
    contacts = Contact.query.join(User, User.id == Contact.receiver).filter(
        Contact.sender == current_user.id
    ).with_entities(
        Contact.create_time,
        Contact.spend,
        Contact.status,
        User.username,
        User.hospital
    ).all()
    data = []
    for contact in contacts:
        data.append(dict(
            doctor=contact.username,
            status=contact.status.name,
            time=str(contact.create_time),
            spend=contact.spend
        ))
    return jsonify(
        code=200,
        data=data
    )


@message.route('/new/contact', methods=['POST'])
@jwt_required()
def new_contact():
    existed_contact = Contact.query.filter(
        Contact.sender == current_user.id,
        Contact.receiver == request.json.get('to'),
        Contact.status == ContactStatus.doing
    ).first()
    if existed_contact:
        return jsonify(
            code=200,
            msg='Your chat with the doctor is not over, so no charge will be charged this time.'
        )
    doctor = User.query.filter_by(id=request.json.get('to')).first()
    user = User.query.filter_by(id=current_user.id).first()
    if user.balance < doctor.price:
        return jsonify(
            code=403,
            msg='Your balance is insufficient!'
        )
    contact = Contact(
        sender=current_user.id,
        receiver=request.json.get('to'),
        spend=doctor.price
    )
    user.balance = user.balance - doctor.price
    db.session.add(contact)
    db.session.commit()
    return jsonify(
        code=200,
        msg=f'Start consulting the doctor, which costs ￥{int(doctor.price)} this time.'
            f'Your account balance is ￥{int(user.balance)}.'
    )


@message.route('/list')
@jwt_required()
def message_list():
    doctor = User.query.filter_by(id=request.args.get('did')).first()
    messages = Message.query.join(User, User.id == Message.sender).filter(
        or_(
            and_(
                Message.sender == current_user.id,
                Message.receiver == doctor.id
            ),
            and_(
                Message.sender == doctor.id,
                Message.receiver == current_user.id
            )
        )
    ).with_entities(
        User.username,
        User.id,
        Message.content,
        Message.sender,
        Message.receiver,
        User.avatar,
        Message.id.label('mid'),
        Message.create_time,
        Message.type
    ).order_by(Message.create_time).all()
    data = []
    for msg in messages:
        data.append(dict(
            uid=msg.id,
            username=msg.username,
            content=msg.content,
            avatar='http://127.0.0.1:5000' + msg.avatar,
            mid=msg.mid,
            create_time=str(msg.create_time),
            doctor=dict(
                id=msg.id,
                avatar='http://127.0.0.1:5000'+msg.avatar,
                displayName=msg.username
            ),
            type=msg.type
        ))
    return jsonify(
        code=200,
        data=data
    )


@message.route('/new', methods=['POST'])
@jwt_required()
def new():
    message = Message(
        content=request.json.get('content'),
        receiver=request.json.get('to'),
        sender=current_user.id,
        type=request.json.get("type")
    )
    db.session.add(message)
    db.session.commit()
    return jsonify(
        code=200,
        msg='Send message successful!',
        data=dict(mid=message.id, content=message.content)
    )


@message.route('/upload/img', methods=['POST'])
@jwt_required()
def img_upload():
    file = request.files['file']
    filename = file.filename
    img_path = os.path.join(IMG_DIR, filename)
    file.save(img_path)
    return jsonify(
        code=200,
        url=f'http://127.0.0.1:5000/infos/image/{filename}'
    )
