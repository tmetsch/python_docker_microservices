
import bottle
import os
import sys

from suricate.ui import ui_app


class SessionMiddleWare(object):
    """
    Demo Session middleware adding the required environment id.
    """

    def __init__(self, app_to_wrap):
        self.wrap_app = app_to_wrap

    def __call__(self, environ, start_response):
        environ['HTTP_X_UID'] = 'foo'
        environ['HTTP_X_TOKEN'] = 'bar'
        return self.wrap_app(environ, start_response)


if __name__ == '__main__':
    # TODO: rather join right docker env vars which are set by docker links.
    mongo = os.environ['MONGO_PORT'].replace('tcp', 'mongodb')
    broker = os.environ['RABBIT_PORT'].replace('tcp', 'amqp')

    app = ui_app.AnalyticsApp(mongo, broker).get_wsgi_app()
    app = SessionMiddleWare(app)

    bottle.TEMPLATE_PATH.insert(0, '/tmp/suricate/ui/views')
    bottle.run(app=app, host='0.0.0.0', port=8888)

