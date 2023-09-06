func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
	employeesMeetingTarget := 0
	for _, employeeHours := range hours {
		if target <= employeeHours {
			employeesMeetingTarget += 1
		}
	}
	return employeesMeetingTarget
}
