from os.path import join
import re
import warnings

from setuptools_scm import Configuration
from setuptools_scm.integration import data_from_mime
from setuptools_scm.version import meta, tag_to_version
from setuptools_scm.git import archival_to_version


warnings.warn(DeprecationWarning(
    "This plugin is obsolete. setuptools_scm >= 7.0.0 supports Git archives by itself."
))


config = Configuration()



def parse(root):
    archival = join(root, '.git_archival.txt')
    data = data_from_mime(archival)
    return archival_to_version(data, config)
