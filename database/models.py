from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String, nullable=True)
    full_name = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

# ایجاد دیتابیس SQLite
engine = create_engine('sqlite:///bot.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("✅ دیتابیس با موفقیت ساخته شد!")