from flask import Flask, request

from datadog_lambda.wrapper import datadog_lambda_wrapper
from datadog_lambda.metric import lambda_metric

app = Flask(__name__)

@datadog_lambda_wrapper
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        request_string = request.get_json()['string'] # expecting {"string": "blahhh"}
        app.logger.info(f"Reverser called with {request_string}")

        lambda_metric("reverse_service.string_length", # metric
                      len(request_string), # value
                      tags=['serverless:reverser'])

        response = {'response': request_string.swapcase()}
        return response

    return {'hello': 'world'}

if __name__ == "__main__":
    app.run()
