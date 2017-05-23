#! /usr/bin/env python3
# encoding: utf-8
"""
    Homework1.py
Created by PythonStudy on 2017/5/22 下午6:04
Copyright 2017 azhen All rights reserved.
"""


# 学校
class School(object):
    """
    关联教师班级课程的容器
    """
    name = "只是个学校名"

    def __init__(self, address):
        """
        初始化属性
        :param address:地点 
        """
        self.address = address
        self.courses = []
        self.grades = []
        self.teachers = []
        self.students = []

    def create_teacher(self, obj_teacher):
        """
        创建教师
        :param obj_teacher: 老师对象
        """
        print(f"创建老师{obj_teacher.name}")
        self.teachers.append(obj_teacher)

    def create_student(self, obj_student):
        """
        创建学生
        :param obj_student: 学生对象
        """
        print(f"创建学生{obj_student.name}")
        self.students.append(obj_student)

    def create_Greade(self, obj_grade):
        """
        创建课程
        :param obj_grade:课程对象
        :return: 
        """
        print(f" 创建课程{obj_grade.name}")
        self.grades.append(obj_grade)


# 班级
class Grades(School):
    def __init__(self, name, semester, start_date, course, teacher):
        """
        初始化并创建班级实力
        :param name: 班级名
        :param semester: 学期
        :param start_date: 开课时间
        :param course: 课程
        :param teacher: 老师
        """
        self.name = name
        self.semester = semester
        self.start_date = start_date
        self.course = course
        self.teacher = teacher

    def add_student(self, obj_student):
        """
        班级添加学生
        :param obj_student: 
        :return: 
        """
        self.students.append(obj_student)

    def rem_student(self, obj_student):
        """
        删除学生
        :param obj_student: 学生对象 
        :return: 
        """
        self.students.remove(obj_student)

    def inquiry_student(self,*args):
        """
        查询学生成绩
        :return: 
        """
        if not args:
            for obj in self.students:
                print(f"---姓名:{obj.name}---\n---年龄:{obj.age}---\n---性别:{obj.sex}---\n---成绩:{obj.grade}---")
        else:
            for obj in args:
                print(f"---姓名:{obj.name}---\n---年龄:{obj.age}---\n---性别:{obj.sex}---\n---成绩:{obj.grade}---")


# 课程
class Course(object):
    def __init__(self, name, price, outline):
        """
        初始化
        :param name: 名称 
        :param price: 价格
        :param outline: 大纲
        """
        self.name = name
        self.price = price
        self.outline = outline


# 学员
class SchoolMember(object):
    def __init__(self, name, sex, age, coure):
        """
        初始化学员变量
        :param name: 姓名 
        :param sex: 性别
        :param age: 年龄 
        """
        self.name = name
        self.sex = sex
        self.age = age
        self.goure = coure
        self.grade = ""


# 教师
class Teacher(SchoolMember):

    def __init__(self, name, sex, age, coure, grades):
        """
        创建教师
        :param name: 姓名
        :param sex: 
        :param age: 
        :param coure: 
        :param grades: 教授班级
        """
        super(Teacher, self).__init__(name, sex, age, coure)
        self.grades = grades


# 学生
class Students(SchoolMember):
    def __init__(self, name, sex, age, coure):
        """
        学生
        :param name:  
        :param sex: 
        :param age: 
        :param coure: 
        """
        super(Students, self).__init__(name, sex, age, coure)
        self.__tuition_fee = ""

    def pay_tuition_fee(self, tuition_fee):
        """
        交学费
        :param tuition_fee: 
        :return: 
        """
        self.__tuition_fee = tuition_fee

    def isPay(self):
        """
        判断是否已经交费
        :return: 
        """
        if self.__tuition_fee:
            return True
        else:
            return False


sch_bj = School("北京")
sch_sh = School("上海")

print(School.__doc__)