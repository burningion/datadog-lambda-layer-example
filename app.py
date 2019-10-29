from chalice import Chalice

from datadog_lambda.wrapper import datadog_lambda_wrapper
from datadog_lambda.metric import lambda_metric

app = Chalice(app_name='swapcaser')

@datadog_lambda_wrapper
@app.route('/', methods=['POST', 'GET'])
def index():
    request = app.current_request
    if request.method == 'POST':
        request_string = request.json_body['string'] # expecting {"string": "blahhh"}
        app.log.info(f"Reverser called with {request_string}")

        lambda_metric("reverse_service.string_length", # metric
                      len(request_string), # value
                      tags=['serverless:reverser'])

        response = {'response': request_string.swapcase()}
        return response

    return {'hello': 'world'}

