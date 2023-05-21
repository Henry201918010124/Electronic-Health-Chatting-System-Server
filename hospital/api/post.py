"""
coding:utf-8
file: post.py
@time: 2023/4/9 23:46
@desc:
"""
from flask import request, jsonify, Blueprint
from hospital.database import Post, User
from flask_jwt_extended import jwt_required, current_user
from hospital.extensions import db

post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route('/detail/<int:pid>')
def detail(pid):
    post = Post.query.join(User, User.id == Post.user_id).filter(Post.id == pid).with_entities(
        Post.title,
        Post.content,
        Post.create_time,
        User.username,
        User.avatar
    ).first()
    return jsonify(
        code=200,
        data=dict(
            post=dict(title=post.title, content=post.content, ctime=str(post.create_time)),
            user=dict(username=post.username, avatar='http://127.0.0.1:5000' + post.avatar)
        )
    )


@post_bp.route('/list')
def post_list():
    posts = Post.query.join(User, User.id == Post.user_id).with_entities(
        User.username,
        User.avatar,
        Post.title,
        Post.content,
        Post.create_time,
        Post.id
    ).all()
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


@post_bp.route('/new', methods=['POST'])
@jwt_required()
def new():
    print(request.json)
    title = request.json.get('title')
    did = request.json.get('did')
    content = request.json.get('content')
    post = Post(
        title=title,
        content=content,
        user_id=current_user.id,
        section_id=did
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(
        code=200,
        msg='Create article successful!'
    )
