# encoding: utf-8

from attest import Tests
from test.test_runner import runner_unit
from test.test_utils import utils_unit
from test.test_tree import tree_unit
from test.test_toplevel import pkg_unit


def runtests():
    tests = Tests(
        [
            runner_unit,
            utils_unit,
            tree_unit,
            pkg_unit,
        ],
    )
    tests.run()


if __name__ == '__main__':
    runtests()
