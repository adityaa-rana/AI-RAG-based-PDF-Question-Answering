from typing import List

from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class Video(BaseModel):
    title: str
    url: str
    channel: str
    duration: str
    thumbnail: str


class WebResource(BaseModel):
    title: str
    url: str
    content: str


class AskResponse(BaseModel):
    answer: str
    confidence: float
    youtube: List[Video]
    web: List[WebResource]