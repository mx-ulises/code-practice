class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # count the actions of user per minute, store them in a set to remove dupes
        user_active_minutes_log = defaultdict(set)
        while logs:
            user_id, minute = logs.pop()
            user_active_minutes_log[user_id].add(minute)
        # generate the output
        output = [0] * k
        # for each user_id, count the minutes in the user_active_minutes_log
        for user_id in user_active_minutes_log:
            output[len(user_active_minutes_log[user_id]) - 1] += 1
        return output
