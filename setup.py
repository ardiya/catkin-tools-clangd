import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="catkin-tools-clangd",
    version="0.0.2",
    author="Aditya Ardiya",
    author_email="aditya.ardiya@gmail.com",
    description="Catkin verb extension to generate clangd compile commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ardiya/catkin-tools-clangd",
    project_urls={
        "Bug Tracker": "https://github.com/ardiya/catkin-tools-clangd/issues",
    },
    classifiers=[
        "Topic :: Software Development :: Build Tools",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">2.7,>=3",
    entry_points={
        "catkin_tools.commands.catkin.verbs": [
            "build_compile_cmd = catkin_tools_clangd.verbs.catkin_build_compile_cmd:description",
        ],
    },
)
