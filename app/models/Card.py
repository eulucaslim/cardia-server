from models import BaseEntity
from models.enums import CardFormat
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String

class Card(BaseEntity):
    format: Mapped = mapped_column(Enum(CardFormat))
    question: Mapped[String] = mapped_column(String)
    answer: Mapped[String] = mapped_column(String)
