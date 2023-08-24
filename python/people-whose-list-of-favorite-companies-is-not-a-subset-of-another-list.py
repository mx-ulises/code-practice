class Solution:
    def get_company_tuple(favoriteCompanies: List[List[str]], i: int):
        length = len(favoriteCompanies[i])
        favorite = set(favoriteCompanies[i])
        return (length, i, favorite)

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favorite_companies = [Solution.get_company_tuple(favoriteCompanies, i) for i in range(len(favoriteCompanies))]
        favorite_companies.sort()
        favorite_visited = []
        subsets = []
        while favorite_companies:
            _, i, favorite = favorite_companies.pop()
            is_subset = False
            for visited in favorite_visited:
                if len(favorite & visited) == min(len(favorite), len(visited)):
                    is_subset = True
                    break
            if is_subset == False:
                subsets.append(i)
            favorite_visited.append(favorite)
        subsets.sort()
        return subsets
