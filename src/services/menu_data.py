from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as file:
            headers, *rows = csv.reader(file)
            dish_instances = {}

            for row in rows:
                (dish_name, dish_cost,
                 ingredient_name, ingredient_quantity) = row

                if dish_name not in dish_instances:
                    dish = Dish(dish_name, float(dish_cost))
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name), int(ingredient_quantity))
                    dish_instances[dish_name] = dish

                else:
                    dish = dish_instances[dish_name]
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient_name), int(ingredient_quantity))

            self.dishes = set(dish_instances.values())
