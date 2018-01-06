from argparse import ArgumentParser
from advanced_python import CsvParser
from advanced_python import App

import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser(description='Get information about bitcoin from csv.')
    parser.add_argument('csv', default='', help='Path of the csv file.')

    args = parser.parse_args(args=args)

    app = App(CsvParser(args.csv))
    app.print_info()


if __name__ == "__main__":
    main()
