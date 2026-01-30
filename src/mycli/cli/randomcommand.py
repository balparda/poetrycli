# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""CLI: Random commands."""

from __future__ import annotations

import typer
from rich import console as rich_console

from mycli import mycli
from mycli.core import example
from mycli.utils import logging as cli_logging

# Subcommand group: random
_random_app = typer.Typer(no_args_is_help=True)
mycli.app.add_typer(_random_app, name='random', help='Random utilities.')


@_random_app.command('num')
def RandomNum(
  *,
  min_: int = typer.Option(0, '--min', help='Minimum value (inclusive).'),
  max_: int = typer.Option(100, '--max', help='Maximum value (inclusive).'),
) -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Generate a random integer."""  # noqa: DOC501
  if max_ < min_:
    raise typer.BadParameter(f'--max ({max_}) must be >= --min ({min_})')
  console: rich_console.Console = cli_logging.Console()
  console.print(example.RandomNum(min_, max_))


@_random_app.command('str')
def RandomStr(
  *,
  ctx: typer.Context,
  length: int = typer.Option(16, '--length', '-n', min=1, help='String length.'),
  alphabet: str | None = typer.Option(
    None,
    '--alphabet',
    help='Custom alphabet to sample from (defaults to [a-zA-Z0-9]).',
  ),
) -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Generate a random string."""
  config: mycli.MyCLIConfig = ctx.obj  # get application global config
  console: rich_console.Console = cli_logging.Console()
  console.print(
    example.RandomStr(length, alphabet) + (' - in color' if config.color else ' - no colors')
  )
