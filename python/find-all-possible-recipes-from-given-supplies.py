def is_valid_recipe(recipe, tree, memory, visited):
    if recipe in visited:
        memory[recipe] = memory.get(recipe, False)
        return memory[recipe]
    visited[recipe] = True
    if recipe not in memory:
        if recipe not in tree:
            memory[recipe] = False
            return memory[recipe]
        for ingredient in tree[recipe]:
            if not is_valid_recipe(ingredient, tree, memory, visited):
                memory[recipe] = False
                return memory[recipe]
        memory[recipe] = True
    return memory[recipe]

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        tree = {supply: [] for supply in supplies}
        for i in range(len(recipes)):
            tree[recipes[i]] = ingredients[i]
        memory = {}
        output = []
        for recipe in recipes:
            visited = {}
            if is_valid_recipe(recipe, tree, memory, visited):
                output.append(recipe)
        return output
