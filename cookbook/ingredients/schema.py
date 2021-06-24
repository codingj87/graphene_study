import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient

from ingredients.resolver import get_category_by_name, test_extra_field, all_category

# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'ingredients')

#     extra_field = graphene.String()

#     def resolve_extra_field(self, info):
#       print(self)
#       print(info)
#       return 'hi'


# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#         fields = ("id", "name", "notes", "category")


def get_test(self, info):
    return True
  

class Person(graphene.ObjectType):
    full_name = graphene.String()

    def resolve_full_name(parent, info):
      print(parent)
      return 'fullname'


def get_test2(parent, info):
    print(parent)
    return 'test2'


class test4Type(graphene.ObjectType):
    test_value = graphene.String()

    def resolve_test_value(parent, info):
      print(parent)
      return 'test4'


class test5Type(graphene.ObjectType):
    test5_value = graphene.String()

    def resolve_test5_value(parent, info):
        print(parent)
        return 'test5TypeValue'

def test5_resolver(parent, info):
    print(parent)
    return 'test5ResolveValue'

class test7Type(graphene.ObjectType):
    test7_value1 = graphene.List(graphene.Int)
    test7_value2 = graphene.String()

    def resolve_test7_value1(parent, info):
        print(parent)
        return [7,6,5]

    def resolve_test7_value2(parent, info):
        print(parent)
        return 'test7'



def test7_resolver(parnet, info):
    print(parnet)
    return [3,4,5]






class test8MixinType(graphene.ObjectType):
    test8_mixin_val1 = graphene.String()
    test8_mixin_val2 = graphene.Int()
    test8_mixin_val3 = graphene.Boolean()
    

class test8ObjectType(graphene.ObjectType):
    test8_object_val = graphene.String()

    # def resolve_test8_object_val(parent, info):
    #   return 'hello test8'


class test8Type(test8MixinType):
    test8_objects = graphene.List(test8ObjectType)



def test8_resolver(parent, info):
    
    return test8Type(
        test8_mixin_val1 = 'test8_mixin_val1',
        test8_mixin_val2 = 8888,
        test8_mixin_val3 = True,
        test8_objects = [{'test8': 'test8_1'}, {'test8': 'test8_2'}]
    )

class test9Type(graphene.ObjectType):
    test9_val1 = graphene.String()
    test9_val2 = graphene.Int()

def test9_resolver(parent, info):
    return test9Type(
        test9_val1 = 'test9_val',
        test9_val2 = 9999
    )

class Query(graphene.ObjectType):
    
    test1 = graphene.String()

    def resolve_test1(parant, info):
        return 'test1'

    test2 = graphene.String(resolver=get_test2)

    test3 = graphene.Field(graphene.String)

    def resolve_test3(parent, info):
      return 'test3'


    test4 = graphene.Field(test4Type)

    def resolve_test4(parent, info):
      print(parent)
      return 'test4_to_test4Type'

    test5 = graphene.Field(
        test5Type,
        resolver=test5_resolver
    )

    
    test6 = graphene.List(graphene.Int)

    def resolve_test6(parent, info):
      return [1, 2, 3]


    test7 = graphene.List(
        test7Type,
        resolver=test7_resolver
    )


    test8 = graphene.Field(
        test8Type,
        resolver=test8_resolver
    )

    test9 = graphene.Field(
        test9Type,
        resolver=test9_resolver
    )
