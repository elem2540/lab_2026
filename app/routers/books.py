from typing import Annotated
from fastapi import APIRouter, Path, HTTPException
from schemas.book import Book, books
from schemas.review import Review

router = APIRouter()

books_router = APIRouter(prefix="/books", tags=["books"])


@books_router.get("/")
def get_all_books() -> list[Book]:
    return list(books.values())


@books_router.get("/{id}")
def get_book_by_id(
        id: Annotated[int, Path(description="The ID of the book to retrieve")]
) -> Book:
    try:
        return books[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")


@books_router.post("/{id}/review")
def add_review(
        id: Annotated[int, Path(description="The ID of the book to review")],
        review: Review
):
    """
    Add a review to the book
    """
    try:
        books[id].review = review.review
        return "Review added successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail="Book not found")
