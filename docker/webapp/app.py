from loguru import logger
from prometheus_client import Summary, generate_latest, REGISTRY
from flask import Flask, Response, request
import logging_config
import time

# Configura el logger
logging_config.setup_logging()

REQUEST_TIME = Summary(
    'request_processing_seconds',
    'Time spent processing request'
)

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello World!'

    @app.route('/metrics')
    def metrics():
        metrics_data = generate_latest(REGISTRY)
        return Response(
            metrics_data,
            content_type='text/plain; version=0.0.4; charset=utf-8'
        )

    @app.before_request
    def before_request():
        request.start_time = time.time()  # Start the timer

    @app.after_request
    def after_request(response):
        # Calculate the duration of the request
        request_duration = time.time() - request.start_time
        REQUEST_TIME.observe(request_duration)  # Record the time
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
