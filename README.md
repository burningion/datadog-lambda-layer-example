# Datadog Lambda Layer Example

This is a (tiny!) example, using the [Datadog lambda layer](https://github.com/DataDog/datadog-lambda-layer-python) for Python.

It uses Flask with [Zappa](https://github.com/Miserlou/Zappa), a serverless framework.

It's cool because you can do things like respond to SNS notifications or schedule things to run at a certain time in code.

Right now the app doesn't do much, other than get instrumented. That might change soon!

## Running the Example Serverless App Locally

Use virtualenv to separate your Serverless app's requirements:

```bash
$ pip install virtualenv
$ virtualenv ~/.virtualenvs/zappa-demo
$ source ~/.virtualenvs/zappa-demo/bin/activate
```

Once that's done, you can then do a:

```bash
$ pip install -r requirements.txt
$ zappa init
$ zappa deploy dev
```

Send an example request to be reversed with `curl`:

```bash
$ curl -d '{"string": "Hello!"}' -H "Content-Type: application/json" <YOUR_ZAPPA_URL>
{"response":"hELLO!"}
```


