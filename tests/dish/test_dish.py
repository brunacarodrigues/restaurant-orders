from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    ingredient1 = Ingredient('presunto')
    ingredient2 = Ingredient('queijo mussarela')

    dish1 = Dish('Lasanha', 15.99)
    dish2 = Dish('Lasanha', 15.99)
    dish3 = Dish('Bolonhesa', 10.99)

    assert dish1.name == 'Lasanha'
    assert hash(dish1) == hash(dish2)
    assert hash(dish3) != hash(dish1)
    assert dish1 == dish2
    assert dish3 != dish1
    assert repr(dish1) == "Dish('Lasanha', R$15.99)"

    dish1.add_ingredient_dependency(ingredient1, 2)
    dish1.add_ingredient_dependency(ingredient2, 3)

    assert dish1.recipe.get(ingredient1) == 2
    assert dish1.recipe.get(ingredient2) == 3

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish1.get_restrictions() == expected_restrictions
    assert dish1.get_ingredients() == {ingredient1, ingredient2}

    with pytest.raises(TypeError):
        Dish('Invalid Dish', 'invalid_price')

    with pytest.raises(ValueError):
        Dish('Invalid Dish', -25.99)

    dish4 = Dish('Massa', 15.00)
    dish4.add_ingredient_dependency(ingredient1, 2)
    dish4.add_ingredient_dependency(ingredient2, 1)

    assert hash(dish4) == hash(dish4)
    assert repr(dish4) == "Dish('Massa', R$15.00)"
