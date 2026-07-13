==========
rompy-roms
==========


.. image:: https://img.shields.io/pypi/v/rompy_roms.svg
        :target: https://pypi.python.org/pypi/rompy_roms

.. image:: https://img.shields.io/travis/rom-py/rompy_roms.svg
        :target: https://travis-ci.com/rom-py/rompy_roms

.. image:: https://readthedocs.org/projects/rompy-roms/badge/?version=latest
        :target: https://rompy-roms.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Rompy ROMS Config package.


* Free software: BSD license
* Documentation: https://rompy-roms.readthedocs.io.


Features
--------

* TODO



Code Formatting and Pre-commit Hooks
------------------------------------

This repository enforces Python code formatting and linting using [Ruff](https://docs.astral.sh/ruff/) via the pre-commit framework.

To set up pre-commit hooks locally (required for all contributors)::

    pip install pre-commit
    pre-commit install

This will automatically check code formatting and linting before each commit. To format your code manually, run::

    ruff format .

To check formatting and linting without making changes, run::

    ruff check .
    ruff format --check .

Or to run all pre-commit hooks manually::

    pre-commit run --all-files

All code must pass Ruff formatting and linting before it can be committed or merged.

Versioning and Release
----------------------

This project uses [tbump](https://github.com/dmerejkowsky/tbump) for version management.

To bump the version, run::

    tbump <new_version>

This will update the version in `src/rompy_roms/__init__.py`, commit the change, and optionally create a git tag.

tbump is included in the development requirements (`requirements_dev.txt`).

For more advanced configuration, see `tbump.toml` in the project root.
