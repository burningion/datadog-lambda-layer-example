from flask import Flask, request

from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

from datadog_lambda.wrapper import datadog_lambda_wrapper
from datadog_lambda.metric import lambda_metric

import hashlib, sys, json, hmac, base64, boto3, requests

patch_all()

app = Flask(__name__)

xray_recorder.configure(service='reverser')
XRayMiddleware(app, xray_recorder)

@datadog_lambda_wrapper
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        request_string = request.get_json()['string'] # expecting {"string": "blahhh"}
        xray_recorder.put_annotation('request_body', repr(request.get_json()))

        app.logger.info(f"Reverser called with {request_string}")

        lambda_metric("reverse_service.string_length", # metric
                      len(request_string), # value
                      tags=['serverless:reverser'])

        response = {'response': request_string.swapcase()}
        return response

    return {'hello': 'world'}

if __name__ == "__main__":
    app.run()
