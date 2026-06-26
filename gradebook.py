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


def median(scores):
    """Return the middle score of a sorted list."""
    ordered = sorted(scores)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def mode(scores):
    """[60, 60, 70] -> 60"""
    count = {}
    for s in scores:
        if s not in count:
            count[s] = 0
        count[s] += 1


def score_range(scores):
    """Return (lowest, highest) score."""
    return min(scores), max(scores)