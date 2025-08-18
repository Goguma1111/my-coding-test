func solution(n int, t int) int {
	answer := n
	for ; t > 0; t-- {
		answer *= 2
	}
	return answer
}