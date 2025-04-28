from fastapi import FastAPI,Request
from tortoise.contrib.fastapi import register_tortoise
from models import student_Pydantic,student_PydanticIn,Student
from models import instructor_Pydantic,instructor_PydanticIn,Instructor
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

template = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"), name="static")


@app.get('/')
def index():
    return{"Msg":"go to /docs for the API documentation"}

@app.get('/instructor')
async def get_all_instructors():
    response = await instructor_Pydantic.from_queryset(Instructor.all())
    return {"status": "ok", "data": response}

@app.delete('/instructor/{instructor_id}')
async def delete_instructor(instructor_id: int):
    response = await Instructor.get(id=instructor_id).delete()
    return {"Status":"ok","data": response}

@app.post('/instructor')
async def add_instructor(class_info: instructor_PydanticIn):
    instructor_obj = await Instructor.create(**class_info.dict(exclude_unset=True))
    response = await instructor_Pydantic.from_tortoise_orm(instructor_obj)
    return{"Status":"ok","data":response}

@app.put('/instructor/{instructor_id}')
async def update_instructor(instructor_id: int,update: instructor_PydanticIn):
    instructor = await Instructor.get(id=instructor_id)
    update = update.dict(exclude_unset=True)
    instructor.fullname  = update['fullname']
    instructor.age = update['age']
    await instructor.save()
    response = await instructor_Pydantic.from_tortoise_orm(instructor)
    return {"Status":"ok","data": response }

@app.get('/students')
async def get_all_students():
    response = await student_Pydantic.from_queryset(Student.all())
    return {"Status":"ok","data": response}

@app.get('/students/{sttudent_id}')
async def get_stuentID(request: Request,sttudent_id: int):
    student = await student_Pydantic.from_queryset_single(Student.get(id=sttudent_id))
    return template.TemplateResponse("student.html",{
        "request": request,
        "student": student
    })
@app.post('/students')
async def add_students(students_info: student_PydanticIn):
    student_obj = await Student.create(**students_info.dict(exclude_unset=True))
    response = await student_Pydantic.from_tortoise_orm(student_obj)
    return {"Status":"ok","data": response}

@app.put('/students/{students_id}')
async def update_students(students_id: int, students_info: student_PydanticIn):
    students = await Student.get(id=students_id)
    students_info = students_info.dict(exclude_unset=True)
    students.fullname = students_info['fullname']
    students.age = students_info['age']
    students.carrer_interest = students_info['carrer_interest']
    students.bosch_area = students_info['bosch_area']
    students.image = students_info['image']
    await students.save()
    response = await student_Pydantic.from_tortoise_orm(students)
    return {"status":"ok","data":response}

@app.delete('/students/{student_id}')
async def delete_students(student_id: int):
    response = await Student.get(id=student_id).delete()
    return {"status":"ok","data": response}


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,  
    add_exception_handlers=True,
)   