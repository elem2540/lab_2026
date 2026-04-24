from pydantic import BaseModel, Field
from typing import Annotated


class Book(BaseModel):
    id: int
    title: str
    author: str
    review: Annotated[int, Field(ge=1, le=5)] = None  # campo opzionale --> lo imposto di default come None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Il nome della Rosa",
                    "author": "Umberto Eco",
                    "review": 5
                }
            ]
        }
    }


books = {
    0: Book(id=0, title="Il nome della Rosa", author="Umberto Eco", review=5),
    1: Book(id=1, title="Il gioco dei sei colori", author="Agatha Christie", review=4),
    2: Book(id=2, title="Il Signore degli Anelli", author="J.R.R. Tolkien", review=5)
}
