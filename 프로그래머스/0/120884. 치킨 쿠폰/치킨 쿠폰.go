func solution(chicken int) int {
	answer := 0

	for chicken >= 10 {
		coupon := chicken / 10
		answer += coupon
		chicken = chicken%10 + coupon
	}
	return answer
}

