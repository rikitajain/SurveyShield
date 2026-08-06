# Changelog

All notable changes to **SurveyShield** will be documented in this file.

---

## v1.1 - Enhanced Geolocation Support
**Release Date:** 06-Aug-2026

### Added
- Captured respondent GPS latitude and longitude.
- Captured browser location permission status.
- Captured GPS accuracy (in meters).
- Stored geolocation information in the SQLite database.
- Added UUID and Vendor information to respondent records.

### Improved
- Updated JavaScript SDK to include enhanced geolocation payload.
- Updated API request model.
- Updated database schema.
- Updated CRUD operations.
- Updated respondent API endpoint.

### Verified
- End-to-end testing completed successfully.
- Browser → API → Database workflow verified.
- Database records confirmed using DB Browser for SQLite.

---

## v1.0 - Initial Backend Release
**Release Date:** 05-Aug-2026

### Added
- FastAPI backend.
- JavaScript SDK.
- SQLite database integration.
- Fraud detection engine.
- Risk scoring engine.
- Audit logging.
- Device fingerprint generation.
- Browser and country capture.
- Git & GitHub repository setup.