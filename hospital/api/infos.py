"""
coding:utf-8
file: infos.py
@time: 2022/12/16 21:44
@desc:
"""
from flask import jsonify, Blueprint, request, send_from_directory, current_app
from hospital.database import User, Role, Section, Hospital

infos = Blueprint('infos', __name__, url_prefix='/infos')


@infos.route('/roles')
def role_info():
    roles = Role.query.filter(Role.name != 'admin').all()
    return jsonify(
        code=200,
        role=[{'name': role.name, 'id': role.id} for role in roles]
    )


@infos.route('/sections')
def section_info():
    sections = Section.query.all()
    return jsonify(
        code=200,
        section=[{'name': section.name, 'id': section.id} for section in sections]
    )


@infos.route('/avatar/<filename>')
def avatar(filename):
    return send_from_directory(current_app.config['AVATARS_SAVE_PATH'], filename)


@infos.route('/image/<filename>')
def image(filename):
    from hospital.setting import basedir
    import os
    return send_from_directory(os.path.join(basedir, 'assets', 'image'), filename)


@infos.route('/all/department')
def all_department():
    sections = Section.query.all()
    return jsonify(
        code=200,
        departments=[{'name': section.name, 'id': section.id} for section in sections]
    )


@infos.route('/department/detail')
def detail_department():
    import time
    time.sleep(1)
    section_id = request.args.get('did')
    section = Section.query.get_or_404(section_id)
    users = User.query.join(
        Hospital, Hospital.id == User.hospital
    ).join(
        Section, Section.id == User.section_id
    ).with_entities(
        User.username,
        User.id,
        User.avatar,
        User.description,
        User.position,
        User.price,
        Hospital.name.label('hospital'),
        Hospital.level,
        Section.name.label('section')
    ).filter(User.section_id == section_id).all()
    doctors = []
    for user in users:
        doctors.append({
            'id': user.id,
            'name': user.username,
            'avatar': 'http://127.0.0.1:5000' + user.avatar,
            'position': user.position,
            'desc': user.description,
            'hospital': user.hospital,
            'section': user.section,
            'level': user.level,
            'price': user.price,
            'description': user.description
        })
    return jsonify(
        code=200,
        name=section.name,
        id=section.id,
        description=section.description,
        doctors=doctors
    )


@infos.route('/user/<int:uid>')
def user_info(uid):
    user = User.query.join(Hospital, Hospital.id == User.hospital).filter(User.id == uid).with_entities(
        User.username,
        User.avatar,
        Hospital.name,
        User.id.label('id')
    ).first()
    return jsonify(
        code=200,
        data=dict(
            username=user.username,
            avatar='http://127.0.0.1:5000' + user.avatar,
            hospital=user.name,
            id=user.id
        )
    )
