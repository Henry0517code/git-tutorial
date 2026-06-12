"""ClassMetrics - a tiny gradebook tool."""

PASSING = 60


def average(scores):
    """Return the mean of a list of scores."""
    return sum(scores) / len(scores)


def letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= PASSING:
        return "D"
    return "F"