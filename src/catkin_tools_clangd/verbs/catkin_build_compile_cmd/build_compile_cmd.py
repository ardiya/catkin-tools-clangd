from __future__ import print_function

import json
from os import listdir
from os.path import isdir, join, exists


def append_cmake_compile_commands(opts):
    """
    Append "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON" to opts.cmake_args if it doesn't exist already
    """

    if opts.cmake_args is None:
        opts.cmake_args = []

    flag_key = "-DCMAKE_EXPORT_COMPILE_COMMANDS"
    opts.cmake_args = [x for x in opts.cmake_args if flag_key not in x]

    opts.cmake_args.append("{}=ON".format(flag_key))


def combine_compile_commands(ws_path, build_path):
    dirs = [x for x in listdir(build_path) if isdir(join(build_path, x))]

    combined_compile_commands = list()
    for dir in dirs:
        pth = join(build_path, dir, "compile_commands.json")
        if exists(pth):
            with open(pth, "r") as fp:
                data = json.load(fp)
                if type(data) is not list:
                    continue
                combined_compile_commands.extend(data)

    save_path = join(ws_path, "compile_commands.json")
    with open(save_path, "w") as fp:
        json.dump(combined_compile_commands, fp)
        print("Created clangd compile commands in", save_path)
