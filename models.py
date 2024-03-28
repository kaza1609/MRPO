from dataclasses import dataclass
import re
from datetime import datetime


class NegativeEmotions:
    def __init__(self, name: str, emoji: str, strength: int, description: str):
        try:
            validate_name(name)
            validate_non_negative_number(strength)
        except Exception:
            raise Exception
        self.name = name
        self.emoji = emoji
        self.strength = strength
        self.description = description

    def __eq__(self, other):
        if isinstance(other, NegativeEmotions):
            return self.name == other.name
        return False


@dataclass(frozen=True)
class NegativeThought:
    name: str
    emotions: list[NegativeEmotions]
    description: str


@dataclass(frozen=True)
class CalmingTechnique:
    name: str
    duration: int
    related_negative_emotions: list[NegativeEmotions]


class PositiveEmotions:
    def __init__(self, name: str, emoji: str, strength: int, description: str,
                 related_calming_techniques: list[CalmingTechnique] = None):
        try:
            validate_name(name)
            validate_non_negative_number(strength)
        except Exception:
            raise Exception
        self.name = name
        self.emoji = emoji
        self.strength = strength
        self.description = description
        self.related_calming_techniques = related_calming_techniques

    def __eq__(self, other):
        if isinstance(other, PositiveEmotions):
            return self.name == other.name
        return False


@dataclass(frozen=True)
class PositiveThought:
    name: str
    emotions: list[PositiveEmotions]
    description: str


class Event:
    def __init__(self, name: str, date: datetime, negative_emotions: list[NegativeEmotions] = None,
                 positive_emotions: list[PositiveEmotions] = None, calm: CalmingTechnique = None):
        try:
            validate_name(name)
            validate_date(date)
        except Exception:
            raise Exception
        self.name = name
        self.date = date
        self.negative_emotions = negative_emotions
        self.positive_emotions = positive_emotions
        self.calm = calm

    def __eq__(self, other):
        if isinstance(other, Event):
            return (self.name == other.name
                    and self.negative_emotions == other.negative_emotions
                    and self.positive_emotions == other.positive_emotions)
        return False


class Person:
    def __init__(self, name: str, surname: str, gender: str, events: list[Event] = None):
        try:
            validate_name(name)
            validate_name(surname)
            validate_gender(gender)
        except Exception:
            raise Exception
        self.name = name
        self.surname = surname
        self.gender = gender
        self.events = events

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name
                    and self.surname == other.surname
                    and self.events == other.events)
        return False


def validate_name(word: str):
    # Имя не содержит специальных символов и чисел

    pattern = r'^[a-zA-Z]+$'
    if not re.match(pattern, word):
        raise ValueError('Неверное значение.')
    return True


def validate_non_negative_number(number: int):
    # Число не является отрицательным

    if number < 0:
        raise ValueError('Значение не может быть меньше 0.')
    return True


def validate_date(date: datetime):
    # Дата не будущая

    if date > datetime.now():
        raise ValueError('Указана неверная дата.')
    return True


def validate_gender(gender: str):

    # Гендер должен быть либо мужчина, либо женщина
    if gender == 'м' or gender == 'ж':
        return True
    raise ValueError('Вы ввели неверный гендер.')
