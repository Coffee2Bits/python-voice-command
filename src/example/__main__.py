"""Main entry point."""

import sys

from example import APP_NAME

if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = APP_NAME


if __name__ == "__main__":
    from example.do_something import run

    run()
