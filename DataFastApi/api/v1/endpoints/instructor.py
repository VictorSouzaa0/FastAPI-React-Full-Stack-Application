from typing import List
from fastapi import APIRouter,status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.instructor_model import InstructorModel
from schemas.instructor_schema import InstructorSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=InstructorSchema)
async def post_instructor(instructor: InstructorSchema,  db: AsyncSession = Depends(get_session)):
    new_instructor = InstructorModel(
        name=instructor.name,
        age = instructor.age,
        content = instructor.content,
        image = instructor.image
    )
    db.add(new_instructor)

    await db.commit()

    return new_instructor

@router.get("/", response_model=List[InstructorSchema])
async def all_instructors(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstructorModel)
        result = await session.execute(query)

        instructors: List[InstructorModel] = result.scalars().all()

        return instructors
    
@router.get("/{instructor_id}", response_model=InstructorSchema)
async def get_instructor(instructor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstructorModel).filter(InstructorModel.id == instructor_id)

        result = await session.execute(query)

        instructor = result.scalar_one_or_none()

        if instructor:
            return instructor
        else:
            raise HTTPException(detail="Instructor não encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{instructor_id}", response_model=InstructorSchema, status_code=status.HTTP_202_ACCEPTED)
async def edit_instructor(instructor_id: int, instructor: InstructorSchema, db: AsyncSession =Depends(get_session)):
        async with db as session:
            query = select(InstructorModel).filter(InstructorModel.id == instructor_id)

            result = await session.execute(query)

            instructor_edited = result.scalar_one_or_none()

            if instructor_edited:
                instructor_edited.name = instructor.name,
                instructor_edited.age = instructor.age,
                instructor_edited.content = instructor.content
                instructor_edited.image = instructor.image

                await session.commit()
                return instructor_edited
            else:
                raise HTTPException(detail="Instructor not found",
                                status_code=status.HTTP_404_NOT_FOUND)
            

@router.delete("/{instructor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_instructor(instructor_id: int, db: AsyncSession = Depends(get_session)):
        async with db as session:
            query = select(InstructorModel).filter(InstructorModel.id == instructor_id)

            result = await session.execute(query)

            instructor_delete = result.scalar_one_or_none()

            if instructor_delete:
                await session.delete(instructor_delete)
                await session.commit()
                return Response(status_code=status.HTTP_204_NO_CONTENT)
            else:
                raise HTTPException(detail="Instrutor not found",
                                    status_code=status.HTTP_404_NOT_FOUND)