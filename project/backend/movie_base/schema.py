import graphene
import graphene_sqlalchemy as gsa
from movie_base import models


class Film(gsa.SQLAlchemyObjectType):
    rating = graphene.String()
    class Meta:
        model = models.Film
        interfaces = (graphene.relay.Node,)

class Actor(gsa.SQLAlchemyObjectType):
    rating = graphene.String()
    class Meta:
        model = models.Actor
        interfaces = (graphene.relay.Node,)


class FilmsConnection(graphene.relay.Connection):
    class Meta:
        node = Film


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    films = gsa.SQLAlchemyConnectionField(FilmsConnection)


schema = graphene.Schema(query=Query)
