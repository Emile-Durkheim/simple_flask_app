from app import app
import logging


if __name__ == "__main__":
    # If wsgi.py is run directly, like when using 'flask run'
    app.run()
else:
    # If in production, attach gunicorn logger in place of default Flask logger.
    # If this were missing and the app were run with gunicorn, logs wouldn't be saved to log file.
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
