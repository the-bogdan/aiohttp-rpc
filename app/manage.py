import asyncio

from logger import logger
from server import run_server
from database import update_tables
from argparse import ArgumentParser


parser = ArgumentParser(description='Start RPC app based on aiohttp')
parser.add_argument('-r', '--run', action='store_true', help='Run app')
parser.add_argument('-m', '--migrate', action='store_true', help='Create all tables')
args = parser.parse_args()


def main():
    if args.run:
        run_server()
    if args.migrate:
        logger.info('Create all database tables')
        asyncio.run(update_tables())


if __name__ == '__main__':
    main()
