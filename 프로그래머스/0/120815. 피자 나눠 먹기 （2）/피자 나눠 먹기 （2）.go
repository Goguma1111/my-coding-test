func solution(n int) int {
	answer := 1
	for (answer*6)%n != 0 {
		answer++
	}
	return answer
}
