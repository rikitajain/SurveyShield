from app.engine.decision_engine import get_decision


def test_accept():
    assert get_decision(20) == "ACCEPT"


def test_review():
    assert get_decision(60) == "REVIEW"


def test_reject():
    assert get_decision(90) == "REJECT"