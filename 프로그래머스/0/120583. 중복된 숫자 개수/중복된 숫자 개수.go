func solution(array []int, n int) int {
	answer := 0

	for i := 0; i < len(array); i++ {
		if array[i] == n {
			answer++
		}
	}
	return answer
}