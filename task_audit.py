import json

import asyncio

from oauthlib.oauth2 import MobileApplicationClient
from requests_oauthlib import OAuth2Session
from typing import List

from model.task_list import TaskList
from model.task import Task

from auth.secrets_client import TOKEN_URI, CLIENT_SECRET, CLIENT_ID


TASKS_URL = 'https://www.googleapis.com/tasks/v1/'
SHEETS_URL = 'https://sheets.googleapis.com/v4/spreadsheets/'

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly',
         'https://www.googleapis.com/auth/spreadsheets']

async def parse_tlist(item: dict) -> TaskList:
    return TaskList(list_item = item)

async def tlists_main() -> List[TaskList]:
    task_lists_jobs = await asyncio.gather(*[parse_tlist(item) for item in json.loads(task_list_response)['items']])
    return task_lists_jobs

async def get_tasks(tlists: List[TaskList]):
    await asyncio.gather(*[tlist.get_tasks(session=oauth, tasks_url=TASKS_URL) for tlist in tlists if control_list is not None and tlist.title in control_list])

async def log_responses(tasks: List[Task], session: OAuth2Session, sheets_url: str):
    await asyncio.gather(*[task.log_state(session=session, sheets_url=sheets_url) for task in tasks])
        
if __name__ == '__main__':
    with open('control_list.json', 'r') as f:
        control_list = json.loads(f.read()).get('controlled')

    oauth = OAuth2Session(
        client = MobileApplicationClient(
            client_id = CLIENT_ID
        ),
        scope = SCOPES,
        redirect_uri = 'https://localhost'
    )
    
    with open('auth/token.json', 'r') as f:
        stored_token = json.loads(f.read())
        
    refreshed_token = oauth.refresh_token(
        TOKEN_URI,
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        refresh_token=stored_token.get('refresh_token')
    )
    
    with open('auth/token.json', 'w') as f:
        f.write(json.dumps(refreshed_token))
        
    task_list_response = oauth.get(TASKS_URL + 'users/@me/lists').content
        
    task_lists = asyncio.run(tlists_main())
    
    asyncio.run(get_tasks(task_lists))
    # [tlist.get_tasks(session=oauth, tasks_url=TASKS_URL) for tlist in task_lists if control_list is not None and tlist.title in control_list]

    asyncio.run(log_responses(
        tasks = [task for tlist in 
              [tlist for tlist in task_lists if control_list is not None and tlist.title in control_list]
              for task in tlist.tasks if task.title in control_list[tlist.title]],
        session = oauth,
        sheets_url = SHEETS_URL
    ))
    
        