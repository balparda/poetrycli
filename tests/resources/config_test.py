# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""mycli/resources/config.py unittest."""

from __future__ import annotations

from pathlib import Path
from unittest import mock

from mycli.resources import config


def test_get_config_dir() -> None:
  """Test GetConfigDir returns a Path object."""
  config_dir: Path = config.GetConfigDir()
  assert isinstance(config_dir, Path)
  assert 'mycli' in str(config_dir)


def test_get_config_path() -> None:
  """Test GetConfigPath returns correct config file path."""
  config_path: Path = config.GetConfigPath()
  assert isinstance(config_path, Path)
  assert config_path.name == 'config.toml'
  assert 'mycli' in str(config_path)


def test_get_config_path_uses_config_dir() -> None:
  """Test that GetConfigPath uses GetConfigDir."""
  config_dir: Path = config.GetConfigDir()
  config_path: Path = config.GetConfigPath()
  assert config_path.parent == config_dir


def test_get_config_dir_with_mocked_platformdirs() -> None:
  """Test GetConfigDir with mocked platformdirs."""
  mock_path = Path('/mock/config/path')
  with mock.patch('platformdirs.user_config_path', return_value=mock_path) as mock_func:
    result: Path = config.GetConfigDir()
    assert result == mock_path
    mock_func.assert_called_once_with('mycli')


def test_get_config_path_with_mocked_config_dir() -> None:
  """Test GetConfigPath with mocked GetConfigDir."""
  mock_dir = Path('/mock/config')
  with mock.patch.object(config, 'GetConfigDir', return_value=mock_dir):
    result: Path = config.GetConfigPath()
    assert result == mock_dir / 'config.toml'


def test_app_name_constant() -> None:
  """Test that APP_NAME is set correctly."""
  assert config.APP_NAME == 'mycli'
  assert isinstance(config.APP_NAME, str)
