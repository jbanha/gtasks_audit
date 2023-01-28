import os
import json
import asyncio

import configs.env

from datetime import datetime

from requests_oauthlib import OAuth2Session

class Task:
    def __init__(self, task_item:dict, task_list):
        self.parent_list_title = task_list.title
        self.parent_list_id = task_list.id
        self.id = task_item.get('id')
        self.etag = task_item.get('etag')
        self.title = task_item.get('title')
        self.updated = datetime.strptime(
            task_item.get('updated'),
            '%Y-%m-%dT%H:%M:%S.%fZ'
        ) if task_item.get('updated') is not None else None
        self.selfLink = task_item.get('selfLink')
        self.position = int(task_item.get('position'))
        self.status = task_item.get('status')
        self.due = datetime.strptime(
            task_item.get('due'),
            '%Y-%m-%dT%H:%M:%S.%fZ'
        ) if task_item.get('due') is not None else None
        self.links = task_item.get('links')

        self._log_body = {
            'range': 'RawLog',
            'majorDimension': 'ROWS',
            'values': [
                [
                self.parent_list_title,
                self.title,
                self.updated.strftime("%Y-%m-%d %H:%M:%S"),
                self.due.strftime("%Y-%m-%d %H:%M:%S") if self.due is not None else "",
                self.status,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ]
            ]
        }
        
    async def log_state(self, session: OAuth2Session = None,
                  sheets_url = None, log_location = 'sheets'):
    
        if log_location=='sheets':
            self._log_in_sheets(session=session,
                                sheets_url=sheets_url)

    @property
    def log_body(self):
        return self._log_body
        
    
    def _log_in_sheets(self, session: OAuth2Session,
                       sheets_url):
        spreadsheet = json.loads(
            session.get(sheets_url + os.getenv('audit_sheet_id')).content
        )
        print('Logging')
        sheets = spreadsheet.get('sheets')
        
        sheet_match_gen = (sh for sh in sheets if sh['properties']['title']=='RawLog')
        
        log_sheet = next(sheet_match_gen)
        
        response = session.post(sheets_url + os.getenv('audit_sheet_id') + f"/values/RawLog:append?valueInputOption=USER_ENTERED",
                        json=self.log_body)

        print(json.loads(response.content))
        
        return response