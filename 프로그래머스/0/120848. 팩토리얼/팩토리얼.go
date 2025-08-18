func solution(n int) int {
	fact := 1
	for i := 1; ; i++ {
		fact *= i
		if fact > n {
			return i - 1
		}
	}
}
