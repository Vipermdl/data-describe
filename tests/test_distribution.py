import numpy as np
import matplotlib
import pytest

import data_describe as dd


matplotlib.use("Agg")


def test_distribution(data):
    fig = dd.distribution(data, plot_all=True)
    assert isinstance(fig, list)
    assert isinstance(fig[0], matplotlib.artist.Artist)


def test_distribution_all(data):
    fig = dd.distribution(data, plot_all=True)
    assert isinstance(fig, list)
    assert isinstance(fig[0], matplotlib.artist.Artist)


def test_distribution_cats(data):
    fig = dd.distribution(data, max_categories=None)
    assert isinstance(fig, list)
    assert isinstance(fig[0], matplotlib.artist.Artist)


def test_distribution_nonimplemented():
    err_type = np.array([1, 2, 3])
    with pytest.raises(NotImplementedError):
        dd.distribution(err_type)