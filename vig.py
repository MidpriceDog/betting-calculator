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
        implied_prob = implied_probability(odds)
        imp_prob_list.append(implied_prob)
    return sum(imp_prob_list) - 1


def implied_probability(odds):
    if odds > 0:
        # uses formula 1-p/p = odds/100
        implied_prob = 100/(100+odds)
    else:
        implied_prob = abs(odds)/((abs(odds) + 100))
    return implied_prob


def odds(implied_prob):
    p = implied_prob
    return 100*(1-p)/p
