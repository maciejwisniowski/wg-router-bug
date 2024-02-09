import uvicorn
from fastapi import FastAPI

from app import graphql


def get_application():
    application = FastAPI(title="main service", debug=False, version="0.0.0")

    return application


app = get_application()
app.mount("/graphql", graphql)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8074, reload=False)
