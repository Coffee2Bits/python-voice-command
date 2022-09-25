import logging
from setuptools import find_packages, setup
from src.example import __version__, APP_NAME

README_FILE_PATH: str = "../README.md"

try:
    with open(README_FILE_PATH, "r") as file_handler:
        readme_description = file_handler.read()
except Exception as exception:
    logging.error(f"Failed to open readme file {README_FILE_PATH} with error:\n {exception}")
    readme_description = ""

runtime_dependencies: list[str] = []

development_dependencies: list[str] = [
    "wheel == 0.37.0",
    "tomli < 2.0.0",
    "black == 22.3.0",
    "mccabe == 0.6.1",
    "mypy >= 0.961",
    "types-PyYAML >= 6.0.9",
    "mypy-extensions == 0.4.3",
    "pycodestyle >= 2.8.0",
    "pyflakes >= 2.4",
    "build == 0.7.0",
    "twine == 3.4.2",
    "Sphinx == 4.2.0",
    "sphinxcontrib-applehelp == 1.0.2",
    "sphinxcontrib-devhelp == 1.0.2",
    "sphinxcontrib-htmlhelp == 2.0.0",
    "sphinxcontrib-jsmath == 1.0.1",
    "sphinxcontrib-qthelp == 1.0.3",
    "sphinxcontrib-serializinghtml == 1.1.5",
    "furo == 2021.10.9",
    "pipdeptree >= 2.2.0",
    "Pygments >= 2.5.1",
]

test_dependencies: list[str] = [
    "tox >= 3.24",
    "nose2 >= 0.10.0",
    "coverage >= 6.0",
    "flake8 >= 4.0",
    "flake8-docstrings >= 1.6.0",
    "flake8-fixme >= 1.1.1",
    "flake8-eradicate >= 1.2.0",
    "flake8-assertive >= 1.3.0",
    "eradicate<3.0,>=2.0",
]

setup(
    name=APP_NAME,
    version=__version__,
    description=(
        ""
    ),
    license="",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src", exclude="tests"),
    package_dir={"": "src"},
    package_data={"": []},
    install_requires=runtime_dependencies,
    setup_requires=development_dependencies,
    tests_require=test_dependencies,
    entry_points={
        "console_scripts": [
            f"{APP_NAME}=example.do_something:run",
        ]
    },
    extras_require={
        "test": test_dependencies,
        "dev": development_dependencies,
        "all": test_dependencies + development_dependencies,
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    keywords=["MBSE"],
)
