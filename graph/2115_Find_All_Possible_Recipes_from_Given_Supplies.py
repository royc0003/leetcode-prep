class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        recipe_ingredients_mapping = {}
        for i in range(0, len(recipes)):
            cur_recipe = recipes[i]
            cur_ingredient = ingredients[i]
            recipe_ingredients_mapping[cur_recipe] = cur_ingredient
            if cur_recipe not in graph:
                graph[cur_recipe] = []
            # build ingredient -> recipe graph
            for ingredient in cur_ingredient:
                graph[ingredient].append(cur_recipe)
        res = set()
        seen = set()
        def dfs(cur_item):
            if cur_item in recipe_ingredients_mapping:
                for item in recipe_ingredients_mapping[cur_item]:
                    if item not in seen:
                        return
                if cur_item not in res:
                    res.add(cur_item)
            if cur_item in seen:
                return
            seen.add(cur_item)
            # set item found
            for dependency in graph[cur_item]:
                dfs(dependency)
        for supply in supplies:
            dfs(supply)
        return [x for x in res]