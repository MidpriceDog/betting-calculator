import odds_converter as oc
from scipy.linalg import lstsq
from scipy.linalg import inv
import pandas as pd
import numpy as np


pd.set_option('display.float_format', lambda x: '%.3f' % x)
np.set_printoptions(suppress=True)


def make_payoff_matrix(diagonal):
    """Creates payoff matrix with the provided diagonal. Every off-diagonal entry
    is -1 because the amount lost is equal to the amount bet in the event of a losing
    bet. The payoff in the event bet i wins is the diagonal entry i.
    Parameters
    ----------
    diagonal : int
        American Odds for multiple bets
    Returns
    -------
    np.ndarray
        Payoff matrix
    """
    for i, american_odds in enumerate(diagonal):
        # Convert from American odds to European
        diagonal[i] = oc.american_to_decimal(american_odds)
    n = len(diagonal)
    payoff_matrix = np.ndarray(shape=(n, n))
    payoff_matrix.fill(0)
    for i in range(n):
        payoff_matrix[i][i] = diagonal[i]
    return payoff_matrix - 1


def calculate_hedged_bets(payoff_matrix, b_column_vector):
    """Calculates bet sizes to make using a supplied payoff matrix in order to
    make a series of bets that hedge so the same profit is achieved no matter
    what outcome materializes.
    Parameters
    ----------
    payoff_matrix : np.ndarray
        Payoff matrix from placing multiple bets
    Returns
    -------
    np.ndarray
        Column vector of bet sizes to make
    """
    A = payoff_matrix
    b = b_column_vector
    bets, residuals, rank, s = lstsq(A, b)

    if (bets < 0).any():
        bets[:] = np.nan
    return bets


def calculate_risk_free_bets(payoff_matrix):
    """Calculates bet sizes to make using a supplied payoff matrix in order to
    make a single unit of profit no matter what outcome materializes. In other
    words, calculates bets to place to make a risk-free profit.
    Parameters
    ----------
    payoff_matrix : np.ndarray
        Payoff matrix from placing multiple bets
    Returns
    -------
    np.ndarray
        Column vector of bet sizes to make
    """
    n = len(payoff_matrix)
    b_column_vector = np.ndarray(shape=(n, 1))
    b_column_vector.fill(1)
    inv_payoff_matrix = inv(payoff_matrix)
    return inv_payoff_matrix @ b_column_vector


if __name__ == "__main__":
    m = make_payoff_matrix([-280, 380])
    print(calculate_risk_free_bets(m))
