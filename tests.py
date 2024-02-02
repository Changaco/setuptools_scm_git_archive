import pytest
from setuptools_scm.version import format_version
from setuptools_scm_git_archive import archival_to_version
from setuptools_scm import Configuration


git_archival_mapping = {
    '1.0': {'ref-names': 'HEAD -> master, tag: foo, tag: 1.0'},
    '1.1': {'ref-names': 'HEAD -> master, tag: release-1.1, tag: bar'},
    '1.2': {'ref-names': 'HEAD -> master, tag: v1.2'},
}


@pytest.mark.parametrize('expected,data', sorted(git_archival_mapping.items()))
def test_archival_to_version(expected, data):
    config = Configuration(
        version_scheme="guess-next-dev", local_scheme="node-and-date"
    )
    version = archival_to_version(data, config=config)
    assert version is not None
    assert format_version(version) == expected
