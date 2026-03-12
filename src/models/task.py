from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Task:
    '''Task model'''
    id: int
    payload: Any
