from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Instructor(Model):
    id = fields.IntField(pk=True)
    fullname = fields.CharField(max_length=255, null=False)
    age = fields.IntField(default=0)
    classroom = fields.CharField(max_length=100)
    image = fields.CharField(max_length=2048)



class Student(Model):
    id = fields.IntField(pk=True)
    fullname = fields.CharField(max_length=255, null=False)
    age = fields.IntField(default=0)
    carrer_interest = fields.CharField(max_length=255)
    bosch_area = fields.CharField(max_length=255)
    image = fields.CharField(max_length=2048)
    digital_solutions = fields.IntField(default=0)
    aboutme = fields.TextField()

#pydantic_model_creator -  É usado para converter automaticamente os dados tortoise ORM para JSON 


#Student
student_Pydantic = pydantic_model_creator(Student, name="Student")
student_PydanticIn = pydantic_model_creator(Student,name="StudentIn",exclude_readonly=True,exclude="classroom")

#Instructor
instructor_Pydantic = pydantic_model_creator(Instructor, name="Instructor")
instructor_PydanticIn = pydantic_model_creator(Instructor, name="InstructorIn", exclude_readonly=True)
