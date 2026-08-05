from app.engine.risk_engine import calculate_risk


def test_zero_risk():

    results = [
        {
            "score": 0,
            "matched": False,
            "reason": ""
        }
    ]

    risk = calculate_risk(results)

    assert risk["risk_score"] == 0
    assert risk["reasons"] == []


def test_single_match():

    results = [
        {
            "score": 40,
            "matched": True,
            "reason": "Duplicate Email"
        }
    ]

    risk = calculate_risk(results)

    assert risk["risk_score"] == 40
    assert risk["reasons"] == ["Duplicate Email"]


def test_multiple_matches():

    results = [
        {
            "score": 40,
            "matched": True,
            "reason": "Duplicate Email"
        },
        {
            "score": 30,
            "matched": True,
            "reason": "Duplicate IP"
        },
        {
            "score": 0,
            "matched": False,
            "reason": ""
        }
    ]

    risk = calculate_risk(results)

    assert risk["risk_score"] == 70
    assert len(risk["reasons"]) == 2