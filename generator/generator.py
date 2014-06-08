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
from json import loads
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

import sys

from markdown import Markdown
from pystache import render

# we use the github API to look some of the fields we require for the template
GH_REPO_API = "https://api.github.com/repos/pa-pyrus/ubernet"


def absolute_directory(string):
    path = Path(string)
    if not path.is_dir():
        msg = "{0} is not a valid directory.".format(string)
        raise ArgumentTypeError(msg)
    return path.resolve()

arg_parser = ArgumentParser(
    description="Generate HTML output from Markdown files")
arg_parser.add_argument("-i", "--input",
                        help="directory containing Markdown files",
                        action="store", type=absolute_directory, required=True)
arg_parser.add_argument("-o", "--output",
                        help="directory HTML output is saved to",
                        action="store", type=absolute_directory, required=True)
arg_parser.add_argument("-t", "--template",
                        help="mustache template used for generating output",
                        action="store", type=FileType("r"), required=True)

arguments = arg_parser.parse_args()

print("Looking up repository info...")
try:
    response = urlopen(GH_REPO_API)
    gh_api = loads(response.read().decode("utf-8"))
    project_title = gh_api["name"].capitalize()
    project_tagline = gh_api["description"]
    owner_name = gh_api["owner"]["login"]
    repository_url = gh_api["html_url"]
    zip_url = "{0}/zipball".format(gh_api["url"])
    tar_url = "{0}/tarball".format(gh_api["url"])
except URLError as err:
    print("Could not look up repository info: {0}".format(err.reason))
    sys.exit(-1)

input_root = arguments.input
print("Looking for input files in {0}...".format(input_root))
input_mds = (md for md in input_root.glob("**/*.md") if md.is_file())

print("Converting input files...")
# set up markdown parser
md_parser = Markdown(extensions=["def_list",
                                 "headerid",
                                 "codehilite"],
                     extension_configs={"codehilite":
                                        [("linenums", False),
                                         ("css_class", "highlight")]},
                     safe_mode="escape",
                     output_format="html5")

# load template
template = arguments.template.read()

output_root = arguments.output
for md_in in input_mds:
    # determine full output name
    relative = md_in.relative_to(input_root)
    html_out_name = str(relative.with_suffix(".html")).replace("/", "_")
    html_out = output_root / html_out_name

    with md_in.open(encoding="utf-8") as md_in_fp:
        raw_md = md_in_fp.read()
        raw_html = md_parser.reset().convert(raw_md)

        # now put it through the template
        context = {"asset_path_prefix": "static/",
                   "project_title": project_title,
                   "project_tagline": project_tagline,
                   "owner_name": owner_name,
                   "repository_url": repository_url,
                   "zip_url": zip_url,
                   "tar_url": tar_url,
                   "main_content": raw_html}
        full_html = render(template, context)

        with html_out.open("w", encoding="utf-8") as html_out_fp:
            print("Writing {0}...".format(html_out_name))
            html_out_fp.write(full_html)
