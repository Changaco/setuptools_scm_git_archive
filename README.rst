**This plugin is obsolete. ``setuptools_scm >= 7.0.0`` supports Git archives by itself.**

This is a `setuptools_scm <https://pypi.python.org/pypi/setuptools_scm>`_ plugin
that adds support for git archives (for example the ones GitHub automatically
generates).

Note that it only works for archives of tagged commits (because git currently
lacks a format option equivalent to ``git describe --tags``).

Usage
-----

Add ``'setuptools_scm_git_archive'`` to the ``setup_requires`` parameter in your
project's ``setup.py`` file:

.. code:: python

    setup(
        ...,
        use_scm_version=True,
        setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
        ...,
    )

Create a ``.git_archival.txt`` file with the following content::

    ref-names: $Format:%D$

Then add this line to the ``.gitattributes`` file::

    .git_archival.txt  export-subst

Finally, don't forget to commit these two files.
