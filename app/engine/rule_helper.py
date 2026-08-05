def get_rule_result(
    rule,
    default_score,
    default_severity,
    default_reason,
):
    """
    Returns the final score, severity and reason
    after considering project rule overrides.
    """

    if rule is None:

        return {
            "enabled": True,
            "score": default_score,
            "severity": default_severity,
            "reason": default_reason,
        }

    return {
        "enabled": rule.enabled,
        "score": rule.score,
        "severity": rule.severity,
        "reason": rule.reason,
    }