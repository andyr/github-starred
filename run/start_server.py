
import logging
from wsgiref import simple_server

import wsgi_app


logger = logging.getLogger('github_starred.start_server')


def start_http_server(port=10000):
    """Use wsgiref to start an http server on a specified port
    """
    server = simple_server.make_server('0.0.0.0', port, wsgi_app.app())
    logger.info("Server listening on port %d" % port)
    server.serve_forever()


if __name__ == '__main__':
    # TODO: update the start script for operational requirements
    import argparse

    wsgi_app.set_path()

    parser = argparse.ArgumentParser(description='See starred repos for a github user.')
    parser.add_argument('-p', '--port', action="store", dest="port", type=int, default='10000', help='port number')

    args = parser.parse_args()

    # after parsing arguments
    #start_http_server(args.port)
    wsgi_app.app().run()

