# ----------------------------------------------------------------------
# SPDX-FileCopyrightText: 2024 David Brownell <db@DavidBrownell.com>
# SPDX-License-Identifier: MIT
# ----------------------------------------------------------------------
# pylint: disable=missing-module-docstring

import os
import sys

# Parse the arguments
is_debug = False
is_force = False
is_verbose = False
is_package = False
no_cache = False

for arg in sys.argv[
    2:
]:  # First arg is the script name, second arg is the name of the shell script to write to
    if arg == "--debug":
        is_debug = True
    elif arg == "--force":
        is_force = True
    elif arg == "--verbose":
        is_verbose = True
    elif arg == "--package":
        is_package = True
    elif arg == "--no-cache":
        no_cache = True
    else:
        raise Exception("Unrecognized argument: {}".format(arg))

if is_debug:
    is_verbose = True

os.system(
    'pip install --disable-pip-version-check {} --editable ".[dev{}]"'.format(
        "--no-cache-dir" if no_cache else "",
        ", package" if is_package else "",
    )
)
