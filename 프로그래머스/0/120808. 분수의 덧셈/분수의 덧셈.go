func solution(numer1, denom1, numer2, denom2 int) []int { // 분수의 덧셈
	numer := (numer1 * denom2) + (numer2 * denom1)
	denom := denom1 * denom2

	// 최대공약수 함수
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	g := gcd(numer, denom)

	answer := []int{numer / g, denom / g}

	return answer
}