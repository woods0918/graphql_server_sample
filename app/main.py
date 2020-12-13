import sys, pathlib, uvicorn, graphene

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from graphql.execution.executors.asyncio import AsyncioExecutor
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from app.schema.schema import schema

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
