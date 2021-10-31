import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: uuid.UUID
    email: str
    password: str
    created_at: datetime
    modified_at: datetime
