import os
from ariadne import load_schema_from_path
from ariadne.contrib.federation.objects import FederatedObjectType

from .models import UserModel, AccountModel

type_defs = load_schema_from_path(
    os.path.join(os.path.dirname(__file__), "schema.graphql")
)


GQLAccount = FederatedObjectType("Account")
GQLUser = FederatedObjectType("User")


@GQLUser.reference_resolver
async def resolve_user_reference(_, _info, representation: dict):
    return UserModel(
        _id=representation["id"], account_id=representation["account"]["id"]
    )


@GQLAccount.reference_resolver
async def resolve_account_reference(_, _info, representation: dict):
    return AccountModel(_id=representation["id"])


@GQLUser.field("foo")
async def resolve_user_foo(user: UserModel, info):
    return True
