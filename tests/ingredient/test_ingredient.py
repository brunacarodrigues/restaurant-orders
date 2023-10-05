from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient('queijo mussarela')
    ingredient2 = Ingredient('queijo mussarela')
    ingredient3 = Ingredient('bacon')

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert ingredient1.name == 'queijo mussarela'

    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert ingredient1.restrictions == expected_restrictions
    assert hash(ingredient1) == hash(Ingredient('queijo mussarela'))
