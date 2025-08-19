func solution(numbers []int) int {
	max1, max2 := 0, 0

	for _, num := range numbers {
		if num > max1 {
			max2 = max1
			max1 = num
		} else if num > max2 {
			max2 = num
		}
	}

	return max1 * max2
}
