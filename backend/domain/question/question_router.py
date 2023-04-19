from fastapi import APIRouter

from backend.database import SessionLocal
from backend.models import Question

router = APIRouter(
    prefix="/api/question"
)

@router.get("/list")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_dat.desc()).all()
    db.close
    return _question_list