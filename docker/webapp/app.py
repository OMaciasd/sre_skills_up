from prometheus_client import Summary, generate_latest, REGISTRY
from flask import Flask, Response, request
import logging_config

import logging

logging_config.setup_logging()

logging.basicConfig(level=logging.INFO)

logging.info('This is an informational message')


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
        request.start_time = REQUEST_TIME.time()

    @app.after_request
    def after_request(response):
        request.start_time.observe()
        return response

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
