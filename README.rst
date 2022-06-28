**This plugin is obsolete. ``setuptools_scm >= 7.0.0`` supports Git archives by itself.**

Migration guide
---------------

Change the contents of the ``.git_archival.txt`` file in the root directory of your repository from::

    ref-names: $Format:%D$

to::

    node: $Format:%H$
    node-date: $Format:%cI$
    describe-name: $Format:%(describe:tags=true)$
    ref-names: $Format:%D$

Remove ``setuptools_scm_git_archive`` from your project's dependencies (e.g. the
``setup_requires`` list in your ``setup.py`` file).
