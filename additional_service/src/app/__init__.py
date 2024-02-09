from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

from .schema import (
    type_defs,
    GQLAccount,
    GQLUser,
)

types = [
    GQLAccount,
    GQLUser,
]

fedrated_schema = make_federated_schema(type_defs, types)

graphql = GraphQL(fedrated_schema)
