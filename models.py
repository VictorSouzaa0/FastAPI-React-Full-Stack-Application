from tortoise.models import Model
from tortoise import fields

class Class(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100,null=False)

class Instructor(Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=255, null=False)
    age = fields.IntField(null=False)
    
    class_group = fields.ForeignKeyField('models.Class',
    related_name='instructor')

class Students(Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=255, null=False)
    age = fields.IntField(null=False)
    carrer_interest = fields.CharField(max_length=255)

    instructor = fields.ForeignKeyField('models.Instructor',
    related_name='students')

    