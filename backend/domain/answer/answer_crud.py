from datetime import datetime

from sqlalchemy.orm import Session

from backend.domain.answer.answer_schema import AnswerCreate
from backend.models import Question, Answer, User


def create_answer(
    db: Session, question: Question, answer_create: AnswerCreate, user: User
):
    db_answer = Answer(
        question=question, content=answer_create.content, create_date=datetime.now()
    )

    db.add(db_answer)
    db.commit()


def delete_answer(db: Session, db_answer: Answer):
    db.delete(db_answer)
    db.commit()


def get_answer(db: Session, answer_id: int):
    answer = db.query(Answer).filter(answer_id=answer_id)
    return answer
