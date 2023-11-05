from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Student, Subject, Grade, Teacher, Group

engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    students = session.query(Student).all()
    top_students = sorted(students, key=lambda student: student.average_grade, reverse=True)[:5]
    return top_students

def select_2(subject_name):
    subject = session.query(Subject).filter(Subject.name == subject_name).first()
    best_student = session.query(Student).join(Grade).filter(Grade.subject == subject).\
        group_by(Student).order_by(func.avg(Grade.score).desc()).first()
    return best_student

def select_3(subject_name):
    subject = session.query(Subject).filter(Subject.name == subject_name).first()
    avg_scores = session.query(func.avg(Grade.score)).filter(Grade.subject == subject).group_by(Student.group_id)
    return avg_scores.all()

def select_4():
    avg_score = session.query(func.avg(Grade.score)).scalar()
    return avg_score

def select_5(teacher_name):
    teacher = session.query(Teacher).filter(Teacher.name == teacher_name).first()
    subjects_taught = [subject.name for subject in teacher.subjects]
    return subjects_taught

def select_6(group_name):
    group = session.query(Group).filter(Group.name == group_name).first()
    students_in_group = [student.name for student in group.students]
    return students_in_group

def select_7(group_name, subject_name):
    group = session.query(Group).filter(Group.name == group_name).first()
    subject = session.query(Subject).filter(Subject.name == subject_name).first()
    grades = session.query(Grade).filter(Grade.student.group == group, Grade.subject == subject)
    return [(grade.student.name, grade.score) for grade in grades]

def select_8(teacher_name):
    teacher = session.query(Teacher).filter(Teacher.name == teacher_name).first()
    subjects_taught = [subject.id for subject in teacher.subjects]
    avg_score = session.query(func.avg(Grade.score)).filter(Grade.subject_id.in_(subjects_taught)).scalar()
    return avg_score

def select_9(student_name):
    student = session.query(Student).filter(Student.name == student_name).first()
    courses_attended = [subject.name for grade in student.grades]
    return courses_attended

def select_10(student_name, teacher_name):
    student = session.query(Student).filter(Student.name == student_name).first()
    teacher = session.query(Teacher).filter(Teacher.name == teacher_name).first()
    courses_taught_by_teacher = [subject.name for subject in teacher.subjects]
    courses_attended_by_student = [subject.name for grade in student.grades]
    common_courses = set(courses_taught_by_teacher).intersection(courses_attended_by_student)
    return list(common_courses)
