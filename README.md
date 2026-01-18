# poetrycli — Python 3.12-14 Poetry CLI Template (Typer + Rich + Ruff + MyPy)

This repository is a **template** for building modern Python CLI applications using:

- **Python 3.12** or **Python 3.13** or **Python 3.14**
- **Poetry** for packaging, dependency management, and `venv` workflow
- **Typer** for CLI structure (commands, options, subcommands, help)
- **Rich** for consistent console output and pretty logging
- **Ruff** for formatting + linting
- **MyPy** (and Pyright/Pylance) for strict type checking
- **Pytest + coverage** for tests
- **pre-commit** + **GitHub Actions CI** to keep everything enforced automatically

The repo is intentionally opinionated because it was built to help the authors (2-space indentation, single quotes, strict typing, “select ALL rules” linting) but includes escape hatches and TODO markers to customize quickly. Started in Jan/2026, by Daniel Balparda. Since version 0.1.0 it is PyPI package:

<https://pypi.org/project/foobarnotreally/>

**Contents:**

- [poetrycli — Python 3.12-14 Poetry CLI Template (Typer + Rich + Ruff + MyPy)](#poetrycli--python-312-14-poetry-cli-template-typer--rich--ruff--mypy)
  - [License](#license)
  - [Installation](#installation)
  - [Development Instructions](#development-instructions)
    - [Development Setup](#development-setup)
      - [Install Poetry (recommended: `pipx`)](#install-poetry-recommended-pipx)
      - [Make sure `.venv` is local](#make-sure-venv-is-local)
      - [Install dependencies](#install-dependencies)
      - [Optional: VSCode setup](#optional-vscode-setup)
    - [File structure](#file-structure)
    - [Common tasks / workflows](#common-tasks--workflows)
      - [Lint / format](#lint--format)
      - [Type checking](#type-checking)
      - [Tests + coverage](#tests--coverage)
    - [Repository and Poetry Maintenance](#repository-and-poetry-maintenance)
      - [Updating versions](#updating-versions)
        - [Bump project version (patch/minor/major)](#bump-project-version-patchminormajor)
        - [Update dependency versions](#update-dependency-versions)
      - [Exporting `requirements.txt` (optional)](#exporting-requirementstxt-optional)
        - [Install the export plugin (once per machine)](#install-the-export-plugin-once-per-machine)
        - [Export requirements](#export-requirements)
  - [Appendix **I**: Using the `poetrycli` template](#appendix-i-using-the-poetrycli-template)
    - [New Projects](#new-projects)
      - [Rename the package + CLI entrypoint](#rename-the-package--cli-entrypoint)
      - [Update app name used for config paths](#update-app-name-used-for-config-paths)
      - [Pick a Python version (skip if 3.12 is good)](#pick-a-python-version-skip-if-312-is-good)
      - [Customize CLI banner + top-level options](#customize-cli-banner--top-level-options)
      - [Optional: adjust style/lint strictness](#optional-adjust-stylelint-strictness)
    - [`poetrycli` Features explained](#poetrycli-features-explained)
      - [CLI design (Typer)](#cli-design-typer)
      - [Rich logging + Console singleton (`utils/logging.py`)](#rich-logging--console-singleton-utilsloggingpy)
      - [Separation of CLI and business logic](#separation-of-cli-and-business-logic)
      - [Config path helper (`resources/config.py`)](#config-path-helper-resourcesconfigpy)
      - [Strict linting + formatting with Ruff (pyproject.toml)](#strict-linting--formatting-with-ruff-pyprojecttoml)
      - [Typing checks (MyPy + Pyright)](#typing-checks-mypy--pyright)
      - [Tests + coverage (pytest)](#tests--coverage-pytest)
      - [Pre-commit checks](#pre-commit-checks)
      - [CI (GitHub Actions)](#ci-github-actions)

## License

Copyright 2025 Daniel Balparda <balparda@github.com>

Licensed under the ***Apache License, Version 2.0*** (the "License"); you may not use this file except in compliance with the License. You may obtain a [copy of the License here](http://www.apache.org/licenses/LICENSE-2.0).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Installation

To use in your project just do:

```sh
pip3 install <your_pkg>
```

and then `from <your_pkg> import <your_library>` (or other parts of the library) for using it.

Known dependencies:

- **[python 3.12](https://python.org/)** - [documentation](https://docs.python.org/3.12/)
- **[rich 14.2+](https://pypi.org/project/rich/)** - Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal - [documentation](https://rich.readthedocs.io/en/latest/)
- **[typer 0.21+](https://pypi.org/project/typer/)** - CLI parser - [documentation](https://typer.tiangolo.com/)
- **[platformdirs 4.5+](https://pypi.org/project/platformdirs/)** - Determines appropriate platform-specific dirs
- **[poetrycli](https://github.com/balparda/poetrycli)** - CLI app templates and utils

## Development Instructions

### Development Setup

#### Install Poetry (recommended: `pipx`)

[Poetry reference.](https://python-poetry.org/docs/cli/)

Install `pipx` (if you don’t have it):

```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

If you previously had **Poetry** installed, but ***not*** through `pipx` make sure to remove it first: `brew uninstall poetry` (mac) / `sudo apt-get remove python3-poetry` (linux). You should install Poetry with `pipx` and configure poetry to create `.venv/` locally. This keeps Poetry isolated from project virtual environments and python for the environments is isolated from python for Poetry. Do:

```sh
pipx install poetry
poetry --version
```

#### Make sure `.venv` is local

This template expects a project-local virtual environment at `./.venv` (VSCode settings assume it, for example).

```sh
poetry config virtualenvs.in-project true
```

#### Install dependencies

From the repository root:

```sh
poetry install
poetry run mycli --help  # simple test if everything loaded OK
```

#### Optional: VSCode setup

This repo ships a `.vscode/settings.json` configured to:

- use `./.venv/bin/python`
- run `pytest`
- use **Ruff** as formatter
- disable deprecated pylint/flake8 integrations
- configure Google-style docstrings via **autoDocstring**
- use **Code Spell Checker**

Recommended VSCode extensions:

- Python (`ms-python.python`)
- Python Environments (`ms-python.vscode-python-envs`)
- Python Debugger (`ms-python.debugpy`)
- Pylance (`ms-python.vscode-pylance`)
- Mypy Type Checker (`ms-python.mypy-type-checker`)
- Ruff (`charliermarsh.ruff`)
- autoDocstring – Python Docstring Generator (`njpwerner.autodocstring`)
- Code Spell Checker (`streetsidesoftware.code-spell-checker`)
- markdownlint (`davidanson.vscode-markdownlint`)
- Markdown All in One (`yzhang.markdown-all-in-one`) - helps maintain this `README.md` table of contents
- Markdown Preview Enhanced (`shd101wyy.markdown-preview-enhanced`, optional)

### File structure

```txt
.
├── pyproject.toml           ⟸ most important configurations live here
├── LICENSE
├── README.md
├── .pre-commit-config.yaml  ⟸ pre-submit
├── .github/
│   └── workflows/
│       └── ci.yaml          ⟸ Github CI pipeline
├── .vscode/
│   └── settings.json        ⟸ VSCode configs
├── scripts/
│   └── template.py          ⟸ Use template & directory for executable standalone scripts
├── src/
│   └── <your_pkg>/          ⟸ change this directory's name (originally mycli)
│       ├── __init__.py
│       ├── cli.py           ⟸ Main CLI app entry point (Main())
│       ├── core/
│       │   ├── __init__.py
│       │   └── example.py   ⟸ Business logic goes in this directory
│       ├── resources/
│       │   ├── __init__.py
│       │   └── config.py    ⟸ Project resources/files go in this directory
│       └── utils/
│           ├── __init__.py
│           ├── logging.py   ⟸ Useful modules go in this directory; Logging logic for example
│           └── template.py  ⟸ Use template for starting regular modules
└── tests/
    └── test_cli.py          ⟸ Testing goes in this directory
```

What each area is for:

- `src/<your_pkg>/cli.py`: **Typer app** definition, top-level callback (**Main**), and all **commands/subcommands**.
- `src/<your_pkg>/core/example.py`: **“Business logic”** layer. CLI commands call into here. This is the main testable logic layer.
- `src/<your_pkg>/utils/template.py`: A template module showing a recommended docstring structure for **new modules**.
- `src/<your_pkg>/utils/logging.py`: Rich-based **logging** config + a **Console** singleton for consistent output everywhere.
- `src/<your_pkg>/resources/config.py`: **“Where is my config file?”** logic using platformdirs.
- `tests/test_cli.py`: Comprehensive CLI **tests** using Typer’s CliRunner, pytest.mark.parametrize, and unittest.mock.patch.
- `scripts/template.py`: A template for **“directly executable scripts”** (includes a shebang).

Specifically note and use the templates.

- **`src/<your_pkg>/utils/template.py`** is a suggested “module docstring skeleton” (purpose, API, inputs, errors, security, etc.). Copy it when creating new modules.
- **`scripts/template.py`** is a suggested “executable script skeleton” (with shebang) that imports and calls into the package. Scripts should remain thin.

Make sure you are familiar with the [`poetrycli` Features explained](#poetrycli-features-explained) for this project so you understand the philosophy behind developing for the structure here.

### Common tasks / workflows

#### Lint / format

```sh
poetry run ruff check .
poetry run ruff format .
```

To check formatting without rewriting:

```sh
poetry run ruff format --check .
```

#### Type checking

```sh
poetry run mypy src
```

(Pyright is primarily for editor-time; MyPy is what CI enforces.)

#### Tests + coverage

```sh
poetry run pytest
poetry run pytest --cov=src --cov-report=term-missing
```

### Repository and Poetry Maintenance

Make sure you are familiar with the [`poetrycli` Features explained](#poetrycli-features-explained) for this project so you understand the philosophy behind developing for the structure here.

#### Updating versions

##### Bump project version (patch/minor/major)

Poetry can bump versions:

```sh
poetry version patch
poetry version minor
poetry version major
```

This updates `[project].version` in `pyproject.toml`. *Also update `src/<your_pkg>/__init__.py` to match (this repo gets/prints `__version__` from there)!*

Recommended workflow:

1. `poetry version patch` (or `minor`/`major`)
1. update `src/<your_pkg>/__init__.py` (`__version__ = "..."`)
1. run `poetry run <yourcli> --version`
1. run tests + lint + typing
1. commit both files together

##### Update dependency versions

To update locked dependencies:

```sh
poetry update
```

To add a dependency:

```sh
poetry add <package>
```

To add a developer-only dependency:

```sh
poetry add --group dev <package>
```

Keep tool versions aligned. This repo pins:

- `ruff` and `mypy` versions in `pyproject.toml`
- and also pins them in `.pre-commit-config.yaml`

If you bump one, bump the other (otherwise you’ll get “works in CI/IDE but fails in pre-commit” mismatches).

#### Exporting `requirements.txt` (optional)

This template does not generate `requirements.txt` automatically (Poetry uses poetry.lock). If you need a `requirements.txt` for Docker/legacy tooling, use Poetry’s export plugin:

##### Install the export plugin (once per machine)

```sh
poetry self add poetry-plugin-export
```

##### Export requirements

```sh
poetry export -f requirements.txt -o requirements.txt --without-hashes
```

Tip: If you want auto-export every time the lockfile changes, consider a plugin like poetry-auto-export (optional policy choice).

## Appendix **I**: Using the `poetrycli` template

### New Projects

If you are starting a new CLI app based on [`poetrycli`](https://github.com/balparda/poetrycli), then these are the steps to follow. Know that if you just used the `poetrycli` template to start a new repository then your files in this repo include many `# TODO:` markers to guide you on where to change the files. The suggested checklist to start with is:

#### Rename the package + CLI entrypoint

1. Rename the package directory: `src/mycli/` → `src/<your_pkg>/`

1. Update the script entrypoint in `pyproject.toml`:

```toml
[tool.poetry.scripts]
mycli = "mycli.cli:app" → <yourcli> = "<your_pkg>.cli:app"
```

1. Update Poetry packaging (change `mycli` to your package name):

```toml
[tool.poetry]
packages = [{ include = "<your_pkg>", from = "src" }]
```

1. Update the project metadata:

```toml
[project]
name = "<your_pkg>" → your PyPI/project name
also change version, description, authors, classifiers

[project.urls]
change GitHub URLs and others
```

1. Update `src/<your_pkg>/__init__.py`: keep `__version__ = "..."` in sync with `[project].version`.

#### Update app name used for config paths

In `src/<your_pkg>/resources/config.py`:

```py
APP_NAME = '<your_pkg>'  # TODO: change this to your app name
```

Change `APP_NAME` to your app name so config ends up under the correct OS-specific directory.

#### Pick a Python version (skip if 3.12 is good)

This template currently targets **Python 3.12** (or **Python 3.13** or **Python 3.14**). It may possibly work with more versions, but these ones the authors have tested. If you want a different Python version, update the “Python version cluster” in multiple places, *at least* update all of these:

- `pyproject.toml`:
  - [project.classifiers] (e.g., "Programming Language :: Python :: 3.12")
  - [project.requires-python] (e.g., ">=3.12")
  - [tool.poetry.dependencies].python (e.g., "^3.12")
  - [tool.ruff].target-version (e.g., "py312")
  - [tool.mypy].python_version (e.g., "3.12")
  - [tool.pyright].pythonVersion (e.g., "3.12")
- `.github/workflows/ci.yaml`: matrix `python-version`
- `README.md` (this file): Python version references in install instructions

After changing versions, re-create your `.venv` (if you have already created it):

```sh
rm -rf .venv
poetry install
```

#### Customize CLI banner + top-level options

In `src/<your_pkg>/cli.py`, `Main()` prints a banner and logs an example warning:

- Replace banner text (`“<your_pkg>”`, email, etc.)
- Remove example options you don’t want (`--foo`, `--bar`) or rename them into real app options

#### Optional: adjust style/lint strictness

[Ruff rule reference](https://docs.astral.sh/ruff/rules/). This template currently uses:

```toml
[tool.ruff.lint]
select = ["ALL"]
ignore = [...a few specific ones...]
```

If that’s too strict for your team, you can:

- Keep `ALL` and expand the `ignore = [...]` list, or
- Remove `ALL` and select only the groups you want that come commented out by default.

### `poetrycli` Features explained

This documents how to use [`poetrycli`](https://github.com/balparda/poetrycli)-derived projects. Some things here are a result of how this project is organized and meant to be used. Others may be good ideas regardless.

Before continuing it makes sense to make sure you are familiar with the [Development Instructions](#development-instructions) and have gone over the [Development Setup](#development-setup) and understand the [File structure](#file-structure) of the project.

#### CLI design (Typer)

The CLI is defined as a **Typer** application object:

```py
app = typer.Typer(add_completion=True, no_args_is_help=True)
```

A single callback works as the global “constructor”:

```py
@app.callback(invoke_without_command=True)
```

supports out-of-the-box:

- `--version` flag (prints version and exits)
- `-v/--verbose` (verbosity counter)
- example options `--foo` and `--bar`

Verbosity is an integer counter:

- no `-v`: verbosity = 0 → `ERROR` level logging
- `-v`: verbosity = 1 → `WARNING` level logging
- `-vv`: verbosity = 2 → `INFO` level logging
- `-vvv`: verbosity >= 3 → `DEBUG` level logging

The callback calls:

```py
console = cli_logging.InitLogging(verbose)
```

That configures logging and installs a shared **Rich** console singleton. Commands included out-of-the-box:

- `poetry run <yourcli> config-path` → prints the config file path
- `poetry run <yourcli> hello [name]` → prints `Hello, <name>!`

Subcommand **example** group included:

- `poetry run <yourcli> random num --min 0 --max 100`
- `poetry run <yourcli> random str --length 16 [--alphabet ...]`

This is implemented via:

```py
_random_app = typer.Typer(no_args_is_help=True)
app.add_typer(_random_app, name='random', help='Random utilities.')
```

#### Rich logging + Console singleton (`utils/logging.py`)

This is a key opinionated feature of the template. `Console()` returns the global singleton if initialized, otherwise returns a fallback `rich.console.Console()`. This allows any command do:

```py
console = cli_logging.Console()
console.print(...)
```

without worrying whether logging was initialized, which should be done only once:

```py
InitLogging(verbosity, include_process=False, soft_wrap=False)
```

this:

- creates a **Rich** `Console(soft_wrap=...)`
- configures Python logging with `RichHandler`
- sets logging level based on verbosity
- sets `force=True` in `logging.basicConfig(...)` to override prior config
- normalizes logging for “common providers” (uvicorn/gunicorn/etc.) to propagate into your handler
- logs a startup info line: Logging initialized at level ...

*Testing note:* For tests that rely on fresh logging init, call `ResetConsole()` in an `autouse` fixture (there is an example in `tests/test_cli.py`). This prevents cross-test leakage of the singleton.

#### Separation of CLI and business logic

Commands call into `src/<your_pkg>/core/example.py`, which should contain your business logic. Why this pattern is useful:

- CLI remains thin and testable
- Business logic can be tested independently (and reused elsewhere)
- Mocking business logic is cleaner

#### Config path helper (`resources/config.py`)

This is minimal and cross-platform.

- `GetConfigDir()` uses `platformdirs.user_config_path(APP_NAME)`
- `GetConfigPath()` returns `GetConfigDir() / "config.toml"`

So your config location becomes OS-native:

- macOS: `~/Library/Application Support/<APP_NAME>/...`
- Linux: `~/.config/<APP_NAME>/...`
- Windows: user `AppData` equivalent

#### Strict linting + formatting with Ruff (pyproject.toml)

This template uses Ruff for both: `ruff check` (lint) and `ruff format` (format). Key formatting opinions:

```toml
indent-width = 2
quote-style = "single"
docstring-code-format = true
```

Lint configuration by default selects `ALL` rules, then ignores specific rules that conflict with this template’s choices. Notable ignores:

- `N802`: allow PascalCase for function/method names
- `E111`, `E114`: allow 2-space indentation
- formatter-conflict ignores: `D203`, `D213`, `COM812`
- `TC002`: allow “third-party import only used for typing” patterns
- a few practical exceptions for CLI ergonomics and TODO policy

If you want a calmer baseline, remove `"ALL"` and explicitly select rule groups.

#### Typing checks (MyPy + Pyright)

This repo supports strict typing in two ways:

- **MyPy**: configured via `[tool.mypy]` in `pyproject.toml` (`strict = true`, plus many explicit strict flags)
- **Pyright/Pylance**: configured via `[tool.pyright]` in `pyproject.toml` (`typeCheckingMode = "strict"`)

VSCode uses Pylance by default, so you get IDE-time feedback and CI-time enforcement.

#### Tests + coverage (pytest)

Tests run with `pytest`, and CI runs coverage:

```sh
poetry run pytest --cov=src --cov-report=term-missing
```

Coverage configuration in `pyproject.toml` omits:

- `*/__init__.py`
- `*/__main__.py`
- `*/template.py`

Rationale: these files should remain “thin” and are usually not meaningful coverage targets.

#### Pre-commit checks

File `.pre-commit-config.yaml` defines hooks for Ruff lint (`ruff-check`), Ruff format (`ruff-format`), and MyPy (`mypy`). Install hooks:

```sh
poetry run pre-commit install
```

Run on all files:

```sh
poetry run pre-commit run --all-files
```

Important: pre-commit runs tools in its own isolated environments pinned by `rev:` so if you bump Ruff/MyPy versions in `pyproject.toml` remember to update `.pre-commit-config.yaml` too.

[Ruff pre-commit reference.](https://github.com/astral-sh/ruff-pre-commit)

#### CI (GitHub Actions)

File `.github/workflows/ci.yaml` runs on pushes and PRs:

- `poetry install`
- `ruff check .`
- `ruff format --check .`
- `mypy src`
- `pytest --cov=src --cov-report=term-missing`

CI is the “source of truth” that the template remains clean.

---

*Thanks!* - Daniel Balparda
