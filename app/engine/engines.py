from app.engine.email_engine import check_email
from app.engine.ip_engine import check_ip
from app.engine.device_engine import check_device


def run_all_engines(
    db,
    respondent,
    client_ip,
):

    results = []

    if respondent.email:

        results.append(

            check_email(
                db,
                respondent.project_id,
                respondent.email,
            )

        )

    results.append(

        check_ip(
            db,
            respondent.project_id,
            client_ip,
        )

    )

    results.append(

        check_device(
            db,
            respondent.project_id,
            respondent.device_id,
        )

    )

    return results