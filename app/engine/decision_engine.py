from app.config.settings import REVIEW_THRESHOLD, REJECT_THRESHOLD

def get_decision(
    score: int,
) -> str:

    if score >= REJECT_THRESHOLD:
        return "REJECT"

    elif score >= REVIEW_THRESHOLD:
        return "REVIEW"

    return "ACCEPT"