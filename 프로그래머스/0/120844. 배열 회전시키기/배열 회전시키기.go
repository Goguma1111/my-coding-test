func solution(numbers []int, direction string) []int {
	var answer []int
	if direction == "right" {
		answer = append([]int{numbers[len(numbers)-1]}, numbers[:len(numbers)-1]...)
	} else if direction == "left" {
		answer = append(numbers[1:], numbers[0])
	}
	return answer
}