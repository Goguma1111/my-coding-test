func solution(balls int, share int) int {
	answer := 1

	num1 := make([]int, share)
	num2 := make([]int, share)

	index := 0

	for i := balls; i > balls-share; i-- {
		num1[index] = i
		index++
	}

	for i := 1; i <= share; i++ {
		num2[i-1] = i
	}

	for i := 0; i < len(num1); i++ {
		answer = answer * num1[i] / num2[i]
	}

	return answer
}
