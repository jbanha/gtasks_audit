import os
import json

from dataclasses import dataclass
from typing import List

from requests_oauthlib import OAuth2Session

from model.task import Task

class TaskList:
    tasks = None
    
    def __init__(self, list_item: dict):
        self.id = list_item.get('id')
        self.etag = list_item.get('etag')
        self.title = list_item.get('title')
        self.updated = list_item.get('updated')
        self.selfLink = list_item.get('selfLink')
        
    def get_tasks(self, session: OAuth2Session, tasks_url):
        request_url = tasks_url + 'lists/' + self.id + '/tasks?showCompleted=True&showHidden=True'
                
        tasks_response = session.get(request_url)
        
        self.tasks = [Task(item, self) for item in json.loads(tasks_response.content)['items']]
        
        print(f"Retrieved {len(self.tasks)} tasks from list \"{self.title}\"")
        return self.tasks
        