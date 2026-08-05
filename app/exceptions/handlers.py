from fastapi import Request
from fastapi.responses import JSONResponse

from app.logger.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(exc)

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Unexpected server error.",
            "error_code": "INTERNAL_SERVER_ERROR",
        },
    )