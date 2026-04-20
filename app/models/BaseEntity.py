from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import DateTime, Integer
from sqlalchemy import Column


class BaseEntity(DeclarativeBase):
    id: Integer = Column(Integer, primary_key=True)
    created_at: DateTime = Column(DateTime, default=datetime.now(timezone.utc)) 
    updated_at: DateTime = Column(DateTime, default=datetime.now(timezone.utc)) 
    deleted_at: DateTime = Column(DateTime, default=datetime.now(timezone.utc)) 
