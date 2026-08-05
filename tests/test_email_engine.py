from unittest.mock import MagicMock, patch

from app.engine.email_engine import check_email


def test_duplicate_email(mock_db):

    mock_db = MagicMock()

    with patch("app.engine.email_engine.get_respondent_by_email") as mock_get:

        mock_get.return_value = True

        with patch("app.engine.email_engine.get_rule") as mock_rule:

            mock_rule.return_value = None

            result = check_email(
                mock_db,
                "P001",
                "abc@test.com",
            )

            assert result["matched"] is True
            assert result["score"] == 40
            assert result["reason"] == "Duplicate Email"


def test_unique_email(mock_db):

    mock_db = MagicMock()

    with patch("app.engine.email_engine.get_respondent_by_email") as mock_get:

        mock_get.return_value = None

        result = check_email(
            mock_db,
            "P001",
            "abc@test.com",
        )

        assert result["matched"] is False
        assert result["score"] == 0
        assert result["reason"] == ""