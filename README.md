pip-bundle
==========

[![PyPI Version](https://img.shields.io/pypi/v/pip-bundle.svg)](https://pypi.python.org/pypi/pip-bundle)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pip-bundle.svg)](https://pypi.python.org/pypi/pip-bundle)
[![MIT License](https://img.shields.io/badge/license-mit-blue.svg)](http://choosealicense.com/licenses/mit/)

A quick and dirty script to bundle up all Python dependencies used by a project. Best used with
[virtualenv](https://virtualenv.pypa.io/en/latest/).


# Installation

If you are on OS X and have Homebrew's Python:

    pip install pip-bundle

Otherwise:

    pip install --user pip-bundle

Then make sure to add the local pip's `bin` directory to the `$PATH`. Since it is different on each
platform, please refer to its documentation.

Otherwise, if you're feeling a badass and want to `sudo` your way out, then run:

    sudo pip install pip-bundle


# Usage

Make sure your current directory has the `requirements.txt` file, then run the following command to
create a file called `bundle.pip-bundle`:

    pip-bundle -c

To install the bundle then run:

    pip-bundle bundle.pip-bundle

You can also change the name of the bundle by giving it on the command line:

    pip-bundle -c mybundle.pip-bundle # Create
    pip-bundle mybundle.pip-bundle    # Install

And you can use an alternate name for the `requirements.txt` file:

    pip-bundle -c -r my-own-requirements.txt
