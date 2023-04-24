from datetime import datetime

from backend.domain.question.question_schema import QuestionCreate
from backend.models import Question
from sqlalchemy.orm import Session

def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question)\
        .order_by(Question.create_date.desc())
    
    total = _question_list.count()
    _question_list = _question_list.offset(skip).limit(limit).all()
    return total, _question_list # (전체 건수, 페이징 적용된 질문 목록)

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,content=question_create.content ,create_date=datetime.now())
    db.add(db_question)
    db.commit()

