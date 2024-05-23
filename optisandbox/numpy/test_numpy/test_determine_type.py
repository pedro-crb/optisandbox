from optisandbox.numpy.determine_type import *
import pytest
import numpy as np
import casadi as cas


def test_int():
    assert is_casadi_type(5, recursive=True) is False
    assert is_casadi_type(5, recursive=False) is False


def test_float():
    assert is_casadi_type(5., recursive=True) is False
    assert is_casadi_type(5., recursive=False) is False


def test_numpy():
    assert is_casadi_type(
        np.array([1, 2, 3]),
        recursive=True
    ) is False
    assert is_casadi_type(
        np.array([1, 2, 3]),
        recursive=False
    ) is False


def test_casadi():
    assert is_casadi_type(
        cas.MX(np.ones(5)),
        recursive=False
    ) is True
    assert is_casadi_type(
        cas.MX(np.ones(5)),
        recursive=True
    ) is True


def test_numpy_list():
    assert is_casadi_type(
        [np.array(5), np.array(7)],
        recursive=False
    ) is False
    assert is_casadi_type(
        [np.array(5), np.array(7)],
        recursive=True
    ) is False


def test_casadi_list():
    assert is_casadi_type(
        [cas.MX(np.ones(5)), cas.MX(np.ones(5))],
        recursive=False
    ) is False
    assert is_casadi_type(
        [cas.MX(np.ones(5)), cas.MX(np.ones(5))],
        recursive=True
    ) is True


def test_mixed_list():
    assert is_casadi_type(
        [np.array(5), cas.MX(np.ones(5))],
        recursive=False
    ) is False
    assert is_casadi_type(
        [np.array(5), cas.MX(np.ones(5))],
        recursive=True
    ) is True


def test_multi_level_contaminated_list():
    a = [[1 for _ in range(10)] for _ in range(10)]

    assert is_casadi_type(a, recursive=False) is False
    assert is_casadi_type(a, recursive=True) is False

    a[5][5] = cas.MX(1)

    assert is_casadi_type(a, recursive=False) is False
    assert is_casadi_type(a, recursive=True) is True

    a[5][5] = np.array(cas.DM(1), dtype="O")

    assert is_casadi_type(a, recursive=False) is False
    assert is_casadi_type(a, recursive=True) is False


if __name__ == '__main__':
    pytest.main([__file__])
