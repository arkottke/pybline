#!/usr/bin/env python3

import pytest

from numpy.testing import assert_allclose

from pybline.models import TimeSeries


from . import FPATH_DATA


@pytest.fixture()
def ts():
    return TimeSeries.read(
        FPATH_DATA / 'RSN763_LOMAP_GIL067.AT2'
    )


def test_read_at2():
    ts = TimeSeries.read(
        FPATH_DATA / 'RSN763_LOMAP_GIL067.AT2'
    )

    assert len(ts.accels) == 7999
    assert_allclose(ts.time_step, 0.005)
    assert_allclose(
        ts.accels[:5],
        [-0.8075668E-03, -0.8063926E-03, -0.8051829E-03, -0.8039424E-03,
         -0.8026800E-03],
    )


def test_read_acc():
    ts = TimeSeries.read(
        FPATH_DATA / 'set1_TH01_h1.acc'
    )

    assert len(ts.accels) == 7999
    assert_allclose(ts.time_step, 0.005)
    assert_allclose(
        ts.accels[:5],
        [0.19847E-03, 0.19966E-03, 0.20284E-03, 0.20840E-03, 0.21622E-03]
    )
