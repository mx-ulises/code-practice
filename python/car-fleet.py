P, V = 0, 1 # Index for Position and Velocity

def catching_before_target(lead_car, follower_car, target):
    if follower_car[V] <= lead_car[V]:
        # Follower will never catch leader
        return False
    step_of_catching = (follower_car[P] - lead_car[P]) / (lead_car[V] - follower_car[V])
    catch_position = follower_car[P] + follower_car[V] * step_of_catching
    return catch_position <= target


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        cars.reverse()
        fleet_number = 1
        current_lead_car = cars[0]
        for i in range(1, n):
            follower_car = cars[i]
            if not catching_before_target(current_lead_car, follower_car, target):
                # Won't catch before target (or not at all), start a new fleet
                current_lead_car = follower_car
                fleet_number += 1
        return fleet_number
