import graphene

from ingredients.schema import Query as ingredients

class Query(
    ingredients,
    graphene.ObjectType
):
  pass

class Mutation(graphene.ObjectType):
  pass


schema = graphene.Schema(query=Query)