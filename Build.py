# ----------------------------------------------------------------------
# SPDX-FileCopyrightText: 2024 David Brownell <db@DavidBrownell.com>
# SPDX-License-Identifier: MIT
# ----------------------------------------------------------------------
"""Build tasks for this python module."""

import sys

from pathlib import Path

import typer

from dbrownell_Common import PathEx
from typer.core import TyperGroup

from dbrownell_DevTools.RepoBuildTools import Python as RepoBuildTools


# ----------------------------------------------------------------------
class NaturalOrderGrouper(TyperGroup):
    # pylint: disable=missing-class-docstring
    # ----------------------------------------------------------------------
    def list_commands(self, *args, **kwargs):  # pylint: disable=unused-argument
        return self.commands.keys()


# ----------------------------------------------------------------------
app = typer.Typer(
    cls=NaturalOrderGrouper,
    help=__doc__,
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
    pretty_exceptions_enable=False,
)


# ----------------------------------------------------------------------
this_dir = PathEx.EnsureDir(Path(__file__).parent)
src_dir = PathEx.EnsureDir(this_dir / "src")
tests_dir = PathEx.EnsureDir(this_dir / "tests")


# ----------------------------------------------------------------------
Black = RepoBuildTools.BlackFuncFactory(this_dir, app)

Pylint = RepoBuildTools.PylintFuncFactory(
    src_dir,
    app,
    default_min_score=9.5,
)

Pytest = RepoBuildTools.PytestFuncFactory(
    tests_dir,
    "dbrownell_devtools_test2",
    app,
    default_min_coverage=90.0,
)

UpdateVersion = RepoBuildTools.UpdateVersionFuncFactory(
    src_dir,
    PathEx.EnsureFile(src_dir / "dbrownell_devtools_test2" / "__init__.py"),
    app,
)

Package = RepoBuildTools.PackageFuncFactory(this_dir, app)
Publish = RepoBuildTools.PublishFuncFactory(this_dir, app)
BuildBinary = RepoBuildTools.BuildBinaryFuncFactory(this_dir, app, build_filename="BuildBinary.py")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(app())
