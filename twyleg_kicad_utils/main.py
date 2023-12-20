# Copyright (C) 2023 twyleg
import sys
import argparse
import logging
import subprocess
import twyleg_kicad_utils.build
import twyleg_kicad_utils.diff

from pathlib import Path

from twyleg_kicad_utils import __version__
from twyleg_kicad_utils.submodules import SubmoduleProtocol, set_submodules_protocol, list_submodules

FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"


def init(args: argparse.Namespace):
    logging.error("Not yet implemented!")


def submodules(args: argparse.Namespace):
    gitmodules_file_path = Path(args.working_dir) / ".gitmodules"
    list_submodules(gitmodules_file_path)


def submodules_set_protocol(args: argparse.Namespace):
    gitmodules_file_path = Path(args.working_dir) / ".gitmodules"
    target_submodule_protocol = SubmoduleProtocol.HTTPS if "https" in args.protocol else SubmoduleProtocol.SSH

    set_submodules_protocol(target_submodule_protocol, gitmodules_file_path)


def build(args: argparse.Namespace):
    twyleg_kicad_utils.build.build_all(args.working_dir)


def build_bom(args: argparse.Namespace):
    logging.error("Not yet implemented!")


def build_images(args: argparse.Namespace):
    logging.error("Not yet implemented!")


def build_pdf(args: argparse.Namespace):
    logging.error("Not yet implemented!")


def build_3d(args: argparse.Namespace):
    logging.error("Not yet implemented!")

def diff(args: argparse.Namespace):
    twyleg_kicad_utils.diff.diff(args.port, args.clean)



def main():
    logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.INFO)

    #
    # Top-level parser
    #
    parser = argparse.ArgumentParser(description="foo")
    parser.add_argument(
        "-v",
        "--version",
        help="Show version and exit",
        action="version",
        version=__version__,
    )

    parser.add_argument(
        "-w", "--working_dir", help="Use a specific working directory. Default=./", type=str, default=Path.cwd()
    )

    subparsers = parser.add_subparsers(required=True, title="subcommands")

    #
    # Subcommand: init
    #
    parser_build = subparsers.add_parser("init", description="Initialize a project.")
    parser_build.set_defaults(func=init)

    #
    # Subcommand: submodules
    #
    parser_build = subparsers.add_parser("submodules", description="Manage git submodules.")
    parser_build.set_defaults(func=submodules)

    subparsers_submodules = parser_build.add_subparsers(required=False, title="subcommands")
    parser_submodules_set_protocol = subparsers_submodules.add_parser("set_protocol")
    parser_submodules_set_protocol.set_defaults(func=submodules_set_protocol)
    parser_submodules_set_protocol.add_argument(
        dest="protocol", metavar="{ssh,https}", choices=["ssh", "https"], nargs=1, help='Chose "ssh" or "https"'
    )

    #
    # Subcommand: build
    #
    parser_build = subparsers.add_parser("build", description="Build project or specific parts of it.")
    parser_build.set_defaults(func=build)

    parser_build.add_argument(
        "-o",
        "--output_dir",
        help=f"Use a specific output dir for the results. Default=./export",
        type=str,
        default=Path.cwd() / "export",
    )

    subparsers_build = parser_build.add_subparsers(required=False, title="subcommands")
    parser_build_bom = subparsers_build.add_parser("bom")
    parser_build_bom.set_defaults(func=build_bom)

    parser_build_images = subparsers_build.add_parser("images")
    parser_build_images.set_defaults(func=build_images)

    parser_build_pdf = subparsers_build.add_parser("pdf")
    parser_build_pdf.set_defaults(func=build_pdf)

    parser_build_3d = subparsers_build.add_parser("3d")
    parser_build_3d.set_defaults(func=build_3d)

    #
    # Subcommand: diff
    #
    parser_diff = subparsers.add_parser("diff", description="Git diff.")
    parser_diff.add_argument('-c', '--clean', action='store_true', help="Clean files from previous run before running again.")
    parser_diff.add_argument('-p', '--port', type=int, default=8000, help="Port to start kiri on.")
    parser_diff.set_defaults(func=diff)

    #
    # Subcommands end
    #
    args = parser.parse_args(sys.argv[1:])

    logging.info("twyleg_kicad_utils started!")
    logging.info("Command: %s", args.func.__name__.replace("_", " -> "))
    logging.info("Working dir: %s", args.working_dir)
    args.func(args)


if __name__ == "__main__":
    main()
