#! /usr/bin/env python3
# encoding: utf-8
"""
    Homework1.py
Created by PythonStudy on 2017/5/22 下午6:04
Copyright 2017 azhen All rights reserved.
"""


class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.courses = []
        self.grades = []
        self.teachers = []
        self.students = []


# 班级
class Grades(School):
    pass


# 课程
class Course(object):
    def __init__(self, cycle, price):
        self.cycle = cycle
        self.price = price


# 学员
class SchoolMember(object):
    pass


# 教师
class Teacher(SchoolMember):
    pass


# 学生
class Students(SchoolMember):
    pass

