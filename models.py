from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Classroom(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100,null=False)

class Instructor(Model):
    id = fields.IntField(pk=True)
    fullname = fields.CharField(max_length=255, null=False)
    age = fields.IntField(null=False)
    classgroup = fields.ForeignKeyField('models.Classroom',
    related_name='instructor')

class Student(Model):
    id = fields.IntField(pk=True)
    fullname = fields.CharField(max_length=255, null=False)
    age = fields.IntField(null=False)
    carrer_interest = fields.CharField(max_length=255)

    instructor = fields.ForeignKeyField('models.Instructor',
    related_name='students')


#pydantic_model_creator -  É usado para converter automaticamente os dados tortoise ORM para JSON 


#Student
student_Pydantic = pydantic_model_creator(Student, name="Student")
student_PydanticIn = pydantic_model_creator(Student,name="StudentIn",exclude_readonly=True)

#Instructor
instructor_Pydantic = pydantic_model_creator(Instructor, name="Instructor")
instructor_PydanticIn = pydantic_model_creator(Instructor, name="InstructorIn", exclude_readonly=True)


#Class
class_Pydantic = pydantic_model_creator(Classroom, name="Class")
class_PydanticIn = pydantic_model_creator(Classroom, name="ClassIn", exclude_readonly=True)