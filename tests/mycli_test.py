# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""Tests for: cli.py."""

from __future__ import annotations

from collections import abc
from unittest import mock

import pytest
import typeguard
from click import testing as click_testing
from typer import testing

from mycli import mycli
from mycli.core import example
from mycli.utils import logging as cli_logging


def _CallCLI(args: list[str]) -> click_testing.Result:
  """Call the CLI with args.

  Args:
      args (list[str]): CLI arguments.

  Returns:
      click_testing.Result: CLI result.

  """
  with typeguard.suppress_type_checks():  # <-- example of suppressing typeguard checks
    # we suppress type checks here because CliRunner.invoke expects a click.Command,
    # but we are passing a typer.Typer (which is a subclass of click.Command)
    return testing.CliRunner().invoke(mycli.app, args)


@pytest.fixture(autouse=True)
def reset_cli_logging_singletons() -> abc.Generator[None, None, None]:
  """Reset global console/logging state between tests.

  The CLI callback initializes a global Rich console singleton via InitLogging().
  Tests invoke the CLI multiple times across test cases, so we must reset that
  singleton to keep tests isolated.
  """
  cli_logging.ResetConsole()
  yield  # noqa: PT022


def test_version_flag() -> None:
  """Test."""
  result: click_testing.Result = _CallCLI(['--version'])
  assert result.exit_code == 0
  assert result.stdout.strip() == '0.1.0'


def test_version_flag_ignores_extra_args() -> None:
  """Test."""
  result: click_testing.Result = _CallCLI(['--version', 'hello'])
  assert result.exit_code == 0
  assert result.stdout.strip() == '0.1.0'


def test_hello_default_name() -> None:
  """Test."""
  result: click_testing.Result = _CallCLI(['hello'])
  assert result.exit_code == 0
  assert 'Hello, World!' in result.stdout


def test_hello_custom_name() -> None:
  """Test."""
  result: click_testing.Result = _CallCLI(['hello', 'Ada'])
  assert result.exit_code == 0
  assert 'Hello, Ada!' in result.stdout


# -------------------------------------------------------------------------------------------------


def _printed_value(console_mock: mock.Mock) -> object:
  """Return first argument passed to console.print(...).

  Args:
      console_mock (mock.Mock): console mock.

  Returns:
      object: first argument passed to console.print(...).

  """
  # console.print is a Mock; .call_args is (args, kwargs)
  args, _kwargs = console_mock.print.call_args
  return args[0] if args else None


def _assert_random_str_printed_value(printed: object, expected_prefix: str) -> None:
  """Assert RandomStr output matches CLI behavior.

  RandomStr prints the generated string plus a suffix that depends on whether color is enabled.
  We don't want tests to depend on NO_COLOR env var or rich console internals, so accept either.
  """
  assert isinstance(printed, str)
  assert printed.startswith(expected_prefix)
  suffix: str = printed[len(expected_prefix) :]
  assert suffix in {' - in color', ' - no colors'}


# -------------------------------------------------------------------------------------------------
# random num
# -------------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
  ('min_', 'max_', 'randbelow_return', 'expected'),
  [
    # If min=0 max=0, range size is 1, randbelow(1) must return 0, expected = 0
    (0, 0, 0, 0),
    # min=0 max=10 -> range size 11
    # if randbelow returns 0 => 0
    (0, 10, 0, 0),
    # min=0 max=10 -> if randbelow returns 10 => 10
    (0, 10, 10, 10),
    # min=10 max=20 -> range size 11
    # if randbelow returns 0 => 10
    (10, 20, 0, 10),
    # min=10 max=20 -> if randbelow returns 10 => 20
    (10, 20, 10, 20),
    # negative ranges also work
    (-5, 5, 0, -5),
    (-5, 5, 10, 5),
  ],
)
@mock.patch('mycli.core.example.secrets.randbelow')
@mock.patch('mycli.mycli.cli_logging.Console')
def test_random_num_prints_expected_integer(
  console_factory_mock: mock.Mock,
  randbelow_mock: mock.Mock,
  min_: int,
  max_: int,
  randbelow_return: int,
  expected: int,
) -> None:
  """Test.

  Didactic notes:
  - We patch secrets.randbelow so the test is deterministic.
  - We patch cli_logging.Console so we can assert on console.print(...) without writing to stdout.
  - We run the command through CliRunner to test the real CLI wiring.
  """
  # Arrange
  console = mock.Mock()
  console_factory_mock.return_value = console
  randbelow_mock.return_value = randbelow_return
  # Act
  result: click_testing.Result = _CallCLI(
    ['random', 'num', '--min', str(min_), '--max', str(max_)],
  )
  # Assert
  assert result.exit_code == 0, result.output
  # Verify the randomness function was called correctly:
  randbelow_mock.assert_called_once_with(max_ - min_ + 1)  # range_size = (max - min + 1)
  # Verify we printed exactly the expected number
  console.print.assert_called_once()
  assert _printed_value(console) == expected


@pytest.mark.parametrize(
  ('min_', 'max_'),
  [
    (1, 0),
    (10, 9),
    (0, -1),
  ],
)
@mock.patch('mycli.core.example.secrets.randbelow')
@mock.patch('mycli.mycli.cli_logging.Console')
def test_random_num_rejects_invalid_range(
  console_factory_mock: mock.Mock,
  randbelow_mock: mock.Mock,
  min_: int,
  max_: int,
) -> None:
  """Test.

  Didactic notes:
  - When max < min, your command raises typer.BadParameter.
  - CliRunner captures that and returns a non-zero exit code.
  - In this failure path, randbelow should never be called and we should not print anything.
  """
  console_factory_mock.return_value = mock.Mock()
  result: click_testing.Result = _CallCLI(
    ['random', 'num', '--min', str(min_), '--max', str(max_)],
  )
  assert result.exit_code != 0
  randbelow_mock.assert_not_called()
  # It's okay if your command prints an error (Typer/Click will emit error text).
  # We just ensure our console printing didn't happen.
  console_factory_mock.return_value.print.assert_not_called()


# -------------------------------------------------------------------------------------------------
# random str
# -------------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
  ('length', 'choices', 'expected'),
  [
    # simplest case: 1 character
    pytest.param(1, ['A'], 'A', id='only As'),
    # multiple characters: join of choices in order
    pytest.param(4, ['a', 'b', 'c', 'd'], 'abcd', id='a to d'),  # <== you can name test cases!!
    # length 8
    pytest.param(8, list('ABCDEFGH'), 'ABCDEFGH', id='A to H'),
  ],
)
@mock.patch('mycli.core.example.secrets.choice')
@mock.patch('mycli.mycli.cli_logging.Console')
def test_random_str_default_alphabet_prints_expected(
  console_factory_mock: mock.Mock,
  choice_mock: mock.Mock,
  length: int,
  choices: list[str],
  expected: str,
) -> None:
  """Test.

  Didactic notes:
  - RandomStr uses secrets.choice(chars) inside a generator expression.
  - We patch secrets.choice and provide a side_effect list so each call returns a known char.
  - We still run through the CLI to verify command registration and argument parsing.
  """
  console = mock.Mock()
  console_factory_mock.return_value = console
  # Each call to secrets.choice returns the next item from choices
  choice_mock.side_effect = choices
  result: click_testing.Result = _CallCLI(['random', 'str', '--length', str(length)])
  assert result.exit_code == 0, result.output
  # We should call choice exactly 'length' times
  assert choice_mock.call_count == length
  # For default alphabet, RandomStr uses ascii_letters + digits
  # We don't need to replicate that exact string here; instead we assert:
  # - choice was called with a string
  # - and it's the same object each time (the same alphabet)
  first_call_arg = choice_mock.call_args_list[0][0][0]
  assert isinstance(first_call_arg, str)
  for call in choice_mock.call_args_list:
    assert call[0][0] == first_call_arg
  console.print.assert_called_once()
  _assert_random_str_printed_value(_printed_value(console), expected)


@pytest.mark.slow  # <-- example of marking a test as slow
@pytest.mark.parametrize(
  ('alphabet', 'length', 'choices', 'expected'),
  [
    ('abc', 5, ['a', 'b', 'c', 'a', 'b'], 'abcab'),  # cspell:disable-line
    ('01', 6, ['0', '1', '0', '1', '1', '0'], '010110'),
  ],
)
@mock.patch('mycli.core.example.secrets.choice')
@mock.patch('mycli.mycli.cli_logging.Console')
def test_random_str_custom_alphabet_is_used(
  console_factory_mock: mock.Mock,
  choice_mock: mock.Mock,
  alphabet: str,
  length: int,
  choices: list[str],
  expected: str,
) -> None:
  """Test.

  Didactic notes:
  - This ensures that when --alphabet is provided, we pass THAT alphabet to secrets.choice,
    rather than the default [a-zA-Z0-9] alphabet.
  """
  console = mock.Mock()
  console_factory_mock.return_value = console
  choice_mock.side_effect = choices
  result: click_testing.Result = _CallCLI(
    ['random', 'str', '--alphabet', alphabet, '--length', str(length)],
  )
  assert result.exit_code == 0, result.output
  assert choice_mock.call_count == length
  # Now we *can* assert the exact alphabet used
  for call in choice_mock.call_args_list:
    assert call[0][0] == alphabet
  console.print.assert_called_once()
  _assert_random_str_printed_value(_printed_value(console), expected)


# @typeguard.suppress_type_checks  # <-- example of suppressing typeguard checks
@pytest.mark.parametrize(
  'bad_length',
  [
    '0',  # min=1 should reject 0
    '-1',  # negative should be rejected
  ],
)
@mock.patch('mycli.core.example.secrets.choice')
@mock.patch('mycli.mycli.cli_logging.Console')
def test_random_str_rejects_non_positive_length(
  console_factory_mock: mock.Mock,
  choice_mock: mock.Mock,
  bad_length: str,
) -> None:
  """Test.

  Didactic notes:
  - In your command signature you used: length: int = typer.Option(..., min=1, ...)
  - Typer/Click enforces this before your function body runs.
  - Therefore: secrets.choice should not be called, and no console printing should happen.
  """
  console_factory_mock.return_value = mock.Mock()
  result: click_testing.Result = _CallCLI(['random', 'str', '--length', bad_length])
  assert result.exit_code != 0
  choice_mock.assert_not_called()
  console_factory_mock.return_value.print.assert_not_called()
  with typeguard.suppress_type_checks():  # <-- example of suppressing typeguard checks
    # this method "works" but typeguard complains about int/float mix
    assert example.RandomNum(1, 1.1) == 1  # type: ignore
