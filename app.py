from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import student_Pydantic,student_PydanticIn,Student
from models import instructor_Pydantic,instructor_PydanticIn,Instructor
from models import class_Pydantic,class_PydanticIn,Classroom

app = FastAPI()
@app.get('/')
def index():
    return{"Msg":"go to /docs for the API documentation"}


@app.post('/class')
async def add_class(class_info: class_PydanticIn):
    class_obj = await Classroom.create(**class_info.dict(exclude_unset=True))
    response = await class_Pydantic.from_tortoise_orm(class_obj)
    return {"status":"ok","data" :response}

@app.get('/class')
async def get_all_class():
    response = await class_Pydantic.from_queryset(Classroom.all())
    return{"Status": "ok","data": response}

@app.get('/class/{class_id}')
async def get_specific_class(class_id: int):
    response = await class_Pydantic.from_queryset_single(Classroom.get(id=class_id))
    return {"Status":"ok","data": response}

@app.put('/class/{class_id}')
async def update_class(class_id:int , update_info: class_PydanticIn):
    classs = await Classroom.get(id=class_id)
    update_info = update_info.dict(exclude_unset=True)
    classs.name = update_info['name']
    await classs.save()
    response =  await class_Pydantic.from_tortoise_orm(classs)
    return {"Status":"ok","data": response}

@app.delete('/class/{class_id}')
async def delete_class(class_id: int):
    response = await Classroom.get(id=class_id).delete()
    return{"Status":"ok","data":response}

async def add_instructor(instructor_info: instructor_PydanticIn):
    instructor_obj = await Instructor.create(**instructor_info.dict(exclude_unset=True))
    response = await instructor_Pydantic.from_tortoise_orm(instructor_obj)
    return {"status":"ok","data" :response}

@app.get('/instructor')
async def get_all_instructors():
    response = await instructor_Pydantic.from_queryset(Instructor.all())
    return {"status": "ok", "data": response}



register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,  
    add_exception_handlers=True,
)