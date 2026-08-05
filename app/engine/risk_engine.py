def calculate_risk(
    results: list,
) -> dict:

    total_score = 0
    reasons = []

    for result in results:

        total_score += result["score"]

        if result["matched"]:
            reasons.append(result["reason"])

    return {
        "risk_score": total_score,
        "reasons": reasons
    }