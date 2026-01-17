# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""Logging configuration."""

from __future__ import annotations

import logging
import threading

from rich import console as rich_console
from rich import logging as rich_logging

_LOG_FORMAT_NO_PROCESS: str = '%(funcName)s: %(message)s'
_LOG_FORMAT_WITH_PROCESS: str = '%(processName)s/' + _LOG_FORMAT_NO_PROCESS
_LOG_FORMAT_DATETIME: str = '[%Y%m%d-%H:%M:%S]'  # e.g., [20240131-13:45:30]
_LOG_LEVELS: list[int] = [logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
_LOG_COMMON_PROVIDERS: set[str] = {
  'werkzeug',
  'gunicorn.error',
  'gunicorn.access',
  'uvicorn',
  'uvicorn.error',
  'uvicorn.access',
  'django.server',
}

__console_lock: threading.RLock = threading.RLock()
__console_singleton: rich_console.Console | None = None


def Console() -> rich_console.Console:
  """Get the global console instance.

  Returns:
    rich.console.Console: The global console instance.

  """
  with __console_lock:
    if __console_singleton is None:
      return rich_console.Console()  # fallback console if InitLogging hasn't been called yet
    return __console_singleton


def ResetConsole() -> None:
  """Reset the global console instance."""
  global __console_singleton  # noqa: PLW0603
  with __console_lock:
    __console_singleton = None


def InitLogging(
  verbosity: int,
  /,
  *,
  include_process: bool = False,
  soft_wrap: bool = False,
) -> rich_console.Console:
  """Initialize logger (with RichHandler) and get a rich.console.Console singleton.

  If you have a CLI app that uses this, its pytests should call `ResetConsole()` in a fixture, like:

      from mycli import logging
      @pytest.fixture(autouse=True)
      def _reset_base_logging() -> Generator[None, None, None]:  # type: ignore
        logging.ResetConsole()
        yield  # stop

  Args:
    verbosity (int): Logging verbosity level: 0==ERROR, 1==WARNING, 2==INFO, 3==DEBUG
    include_process (bool, optional): Whether to include process name in log output.
    soft_wrap (bool, optional): Whether to enable soft wrapping in the console.
        Default is False, and it means rich will hard-wrap long lines (by adding line breaks).

  Returns:
    rich.console.Console: The initialized console instance.

  """
  global __console_singleton  # noqa: PLW0603
  with __console_lock:
    if __console_singleton is not None:
      return __console_singleton
    logging_level: int = _LOG_LEVELS[max(0, min(verbosity, len(_LOG_LEVELS) - 1))]
    console = rich_console.Console(soft_wrap=soft_wrap)
    logging.basicConfig(
      level=logging_level,
      format=_LOG_FORMAT_WITH_PROCESS if include_process else _LOG_FORMAT_NO_PROCESS,
      datefmt=_LOG_FORMAT_DATETIME,
      handlers=[
        rich_logging.RichHandler(  # we show name/line, but want time & level
          console=console,
          rich_tracebacks=True,
          show_time=True,
          show_level=True,
          show_path=True,
        ),
      ],
      force=True,
    )  # force=True to override any previous logging config
    logging.captureWarnings(True)
    for name in _LOG_COMMON_PROVIDERS:
      log: logging.Logger = logging.getLogger(name)
      log.handlers.clear()
      log.propagate = True
      log.setLevel(logging_level)
    __console_singleton = console  # need a global statement to re-bind this one
    logging.info(f'Logging initialized at level {logging.getLevelName(logging_level)}')
    return console
