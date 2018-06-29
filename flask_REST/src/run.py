from server import application
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='FLASK server')
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=80,
        help='Port to run app on (default 80)'
    )
    args = vars(parser.parse_args())

    application.run(host='0.0.0.0', port=args['port'])