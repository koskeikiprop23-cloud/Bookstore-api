from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    title: str = Field(index=True, min_length=1, max_length=200)
    author: str = Field(index=True, min_length=2, max_length=100)
    isbn: str = Field(unique=True, index=True)

    published_year: int = Field(
        ge=1000,
        le=datetime.now().year
    )

    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)
    available: bool = Field(default=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BookCreate(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=2, max_length=100)
    isbn: str
    published_year: int = Field(
        ge=1000,
        le=datetime.now().year
    )
    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)
    available: bool = True


class BookUpdate(SQLModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=2, max_length=100)
    isbn: Optional[str] = None
    published_year: Optional[int] = Field(
        None,
        ge=1000,
        le=datetime.now().year
    )
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    available: Optional[bool] = None