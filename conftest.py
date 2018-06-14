# -*- coding: utf-8 -*-

import pytest

from restaurant import Restaurant, Dish
from food import SUSHI_RECIPES


@pytest.fixture(name="fooshi_bar")
def fixture_fooshi_bar():
    """Returns a Restaurant instance with a great menu."""
    return Restaurant(
        "Fooshi Bar",
        location="Buenos Aires",
        menu=[
            "Ebi Nigiri",
            "Edamame",
            "Inarizushi",
            "Kappa Maki",
            "Miso Soup",
            "Sake Nigiri",
            "Tamagoyaki",
        ],
    )


@pytest.fixture(
    name="sushi",
    params=[
        "California Roll",
        "Ebi Nigiri",
        "Inarizushi",
        "Kappa Maki",
        "Maguro Nigiri",
        "Sake Nigiri",
        "Tamagoyaki",
        "Tsunamayo Maki",
    ],
)
def fixture_sushi(request):
    """Create a Sushi instance based on recipes."""
    sushi_name = request.param
    return Dish(sushi_name, ingredients=SUSHI_RECIPES[sushi_name], labels=["sushi"])
