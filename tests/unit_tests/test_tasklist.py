import json
import os
import pytest

from model.task_list import TaskList

TASK_LIST_RESPONSE_PATH = 'tests/resources/task_list.json'

class TestTaskList:
    def setup_class(self):
        with open(TASK_LIST_RESPONSE_PATH, 'r') as f:
            self.task_list_response = json.loads(f.read())
        
    def test_load(self):
        assert self.task_list_response is not None
        
        list_items = self.task_list_response.get('items')
        
        tasklists = [TaskList(item) for item in list_items]
        
        assert len(tasklists) == 5
        
        assert 'As minhas tarefas' in [tlist.title for tlist in tasklists]
        
    def test_titles(self):
        assert 1==1
        
    def test_test(self):
        assert 3==3