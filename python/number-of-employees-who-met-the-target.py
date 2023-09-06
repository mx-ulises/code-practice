class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        employees_meeting_target = 0
        for employee_hours in hours:
            if target <= employee_hours:
                employees_meeting_target += 1
        return employees_meeting_target
