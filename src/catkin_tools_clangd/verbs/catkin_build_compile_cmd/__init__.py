from catkin_tools.argument_parsing import argument_preprocessor

from .cli import main
from .cli import prepare_arguments

# This describes this command to the loader
description = dict(
    verb="build_compile_cmd",
    description="Generate clangd compile commands at current workspace",
    main=main,
    prepare_arguments=prepare_arguments,
    argument_preprocessor=argument_preprocessor,
)
