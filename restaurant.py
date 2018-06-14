# -*- coding: utf-8 -*-

import attr
import typing

FISH = ["Crab", "Salmon", "Shrimp", "Tuna"]
MEAT = ["Beef", "Chicken", "Pork"]


@attr.s
class Restaurant:
    name: str = attr.ib()
    location: str = attr.ib()
    menu: typing.List[str] = attr.ib(default=attr.Factory(list))


@attr.s
class Dish:
    name: str = attr.ib()
    ingredients: typing.List[str] = attr.ib(default=attr.Factory(list))
    labels: typing.List[str] = attr.ib(default=attr.Factory(list))

    def __contains__(self, ingredient):
        return ingredient in self.ingredients

    @property
    def is_vegetarian(self):
        for ingredient in [*FISH, *MEAT]:
            if ingredient in self:
                return False
        return True
