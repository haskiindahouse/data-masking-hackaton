import os
import sys
from pathlib import Path

from setuptools import setup
try:
    from sphinx.setup_command import BuildDoc
except ImportError:
    BuildDoc = None

from explorer import get_version


name = "django-masking-sql-explorer"
version = get_version()
release = get_version(True)


def requirements(fname):
    path = os.path.join(os.path.dirname(__file__), "requirements", fname)
    with open(path) as f:
        return f.read().splitlines()


if sys.argv[-1] == "build":
    os.system("python setup.py sdist bdist_wheel")
    print(f"Built release {release} (version {version})")
    sys.exit()

if sys.argv[-1] == "release":
    os.system("twine upload --skip-existing dist/*")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version:")
    os.system(f"git tag -a {version} -m 'version {version}'")
    os.system("git push --tags")
    sys.exit()

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()
