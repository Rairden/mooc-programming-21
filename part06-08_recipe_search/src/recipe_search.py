def createRecipes(filename):
    with open(filename) as file:
        recipes = {}
        ingredients = []

        for line in file:
            if line == "\n":
                recipes[ingredients[0]] = (ingredients[1], set(ingredients[2:]))
                ingredients = []
                continue

            ingredients.append(line.replace("\n", ""))

        recipes[ingredients[0]] = (ingredients[1], set(ingredients[2:]))

    return recipes


def search_by_ingredient(filename: str, ingredient: str):
    recipes = createRecipes(filename)
    foundRecipes = []

    for recipe in recipes:
        if ingredient in recipes[recipe][1]:
            time = recipes[recipe][0]
            foundRecipes.append(f"{recipe}, preparation time {time} min")

    return foundRecipes


def search_by_time(filename: str, prepTime: int):
    recipes = createRecipes(filename)
    foundRecipes = []

    for recipe in recipes:
        time = int(recipes[recipe][0])
        if time <= prepTime:
            foundRecipes.append(f"{recipe}, preparation time {time} min")

    return foundRecipes


def search_by_name(filename: str, word: str):
    recipes = createRecipes(filename)
    foundRecipes = []

    for recipe in recipes:
        if word.lower() in recipe.lower():
            foundRecipes.append(recipe)

    return foundRecipes


if __name__ == '__main__':
    foundRecipesWord = search_by_name("recipes1.txt", "cake")
    foundRecipesTime = search_by_time("recipes1.txt", 20)
    foundRecipesIngr = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in foundRecipesWord:
        print(recipe)

    for recipe in foundRecipesTime:
        print(recipe)

    for recipe in foundRecipesIngr:
        print(recipe)
