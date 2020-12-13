import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from app.cruds.users import fetch_user
from app.cruds.todos import fetch_todo
from app.schema.users import User, UserConnections, InsertUser
from app.schema.todos import Todo, TodoConnections, InsertTodo

#-------------------------
# Query
#-------------------------
class Query(graphene.ObjectType):
    node = relay.Node.Field()

    user = graphene.Field(
        lambda: graphene.List(User),
        id=graphene.Int(required=False),
        name=graphene.String(required=False)
    )
    todo = graphene.Field(
        lambda: graphene.List(Todo),
        id=graphene.Int(required=False),
        user_id=graphene.Int(required=False),
        title=graphene.String(required=False),
        description=graphene.String(required=False),
        deadline=graphene.DateTime(required=False)
    )
    all_users = SQLAlchemyConnectionField(UserConnections)
    all_todos = SQLAlchemyConnectionField(TodoConnections, sort=None)

    def resolve_user(self, info, id=None, name=None):
        return fetch_user(id, name)
    
    def resolve_todo(self, info, id=None, user_id=None, title=None, description=None, deadline=None):
        return fetch_todo(id, user_id, title, description, deadline)

#-------------------------
# Mutation
#-------------------------
class Mutation(graphene.ObjectType):
    insert_user = InsertUser.Field()
    insert_todo = InsertTodo.Field()

#-------------------------
# Schema
#-------------------------
schema = graphene.Schema(query = Query, mutation=Mutation)
