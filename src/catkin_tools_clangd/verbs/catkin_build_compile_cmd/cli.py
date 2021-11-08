from __future__ import print_function

from io import StringIO
from argparse import ArgumentParser
from os.path import join as osp_join
import sys


from catkin_tools.verbs.catkin_build import (
    prepare_arguments as catkin_build_prepare_arguments,
    main as catkin_build_main,
)
from catkin_tools.verbs.catkin_locate import (
    prepare_arguments as catkin_locate_prepare_arguments,
    main as catkin_locate_main,
)
from .build_compile_cmd import append_cmake_compile_commands, combine_compile_commands


def prepare_arguments(parser):
    parser = catkin_build_prepare_arguments(parser)
    parser.description = (
        parser.description
        + "After the build is finished, create compile commands in root workspace"
    )

    return parser


def main(opts):
    append_cmake_compile_commands(opts)

    err = catkin_build_main(opts)
    if err != 0:
        return err  # exit if failed

    # Figure out where's the catkin workspace
    catkin_locate_opts = catkin_locate_prepare_arguments(ArgumentParser()).parse_args()
    catkin_locate_opts.package = None
    if opts.workspace is not None:
        catkin_locate_opts.workspace = opts.workspace

    # Redirect stdout to string
    original_stdout = sys.stdout
    sys.stdout = stringio = StringIO()

    # call locate workspace
    catkin_locate_main(catkin_locate_opts)
    pth = stringio.getvalue().splitlines()[0]

    # revert stdout & cleanup
    sys.stdout = original_stdout
    del stringio

    combine_compile_commands(pth, osp_join(pth, "build"))
