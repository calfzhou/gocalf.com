from collections import defaultdict
from heapq import heapify, heappop, heappush


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self._foods: dict[str, tuple[str, int]] = {} # food -> (cuisine, rating)
        self._rankings: dict[str, list[tuple[int, str]]] = defaultdict(list) # cuisine -> [(-rating, food)] min-heap

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self._foods[food] = (cuisine, rating)
            self._rankings[cuisine].append((-rating, food))

        for ranking in self._rankings.values():
            heapify(ranking)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self._foods[food]
        self._foods[food] = (cuisine, newRating)
        heappush(self._rankings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        ranking = self._rankings[cuisine]
        while True:
            rating, food = ranking[0]
            if self._foods[food][1] == -rating:
                return food
            else:
                heappop(ranking)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
