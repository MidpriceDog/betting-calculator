from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from vig import *
import time
from matplotlib.ticker import LinearLocator


def plot_vig(df, plot_function):
    """Given a dataframe of different moneyline odds, calculate and plot the vig as a function of the odds

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe of moneyline odds
    """
    odds1_arr, odds2_arr = np.array(df['odds1']), np.array(df['odds2'])
    m, n = len(odds1_arr), len(odds2_arr)
    Z = np.ndarray(shape=(m, n))
    for i, odds1 in enumerate(odds1_arr):
        for j, odds2 in enumerate(odds2_arr):
            Z[i][j] = abs(vig_on_moneyline_split(odds1, odds2))

    X, Y = np.meshgrid(odds1_arr, odds2_arr)
    plot_function(X, Y, Z)


def plot_level_curves_3D(X, Y, Z):
    """Plots level curves in 3D plot

    Note: Code modified from matplotlib docs

    Parameters
    ----------
    X : ndarray
        1D array representing the coordinates of a grid on x axis
    Y : ndarray
        1D array representing the coordinates of a grid on y axis
    Z : ndarray
        1D array representing the z axis values
    """
    ax = plt.figure().add_subplot(projection='3d')
    ax.contour(X, Y, Z, cmap=cm.coolwarm)  # Plot contour curves
    plt.show()


def plot_surface(X, Y, Z):
    """Plots 3D surface plot

    Note: Code modified from matplotlib docs

    Parameters
    ----------
    X : ndarray
        1D array representing the coordinates of a grid on x axis
    Y : ndarray
        1D array representing the coordinates of a grid on y axis
    Z : ndarray
        1D array representing the z axis values
    """

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


def plot_surface_with_projected_filled_contours(X, Y, Z):
    """Plots 3D surface plot with filled contour profiles onto the walls of the
    graph to make it easier to visualize changes in elevation.

    Note: Code modified from matplotlib docs

    Parameters
    ----------
    X : ndarray
        1D array representing the coordinates of a grid on x axis
    Y : ndarray
        1D array representing the coordinates of a grid on y axis
    Z : ndarray
        1D array representing the z axis values
    """
    ax = plt.figure().add_subplot(projection='3d')
    # Plot the 3D surface
    ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=5, cstride=5,
                    alpha=0.3)

    # Plot projections of the contours for each dimension.  By choosing offsets
    # that match the appropriate axes limits, the projected contours will sit on
    # the 'walls' of the graph
    ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
    ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
    ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
    plt.show()


if __name__ == "__main__":
    df = pd.DataFrame(
        {'odds1': np.arange(-500, -100), 'odds2': np.arange(100, 500)})
    print(plot_vig(df, plot_function=plot_surface))
