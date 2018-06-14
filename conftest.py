# -*- coding: utf-8 -*-

import pytest

from restaurant import Restaurant, Dish


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


@pytest.fixture(name="recipes", scope="session")
def fixture_recipes():
    """Return a map from types of sushi to ingredients."""
    return {
        "California Roll": ["Rice", "Cucumber", "Avocado", "Crab"],
        "Ebi Nigiri": ["Shrimp", "Rice"],
        "Inarizushi": ["Fried tofu", "Rice"],
        "Kappa Maki": ["Cucumber", "Rice", "Nori"],
        "Maguro Nigiri": ["Tuna", "Rice", "Nori"],
        "Sake Nigiri": ["Salmon", "Rice", "Nori"],
        "Tamagoyaki": ["Fried egg", "Rice", "Nori"],
        "Tsunamayo Maki": ["Tuna", "Mayonnaise"],
    }


@pytest.fixture(
    params=[
        "California Roll",
        "Ebi Nigiri",
        "Inarizushi",
        "Kappa Maki",
        "Maguro Nigiri",
        "Sake Nigiri",
        "Tamagoyaki",
        "Tsunamayo Maki",
    ]
)
def sushi(recipes, request):
    """Create a Sushi instance based on recipes."""
    name = request.param
    return Dish(name, ingredients=recipes[name], labels=["sushi"])
