<!-- SPDX-FileCopyrightText: Copyright 2026 Daniel Balparda <balparda@github.com> -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
# poetrycli - Python/Poetry/Typer/Rich CLI Template

***TODO:*** *One-line description of what this CLI does and who it’s for. Change the title above.*

- **Primary use case:** *<e.g., bulk process files, manage deployments, query APIs>*
- **Works with:** *<e.g., local files, Git repos, Kubernetes, AWS, JSON logs>*
- **Status:** *<stable | beta | experimental>*
- **License:** *<MIT | Apache-2.0 | GPL-3.0 | Proprietary>*

***TODO:*** *throughout this documentation* ***ITALICS*** *mark* ***placeholder content*** *that a new project would typically want to edit with its own information.*

***TODO:*** *If you are starting a new project, there are lots of instructions and useful information in the* "[Appendix **I**: Using the `poetrycli` template](#appendix-i-using-the-poetrycli-template)" *and* [Appendix **II**: Template Checklist](#appendix-ii-template-checklist-turning-poetrycli-into-your-new-cli-project-in-12-steps) *sections.*

**`poetrycli`** is a **template** for building modern Python CLI applications using:

- **Python 3.12** or **Python 3.13** or **Python 3.14**
- **Poetry** for packaging, dependency management, and `venv` workflow
- **Typer** for CLI structure (commands, options, subcommands, help)
- **Rich** for consistent console output and pretty logging
- **Ruff** for formatting + linting
- **MyPy** (and **Pyright/Pylance/typeguard**) for strict type checking
- **Pytest + coverage** for tests
- **pre-commit** + **GitHub Actions CI** to keep everything enforced automatically

The `poetrycli` repo is intentionally opinionated because it was built to help the authors (2-space indentation, single quotes, strict typing, “select ALL rules” linting are examples) but includes escape hatches and ***TODO*** markers to customize quickly. Started in Jan/2026, by ***Daniel Balparda***.

*Since version 0.1.0 it is PyPI package: <https://pypi.org/project/foobarnotreally/>*

***TODO:*** *change this header to match your project's conditions.*

## Table of contents

- [poetrycli - Python/Poetry/Typer/Rich CLI Template](#poetrycli---pythonpoetrytyperrich-cli-template)
  - [Table of contents](#table-of-contents)
  - [License](#license)
    - [*Third-party notices (TODO)*](#third-party-notices-todo)
    - [*Contributions and inbound licensing (TODO)*](#contributions-and-inbound-licensing-todo)
  - [*Installation (TODO)*](#installation-todo)
    - [*Supported platforms (TODO)*](#supported-platforms-todo)
    - [Known dependencies (Prerequisites)](#known-dependencies-prerequisites)
  - [*Context / Problem Space (TODO)*](#context--problem-space-todo)
    - [*What this tool is (TODO)*](#what-this-tool-is-todo)
    - [*What this tool is not (TODO)*](#what-this-tool-is-not-todo)
    - [*Key concepts and terminology* (TODO)](#key-concepts-and-terminology-todo)
    - [*Inputs and outputs (TODO)*](#inputs-and-outputs-todo)
      - [*Inputs (TODO)*](#inputs-todo)
      - [*Outputs (TODO)*](#outputs-todo)
  - [*Design assumptions / Disclaimers (TODO)*](#design-assumptions--disclaimers-todo)
    - [*Guarantees and stability (TODO)*](#guarantees-and-stability-todo)
    - [*Assumptions (TODO)*](#assumptions-todo)
    - [*Known limitations (TODO)*](#known-limitations-todo)
    - [*Deprecation policy (TODO)*](#deprecation-policy-todo)
    - [*Privacy / telemetry (TODO)*](#privacy--telemetry-todo)
  - [*CLI Interface (TODO)*](#cli-interface-todo)
    - [*Quick start (TODO)*](#quick-start-todo)
    - [*Common workflows (TODO)*](#common-workflows-todo)
      - [*Workflow 1 (TODO)*](#workflow-1-todo)
      - [*Workflow 2 (TODO)*](#workflow-2-todo)
    - [*Command structure (TODO)*](#command-structure-todo)
    - [*Global flags (TODO)*](#global-flags-todo)
    - [*Commands overview (TODO)*](#commands-overview-todo)
    - [*Configuration (TODO)*](#configuration-todo)
      - [*Config file locations (TODO)*](#config-file-locations-todo)
      - [*Configuration schema (TODO)*](#configuration-schema-todo)
      - [*Validate configuration (TODO)*](#validate-configuration-todo)
      - [*Environment variables (TODO)*](#environment-variables-todo)
    - [*Input / output behavior (TODO)*](#input--output-behavior-todo)
      - [*`stdin` and piping (TODO)*](#stdin-and-piping-todo)
      - [*Output formats (TODO)*](#output-formats-todo)
      - [*Color and formatting (TODO)*](#color-and-formatting-todo)
      - [*Exit codes (TODO)*](#exit-codes-todo)
    - [*Logging and observability (TODO)*](#logging-and-observability-todo)
    - [*Safety features (TODO)*](#safety-features-todo)
  - [*Project Design (TODO)*](#project-design-todo)
    - [*Architecture overview (TODO)*](#architecture-overview-todo)
    - [*Modules / packages (TODO)*](#modules--packages-todo)
    - [*Data flow (TODO)*](#data-flow-todo)
    - [*Error handling philosophy (TODO)*](#error-handling-philosophy-todo)
    - [*Security model (TODO)*](#security-model-todo)
    - [*Performance characteristics (TODO)*](#performance-characteristics-todo)
  - [Development Instructions](#development-instructions)
    - [File structure](#file-structure)
    - [Development Setup](#development-setup)
      - [*Requirements (TODO)*](#requirements-todo)
      - [Install Python](#install-python)
      - [Install Poetry (recommended: `pipx`)](#install-poetry-recommended-pipx)
      - [Make sure `.venv` is local](#make-sure-venv-is-local)
      - [Get the repository](#get-the-repository)
      - [Create environment and install dependencies](#create-environment-and-install-dependencies)
      - [Optional: VSCode setup](#optional-vscode-setup)
    - [*Build (TODO)*](#build-todo)
    - [*Run locally (TODO)*](#run-locally-todo)
    - [Testing](#testing)
      - [Unit tests / Coverage](#unit-tests--coverage)
      - [Instrumenting your code](#instrumenting-your-code)
      - [*Integration / e2e tests (TODO)*](#integration--e2e-tests-todo)
      - [*Golden tests for CLI output (TODO)*](#golden-tests-for-cli-output-todo)
    - [Linting / formatting / static analysis](#linting--formatting--static-analysis)
      - [Type checking](#type-checking)
    - [*Documentation updates (TODO)*](#documentation-updates-todo)
    - [Versioning and releases](#versioning-and-releases)
      - [Versioning scheme](#versioning-scheme)
      - [Updating versions](#updating-versions)
        - [Bump project version (patch/minor/major)](#bump-project-version-patchminormajor)
        - [Update dependency versions](#update-dependency-versions)
        - [Exporting the `requirements.txt` file](#exporting-the-requirementstxt-file)
        - [Git tag and commit](#git-tag-and-commit)
        - [Publish to PyPI](#publish-to-pypi)
    - [*Contributing (TODO)*](#contributing-todo)
  - [*Security (TODO)*](#security-todo)
    - [*Supported versions (TODO)*](#supported-versions-todo)
    - [*Reporting vulnerabilities (TODO)*](#reporting-vulnerabilities-todo)
    - [*Supply chain (TODO)*](#supply-chain-todo)
  - [*Reliability (TODO)*](#reliability-todo)
    - [*Operational guidance (TODO)*](#operational-guidance-todo)
    - [*Running in automation (TODO)*](#running-in-automation-todo)
    - [*Failure modes (TODO)*](#failure-modes-todo)
  - [*Troubleshooting (TODO)*](#troubleshooting-todo)
    - [*Enable debug output (TODO)*](#enable-debug-output-todo)
    - [*Common issues (TODO)*](#common-issues-todo)
    - [*Collect diagnostics (TODO)*](#collect-diagnostics-todo)
  - [*FAQ (TODO)*](#faq-todo)
    - [*FAQ Section I (TODO)*](#faq-section-i-todo)
      - [*Why does `<project>` need `<permission/dependency>`? (TODO)*](#why-does-project-need-permissiondependency-todo)
      - [*How do I migrate from version X to Y? (TODO)*](#how-do-i-migrate-from-version-x-to-y-todo)
      - [*How stable is the JSON output? (TODO)*](#how-stable-is-the-json-output-todo)
  - [*Glossary (TODO)*](#glossary-todo)
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
      - [Tests + coverage (`pytest`)](#tests--coverage-pytest)
      - [Pre-commit checks](#pre-commit-checks)
      - [CI (GitHub Actions)](#ci-github-actions)
  - [Appendix **II**: Template Checklist: turning `poetrycli` into your new CLI project in 12 steps](#appendix-ii-template-checklist-turning-poetrycli-into-your-new-cli-project-in-12-steps)
    - [0: Prerequisites (one-time per machine)](#0-prerequisites-one-time-per-machine)
    - [1: Decide your identity](#1-decide-your-identity)
    - [2: Rename the Python package directory](#2-rename-the-python-package-directory)
    - [3: Update `pyproject.toml` (the big one)](#3-update-pyprojecttoml-the-big-one)
    - [3.1 Required metadata](#31-required-metadata)
      - [3.2: Poetry packaging + entrypoint wiring](#32-poetry-packaging--entrypoint-wiring)
      - [3.3: If you change Python version…](#33-if-you-change-python-version)
    - [4: Sync the runtime `__version__`](#4-sync-the-runtime-__version__)
    - [5: Update config app name](#5-update-config-app-name)
    - [6: Customize the CLI banner / intro lines](#6-customize-the-cli-banner--intro-lines)
    - [7: Review lint policy (Ruff)](#7-review-lint-policy-ruff)
    - [8: Keep tool versions aligned across files](#8-keep-tool-versions-aligned-across-files)
    - [9: Run the full validation suite (before first commit)](#9-run-the-full-validation-suite-before-first-commit)
    - [10: First release workflow (suggested)](#10-first-release-workflow-suggested)
    - [11:  Update README](#11--update-readme)
    - [12: “Cleanup”](#12-cleanup)

## License

Copyright 2025 Daniel Balparda <balparda@github.com>

Licensed under the ***Apache License, Version 2.0*** (the "License"); you may not use this file except in compliance with the License. You may obtain a [copy of the License here](http://www.apache.org/licenses/LICENSE-2.0).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

### *Third-party notices (TODO)*

*This project includes or depends on third-party software. See:*

- *NOTICE \<link\> (if applicable)*
- *Dependency license list: \<link or section\>*

### *Contributions and inbound licensing (TODO)*

- *Contributions are accepted under: \<same as project license | CLA | DCO\>*
- *Policy: \<link to CONTRIBUTING.md\>*

## *Installation (TODO)*

*To use in your project just do:*

```sh
pip3 install <your_pkg>
```

*and then `from <your_pkg> import <your_library>` (or other parts of the library) for using it.*

### *Supported platforms (TODO)*

- *OS: \<Linux | macOS | Windows\>*
- *Architectures: \<x86_64 | arm64\>*
- *Minimum versions: \<e.g., macOS 12+, Ubuntu 20.04+, Windows 11\>*

### Known dependencies (Prerequisites)

- **[python 3.12](https://python.org/)** - [documentation](https://docs.python.org/3.12/)
- **[rich 14.2+](https://pypi.org/project/rich/)** - Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal - [documentation](https://rich.readthedocs.io/en/latest/)
- **[typer 0.21+](https://pypi.org/project/typer/)** - CLI parser - [documentation](https://typer.tiangolo.com/)
- **[platformdirs 4.5+](https://pypi.org/project/platformdirs/)** - Determines appropriate platform-specific dirs
- **[poetrycli](https://github.com/balparda/poetrycli)** - CLI app templates and utils
- ***TODO:*** *add your main dependencies here too*

## *Context / Problem Space (TODO)*

### *What this tool is (TODO)*

*\<Describe the CLI in one paragraph. Emphasize outcomes and workflows.\>*

### *What this tool is not (TODO)*

- *Not intended for:*
- *Not a replacement for:*

### *Key concepts and terminology* (TODO)

- *A*
- *B*

### *Inputs and outputs (TODO)*

#### *Inputs (TODO)*

- *stdin: \<supported | not supported\>*
- *Files: \<paths, globs, formats\>*
- *Network/API: \<endpoints, services\>*
- *Environment variables/config:*

#### *Outputs (TODO)*

- *stdout: \<human output / structured output\>*
- *stderr: \<errors/logging\>*
- *Files/artifacts:*

## *Design assumptions / Disclaimers (TODO)*

### *Guarantees and stability (TODO)*

- *CLI flags/commands stability: \<stable | may change\>*
- *JSON output stability: \<stable schema | best-effort\>*
- *Backward compatibility:*

### *Assumptions (TODO)*

- *Environment: \<filesystem, permissions, network access\>*
- *Locale/encoding: \<UTF-8 expected?\>*
- *Time/timezone:*

### *Known limitations (TODO)*

- *Scale limits: \<e.g., tested up to 10k files\>*
- *Platform limitations: \<e.g., Windows path edge cases\>*
- *Edge cases: \<symlinks, long paths, etc.\>*

### *Deprecation policy (TODO)*

- *Deprecations are announced via:*
- *Timeline: \<e.g., 2 minor versions\>*
- *Migration guidance:*

### *Privacy / telemetry (TODO)*

- *Telemetry: \<none | optional | on by default\>*
- *What is collected:*
- *How to disable: \<env var | config flag\>*

## *CLI Interface (TODO)*

### *Quick start (TODO)*

*Minimal example.*

```sh
<project> <command> <arg>
```

### *Common workflows (TODO)*

#### *Workflow 1 (TODO)*

```sh
<project> <cmd> --flag value <input>
```

#### *Workflow 2 (TODO)*

```sh
<project> <cmd> <input> --output <file>
```

### *Command structure (TODO)*

General shape:

```sh
<project> [global flags] <command> [command flags] [args]
```

### *Global flags (TODO)*

| Flag | Description | Default |
| --- | --- | --- |
| -h, --help | Show help | |
| --version | Show version | |
| -v, --verbose | Increase log verbosity | \<off\> |
| --quiet | Reduce output | \<off\> |
| --no-color | Disable colorized output | \<auto\> |
| --json | Emit machine-readable JSON | \<off\> |

Add only the flags you actually support.

### *Commands overview (TODO)*

| Command | Description |
| --- | --- |
| `<command1>` | |
| `< command2>` | |
| `help` | Show help for commands |

```sh
Command reference template

Use this template for each command:

<command>
Purpose:

Syntax

<project> <command> [flags] <arg1> [arg2...]

Arguments

- <arg1>:
- <arg2>:

Flags

| Flag | Type | Description | Default |
| --- | --- | --- | --- |
| --foo | string | | <default> |
| --bar | bool | | <false> |

Examples

<project> <command> <arg1>
<project> <command> <arg1> --foo value

Output

- Human mode:
- JSON mode (--json): \<top-level fields / schema link\>
- Files created:

Exit codes

- 0: Success
- 2: Usage error (invalid args)
- 3: Runtime error (network, filesystem, etc.)
- \<other\>:

Common errors

- \<error message\> →
- \<error message\> →
```

### *Configuration (TODO)*

#### *Config file locations (TODO)*

- *Linux: `~/.config/<project>/config.<json|yaml|toml>`*
- *macOS: `~/Library/Application Support/<project>/config.<...>`*
- *Windows: `%APPDATA%\<project>\config.<...>`*

#### *Configuration schema (TODO)*

```yaml
# ~/.config/<project>/config.yaml
profile: default
timeout_ms: 30000
retries: 3
output:
  format: human # or json
  color: auto   # auto|always|never
```

#### *Validate configuration (TODO)*

```sh
<project> config validate
<project> config show --effective
```

#### *Environment variables (TODO)*

| Variable | Description | Default | Notes |
| --- | --- | --- | --- |
| `<PROJECT>_CONFIG` | Config file path | \<auto\> | |
| `<PROJECT>_LOG_LEVEL` | Log level | info | debug |
| `<PROJECT>_NO_COLOR` | Disable color | \<unset\> | obeys `NO_COLOR` too |

### *Input / output behavior (TODO)*

#### *`stdin` and piping (TODO)*

```sh
cat input.txt | <project> <command> --from-stdin
```

#### *Output formats (TODO)*

- *Human-readable (default)*
- *JSON (`--json`) for automation and scripting*

#### *Color and formatting (TODO)*

- *Respects NO_COLOR (recommended)*
- *`--no-color` / `--color`=auto|always|never (if supported)*

#### *Exit codes (TODO)*

| Code | Meaning |
| --- | --- |
| 0 | Success |
| 1 | Generic failure |
| 2 | CLI usage error |
| 3 | Runtime dependency failure (network/filesystem) |
| 4 | Partial success (some items failed) |

*Keep this stable if users will script against it.*

### *Logging and observability (TODO)*

- *Log levels: error|warn|info|debug|trace*
- *Structured logs: \<supported? --log-format=json\>*
- *Debug bundle: \<project\> debug report (if available)*

### *Safety features (TODO)*

- *Dry run: `--dry-run` (no side effects)*
- *Non-interactive: `--yes` / `--no-input`*
- *Force: `--force` (document exactly what it bypasses)*

## *Project Design (TODO)*

### *Architecture overview (TODO)*

*\<High-level description of components and how they interact.\>*

*Example:*

- *CLI parser → configuration loader → core engine → output renderer*
- *Optional: plugins/adapters for external systems*

### *Modules / packages (TODO)*

| Component | Responsibility |
| --- | --- |
| cmd/ | CLI entrypoints and subcommands |
| internal/core/ | Core business logic |
| internal/io/ | Filesystem/network adapters |
| internal/output/ | Output formatting (human/JSON) |

### *Data flow (TODO)*

1. *Parse args + load config*
1. *Validate inputs*
1. *Execute core operation(s)*
1. *Collect results and render output*
1. *Return exit code*

### *Error handling philosophy (TODO)*

- *Clear actionable messages for user errors*
- *Structured errors for --json*
- *Avoid leaking secrets in errors/logs*

### *Security model (TODO)*

- *Principle of least privilege*
- *Secret handling: never log secrets; redact by default*
- *TLS verification: on by default; disabling requires explicit opt-in*

### *Performance characteristics (TODO)*

- *Intended scale:*
- *Complexity notes:*
- *Benchmarks:*

## Development Instructions

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
│       ├── __main__.py
│       ├── cli.py           ⟸ Main CLI app entry point (Main())
│       ├── py.typed
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

### Development Setup

#### *Requirements (TODO)*

#### Install Python

Here is a suggested recipe to install an arbitrary Python version on **Linux**:

```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git python3 python3-dev python3-venv build-essential software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.12  # or python3.13 or python3.14 - TODO: pick a version
```

and on **Mac**:

```sh
brew update
brew upgrade
brew cleanup -s

brew install git python@3.12  # or python3.13 or python3.14 - TODO: pick a version
```

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

If you will use [PyPI](https://pypi.org/) to publish:

```sh
poetry config pypi-token.pypi <TOKEN>  # add your personal PyPI project token, if any
```

#### Make sure `.venv` is local

This template expects a project-local virtual environment at `./.venv` (VSCode settings assume it, for example).

```sh
poetry config virtualenvs.in-project true
```

#### Get the repository

```sh
git clone https://github.com/balparda/poetrycli.git poetrycli  # TODO: change to your project's repo
cd poetrycli
```

#### Create environment and install dependencies

From the repository root:

```sh
poetry env use python3.12  # creates the .venv with the correct Python version - TODO: pick correct Python version
poetry sync                # sync env to project's poetry.lock file
poetry env info            # no-op: just to check that environment looks good
poetry check               # no-op: make sure all pyproject.toml fields are being used correctly

poetry run mycli --help    # simple test if everything loaded OK
make ci                    # should pass OK on clean repo
```

To activate and use the environment do:

```sh
poetry env activate        # (optional) will print activation command for environment, but you can just use:
source .venv/bin/activate  # because .venv SHOULD BE LOCAL
...
pytest -vvv  # for example, or other commands you want to execute in-environment
...
deactivate  # to close environment
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

### *Build (TODO)*

```sh
<build command>
```

### *Run locally (TODO)*

```sh
<project> --help
<run-from-source command>
```

### Testing

#### Unit tests / Coverage

```sh
make test               # plain test run
poetry run pytest -vvv  # verbose test run

make cov  # coverage run, equivalent to: poetry run pytest --cov=src --cov-report=term-missing
```

A test can be marked with a "tag" by just adding a decorator:

```py
@pytest.mark.slow
def test_foo_method() -> None:
  """Test."""
  ...
```

These tags, like `slow` above are defined in `pyproject.toml`, in section `[tool.pytest.ini_options.markers]`, and you can define your own there. The ones already defined are:

| Tag | Meaning |
| --- | --- |
| `slow` | test is slow (> 1s) |
| `flaky` | AVOID! - test is known to be flaky |
| `stochastic` | test is capable of failing (even if very unlikely) |

You can use them to filter tests, for example:

```sh
poetry run pytest -vvv -m slow  # run only the slow tests
```

You can find the slowest tests by running (example suggestions):

```sh
poetry run pytest -vvv -q --durations=20
poetry run pytest -vvv -q --durations=20 -m "not slow"  # find unknown slow methods
poetry run pytest -vvv -q --durations=20 -m slow        # check methods marked `slow` are in fact slow
```

You can search for flaky tests by running `make flakes`, which runs all tests 100 times. Or you can do more, like in the example:

```sh
make flakes  # equivalent to: poetry run pytest --flake-finder --flake-runs=100
poetry run pytest --flake-finder --flake-runs=10000 -m "not slow"
```

#### Instrumenting your code

You can instrument your code to find bottlenecks:

```sh
$ source .venv/bin/activate
$ which mycli
/path/to/.venv/bin/mycli  # <== place this in the command below:
$ pyinstrument -r html -o output1.html -- /path/to/.venv/bin/mycli <your-cli-command> <your-cli-flags>
$ deactivate
```

This will save a file `output1.html` to the project directory with the timings for all method calls. Make sure to **cleanup** these html files later.

#### *Integration / e2e tests (TODO)*

```sh
<integration test command>
```

#### *Golden tests for CLI output (TODO)*

- *Human output:*
- *JSON output:*

### Linting / formatting / static analysis

```sh
make lint  # equivalent to: poetry run ruff check .
make fmt   # equivalent to: poetry run ruff format .
```

To check formatting without rewriting:

```sh
poetry run ruff format --check .
```

#### Type checking

```sh
make type  # equivalent to: poetry run mypy src
```

(Pyright is primarily for editor-time; MyPy is what CI enforces.)

### *Documentation updates (TODO)*

- *How docs are built: \<mkdocs/docusaurus/sphinx/etc.\>*
- *CLI reference generation:*

### Versioning and releases

Make sure you are familiar with the [`poetrycli` Features explained](#poetrycli-features-explained) for this project so you understand the philosophy behind developing for the structure here.

#### Versioning scheme

This project follows a pragmatic versioning approach:

- **Patch**: bug fixes / docs / small improvements.
- **Minor**: new template features or non-breaking developer workflow changes.
- **Major**: breaking template changes (e.g., required file/command renames).

See: [CHANGELOG.md](CHANGELOG.md)

#### Updating versions

##### Bump project version (patch/minor/major)

Poetry can bump versions:

```sh
# bump the version!
poetry version minor  # updates 1.6 to 1.7, for example
# or:
poetry version patch  # updates 1.6 to 1.6.1
# or:
poetry version <version-number>
# (also updates `pyproject.toml` and `poetry.lock`)
```

This updates `[project].version` in `pyproject.toml`. **Remember to also update `src/<your_pkg>/__init__.py` to match (this repo gets/prints `__version__` from there)!**

##### Update dependency versions

To update `poetry.lock` file to more current versions do `poetry update`, it will ignore the current lock, update, and rewrite the `poetry.lock` file. If you have cache problems `poetry cache clear PyPI --all` will clean it.

To add a new dependency you should do:

```sh
poetry add "pkg>=1.2.3"  # regenerates lock, updates env (adds dep to prod code)
poetry add -G dev "pkg>=1.2.3"  # adds dep to dev code ("group" dev)
# also remember: "pkg@^1.2.3" = latest 1.* ; "pkg@~1.2.3" = latest 1.2.* ; "pkg@1.2.3" exact
```

Keep tool versions aligned. This repo pins:

- `ruff` and `mypy` versions in `pyproject.toml`
- and also pins them in `.pre-commit-config.yaml`

If you bump one, bump the other (otherwise you’ll get “works in CI/IDE but fails in pre-commit” mismatches). Remember to check your diffs before submitting (especially `poetry.lock`) to avoid surprises!

##### Exporting the `requirements.txt` file

This template does not generate `requirements.txt` automatically (Poetry uses `poetry.lock`). If you need a `requirements.txt` for Docker/legacy tooling, use Poetry’s export plugin (`poetry-plugin-export`) by simply running:

```sh
poetry export --format requirements.txt --without-hashes --output requirements.txt
```

Tip: If you want auto-export every time the lockfile changes, consider a plugin like `poetry-auto-export` (optional policy choice).

##### Git tag and commit

Publish to GIT, including a TAG:

```sh
git commit -a -m "release version 0.1.0"
git tag 0.1.0
git push
git push --tags
```

##### Publish to PyPI

If you already have your PyPI token registered with Poetry (see [Install Poetry](#install-poetry-recommended-pipx)) then just:

```sh
poetry build
poetry publish
```

### *Contributing (TODO)*

- *See `CONTRIBUTING.md*`
- *Code of conduct: `CODE_OF_CONDUCT.md`*

## *Security (TODO)*

### *Supported versions (TODO)*

- *\<Which versions receive security fixes?\>*

### *Reporting vulnerabilities (TODO)*

*Please report security issues privately via:*

- *Email:*
- *Or: \<security policy link / issue template\>*

***Do not open public issues for suspected vulnerabilities.***

### *Supply chain (TODO)*

- *Dependency pinning:*
- *Signed releases: \<GPG/cosign\>*
- *SBOM: \<available? where?\>*

## *Reliability (TODO)*

### *Operational guidance (TODO)*

- *Recommended timeouts:*
- *Retry behavior:*
- *Idempotency:*

### *Running in automation (TODO)*

- *CI usage examples*
- *Cron usage examples*
- *Non-interactive flags (`--yes`, `--json`, `--quiet`)*

### *Failure modes (TODO)*

- *Network failures:*
- *Partial failures: \<exit code + output behavior\>*
- *Rate limiting:*

## *Troubleshooting (TODO)*

### *Enable debug output (TODO)*

```sh
<project> --verbose
<project> --log-level debug <command>
```

### *Common issues (TODO)*

- *Problem:*
*Cause:*
*Fix:*

- *Problem:*
*Fix:*

### *Collect diagnostics (TODO)*

```sh
<project> debug report --output diagnostics.zip
```

## *FAQ (TODO)*

### *FAQ Section I (TODO)*

#### *Why does `<project>` need `<permission/dependency>`? (TODO)*

*\<Answer\>*

#### *How do I migrate from version X to Y? (TODO)*

*\<Answer + link to migration guide\>*

#### *How stable is the JSON output? (TODO)*

*\<Answer + schema contract\>*

## *Glossary (TODO)*

- A
- B

## Appendix **I**: Using the `poetrycli` template

### New Projects

If you are starting a new CLI app based on [`poetrycli`](https://github.com/balparda/poetrycli), then these are the steps to follow. Know that if you just used the `poetrycli` template to start a new repository then your files in this repo include many `# TODO:` markers to guide you on where to change the files.

**(Note there is also an [Appendix **II**: Template Checklist](#appendix-ii-template-checklist-turning-poetrycli-into-your-new-cli-project-in-12-steps))**

The suggested instructions to start with is:

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
make  # equivalent to: poetry install
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

This repo supports strict typing in three ways:

- **MyPy**: configured via `[tool.mypy]` in `pyproject.toml` (`strict = true`, plus many explicit strict flags)
- **Pyright/Pylance**: configured via `[tool.pyright]` in `pyproject.toml` (`typeCheckingMode = "strict"`)
- **typeguard**: configured in `[tool.pytest.ini_options.typeguard-*]` in `pyproject.toml`

VSCode uses Pylance by default, so you get IDE-time feedback and CI-time enforcement. `typeguard` will be active during tests by default. You can suppress type checking in specific tests by invoking `@typeguard.suppress_type_checks` decorator or context:

```py
import typeguard

@typeguard.suppress_type_checks
def test_crazy_types() -> None:
  # whole method is exempt from typeguard

def test_less_crazy_types_test() -> None:
  # this part of test is type-checked
  with typeguard.suppress_type_checks():
    # this part is not type checked
```

#### Tests + coverage (`pytest`)

Tests run with `pytest`, and CI runs coverage:

```sh
make cov  # equivalent to: poetry run pytest --cov=src --cov-report=term-missing
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
make precommit  # equivalent to: poetry run pre-commit run --all-files
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

## Appendix **II**: Template Checklist: turning `poetrycli` into your new CLI project in 12 steps

This checklist is designed to be **mechanical**: do every step, run the commands, and you’ll end up with a renamed, clean, working project.

### 0: Prerequisites (one-time per machine)

- Install **Python 3.12** (or your chosen target version).
- Install Poetry via `pipx`:

```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install poetry
```

- Configure Poetry to put the virtualenv in-project:

```sh
poetry config virtualenvs.in-project true
```

### 1: Decide your identity

Choose:

- **project name** (PyPI name): e.g. `coolcli`
- **package name** (import name): e.g. `coolcli` (usually same as project name)
- **CLI command** name: e.g. `cool`
- **app config name**: e.g. `coolcli` (used for config directories)

### 2: Rename the Python package directory

1. Rename the package folder: `src/mycli/` → `src/<your_pkg>/`
1. Search/replace imports:

   - `from mycli ...` → `from <your_pkg> ...`
   - `import mycli ...` → `import <your_pkg> ...`

1. Update tests that import the CLI app (e.g. `tests/test_cli.py`).

### 3: Update `pyproject.toml` (the big one)

Open `pyproject.toml` and update all the `# TODO:` markers.

### 3.1 Required metadata

Under `[project]`:

- `name = "mycli"` → your project name
- `version = "0.1.0"` → your initial version
- `description = ...`
- `authors = [...]`
- `license = ...`
- `classifiers` (especially the Python version classifier)
- `requires-python = ">=3.12"` (or your chosen version)
- `license-files = ["LICENSE"]` (keep unless you change licensing docs)

Under `[project.urls]`:

- Homepage/Repository/Issues/Changelog → update to your repo URLs

#### 3.2: Poetry packaging + entrypoint wiring

- Under `[tool.poetry]`: `packages = [{ include = "mycli", from = "src" }]` → update `include` to your package name
- Under `[tool.poetry.scripts]`: `mycli = "mycli.cli:app"` → update both sides:
  - CLI command name (left)
  - import path (right) to match your renamed package
- In `.github/workflows/ci.yaml` update `mycli` name in `typeguard-packages`

#### 3.3: If you change Python version…

There are **at least six** places to update (the file literally warns you). Update all of:

- `[project.classifiers]` → `Programming Language :: Python :: 3.xx`
- `[project.requires-python]`
- `[tool.poetry.dependencies] python = ...`
- `[tool.ruff] target-version = "py3xx"`
- `[tool.mypy] python_version = "3.xx"`
- `[tool.pyright] pythonVersion = "3.xx"`

Also update:

- `.github/workflows/ci.yaml` python matrix version.
- README references

### 4: Sync the runtime `__version__`

The CLI prints `__version__` from your package. Update:

- `src/<your_pkg>/__init__.py` → `__version__ = "<same as pyproject.toml>"`

Update tests that assert version output (there is a version test).

### 5: Update config app name

In `src/<your_pkg>/resources/config.py`: `APP_NAME = 'mycli'` → your app name

This affects where the OS-native config directory lives.

### 6: Customize the CLI banner / intro lines

In `src/<your_pkg>/cli.py`, update:

- the “MYCLI” banner text
- the email/name line
- remove example “foo/bar” options if you don’t want them (or repurpose them).

### 7: Review lint policy (Ruff)

This template uses `select = ["ALL"]` and then ignores a curated list. Decide:

- Keep `ALL` (recommended if you like strictness), or
- Replace `ALL` with a smaller `select` list.

If you want to keep *PascalCase* methods:

- Ensure `N802` remains ignored (that’s the “function name should be lowercase” complaint).

### 8: Keep tool versions aligned across files

- `pyproject.toml` dev deps (ruff/mypy/pytest etc.)
- `.pre-commit-config.yaml` rev pins + mypy `additional_dependencies` pins

Rule of thumb:

- If you bump **ruff** or **mypy** in `pyproject.toml`, bump their pre-commit `rev` too.
- If you bump runtime deps like **rich**/**typer**/**pytest**, update **mypy** hook’s `additional_dependencies` pins.

### 9: Run the full validation suite (before first commit)

From repo root:

```bash
make     # equivalent to: poetry install
make ci  # runs complete CI pipeline
```

Expected:

- Ruff: no diffs after `ruff format .`
- Ruff lint: clean
- MyPy: clean
- Pytest: green
- Coverage: acceptable (note: init/template files are omitted by design)  ￼

### 10: First release workflow (suggested)

1. Ensure version is correct: confirm in `pyproject.toml` + `__init__.py`
1. Run the full validation suite ([Step 9](#9-run-the-full-validation-suite-before-first-commit))
1. Commit, tag, and publish per your release process

### 11:  Update README

- Delete this "Appendix II" from the docs
- You probably want to at least partially keep the rest of the documentation
- Look for TODOs and *ITALICS* for places to edit
- Not all topics and sections are relevant for every project: pick the ones you want, and maybe delete the rest
- rename “mycli” references, usage examples, repo links
- `CHANGELOG.md` (reset it to your new project)
- `LICENSE` file and [README header](#license) if your project changes license/ownership

### 12: “Cleanup”

Once your project is real:

- Remove or repurpose the example commands (Hello, random, etc.)
- Remove `scripts/template.py` if you don’t use direct executable scripts
- Remove `src/<pkg>/utils/template.py` once everyone knows the pattern
- Tighten or relax Ruff ignores based on your team’s preferences

---

*Thanks!* - Daniel Balparda
