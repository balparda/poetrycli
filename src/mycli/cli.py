# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""CLI name / short purpose.

Delete sections you don't need. Keep this docstring focused and truthful.

Purpose
- What this module does and what it does NOT do.
- Key invariants / assumptions.

Public API
- Main entry points (functions/classes) intended for other modules to import.
- Stability expectations (e.g., "internal/private", "public and stable").

Usage
- Typical usage patterns (short, runnable examples).
- If CLI-related, show how other code calls into it (not necessarily shell commands).

Inputs / Outputs
- Expected inputs, types, constraints.
- What gets printed to stdout vs stderr (if relevant).

Errors and exit codes
- Exceptions raised (and which are "user errors" vs "bugs").
- For CLI-facing modules: mapping to exit codes (if applicable).

Configuration
- Environment variables (e.g., MYCLI_*), config files, defaults.
- Where config is read from and precedence rules.

Performance / limits
- Any complexity notes, big-O, or known bottlenecks.

Security
- Handling of secrets, filesystem paths, command execution, input validation.

Notes
-----
- Links to related modules, design decisions, TODOs.

"""

from __future__ import annotations

import logging
import secrets
import string

import typer
from rich import console as rich_console

from . import __version__, config
from . import logging as cli_logging

# CLI app setup, this is an important object and can be imported elsewhere and called
app = typer.Typer(add_completion=True, no_args_is_help=True)


@app.callback(invoke_without_command=True)  # have only one; this is the "constructor"
def Main(
  version: bool = typer.Option(False, '--version', help='Show version and exit.'),  # noqa: FBT001
  verbose: int = typer.Option(
    0,
    '-v',
    '--verbose',
    count=True,
    help='Verbosity (nothing=ERROR, -v=WARNING, -vv=INFO, -vvv=DEBUG).',
  ),
  foo: int = typer.Option(1000, '-f', '--foo', help='Some integer option.'),
  bar: str = typer.Option('str default', '-b', '--bar', help='Some string option.'),
) -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Set things up; Main CLI entry point."""  # noqa: DOC501
  if version:
    typer.echo(__version__)
    raise typer.Exit(0)
  console: rich_console.Console = cli_logging.InitLogging(verbose)
  console.print('[bold blue]**********************************************[/]')
  console.print(
    '[bold blue]**[/]                 [bold yellow]MYCLI[/]                    [bold blue]**[/]',
  )
  console.print('[bold blue]**   balparda@gmail.com (Daniel Balparda)   **[/]')
  console.print('[bold blue]**********************************************[/]')
  logging.warning(f'Will do foo={foo} and bar={bar!r}')


@app.command()  # create one per command
def ConfigPath() -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Print the config file path."""
  console: rich_console.Console = cli_logging.Console()
  console.print(str(config.GetConfigPath()))


@app.command()  # create one per command
def Hello(name: str = typer.Argument('World')) -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Say hello."""
  console: rich_console.Console = cli_logging.Console()
  console.print(f'Hello, {name}!')


# Subcommand group: random
_random_app = typer.Typer(no_args_is_help=True)
app.add_typer(_random_app, name='random', help='Random utilities.')


@_random_app.command('num')
def RandomNum(
  min_: int = typer.Option(0, '--min', help='Minimum value (inclusive).'),
  max_: int = typer.Option(100, '--max', help='Maximum value (inclusive).'),
) -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Generate a random integer."""  # noqa: DOC501
  if max_ < min_:
    raise typer.BadParameter(f'--max ({max_}) must be >= --min ({min_})')
  console: rich_console.Console = cli_logging.Console()
  console.print(secrets.randbelow(max_ - min_ + 1) + min_)


@_random_app.command('str')
def RandomStr(
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
  console: rich_console.Console = cli_logging.Console()
  chars: str = alphabet or str(string.ascii_letters + string.digits)
  console.print(''.join(secrets.choice(chars) for _ in range(length)))


def Run() -> None:
  """Run the CLI."""
  app()
