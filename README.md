# Catkin Tools Clangd

Define new verb `build_compile_command` in `catkin` to generate clangd compile commands

## Backstory
This project is made because I've always have issues getting autocomplete to work in VSCode C++ Intellisense with catkin/ROS environment. My solution is to use this catkin-tools-clangd in tandem with [vscode-clangd](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd) or [sublime-text-lsp](https://github.com/sublimelsp/LSP)

## Installation
This package installs a new verb for catkin_tools. The easiest way to install this verb is from PyPI:
```sh
pip install catkin-tools-clangd
```

## Usage
After installing you'd be able to use `catkin build_compile_cmd` that will automatically generate compile commands for clangd for you.

## Aliasing
You can easily change your alias in `/home/ardiya/.config/catkin/verb_aliases/00-default-aliases.yaml`
e.g. add the following line:
```yaml
bcc: build_compile_cmd
```
and you'd be able to call `catkin bcc` to run the same `catkin build_compile_cmd`

## VS Code setup
Install [vscode-clangd](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd) extension

Actually, that's it. But I also recommend to add following line into ${HOME}/.config/Code/User/settings.json
```json
{
    ...
    "clangd.semanticHighlighting": true,
    "clangd.arguments": [
        // If set to true, code completion will include index symbols that are not defined in the scopes
        // (e.g. namespaces) visible from the code completion point. Such completions can insert scope qualifiers
        "--all-scopes-completion",
        // Index project code in the background and persist index on disk.
        "--background-index",
        // Enable clang-tidy diagnostics
        "--clang-tidy",
        // Whether the clang-parser is used for code-completion
        //   Use text-based completion if the parser is not ready (auto)
        "--completion-parse=auto",
        // Granularity of code completion suggestions
        //   One completion item for each semantically distinct completion, with full type information (detailed)
        "--completion-style=detailed",
        // clang-format style to apply by default when no .clang-format file is found
        "--fallback-style=Google",
        // When disabled, completions contain only parentheses for function calls.
        // When enabled, completions also contain placeholders for method parameters
        "--function-arg-placeholders",
        // Add #include directives when accepting code completions
        //   Include what you use. Insert the owning header for top-level symbols, unless the
        //   header is already directly included or the symbol is forward-declared
        "--header-insertion=iwyu",
        // Prepend a circular dot or space before the completion label, depending on whether an include line will be inserted or not
        "--header-insertion-decorators",
        // Enable index-based features. By default, clangd maintains an index built from symbols in opened files.
        // Global index support needs to enabled separatedly
        "--index",
        // Attempts to fix diagnostic errors caused by missing includes using index
        "--suggest-missing-includes",
    ],
    ...
}
```

## Sublime text setup
Install [sublime-text-lsp](https://github.com/sublimelsp/LSP)

Add following lines to `Preferences`->`Package Settings` -> `LSP` -> `Settings`
```json
{
  "clients": {
    "clangd": {
      "enabled": true,
      "command": [
        "clangd",  // you may use an absolute path for this clangd executable
        "--all-scopes-completion",
        "--background-index",
        "--clang-tidy",
        "--completion-style=detailed",
        "--fallback-style=Google",
        "--function-arg-placeholders",
        "--header-insertion=iwyu",
        "--header-insertion-decorators",
        "--index",
        "--suggest-missing-includes",
      ],
      "scopes": ["source.c", "source.c++", "source.objc", "source.objc++"],
      "syntaxes": [
        "Packages/C++/C.sublime-syntax",
        "Packages/C++/C++.sublime-syntax",
        "Packages/Objective-C/Objective-C.sublime-syntax",
        "Packages/Objective-C/Objective-C++.sublime-syntax",
      ],
      "languageId": "cpp",
    },
  },
}
```
