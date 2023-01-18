from dataclasses import dataclass
from typing import List

from model.task import Task


@dataclass
class TaskList:
    title: str
    id: str
    tasks: list[Task] = None
    
    def get_tasks(session: OAuth2Session) -> list(Task):
        return 1