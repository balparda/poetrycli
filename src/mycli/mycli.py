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
from dataclasses import dataclass

import typer
from rich import console as rich_console

from . import __version__
from .cli import clibase
from .core import example
from .resources import config
from .utils import logging as cli_logging


@dataclass(kw_only=True, slots=True, frozen=True)
class MyCLIConfig(clibase.CLIConfig):
  """MyCLI global context, storing the configuration."""

  foo: int
  bar: str


# CLI app setup, this is an important object and can be imported elsewhere and called
app = typer.Typer(add_completion=True, no_args_is_help=True)


def Run() -> None:
  """Run the CLI."""
  app()


@app.callback(invoke_without_command=True)  # have only one; this is the "constructor"
@clibase.CLIErrorGuard
def Main(  # documentation is help/epilog/args # noqa: D103
  *,
  ctx: typer.Context,  # global context
  version: bool = typer.Option(False, '--version', help='Show version and exit.'),
  verbose: int = typer.Option(
    0,
    '-v',
    '--verbose',
    count=True,
    help='Verbosity (nothing=ERROR, -v=WARNING, -vv=INFO, -vvv=DEBUG).',
    min=0,
    max=3,
  ),
  color: bool | None = typer.Option(
    None,
    '--color/--no-color',
    help=(
      'Force enable/disable colored output (respects NO_COLOR env var if not provided). '
      'Defaults to having colors.'  # state default because None default means docs don't show it
    ),
  ),
  foo: int = typer.Option(1000, '-f', '--foo', help='Some integer option.'),
  bar: str = typer.Option('str default', '-b', '--bar', help='Some string option.'),
) -> None:
  if version:
    typer.echo(__version__)
    raise typer.Exit(0)
  console: rich_console.Console
  console, verbose, color = cli_logging.InitLogging(
    verbose,
    color=color,
    include_process=False,  # decide if you want process names in logs
    soft_wrap=False,  # decide if you want soft wrapping of long lines
  )
  # create context with the arguments we received
  ctx.obj = MyCLIConfig(console=console, verbose=verbose, color=color, foo=foo, bar=bar)
  # print / log / etc
  console.print('[bold blue]**********************************************[/]')
  console.print(  # TODO: change your intro lines to taste
    '[bold blue]**[/]                 [bold yellow]MYCLI[/]                    [bold blue]**[/]',
  )
  console.print('[bold blue]**   balparda@gmail.com (Daniel Balparda)   **[/]')
  console.print('[bold blue]**********************************************[/]')
  logging.warning(f'Will do foo={foo} and bar={bar!r}')


@app.command(
  'markdown',
  help='Emit Markdown docs for the CLI (see README.md section "Creating a New Version").',
  epilog=('Example:\n\n\n\n$ poetry run mycli markdown > mycli.md\n\n<<saves CLI doc>>'),
)
@clibase.CLIErrorGuard
def Markdown(*, ctx: typer.Context) -> None:  # documentation is help/epilog/args # noqa: D103
  config: MyCLIConfig = ctx.obj
  config.console.print(clibase.GenerateTyperHelpMarkdown(app, prog_name='mycli'))


@app.command()  # create one per command
def ConfigPath() -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Print the config file path."""
  console: rich_console.Console = cli_logging.Console()
  console.print(str(config.GetConfigPath()))


@app.command()  # create one per command
def Hello(ctx: typer.Context, name: str = typer.Argument('World')) -> None:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Say hello."""
  config: MyCLIConfig = ctx.obj  # get application global config
  console: rich_console.Console = cli_logging.Console()
  console.print(f'{config.foo} times "Hello, {name}!"')


# Subcommand group: random
_random_app = typer.Typer(no_args_is_help=True)
app.add_typer(_random_app, name='random', help='Random utilities.')


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
  config: MyCLIConfig = ctx.obj  # get application global config
  console: rich_console.Console = cli_logging.Console()
  console.print(
    example.RandomStr(length, alphabet) + (' - in color' if config.color else ' - no colors')
  )
