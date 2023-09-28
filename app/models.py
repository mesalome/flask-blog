from app import db
from datetime import datetime

# Associative table for many-to-many relationship between "users" and "groups"
user_group_association = db.Table(
    "user_group_association",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"))
)

# Associative table for many-to-many relationship between "users" and "favourite_posts"
favourite_posts_association = db.Table(
    "favourite_posts_association",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id")),
)


# Model for table "users"
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # Establishing one-to-many relationship with "posts"
    posts = db.relationship("Post", back_populates="user")

    # Establishing many-to-many relationship with "groups"
    groups = db.relationship("Group",
                             secondary=user_group_association,
                             back_populates="users")

    # Establishing many-to-many relationship with "posts" for "favourite_posts"
    favourite_posts = db.relationship("Post",
                                       secondary=favourite_posts_association,
                                       back_populates="users")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    # Establishing many-to-many relationship with "users"
    users = db.relationship("User",
                            secondary=user_group_association,
                            back_populates="groups")
    
    def __repr__(self):
        return f"<Group(id={self.id}, name='{self.name}')>"
    

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    picture = db.Column(db.LargeBinary)

    # Establishing many-to-one relationship with "users"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="posts")

    # Establishing many-to-many relationship with "users" for "favourite posts"
    users = db.relationship("User",
                            secondary=favourite_posts_association,
                            back_populates="favourite_posts")
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"