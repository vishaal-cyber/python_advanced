#region Setup ################################################################################################################################
from sqlmodel import Session, create_engine


engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},
    echo = False
)


def get_session():
    with Session(engine) as session:
        yield session