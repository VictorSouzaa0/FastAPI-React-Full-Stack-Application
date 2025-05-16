from fastapi import APIRouter

from api.v1.endpoints import instructor

api_router = APIRouter()

api_router.include_router(instructor.router, prefix="/instructor", tags=["Instructor"])

# api_router.include_router(students.router, prefix="/students", tags=["Studenrs"])