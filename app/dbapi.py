from __future__ import annotations

import uuid
from dataclasses import dataclass

from sqlalchemy import create_engine, text

from .main import settings
from .models import User


def engine():
    return create_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)


@dataclass
class Error:
    message: str


def create_user(email: str, password: str) -> (User, Error):
    id = str(uuid.uuid4())
    with engine().connect() as con:
        res = con.execute(
            text("SELECT COUNT(*) > 0 FROM users WHERE email = :email"),
            [{"email": email}]
        ).first()
        if res and res[0]:
            return None, Error("Email already exists")
        con.execute(
            text("INSERT INTO users(id, email, password) VALUES (:id, :email, :password)"),
            [{"id": id, "email": email, "password": password}]
        )
        con.commit()
        user = get_user(id)
        return user, None


def get_user(id: str) -> User | None:
    with engine().connect() as con:
        res = con.execute(
            text("SELECT id, email, password, created_at, modified_at FROM users WHERE id = :id"),
            [{"id": id}]
        ).first()
        if res:
            return User(
                res.id,
                res.email,
                res.password,
                res.created_at,
                res.modified_at
            )
        else:
            return None


def delete_user(id: str):
    with engine().connect() as con:
        con.execute(
            text("DELETE FROM  users WHERE id = :id"),
            [{"id": id}]
        )
        con.commit()
