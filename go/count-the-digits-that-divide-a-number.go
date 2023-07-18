func countDigits(num int) int {
	num_aux := num
	digit_count := 0
	for 0 < num_aux {
		digit := num_aux % 10
		num_aux /= 10
		if (num % digit) == 0 {
			digit_count += 1
		}
	}
	return digit_count
}
