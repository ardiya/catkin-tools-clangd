"""
Test build_compile_cmd.py
Note: run this file with python -m pytest
"""
from catkin_tools_clangd.verbs.catkin_build_compile_cmd.build_compile_cmd import (
    append_cmake_compile_commands,
)


class TestAppendCmakeCompileCommands:
    def _create_dummy_opts(self):
        class DummyOpts:
            def __init__(self):
                self.cmake_args = []

        return DummyOpts()

    def test_compile_commands_none(self):
        # case where it's None
        opts = self._create_dummy_opts()
        opts.cmake_args = None

        append_cmake_compile_commands(opts)

        assert "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON" in opts.cmake_args

    def test_compile_commands_added(self):
        opts = self._create_dummy_opts()

        append_cmake_compile_commands(opts)

        assert "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON" in opts.cmake_args

    def test_compile_commands_added_and_no_duplicate_dkey(self):
        # Add case where user might do weird stuff with export compile commands
        # we also should remove duplicate CMAKE_EXPORT_COMPILE_COMMANDS
        opts = self._create_dummy_opts()
        opts.cmake_args.append("-DCMAKE_EXPORT_COMPILE_COMMANDS=OFF")
        opts.cmake_args.append("-DCMAKE_EXPORT_COMPILE_COMMANDS=ASD")

        append_cmake_compile_commands(opts)

        assert "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON" in opts.cmake_args
        assert "-DCMAKE_EXPORT_COMPILE_COMMANDS=OFF" not in opts.cmake_args
        assert "-DCMAKE_EXPORT_COMPILE_COMMANDS=ASD" not in opts.cmake_args
