# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda
# SPDX-License-Identifier: Apache-2.0

"""Integration tests: build wheel, install into a fresh venv, run the installed CLI.

Run this with: make integration
"""

from __future__ import annotations

import pathlib
import shutil
import subprocess  # noqa: S404

import pytest
from transcrypto.utils import base

import mycli


@pytest.mark.integration
@pytest.mark.slow
def test_installed_cli_smoke() -> None:
  """Test the installed CLI from the current environment."""
  # find the installed console script; will raise if not found
  cli_path: str | None = shutil.which('mycli')
  if cli_path is None:
    pytest.fail('Console script "mycli" not found in PATH')
  # verify version
  base.VersionCallCheck(pathlib.Path(cli_path), mycli.__version__)
  # basic command smoke tests
  _hello_call(pathlib.Path(cli_path))  # TODO: change


def _hello_call(cli: pathlib.Path) -> None:
  # basic command smoke test; use --no-color to avoid ANSI codes in asserts.
  r: subprocess.CompletedProcess[str] = base.Run(
    # run
    [
      str(cli),
      '--no-color',
      'hello',
      'Ada',
    ]
  )  # TODO: change
  assert 'Hello, Ada!' in r.stdout
  assert '\x1b[' not in r.stdout  # no ANSI escape sequences
  assert '\x1b[' not in r.stderr
