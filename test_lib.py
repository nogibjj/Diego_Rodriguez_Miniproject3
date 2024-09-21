# test the statistics output with a synthetic dataframe
# test the plot if the route exist. from main import add

import polars as pl
import numpy as np
import os

from mylib.lib import summary_statistics, log_func, scatter_plot

file = "test.csv"
y_log = "Log y"
x = "x"
y = "y"
title = "Relationship between x and log(y)"
plot = "test_plot.png"


def test_describe():
    """
    Testing describe function.
    Given that it return a list,
    we are making sure that the order of that list
    is equal to the expected function
    """
    df = pl.read_csv(file)
    sum = summary_statistics(df, x)
    mean_value = df.select(pl.col(x).mean()).item()
    std_value = df.select(pl.col(x).std()).item()
    min_value = df.select(pl.col(x).min()).item()
    q25_value = df.select(pl.col(x).quantile(0.25)).item()
    median_value = df.select(pl.col(x).quantile(0.50)).item()  # Or .quantile(0.50)
    q75_value = df.select(pl.col(x).quantile(0.75)).item()
    max_value = df.select(pl.col(x).max()).item()
    assert sum.row(2)[1] == mean_value
    assert sum.row(3)[1] == std_value
    assert sum.row(4)[1] == min_value
    assert sum.row(5)[1] == q25_value
    assert sum.row(6)[1] == median_value
    assert sum.row(7)[1] == q75_value
    assert sum.row(8)[1] == max_value


def test_log_func():
    """
    Testing that the log function
    is creating a variable using np formula
    """
    df = pl.read_csv(file)
    df = log_func(df, y_log)
    assert (df[y_log] == np.log(df[y_log[4:]])).any()


def test_scatter_plot():
    """Testing that the image exist after running"""
    df = pl.read_csv(file)
    df = log_func(df, y_log)
    scatter_plot(df, x, y_log, title, plot)
    assert os.path.isfile("images/test_plot.png")


def test_markdown_file():
    """testing that the markdown is there"""
    assert os.path.isfile("Data_summary.md")


if __name__ == "__main__":
    test_log_func()
    test_describe()
    test_scatter_plot()
    test_markdown_file()
