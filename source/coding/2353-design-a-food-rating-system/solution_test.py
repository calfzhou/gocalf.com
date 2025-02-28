import pytest

from solution import FoodRatings

null = None


@pytest.mark.parametrize('actions, params, expects', [
    (
        ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"],
        [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]],
        [null, "kimchi", "ramen", null, "sushi", null, "ramen"],
    ),
])
@pytest.mark.parametrize('clazz', [FoodRatings])
def test_solution(clazz, actions, params, expects):
    sol = None
    for action, args, expected in zip(actions, params, expects):
        if action == 'FoodRatings':
            sol = clazz(*args)
        else:
            assert getattr(sol, action)(*args) == expected
