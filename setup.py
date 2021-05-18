from setuptools import setup
import site
import sys
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]


if __name__ == "__main__":
    setup()
