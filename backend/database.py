from typing import Optional

import streamlit as st
from sqlalchemy import func, not_
from sqlmodel import Field, Session, SQLModel, create_engine, select


@st.cache_data()
def get_db_url() -> str:
    return st.secrets["database"]["url"]


class Annotation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    participant_id: str = Field(foreign_key="participant.id")
    stimulus_id: str
    stimulus_type: str
    audio_result_id: str
    query1: str
    query2: str
    aspects1: str
    aspects2: str
    time: Optional[float]


class Participant(SQLModel, table=True):
    id: str = Field(primary_key=True)
    fluency: str
    experience: str
    passed_instructions: bool = False


def num_annotations_for_participant(participant_id: str) -> int:
    engine = connect()
    with Session(engine) as session:
        statement = select(func.count(Annotation.id)).where(
            Annotation.participant_id == participant_id,
        )
        results = session.exec(statement)
        return results.one()


def add_participant(
    participant_id: str,
    fluency,
    experience,
):
    engine = connect()
    with Session(engine) as session:
        participant = Participant(
            id=participant_id,
            fluency=fluency,
            experience=experience,
        )
        session.add(participant)
        session.commit()


def get_participant(participant_id: str) -> Optional[Participant]:
    engine = connect()
    with Session(engine) as session:
        statement = select(Participant).where(Participant.id == participant_id)
        results = session.exec(statement)
        return results.one_or_none()


def participant_passed_instructions(participant_id: str):
    engine = connect()
    with Session(engine) as session:
        participant = session.exec(
            select(Participant).where(Participant.id == participant_id)
        ).one()
        participant.passed_instructions = True
        session.add(participant)
        session.commit()


def add_annotation(
    participant_id: str,
    stimulus_id: str,
    stimulus_type: str,
    audio_result_id: str,
    query1: str,
    query2: str,
    aspects1: list[str],
    aspects2: list[str],
    time: float | None = None,
):
    engine = connect()
    aspects1 = "; ".join(aspects1)
    aspects2 = "; ".join(aspects2)
    with Session(engine) as session:
        annotation = Annotation(
            participant_id=participant_id,
            stimulus_id=stimulus_id,
            stimulus_type=stimulus_type,
            audio_result_id=audio_result_id,
            query1=query1,
            query2=query2,
            aspects1=aspects1,
            aspects2=aspects2,
            time=time,
        )
        session.add(annotation)
        session.commit()


@st.cache_resource(max_entries=1)
def connect(verbose=False):
    engine = create_engine(get_db_url(), echo=verbose)
    return engine


def create_db_and_tables(db_url):
    engine = create_engine(db_url, echo=True)
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    # hint: create the database file first
    # sqlite3 data/music_question_answering.db "VACUUM;"
    base_path = "./"
    # db_url = f"sqlite:///{base_path}data/questionnaire.db"
    db_url = get_db_url()

    create_db_and_tables(db_url)
    # add_questions(db_url, f"{base_path}musiccaps/musiccaps_questions.json", "musiccaps")
    # add_questions(db_url, f"{base_path}SongDescriberDataset/sdd_questions.json", "sdd")
