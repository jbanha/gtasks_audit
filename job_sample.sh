#/bin/bash

cd $REPO_PARENT/gtasks_audit
. venv_tasks/bin/activate
python -m task_audit
deactivate

