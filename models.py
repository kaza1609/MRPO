from dataclasses import dataclass


@dataclass(frozen=True)
class NegativeEmotions:
    name: str
    emoji: str
    strength: int


@dataclass(frozen=True)
class NegativeThought:
    name: str
    emotions: list[NegativeEmotions]


@dataclass(frozen=True)
class CalmingTechnique:
    name: str
    duration: int


@dataclass(frozen=True)
class PositiveEmotions:
    name: str
    emoji: str
    strength: int


@dataclass(frozen=True)
class PositiveThought:
    name: str
    emotions: list[PositiveEmotions]


@dataclass(frozen=True)
class Event:
    name: str
    date: str
    negative_emotions: list[NegativeEmotions] = None
    positive_emotions: list[PositiveEmotions] = None


@dataclass(frozen=True)
class Person:
    name: str
    surname: str
    gender: str
    events: list[Event]
