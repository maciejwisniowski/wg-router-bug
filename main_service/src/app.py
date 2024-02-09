import os
from ariadne import load_schema_from_path, QueryType
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

type_defs = load_schema_from_path(
    os.path.join(os.path.dirname(__file__), "schema.graphql")
)

GQLQuery = QueryType()


@GQLQuery.field("test")
async def resolve_test(_dummy, info, **kwargs):
    return {"name": "Steve", "id": "1", "account": {"id": "1"}}

fedrated_schema = make_federated_schema(type_defs, [GQLQuery])
graphql = GraphQL(fedrated_schema)
