from fastapi import FastAPI, Response, status

from . import settings, schemas

app = FastAPI()

settings = settings.Settings()


@app.post("/api/user/")
def create_user(form: schemas.UserForm, response: Response):
    from .dbapi import create_user
    result = create_user(form.email, form.password)
    if result[1]:  # error
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return result[1]
    else:
        return result[0]


@app.get("/api/user/{id}")
def get_user(id: str):
    from .dbapi import get_user
    return get_user(id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, log_level="debug", reload=settings.DEBUG)
