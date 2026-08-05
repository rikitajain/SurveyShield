from app.database.audit_models import AuditLog


def get_dashboard_summary(db):

    total = db.query(AuditLog).count()

    accepted = (
        db.query(AuditLog)
        .filter(AuditLog.decision == "ACCEPT")
        .count()
    )

    review = (
        db.query(AuditLog)
        .filter(AuditLog.decision == "REVIEW")
        .count()
    )

    rejected = (
        db.query(AuditLog)
        .filter(AuditLog.decision == "REJECT")
        .count()
    )

    return {

        "total_respondents": total,
        "accepted": accepted,
        "review": review,
        "rejected": rejected
    }