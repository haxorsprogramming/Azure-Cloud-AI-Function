import logging
import logging, json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    logging.info('Python HTTP trigger function processed a request.')
    data = {
        "todos": [
        {
            "id": 1,
            "task": 'task1',
            "assignee": 'assignee1000',
            "status": 'completed',
            'name' : name
        }
        ]
    }
    
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
