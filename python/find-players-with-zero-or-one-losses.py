class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        team_loses = {matches[i][0]: 0 for i in range(len(matches))}
        for i in range(len(matches)):
            looser = matches[i][1]
            if looser in team_loses:
                team_loses[looser] += 1
            else:
                team_loses[looser] = 1
        lost_0 = []
        lost_1 = []
        for team in team_loses:
            if team_loses[team] == 0:
                lost_0.append(team)
            if team_loses[team] == 1:
                lost_1.append(team)
        lost_0.sort()
        lost_1.sort()
        return [lost_0, lost_1]
