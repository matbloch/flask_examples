from server import create_app, init_extensions
from server import config
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='FLASK server')
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=3000,
        help='Port to run app on (default 3000)'
    )
    args = vars(parser.parse_args())

    application = create_app(config.DevelopmentConfig)
    init_extensions(application)
    application.run(host='0.0.'
                         ''
                         '0.0', port=args['port'])