
from ingredients.models import Category, Ingredient


def get_category_by_name(parent, info, **kwargs):
    name = kwargs.get('name')
    print(parent)
    print(info)
    print(kwargs)
    try:
        return Category.objects.all()
    except Category.DoesNotExist:
        return None

def test_extra_field(parent, info):
    return 'hello'

def all_category(parent, info, **kwargs):
    print('resolver')
    try:
        return list(Category.objects.all())
    except Category.DoesNotExist:
        return None