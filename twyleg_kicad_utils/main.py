# Copyright (C) 2023 twyleg
import sys
import argparse
import logging

from twyleg_kicad_utils import __version__

FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"


def main() -> None:
    logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.INFO)

    parser = argparse.ArgumentParser(usage="twyleg_kicad_utils <command> [<args>] <files>")
    parser.add_argument(
        "-v",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )
    args = parser.parse_args(sys.argv[1:2])


if __name__ == "__main__":
    main()
