from unittest.mock import patch

from app.engine.ip_engine import check_ip
from app.config.settings import IP_DUPLICATE_SCORE

def test_duplicate_ip(mock_db):

    with patch("app.engine.ip_engine.get_respondent_by_ip") as mock_get:

        mock_get.return_value = True

        with patch("app.engine.ip_engine.get_rule") as mock_rule:

            mock_rule.return_value = None

            result = check_ip(
                mock_db,
                "P001",
                "192.168.1.1",
            )

            assert result["matched"] is True
            assert result["score"] == IP_DUPLICATE_SCORE
            assert result["reason"] == "Duplicate IP"


def test_unique_ip(mock_db):

    with patch("app.engine.ip_engine.get_respondent_by_ip") as mock_get:

        mock_get.return_value = None

        result = check_ip(
            mock_db,
            "P001",
            "192.168.1.1",
        )

        assert result["matched"] is False
        assert result["score"] == 0
        assert result["reason"] == ""