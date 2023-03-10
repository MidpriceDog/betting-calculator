from fractions import Fraction
from decimal import Decimal


def odds_to_implied_probability(odds, odds_type='american'):
    """Converts odds to implied probability. Default type is 'american'

    Parameters
    ----------
    odds : float or Fraction
        Value of american, decimal, or fractional odds

    odds_type : str
        Can be 'american', 'decimal', or 'fractional'

    Returns
    -------
    float
        Returns the implied probability of the provided odds
    """
    if odds_type == 'fractional':
        odds = fractional_to_american(odds)
    elif odds_type == 'decimal':
        odds = decimal_to_american(odds)

    if odds > 0:
        # uses formula 1-p/p = odds/100
        implied_prob = 100/(100+odds)
    else:
        implied_prob = abs(odds)/((abs(odds) + 100))
    return implied_prob


def decimal_to_american(decimal_odds):
    """Converts decimal odds to American odds.

    Examples:
      1.25 -> -400
      2.4 -> 140
      10 -> 900

    Parameters
    ----------
    decimal_odds : float
        Decimal representation of the odds
    """
    if decimal_odds < 2:
        american_odds = -100/(decimal_odds - 1)
    else:
        american_odds = (decimal_odds - 1) * 100
    return int(american_odds)


def american_to_decimal(american_odds):
    """Convert American odds to decimal (European odds)

    Examples:
      400 -> 5.0
      -100 -> 2.0
      -760 -> 1.13

    Parameters
    ----------
    american_odds : int
        American representation of the odds

    Returns
    -------
    float
        Decimal representation of the odds
    """
    if american_odds < 0:
        decimal_odds = 1.0 + 100/(abs(american_odds))
    else:
        decimal_odds = (100+american_odds)/100
    return decimal_odds


def american_to_fractional(american_odds):
    """Convert American odds to fractional odds

    Examples:
      400 -> 4/1
      -200 -> 1/2
      120  -> 6/5

    Parameters
    ----------
    american_odds : int
        American representation of the odds

    Returns
    -------
    Fraction
        Fractional representation of the odds
    """
    decimal_odds = american_to_decimal(american_odds)
    return decimal_to_fractional(decimal_odds)


def fractional_to_american(fractional_odds):
    """Convert fractional odds to American odds

    Examples:
      400 -> 5.0
      -100 -> 2.0
      -760 -> 1.13

    Parameters
    ----------
    fractional_odds : Fraction
        Fractional representation of the odds

    Returns
    -------
    int
        American representation of the odds
    """
    decimal_odds = 1 + fractional_odds.numerator*1.0 / fractional_odds.denominator
    return decimal_to_american(decimal_odds)


def decimal_to_fractional(decimal_odds):
    """Convert decimal odds to fractional odds

    Examples:
      5.0 -> Fraction(4,1)
      2.0 -> Fraction(1,1)
      1.13 -> Fraction(13,100)

    Parameters
    ----------
    decimal_odds : float
        [description]

    Returns
    -------
    Fraction
        Fractional representation of the odds
    """
    fraction = Fraction(decimal_odds - 1.0)
    return fraction


def fractional_to_decimal(fractional_odds):
    """Convert fractional odds to decimal odds

    Parameters
    ----------
    fractional_odds : Fraction
        Fractional representation of the odds

    Returns
    -------
    float
        Decimal representation of the odds
    """
    numerator, denominator = fractional_odds.numerator, fractional_odds.denominator
    decimal_odds = 1 + numerator*1.0/denominator
    return decimal_odds


if __name__ == "__main__":
    print(american_to_decimal(500))
