from dataclasses import dataclass


@dataclass()
class NegativeEmotions:
    name: str
    emoji: str
    strength: int
    description: str


@dataclass()
class NegativeThought:
    name: str
    emotions: list[NegativeEmotions]
    description: str


@dataclass()
class CalmingTechnique:
    name: str
    duration: int
    related_negative_emotions: list[NegativeEmotions]


@dataclass()
class PositiveEmotions:
    name: str
    emoji: str
    strength: int
    description: str
    related_calming_techniques: list[CalmingTechnique] = None


@dataclass()
class PositiveThought:
    name: str
    emotions: list[PositiveEmotions]
    description: str


@dataclass()
class Person:
    name: str
    surname: str
    gender: str
    events: list['Event'] = None


@dataclass()
class Event:
    name: str
    date: str
    person: Person
    negative_emotions: list['NegativeEmotions'] = None
    positive_emotions: list['PositiveEmotions'] = None
    calm: 'CalmingTechnique' = None
