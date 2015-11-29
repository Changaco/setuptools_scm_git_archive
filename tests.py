import pytest
from setuptools_scm import format_version
from setuptools_scm_git_archive import archival_to_version


git_archival_mapping = {
    '1.0': {'ref-names': 'HEAD -> master, tag: foo, tag: 1.0'},
    '1.1': {'ref-names': 'HEAD -> master, tag: release-1.1, tag: bar'},
    '1.2': {'ref-names': 'HEAD -> master, tag: v1.2'},
}


@pytest.mark.parametrize('expected,data', sorted(git_archival_mapping.items()))
def test_archival_to_version(expected, data):
    version = archival_to_version(data)
    assert format_version(
        version,
        version_scheme='guess-next-dev',
        local_scheme='node-and-date') == expected
