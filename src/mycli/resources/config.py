# SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com>
# SPDX-License-Identifier: Apache-2.0
"""User config paths."""

from __future__ import annotations

from pathlib import Path

import platformdirs

APP_NAME = 'mycli'  # TODO: change this to your app name


def GetConfigDir() -> Path:
  """Get configuration directory.

  Returns:
      Path: Configuration directory path.

  """
  return Path(platformdirs.user_config_path(APP_NAME))


def GetConfigPath() -> Path:
  """Get configuration file path.

  Returns:
      Path: Configuration file path.

  """
  return GetConfigDir() / 'config.toml'
