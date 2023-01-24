import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def vig_on_moneyline_split(odds1, odds2):
    """Calculate vig based on the moneyline split odds

    Parameters
    ----------
    odds1 : int
        Odds being offered by a sportsbook on one side
    odds2 : int
        Odds being offered by the sportsbook on the other side

    Returns
    -------
    float
        Vig collected by the sportsbook on the split
    """
    imp_prob_list = []
    for odds in [odds1, odds2]:
        if odds > 0:
            # uses formula 1-p/p = odds/100
            implied_prob = 100/(100+odds)
        else:
            implied_prob = abs(odds)/((abs(odds) + 100))
        imp_prob_list.append(implied_prob)

    return sum(imp_prob_list) - 1

