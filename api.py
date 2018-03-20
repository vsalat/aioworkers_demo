import uuid
from aiohttp import web

tasks = dict()


async def add_task(request, data):
    """
    ---
    description: Add new task
    tags: [task]
    parameters:
      - data:
        name: data
        in: body
        required: true
        type: object
    """
    task_id = str(uuid.uuid4())
    tasks[task_id] = data
    return task_id


async def update_task(request, task_id, data):
    """
    ---
    description: Modify task
    tags: [task]
    parameters:
      - task_id:
        name: task_id
        in: path
        required: true
        type: string
        format: uuid
      - data:
        name: data
        in: body
        required: true
        type: object
    """
    # Validation
    if task_id not in tasks.keys():
        return web.Responce(status=404)
    tasks[task_id].update(data)
    return dict(task_id=tasks[task_id])


async def task_status(request, task_id):
    """
    ---
    description: get task_status
    tags: [task]
    parameters:
      - task_id:
        name: task_id
        in: path
        required: true
        type: string
        format: uuid
    """
    # Validation
    if task_id not in tasks.keys():
        return web.Responce(status=404)
    return tasks[task_id]