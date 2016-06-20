# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import pytest
import tempfile
from subprocess import check_output, CalledProcessError


@pytest.fixture(scope='module')
def temp_file(request):
    temp_file = open(tempfile.NamedTemporaryFile().name, 'w+')

    def fin():
        os.unlink(temp_file.name)
        temp_file.close()

    request.addfinalizer(fin)
    return temp_file


def test_script_raises_if_no_arg_given():
    with pytest.raises(CalledProcessError):
        run_cmd('py-minimal')


def test_script_doesnt_raise_if_arg_given(temp_file):
    try:
        run_cmd('py-minimal {}'.format(temp_file.name))
    except CalledProcessError:
        pytest.fail('Should not raise.')


def run_cmd(cmd):
    """Run a shell command `cmd` and return its output."""
    return check_output(cmd, shell=True).decode('utf-8')
