"""ClassMetrics - a tiny gradebook tool."""

PASSING = 60


def average(scores):
    """Return the mean of a list of scores."""
    return sum(scores) / len(scores)