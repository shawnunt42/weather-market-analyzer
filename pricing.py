def choose_best_bet(high_temp, low_temp):
    # very simple logic:
    # make a threshold slightly below the forecasted high
    threshold = high_temp - 1

    return {
        "high": high_temp,
        "low": low_temp,
        "threshold": threshold
    }