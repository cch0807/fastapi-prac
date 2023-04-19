from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.database import SessionLocal
from backend.domain.question import question_schema, question_crud
# from backend.models import Question


router = APIRouter(
    prefix="/api/question"
)

@router.get("/list", response_model= list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    
    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_dat.desc()).all()
    # db.close

    # with get_db() as db:
    #     _question_list = db.query(Question).all()

    # _question_list = db.query(Question).all()
    _question_list = question_crud.get_question_list(db)

    return _question_list