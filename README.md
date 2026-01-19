# poetrycli — Python 3.12-14 Poetry CLI Template (Typer + Rich + Ruff + MyPy)

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
- **MyPy** (and Pyright/Pylance) for strict type checking
- **Pytest + coverage** for tests
- **pre-commit** + **GitHub Actions CI** to keep everything enforced automatically

The `poetrycli` repo is intentionally opinionated because it was built to help the authors (2-space indentation, single quotes, strict typing, “select ALL rules” linting are examples) but includes escape hatches and ***TODO*** markers to customize quickly. Started in Jan/2026, by ***Daniel Balparda***.

*Since version 0.1.0 it is PyPI package: <https://pypi.org/project/foobarnotreally/>*

***TODO:*** *change this header to match your project's conditions.*

## Table of contents

- [poetrycli — Python 3.12-14 Poetry CLI Template (Typer + Rich + Ruff + MyPy)](#poetrycli--python-312-14-poetry-cli-template-typer--rich--ruff--mypy)
  - [Table of contents](#table-of-contents)
  - [License](#license)
    - [*Third-party notices*](#third-party-notices)
    - [*Contributions and inbound licensing*](#contributions-and-inbound-licensing)
  - [*Installation*](#installation)
    - [*Supported platforms*](#supported-platforms)
    - [Known dependencies (Prerequisites)](#known-dependencies-prerequisites)
  - [*Context / Problem Space*](#context--problem-space)
    - [*What this tool is*](#what-this-tool-is)
    - [*What this tool is not*](#what-this-tool-is-not)
    - [*Key concepts and terminology*](#key-concepts-and-terminology)
    - [*Inputs and outputs*](#inputs-and-outputs)
      - [*Inputs*](#inputs)
      - [*Outputs*](#outputs)
  - [*Design assumptions / Disclaimers*](#design-assumptions--disclaimers)
    - [*Guarantees and stability*](#guarantees-and-stability)
    - [*Assumptions*](#assumptions)
    - [*Known limitations*](#known-limitations)
    - [*Deprecation policy*](#deprecation-policy)
    - [*Privacy / telemetry*](#privacy--telemetry)
  - [*CLI Interface*](#cli-interface)
    - [*Quick start*](#quick-start)
    - [*Common workflows*](#common-workflows)
      - [*Workflow 1*](#workflow-1)
      - [*Workflow 2*](#workflow-2)
    - [*Command structure*](#command-structure)
    - [*Global flags*](#global-flags)
    - [*Commands overview*](#commands-overview)
    - [*Configuration*](#configuration)
      - [Config file locations](#config-file-locations)
      - [*Configuration schema (example)*](#configuration-schema-example)
      - [*Validate configuration*](#validate-configuration)
      - [*Environment variables*](#environment-variables)
    - [*Input / output behavior*](#input--output-behavior)
      - [*`stdin` and piping*](#stdin-and-piping)
      - [*Output formats*](#output-formats)
      - [*Color and formatting*](#color-and-formatting)
      - [*Exit codes*](#exit-codes)
    - [*Logging and observability*](#logging-and-observability)
    - [*Safety features*](#safety-features)
  - [*Project Design*](#project-design)
    - [*Architecture overview*](#architecture-overview)
    - [*Modules / packages*](#modules--packages)
    - [*Data flow*](#data-flow)
    - [*Error handling philosophy*](#error-handling-philosophy)
    - [*Security model (high-level)*](#security-model-high-level)
    - [*Performance characteristics*](#performance-characteristics)
  - [Development Instructions](#development-instructions)
    - [File structure](#file-structure)
    - [Development Setup](#development-setup)
      - [Requirements](#requirements)
      - [Install Poetry (recommended: `pipx`)](#install-poetry-recommended-pipx)
      - [Make sure `.venv` is local](#make-sure-venv-is-local)
      - [Install dependencies](#install-dependencies)
      - [Optional: VSCode setup](#optional-vscode-setup)
    - [*Build*](#build)
    - [*Run locally*](#run-locally)
    - [Testing](#testing)
      - [Unit tests / Coverage](#unit-tests--coverage)
      - [*Integration / e2e tests*](#integration--e2e-tests)
      - [*Golden tests for CLI output*](#golden-tests-for-cli-output)
    - [Linting / formatting / static analysis](#linting--formatting--static-analysis)
      - [Type checking](#type-checking)
    - [*Documentation updates*](#documentation-updates)
    - [Versioning and releases](#versioning-and-releases)
      - [Versioning scheme](#versioning-scheme)
      - [Updating versions](#updating-versions)
        - [Bump project version (patch/minor/major)](#bump-project-version-patchminormajor)
        - [Update dependency versions](#update-dependency-versions)
      - [Exporting `requirements.txt` (optional)](#exporting-requirementstxt-optional)
        - [Install the export plugin (once per machine)](#install-the-export-plugin-once-per-machine)
        - [Export requirements](#export-requirements)
    - [*Contributing*](#contributing)
  - [*Security*](#security)
    - [*Supported versions*](#supported-versions)
    - [*Reporting vulnerabilities*](#reporting-vulnerabilities)
    - [*Supply chain*](#supply-chain)
  - [*Reliability*](#reliability)
    - [*Operational guidance*](#operational-guidance)
    - [\*Running in automation](#running-in-automation)
    - [*Failure modes*](#failure-modes)
  - [*Troubleshooting*](#troubleshooting)
    - [*Enable debug output*](#enable-debug-output)
    - [*Common issues*](#common-issues)
    - [*Collect diagnostics*](#collect-diagnostics)
  - [*FAQ*](#faq)
    - [*FAQ Section I*](#faq-section-i)
      - [*Why does `<project>` need `<permission/dependency>`?*](#why-does-project-need-permissiondependency)
      - [*How do I migrate from version X to Y?*](#how-do-i-migrate-from-version-x-to-y)
      - [*How stable is the JSON output?*](#how-stable-is-the-json-output)
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
  - [*Glossary*](#glossary)

## License

Copyright 2025 Daniel Balparda <balparda@github.com>

Licensed under the ***Apache License, Version 2.0*** (the "License"); you may not use this file except in compliance with the License. You may obtain a [copy of the License here](http://www.apache.org/licenses/LICENSE-2.0).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

### *Third-party notices*

*This project includes or depends on third-party software. See:*

- *NOTICE \<link\> (if applicable)*
- *Dependency license list: \<link or section\>*

### *Contributions and inbound licensing*

- *Contributions are accepted under: \<same as project license | CLA | DCO\>*
- *Policy: \<link to CONTRIBUTING.md\>*

## *Installation*

*To use in your project just do:*

```sh
pip3 install <your_pkg>
```

*and then `from <your_pkg> import <your_library>` (or other parts of the library) for using it.*

### *Supported platforms*

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

## *Context / Problem Space*

### *What this tool is*

*\<Describe the CLI in one paragraph. Emphasize outcomes and workflows.\>*

### *What this tool is not*

- *Not intended for:*
- *Not a replacement for:*

### *Key concepts and terminology*

- *A*
- *B*

### *Inputs and outputs*

#### *Inputs*

- *stdin: \<supported | not supported\>*
- *Files: \<paths, globs, formats\>*
- *Network/API: \<endpoints, services\>*
- *Environment variables/config:*

#### *Outputs*

- *stdout: \<human output / structured output\>*
- *stderr: \<errors/logging\>*
- *Files/artifacts:*

## *Design assumptions / Disclaimers*

### *Guarantees and stability*

- *CLI flags/commands stability: \<stable | may change\>*
- *JSON output stability: \<stable schema | best-effort\>*
- *Backward compatibility:*

### *Assumptions*

- *Environment: \<filesystem, permissions, network access\>*
- *Locale/encoding: \<UTF-8 expected?\>*
- *Time/timezone:*

### *Known limitations*

- *Scale limits: \<e.g., tested up to 10k files\>*
- *Platform limitations: \<e.g., Windows path edge cases\>*
- *Edge cases: \<symlinks, long paths, etc.\>*

### *Deprecation policy*

- *Deprecations are announced via:*
- *Timeline: \<e.g., 2 minor versions\>*
- *Migration guidance:*

### *Privacy / telemetry*

- *Telemetry: \<none | optional | on by default\>*
- *What is collected:*
- *How to disable: \<env var | config flag\>*

## *CLI Interface*

### *Quick start*

*Minimal example.*

```sh
<project> <command> <arg>
```

### *Common workflows*

#### *Workflow 1*

```sh
<project> <cmd> --flag value <input>
```

#### *Workflow 2*

```sh
<project> <cmd> <input> --output <file>
```

### *Command structure*

General shape:

```sh
<project> [global flags] <command> [command flags] [args]
```

### *Global flags*

| Flag | Description | Default |
| --- | --- | --- |
| -h, --help | Show help | |
| --version | Show version | |
| -v, --verbose | Increase log verbosity | \<off\> |
| --quiet | Reduce output | \<off\> |
| --no-color | Disable colorized output | \<auto\> |
| --json | Emit machine-readable JSON | \<off\> |

Add only the flags you actually support.

### *Commands overview*

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

### *Configuration*

#### Config file locations

- Linux: `~/.config/<project>/config.<json|yaml|toml>`
- macOS: `~/Library/Application Support/<project>/config.<...>`
- Windows: `%APPDATA%\<project>\config.<...>`

#### *Configuration schema (example)*

```yaml
# ~/.config/<project>/config.yaml
profile: default
timeout_ms: 30000
retries: 3
output:
  format: human # or json
  color: auto   # auto|always|never
```

#### *Validate configuration*

```sh
<project> config validate
<project> config show --effective
```

#### *Environment variables*

| Variable | Description | Default | Notes |
| --- | --- | --- | --- |
| `<PROJECT>_CONFIG` | Config file path | \<auto\> | |
| `<PROJECT>_LOG_LEVEL` | Log level | info | debug |
| `<PROJECT>_NO_COLOR` | Disable color | \<unset\> | obeys `NO_COLOR` too |

### *Input / output behavior*

#### *`stdin` and piping*

```sh
cat input.txt | <project> <command> --from-stdin
```

#### *Output formats*

- Human-readable (default)
- JSON (--json) for automation and scripting

#### *Color and formatting*

- Respects NO_COLOR (recommended)
- --no-color / --color=auto|always|never (if supported)

#### *Exit codes*

| Code | Meaning |
| --- | --- |
| 0 | Success |
| 1 | Generic failure |
| 2 | CLI usage error |
| 3 | Runtime dependency failure (network/filesystem) |
| 4 | Partial success (some items failed) |

Keep this stable if users will script against it.

### *Logging and observability*

- *Log levels: error|warn|info|debug|trace*
- *Structured logs: \<supported? --log-format=json\>*
- *Debug bundle: \<project\> debug report (if available)*

### *Safety features*

- *Dry run: `--dry-run` (no side effects)*
- *Non-interactive: `--yes` / `--no-input`*
- *Force: `--force` (document exactly what it bypasses)*

## *Project Design*

### *Architecture overview*

*\<High-level description of components and how they interact.\>*

*Example:*

- *CLI parser → configuration loader → core engine → output renderer*
- *Optional: plugins/adapters for external systems*

### *Modules / packages*

| Component | Responsibility |
| --- | --- |
| cmd/ | CLI entrypoints and subcommands |
| internal/core/ | Core business logic |
| internal/io/ | Filesystem/network adapters |
| internal/output/ | Output formatting (human/JSON) |

### *Data flow*

1. *Parse args + load config*
1. *Validate inputs*
1. *Execute core operation(s)*
1. *Collect results and render output*
1. *Return exit code*

### *Error handling philosophy*

- *Clear actionable messages for user errors*
- *Structured errors for --json*
- *Avoid leaking secrets in errors/logs*

### *Security model (high-level)*

- *Principle of least privilege*
- *Secret handling: never log secrets; redact by default*
- *TLS verification: on by default; disabling requires explicit opt-in*

### *Performance characteristics*

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

### Development Setup

#### Requirements

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

### *Build*

```sh
<build command>
```

### *Run locally*

```sh
<project> --help
<run-from-source command>
```

### Testing

#### Unit tests / Coverage

```sh
poetry run pytest
poetry run pytest --cov=src --cov-report=term-missing
```

#### *Integration / e2e tests*

```sh
<integration test command>
```

#### *Golden tests for CLI output*

- *Human output:*
- *JSON output:*

### Linting / formatting / static analysis

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

### *Documentation updates*

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

### *Contributing*

- *See `CONTRIBUTING.md*`
- *Code of conduct: `CODE_OF_CONDUCT.md`*

## *Security*

### *Supported versions*

- *\<Which versions receive security fixes?\>*

### *Reporting vulnerabilities*

*Please report security issues privately via:*

- *Email:*
- *Or: \<security policy link / issue template\>*

***Do not open public issues for suspected vulnerabilities.***

### *Supply chain*

- *Dependency pinning:*
- *Signed releases: \<GPG/cosign\>*
- *SBOM: \<available? where?\>*

## *Reliability*

### *Operational guidance*

- *Recommended timeouts:*
- *Retry behavior:*
- *Idempotency:*

### *Running in automation

- *CI usage examples*
- *Cron usage examples*
- *Non-interactive flags (`--yes`, `--json`, `--quiet`)*

### *Failure modes*

- *Network failures:*
- *Partial failures: \<exit code + output behavior\>*
- *Rate limiting:*

## *Troubleshooting*

### *Enable debug output*

```sh
<project> --verbose
<project> --log-level debug <command>
```

### *Common issues*

- *Problem:*
*Cause:*
*Fix:*

- *Problem:*
*Fix:*

### *Collect diagnostics*

```sh
<project> debug report --output diagnostics.zip
```

## *FAQ*

### *FAQ Section I*

#### *Why does `<project>` need `<permission/dependency>`?*

*\<Answer\>*

#### *How do I migrate from version X to Y?*

*\<Answer + link to migration guide\>*

#### *How stable is the JSON output?*

*\<Answer + schema contract\>*

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
poetry install

poetry run ruff format .
poetry run ruff check .
poetry run mypy src
poetry run pytest --cov=src --cov-report=term-missing

poetry run pre-commit install
poetry run pre-commit run --all-files
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
- rename “mycli” references, usage examples, repo links
- `CHANGELOG.md` (reset it to your new project)
- `LICENSE` file and [README header](#license) if your project changes license/ownership

### 12: “Cleanup”

Once your project is real:

- Remove or repurpose the example commands (Hello, random, etc.)
- Remove `scripts/template.py` if you don’t use direct executable scripts
- Remove `src/<pkg>/utils/template.py` once everyone knows the pattern
- Tighten or relax Ruff ignores based on your team’s preferences

## *Glossary*

- A
- B

---

*Thanks!* - Daniel Balparda
