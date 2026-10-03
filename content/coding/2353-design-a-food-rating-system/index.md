---
title: 2353. Design a Food Rating System
notebook: coding
tags:
- medium
date: 2025-02-28 11:09:56
updated: 2025-02-28 11:09:56
---
## Problem

Design a food rating system that can do the following:

- **Modify** the rating of a food item listed in the system.
- Return the highest-rated food item for a type of cuisine in the system.

Implement the `FoodRatings` class:

- `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.
  - `foods[i]` is the name of the `iᵗʰ` food,
  - `cuisines[i]` is the type of cuisine of the `iᵗʰ` food, and
  - `ratings[i]` is the initial rating of the `iᵗʰ` food.
- `void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`.
- `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of `cuisine`. If there is a tie, return the item with the **lexicographically smaller** name.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

<https://leetcode.cn/problems/design-a-food-rating-system/>

**Example 1:**

> Input
> `["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]`
> `[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]`
> Output
> `[null, "kimchi", "ramen", null, "sushi", null, "ramen"]`
> Explanation
>
> ```cpp
> FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
> foodRatings.highestRated("korean"); // return "kimchi"
> // "kimchi" is the highest rated korean food with a rating of 9.
> foodRatings.highestRated("japanese"); // return "ramen"
> // "ramen" is the highest rated japanese food with a rating of 14.
> foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
> foodRatings.highestRated("japanese"); // return "sushi"
> // "sushi" is the highest rated japanese food with a rating of 16.
> foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
> foodRatings.highestRated("japanese"); // return "ramen"
> // Both "sushi" and "ramen" have a rating of 16.
> // However, "ramen" is lexicographically smaller than "sushi".
> ```

**Constraints:**

- `1 <= n <= 2 * 10⁴`
- `n == foods.length == cuisines.length == ratings.length`
- `1 <= foods[i].length, cuisines[i].length <= 10`
- `foods[i]`, `cuisines[i]` consist of lowercase English letters.
- `1 <= ratings[i] <= 10⁸`
- All the strings in `foods` are **distinct**.
- `food` will be the name of a food item in the system across all calls to `changeRating`.
- `cuisine` will be a type of cuisine of **at least one** food item in the system across all calls to `highestRated`.
- At most `2 * 10⁴` calls **in total** will be made to `changeRating` and `highestRated`.

## Test Cases

```python
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):


    def changeRating(self, food: str, newRating: int) -> None:


    def highestRated(self, cuisine: str) -> str:



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```

{% snippet solution_test.py %}

## Thoughts

这种需要关注最大值的场景用堆就很合适。因为要分数最高且名称（按字典序）最小，可以以 `(-rating, food)` 为元素做最小堆，堆顶记为所求。

每类烹饪方式（cuisine）都需要维护一个堆，堆内是该烹饪方式下的所有食物。需要有一个字典记录每种食物的烹饪方式。

因为食物的评分会被修改，而在堆中想要找到对应的食物的时间复杂度比较高，可以把食物的新评分直接加到堆里。这样同一种食物可能在堆里同时存在多个评分，已经过期了的评分也在。从堆顶取到的最高评分可能已经被后续的评分替换掉了，那么需要单独用字典记录所有食物的最新评分，用以判定从堆顶拿到的分数是否有效。如果有效就直接返回，否则将其弹出，再检查新的堆顶，直到堆顶恢复为有效评分。

构造方法的时间复杂度 `O(n log n)`（需要构造每类烹饪方式的食物列表的最小堆），`changeRating` 方法的时间复杂度 `O(log n)`，`highestRated` 方法的时间复杂度一般情况也是 `O(log n)`。空间复杂度 `O(n)`。

## Code

{% snippet solution.py %}
