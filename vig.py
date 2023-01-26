import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def vig(odds_arr):
    """Calculate vig based on odds offered

    Parameters
    ----------
    odds_arr : list
        Odds being offered by a sportsbook

    Returns
    -------
    float
        Vig collected by the sportsbook
    """
    imp_prob_list = []
    for odds in odds_arr:
        if odds > 0:
            # uses formula 1-p/p = odds/100
            implied_prob = 100/(100+odds)
        else:
            implied_prob = abs(odds)/((abs(odds) + 100))
        imp_prob_list.append(implied_prob)
    return sum(imp_prob_list) - 1


if __name__ == "__main__":
    odds_arr1 = [310, 2000, 110, 210]
    odds_arr2 = [450, 3800, 125, 140]
    print(vig(odds_arr2))
