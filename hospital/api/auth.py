"""
coding:utf-8
file: auth.py
@time: 2022/12/15 20:12
@desc:
"""
from flask import request, Blueprint, redirect, url_for, flash, current_app, jsonify
from flask_jwt_extended import (create_access_token, current_user, jwt_required, get_jwt_identity, create_refresh_token,
                                set_access_cookies, unset_access_cookies)
from hospital.database import User, Section, Role
from hospital.extensions import jwt, db
from sqlalchemy.sql import or_
import datetime

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    username = request.json.get('username')
    password = str(request.json.get('password'))
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify(
            code=404,
            msg='User not exist！',
            success=False
        )

    if not user.check_password(password):
        return jsonify(
            code=400,
            msg='Username or password error！',
            success=False
        )

    access_token = create_access_token(identity=user, additional_claims={'admin': True})
    response = jsonify(
        code=200,
        msg='Login Successful！',
        access_token=access_token,
        user=dict(
            userid=user.id,
            username=user.username,
            timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            success=True,
            avatar='http://127.0.0.1:5000' + user.avatar,
            balance=user.balance,
            email=user.email,
            phone=user.phone,
            age=user.age,
        )
    )
    set_access_cookies(response, access_token)
    return response


@auth.route('/register', methods=['GET', 'POST'])
def register():
    username = request.json.get('username')
    password = str(request.json.get('password'))
    section_id = request.json.get('section')
    role_id = request.json.get('role')
    phone = request.json.get('phone')
    email = request.json.get('email')
    gender = request.json.get('gender')
    age = request.json.get('age') or 0
    hospital = request.json.get('hospital') or 0
    position = request.json.get('position') or ''
    section = 0
    if section_id:
        section = Section.query.filter_by(id=section_id).first()
        if not section:
            return jsonify(
                code=404,
                msg='Section not exist！',
                success=False
            )

    role = Role.query.filter_by(name=role_id).first()
    if User.query.filter(or_(User.username == username,
                             User.email == email,
                             User.phone == phone)).first():
        return jsonify(
            code=400,
            msg='User already exist！',
            success=False
        )

    if not role:
        return jsonify(
            code=404,
            msg='Role not exist！',
            success=False
        )

    if role.name == 'admin':
        return jsonify(
            code=403,
            msg='Permission denied！',
            success=False
        )
    if gender == 'male':
        if role.name == 'user':
            avatar = '/infos/avatar/male.png'
        else:
            avatar = '/infos/avatar/doctor-male.png'
    else:
        if role.name == 'user':
            avatar = '/infos/avatar/female.png'
        else:
            avatar = '/infos/avatar/doctor-female.png'

    user = User(
        username=username,
        section_id=section.id if section else section,
        role_id=role.id,
        phone=phone,
        email=email,
        password=password,
        gender=gender,
        age=age,
        hospital=hospital,
        position=position,
        avatar=avatar
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify(
        code=200,
        msg='Register Successful！',
        userid=user.id,
        username=user.username,
        timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        success=True
    )


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(id=identity).one_or_none()


@auth.route('/userInfo')
@jwt_required()
def user_info():
    return jsonify(
        id=current_user.id,
        username=current_user.username,
        nickname=current_user.nickname,
        avatar=conf.get('frontend_url') + current_user.avatar,
        code=200
    )


@auth.route('/logout')
@jwt_required()
def logout():
    response = jsonify(
        code=200,
        msg='Logout Successful！'
    )
    unset_access_cookies(response)
    return response


@auth.route('/roles')
def role_info():
    roles = Role.query.filter(Role.name != 'admin').all()
    return jsonify(
        code=200,
        role=[{'name': role.name, 'id': role.id} for role in roles]
    )
