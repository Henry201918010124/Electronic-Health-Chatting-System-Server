"""
coding:utf-8
file: search.py
@time: 2023/5/21 10:41
@desc:
"""
from flask import Blueprint, request, jsonify
from hospital.database import User, Post, Hospital, Section
from flask_jwt_extended import current_user, jwt_required
from hospital.extensions import db
from sqlalchemy.sql.expression import or_, and_
from hospital.setting import basedir
import os
search_bp = Blueprint('search', __name__, url_prefix='/search')


@search_bp.route('/article')
def article():
    keyword = request.args.get('keyword')
    posts = Post.query.join(User, User.id == Post.user_id).with_entities(
        User.username,
        User.avatar,
        Post.title,
        Post.content,
        Post.create_time,
        Post.id
    ).filter(Post.title.like(f'%{keyword}%')).all()
    data = []
    for post in posts:
        data.append(dict(
            title=post.title,
            id=post.id,
            username=post.username,
            avatar='http://127.0.0.1:5000' + post.avatar,
            content=post.content,
            ctime=str(post.create_time)
        ))
    return jsonify(
        code=200,
        msg='Successful!',
        data=data
    )


@search_bp.route('/doctor')
def doctor():
    keyword = request.args.get('keyword')
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
    ).filter(User.username.like(f'%{keyword}%')).all()
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
        doctors=doctors
    )
