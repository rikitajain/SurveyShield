from unittest.mock import patch

from app.engine.device_engine import check_device
from app.config.settings import DEVICE_DUPLICATE_SCORE


def test_duplicate_device(mock_db):

    with patch("app.engine.device_engine.get_respondent_by_device") as mock_get:

        mock_get.return_value = True

        with patch("app.engine.device_engine.count_device_usage") as mock_usage:

            mock_usage.return_value = 1

            with patch("app.engine.device_engine.get_rule") as mock_rule:

                mock_rule.return_value = None

                result = check_device(
                    mock_db,
                    "P001",
                    "DEVICE001",
                )

                assert result["matched"] is True
                assert result["score"] == DEVICE_DUPLICATE_SCORE
                assert result["reason"] == "Duplicate Device ID"
                assert result["usage_count"] == 1


def test_unique_device(mock_db):

    with patch("app.engine.device_engine.get_respondent_by_device") as mock_get:

        mock_get.return_value = None

        with patch("app.engine.device_engine.count_device_usage") as mock_usage:

            mock_usage.return_value = 0

            result = check_device(
                mock_db,
                "P001",
                "DEVICE001",
            )

            assert result["matched"] is False
            assert result["score"] == 0
            assert result["reason"] == ""
            assert result["usage_count"] == 0