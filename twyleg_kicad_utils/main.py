# Copyright (C) 2023 twyleg
import sys
import argparse
import logging
import subprocess

from pathlib import Path
from twyleg_kicad_utils import __version__

FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"


def create_subcommand_argument_parser(description = "") -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "working_dir", metavar="working_dir", type=str, nargs="?", default=Path.cwd(), help="KiCad project directory. Default=./"
    )
    return parser

def subcommand_build():
    parser = create_subcommand_argument_parser(description="Build KiCad project")

    args = parser.parse_args(sys.argv[2:])

    logging.info("KiCad project: %s", args.working_dir)
    logging.info("Command: build")
    subprocess.run([
        "podman", "run",
        "-v", f"{args.working_dir}/:/root/project/",
        "-w", "/root/project",
        "ghcr.io/inti-cmnb/kicad7_auto_full:latest",
        "kibot", "-c", "/root/project/external/twyleg_kicad_utils/kibot/default.kibot.yaml"
    ])


def subcommand_submodules():
    parser = create_subcommand_argument_parser(description="Build KiCad project")

    parser.add_argument("--https", action="store_true", help="Switch submodule git protocol to https")
    parser.add_argument("--ssh", action="store_true", help="Switch submodule git protocol to ssh")

    args = parser.parse_args(sys.argv[2:])

    logging.info("KiCad project: %s", args.working_dir)
    logging.info("Command: submodules")

    if args.https:
        logging.info("Setting protocol for submodules to HTTPS")
    elif args.ssh:
        logging.info("Setting protocol for submodules to HTTPS")
    else:
        logging.info("list submodules")


def main() -> None:
    logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.INFO)

    parser = argparse.ArgumentParser(usage="twyleg_kicad_utils <command> [<args>]")
    parser.add_argument("command", help="Available subcommands: build, submodules")
    parser.add_argument(
        "-v",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )
    args = parser.parse_args(sys.argv[1:2])

    match args.command:
        case "build":
            subcommand_build()
        case "submodules":
            subcommand_submodules()
        case _:
            print(f"Command \"{args.command}\" is not supported!")


if __name__ == "__main__":
    main()
