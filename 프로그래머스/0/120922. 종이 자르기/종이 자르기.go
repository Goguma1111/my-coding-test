func solution(M, N int) int { // 종이자르기
	answer := (M - 1) + M*(N-1)
	return answer
}