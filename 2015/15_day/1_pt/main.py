import sys
import copy

class Recipe:
    def __init__(self, ingredient_list):
        self.ingredient_list = ingredient_list
        self.score = self.calculateScore()

    def calculateScore(self):
        ## properties = [<capacity>, <durability>, <flavor>, <texture>]
        property_scores = [0,0,0,0]
        for ingredient in self.ingredient_list:
            for i in range(4):
                property_scores[i] += (ingredient.properties[i] * ingredient.quantity)
        total_score = 1
        for i in range(4):
            if property_scores[i] < 0:
                property_scores[i] = 0
            total_score = total_score * property_scores[i]
        return total_score

    def __str__(self):
        output = ""
        for ingredient in self.ingredient_list:
            output += str(ingredient) + "\n"
        output += "Score: " + str(self.score)
        return output

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.properties = (capacity, durability, flavor, texture)
        self.calories = calories
        self.quantity = 0

    def __str__(self):
        return self.name + ": " + str(self.quantity)

def solve(data):
    ingredient_list = parseData(data.split('\n'))
    recipe_list = generateRecipeList(ingredient_list)
    recipe_list.sort(key = lambda recipe: recipe.score, reverse = True)
    best_recipe = recipe_list[0]
    return best_recipe.score

def generateRecipeList(ingredient_list):
    recipe_list = []
    generateRecipe(100, ingredient_list, recipe_list)
    return recipe_list

def generateRecipe(quantity, ingredients, recipe_list, next_ingredient_index = 0):
    if quantity == 0:
        new_recipe = Recipe(ingredients)
        recipe_list.append(new_recipe)
        return
    if next_ingredient_index == len(ingredients):
        return
    for i in range(quantity, -1, -1):
        ingredients[next_ingredient_index].quantity = i
        generateRecipe(quantity-i, ingredients, recipe_list, next_ingredient_index+1)

def parseData(data_list):
    ingredient_list = []
    for line in data_list:
        parsed_data = line.split(' ')
        name = parsed_data[0][:len(parsed_data[0])-1]
        capacity = int(parsed_data[2][:len(parsed_data[2])-1])
        durability = int(parsed_data[4][:len(parsed_data[4])-1])
        flavor = int(parsed_data[6][:len(parsed_data[6])-1])
        texture = int(parsed_data[8][:len(parsed_data[8])-1])
        calories = int(parsed_data[10])
        ingredient_list.append(Ingredient(name, capacity, durability, flavor, texture, calories))
    return ingredient_list


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
