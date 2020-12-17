from pydantic import BaseModel


class Counter(BaseModel):
    words: int
