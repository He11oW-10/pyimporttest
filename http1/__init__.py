import json
import logging
import os
import sys

import azure.functions as func

logger=logging.getLogger("azure")
logger.setLevel(logging.WARNING)

try:
    current_path=os.path.dirname(os.path.abspath(__file__))
    logging.info(current_path)
    sys.path.insert(0, f"{current_path}/../utils")
    logging.info(str(sys.path))
    from utils.test import hellotest

except Exception as e:
    logging.error("can't import modules")
    raise ImportError(f"pathing error for import. {e}")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    logging.info(hellotest(name))

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
