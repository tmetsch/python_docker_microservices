
import os
import pymongo
import sys
import time
import urlparse

from suricate.analytics import exec_node


def check_database(uri):
    """
    Checks if database for a user exists, if not create it.
    """
    client = pymongo.MongoClient(uri)

    # if user doesn't exist create new DB!
    if 'foo' not in client.database_names():
        db = client['foo']
        db.add_user('foo', 'bar', roles=['readWrite'])
    client.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise AttributeError('please provide the path to the sdk and a tenant '
                             'id for this execution node as arguments!')

    sdk = sys.argv[1]
    user = sys.argv[2]
    # TODO: rather join right docker env vars which are set by docker links.
    mongo = os.environ['MONGO_PORT'].replace('tcp', 'mongodb')
    tmp = urlparse.urlparse(os.environ['RABBIT_PORT_5672_TCP'])
    broker = 'amqp://guest:guest@{}:{}/%2F'.format(tmp.hostname, tmp.port)
    
    time.sleep(3)  # TODO: check wait for rabbitmq to be up & running.
    check_database(mongo)
    exec_node.ExecNode(mongo, broker, sdk, user)

