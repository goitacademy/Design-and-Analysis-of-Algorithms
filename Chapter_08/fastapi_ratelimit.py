from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Перевищено ліміт запитів. Спробуйте пізніше."},
    )


@app.get("/my-endpoint")
@limiter.limit("5/minute")
async def my_endpoint(request: Request):
    return {"message": "Це мій маршрут з обмеженням швидкості"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
