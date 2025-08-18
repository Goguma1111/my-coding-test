func solution(n int) int { // 순서쌍의 개수
	var factors []int

	for i := 1; i <= n/2; i++ {
		if n%i == 0 {
			factors = append(factors, i)
		}
	}
	return len(factors) + 1
}