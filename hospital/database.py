"""
coding:utf-8
file: database.py
@time: 2022/12/15 20:49
@desc:
"""
import enum

from hospital.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from hospital.datas import DEPARTMENTS, HOSPITAL_LIST, DOCTOR_POSITION


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True, comment='username', index=True)
    password = db.Column(db.String(512), nullable=False, comment='password')
    phone = db.Column(db.String(64), nullable=False, unique=True, comment='phone', index=True)
    avatar = db.Column(db.String(64), nullable=False, default='/infos/avatar/male.png', comment='avatar')
    role_id = db.Column(db.Integer, nullable=False, default='user', comment='role')
    email = db.Column(db.String(64), nullable=False, unique=True, comment='email', index=True)
    section_id = db.Column(db.Integer, default=0, comment='department id')
    gender = db.Column(db.String(64), nullable=False, default='male')
    age = db.Column(db.Integer, nullable=False, default=18)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    description = db.Column(db.Text, default='')
    hospital = db.Column(db.Integer, nullable=False, default=0, comment='hospital')
    position = db.Column(db.String(128), nullable=False, default='doctor', comment='position')
    price = db.Column(db.Float, nullable=False, default=0.0, comment='price')
    balance = db.Column(db.Float, nullable=False, default=5000, comment='balance')

    def __repr__(self):
        return f'User: {self.username}'

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    @staticmethod
    def random_doctor():
        from faker import Faker
        import random
        fake = Faker()
        hospital = [h.id for h in Hospital.query.all()]
        section_id = [s.id for s in Section.query.all()]
        role = Role.query.filter_by(name='doctor').first()
        for i in range(100):
            username = random.choice([fake.first_name(), fake.last_name()])
            if User.query.filter_by(username=username).first():
                continue
            gender = random.choice(['male', 'female'])
            user = User()
            user.username = username
            user.gender = gender
            user.age = random.randint(28, 60)
            user.phone = fake.phone_number()
            user.email = fake.email()
            user.hospital = random.choice(hospital)
            user.section_id = random.choice(section_id)
            user.position = random.choice(DOCTOR_POSITION)
            user.price = random.randint(49, 499)
            user.description = fake.text()
            user.set_password('12345678')
            user.role_id = role.id
            db.session.add(user)
            if gender == 'male':
                avatar = '/infos/avatar/doctor-male.png'
            else:
                avatar = '/infos/avatar/doctor-female.png'
            user.avatar = avatar
            print(f'{i + 1}', user)
            db.session.commit()


class Section(db.Model):
    __tablename__ = 't_section'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True, comment='section name', index=True)
    description = db.Column(db.Text, nullable=False, default='')

    def __repr__(self):
        return f'Section: {self.name}'

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def init_data():
        for department in DEPARTMENTS:
            section = Section.query.filter_by(name=department[0]).first()
            if not section:
                section = Section(name=department[0], description=department[1])
                db.session.add(section)
        db.session.commit()


class Hospital(db.Model):
    __tablename__ = 't_hospital'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False, unique=True, comment='hospital name', index=True)
    level = db.Column(db.String(64), nullable=False, default='Level III A', comment='hospital level')
    description = db.Column(db.Text, nullable=False, default='')
    address = db.Column(db.String(512), nullable=False, default='')
    phone = db.Column(db.String(64), nullable=False, default='')

    def __repr__(self):
        return f'Hospital: {self.name}'

    @staticmethod
    def init_data():
        for hospital in HOSPITAL_LIST:
            hos = Hospital.query.filter_by(name=hospital[0]).first()
            if not hos:
                hos = Hospital(name=hospital[0], level=hospital[1])
                db.session.add(hos)
        db.session.commit()


class Role(db.Model):
    __tablename__ = 't_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True, comment='role name', index=True)
    description = db.Column(db.Text, nullable=False, default='')

    def __repr__(self):
        return f'Role: {self.name}'

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def init_data():
        roles = [
            Role('admin', 'admin'),
            Role('doctor', 'doctor'),
            Role('user', 'user'),
        ]
        for role in roles:
            db.session.add(role)
        db.session.commit()


class Post(db.Model):
    __tablename__ = 't_post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, comment='title')
    content = db.Column(db.Text, nullable=False, comment='content')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    user_id = db.Column(db.Integer, nullable=False, comment='user id')
    section_id = db.Column(db.Integer, nullable=False, comment='section id')


class Comment(db.Model):
    __tablename__ = 't_comment'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False, comment='content')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    user_id = db.Column(db.Integer, nullable=False, comment='user id')
    post_id = db.Column(db.Integer, nullable=False, comment='post id')
    parent_id = db.Column(db.Integer, nullable=False, comment='parent id')

    def __repr__(self):
        return f'Comment: {self.content}'

    def __init__(self, content, user_id, post_id, parent_id=0):
        self.content = content
        self.user_id = user_id
        self.post_id = post_id
        self.parent_id = parent_id

    @staticmethod
    def init_data():
        from faker import Faker
        import random
        fake = Faker()
        users = User.query.all()
        posts = Post.query.all()
        for i in range(100):
            user = random.choice(users)
            post = random.choice(posts)
            content = fake.text()
            comment = Comment(content=content, user_id=user.id, post_id=post.id)
            db.session.add(comment)
            print(f'{i + 1}', comment)
            db.session.commit()


class Message(db.Model):
    __tablename__ = 't_message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False, comment='content')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    sender = db.Column(db.Integer, nullable=False, comment='user id')
    receiver = db.Column(db.Integer, nullable=False, comment='user id')
    is_read = db.Column(db.Boolean, nullable=False, default=False, comment='is read')
    type = db.Column(db.String(16), default='text', comment='message type: text or image')


class ContactStatus(enum.Enum):
    doing = 1
    finished = 2


class Contact(db.Model):
    __tablename__ = 't_contact'

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    sender = db.Column(db.Integer, nullable=False, comment='sender user id')
    receiver = db.Column(db.Integer, nullable=False, comment='receiver user id')
    spend = db.Column(db.Integer, default=0, comment='contact spend')
    status = db.Column(db.Enum(ContactStatus), default=ContactStatus.doing, nullable=False, comment='contact status')
