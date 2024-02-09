import uvicorn

from app import graphql
from fastapi import FastAPI


def get_application():
    application = FastAPI(title="additional service", debug=False, version="0.0.0")
    return application


app = get_application()

app.mount("/graphql", graphql)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8064, reload=False)
