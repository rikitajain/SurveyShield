from main import app

def test_dashboard_api(client):

    response = client.get("/api/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert "total_respondents" in data
    assert "accepted" in data
    assert "review" in data
    assert "rejected" in data


# ADD THIS NEW TEST BELOW
def test_check_respondent_api(client):

    payload = {
        "project_id": "P001",
        "email": "john@test.com",
        "country": "India",
        "browser": "Chrome",
        "device_id": "DEVICE001"
    }

    response = client.post(
        "/api/respondent/check",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert "decision" in data
    assert "risk_score" in data
    assert "engines" in data
    assert "reasons" in data