from flask import Flask, Response
from prometheus_client import (
    Summary,
    Counter,
    generate_latest,
    REGISTRY,
)


def create_app():
    app = Flask(__name__)

    REQUEST_TIME = Summary(
        'request_processing_seconds',
        'Time spent processing request'
    )

    HTTP_REQUESTS_TOTAL = Counter(
        'http_requests_total',
        'Total number of HTTP requests'
    )

    @app.route('/')
    @REQUEST_TIME.time()
    def hello():
        HTTP_REQUESTS_TOTAL.inc()
        return 'Hello World!'

    @app.route('/metrics')
    def metrics():
        try:
            metrics_data = generate_latest(REGISTRY)
            return Response(
                metrics_data,
                content_type='text/plain; version=0.0.4; charset=utf-8'
            )
        except Exception as e:
            return Response(f"Error generating metrics: {e}", status=500)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
