# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""Tests for: cli.py."""

from __future__ import annotations

from unittest import mock

import pytest
from click import testing as click_testing
from typer import testing

from mycli import cli

_runner = testing.CliRunner()


def test_version() -> None:
  """Test."""
  result: click_testing.Result = _runner.invoke(cli.app, ['--version'])
  assert result.exit_code == 0
  assert result.stdout.strip() == '0.1.0'
  result = _runner.invoke(cli.app, ['--version', 'hello'])
  assert result.exit_code == 0
  assert result.stdout.strip() == '0.1.0'


def test_hello() -> None:
  """Test."""
  result: click_testing.Result = _runner.invoke(cli.app, ['hello'])
  assert result.exit_code == 0
  assert 'Hello, World!' in result.stdout
  result = _runner.invoke(cli.app, ['hello', 'Ada'])
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
@mock.patch('mycli.cli.cli_logging.Console')
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
  result: click_testing.Result = _runner.invoke(
    cli.app,
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
@mock.patch('mycli.cli.cli_logging.Console')
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
  result: click_testing.Result = _runner.invoke(
    cli.app,
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
@mock.patch('mycli.cli.cli_logging.Console')
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
  result: click_testing.Result = _runner.invoke(cli.app, ['random', 'str', '--length', str(length)])
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
  assert _printed_value(console) == expected


@pytest.mark.parametrize(
  ('alphabet', 'length', 'choices', 'expected'),
  [
    ('abc', 5, ['a', 'b', 'c', 'a', 'b'], 'abcab'),  # cspell:disable-line
    ('01', 6, ['0', '1', '0', '1', '1', '0'], '010110'),
  ],
)
@mock.patch('mycli.core.example.secrets.choice')
@mock.patch('mycli.cli.cli_logging.Console')
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
  result: click_testing.Result = _runner.invoke(
    cli.app,
    ['random', 'str', '--alphabet', alphabet, '--length', str(length)],
  )
  assert result.exit_code == 0, result.output
  assert choice_mock.call_count == length
  # Now we *can* assert the exact alphabet used
  for call in choice_mock.call_args_list:
    assert call[0][0] == alphabet
  console.print.assert_called_once()
  assert _printed_value(console) == expected


@pytest.mark.parametrize(
  'bad_length',
  [
    '0',  # min=1 should reject 0
    '-1',  # negative should be rejected
  ],
)
@mock.patch('mycli.core.example.secrets.choice')
@mock.patch('mycli.cli.cli_logging.Console')
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
  result: click_testing.Result = _runner.invoke(cli.app, ['random', 'str', '--length', bad_length])
  assert result.exit_code != 0
  choice_mock.assert_not_called()
  console_factory_mock.return_value.print.assert_not_called()
