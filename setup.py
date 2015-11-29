from os.path import dirname, isdir, join
from shutil import rmtree

from pkg_resources import DistributionNotFound, load_entry_point, working_set
from setuptools import find_packages, setup


ENTRY_GROUP = 'setuptools_scm.parse_scm'
ENTRY_NAME = '.git_archival.txt'
ENTRY_POINT = ENTRY_NAME + ' = setuptools_scm_git_archive:parse'

meta = dict(
    name='setuptools_scm_git_archive',
    description='setuptools_scm plugin for git archives',
    author='Changaco',
    author_email='changaco@changaco.oy.lc',
    url='https://github.com/Changaco/setuptools_scm_git_archive/',
    license='MIT',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    keywords='scm vcs version tags git archive',
    setup_requires=['setuptools_scm'],
    entry_points={ENTRY_GROUP: ENTRY_POINT},
)

# Clean up first, old eggs seem to confuse setuptools_scm
rmtree(meta['name']+'.egg-info', ignore_errors=True)

# Bootstrap
if not isdir('.git'):
    setup(version='0', **meta)
    working_set.add_entry('.')

setup(use_scm_version=True, **meta)
