import logging_config as logging_config

from web.app import create_app
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

logging_config.setup_logging()
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
