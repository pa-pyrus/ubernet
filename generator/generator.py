#!/usr/bin/env python3
# vim:fileencoding=utf-8:ts=8:et:sw=4:sts=4:tw=79

"""
generator.py: generate HTML output for UberNet API documentation

"THE BEER-WARE LICENSE" (Revision 42):
<pyrus@coffee-break.at> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
"""

from argparse import ArgumentParser, ArgumentTypeError, FileType
from pathlib import Path


def directory_path(string):
    path = Path(string)
    if not path.is_dir():
        msg = "{0} is not a valid directory.".format(string)
        raise ArgumentTypeError(msg)
    return path

parser = ArgumentParser(description="Generate HTML output from Markdown files")
parser.add_argument("-i", "--input",
                    help="the directory containing Markdown files",
                    action="store", type=directory_path, required=True)
parser.add_argument("-o", "--output",
                    help="the directory HTML output is saved to",
                    action="store", type=directory_path, required=True)
parser.add_argument("-t", "--template",
                    help="the mustache template used for generating output",
                    action="store", type=FileType, required=True)

args = parser.parse_args()
