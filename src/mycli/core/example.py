# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""Business logic examples."""

from __future__ import annotations

import secrets
import string


def RandomNum(min_: int, max_: int) -> int:
  """Generate a random integer.

  Args:
      min_ (int): Minimum value (inclusive).
      max_ (int): Maximum value (inclusive).

  Returns:
      int: A random integer between min_ and max_ inclusive.

  """
  return secrets.randbelow(int(max_) - int(min_) + 1) + int(min_)


def RandomStr(length: int, alphabet: str | None) -> str:
  # leave this docstring without args/return/raise sections as it shows up in `--help`
  # one way or another the args are well documented in the CLI help and in the code above
  """Generate a random string.

  Args:
      length (int): Length of the random string.
      alphabet (str): Custom alphabet to sample from (defaults to [a-zA-Z0-9]).

  Returns:
      str: A random string of the specified length.

  """
  chars: str = alphabet or str(string.ascii_letters + string.digits)
  return ''.join(secrets.choice(chars) for _ in range(length))
