func solution(n int, numlist []int) []int {
	answer := []int{}

	for _, num := range numlist {
		if num%n == 0 {
			answer = append(answer, num)
		}
	}
	return answer
}