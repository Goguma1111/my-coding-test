func solution(i int, j int, k int) int {
	answer := 0

	for num := i; num <= j; num++ {
		n := num
		for n > 0 {
			if n%10 == k { 
				answer++
			}
			n /= 10 
		}
	}

	return answer
}