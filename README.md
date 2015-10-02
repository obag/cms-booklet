cms-booklet
===========

Introduction
------------

cms-booklet is a tool meant to facilitate the typesetting of olympic problems. It is designed to work well with [CMS](https://github.com/cms-dev/cms), the Contest Management System.

Dependencies
------------

Ensure that you have the texlive suite installed, and check that the latexmk command is available (on some distros you have to install it explicitly but on the serious ones, like ArchLinux, it's installed by default with the standard texlive package).

Installation
------------

To install the `cms-booklet.py` command, we recommend that you use a Python *virtual environment*. So, ensure that you have the `python-virtualenv` package installed. Then run:

```bash
$ virtualenv -p python2 ~/my_venv
```

Where `my_venv` can be anything you want. Then activate it:

```bash
$ source ~/my_venv/bin/activate
```

You should now see that the command line prompt has changed to something like:

```bash
(my_venv) $
```

Now you can freely install cms-booklet by issuing this command:

```bash
(my_venv) $ pip install https://github.com/algorithm-ninja/binder/archive/master.zip
```

Usage
-----

Once installed, you can use the `cms-booklet.py` command like this: put yourself in a directory where a `contest.yaml` file is present, then run the following command.

```bash
(my_venv) $ cms-booklet.py -t cms-contest -l italian contest.yaml
```

Further options
---------------

// TODO
cms-booklet supports these flags:
  - `--keep`: keeps working files 
