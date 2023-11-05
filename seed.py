from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade

# Підключення до бази даних
engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

groups = [Group(name=fake.word()) for _ in range(3)]

teachers = [Teacher(name=fake.name()) for _ in range(3)]

subjects = [Subject(name=fake.word(), teacher=teachers[i % 3]) for i in range(5)]

students = [Student(name=fake.name(), group=groups[i % 3]) for i in range(30)]

for student in students:
    for subject in subjects:
        session.add(Grade(student=student, subject=subject, score=fake.random_int(1, 100)))

session.commit()
