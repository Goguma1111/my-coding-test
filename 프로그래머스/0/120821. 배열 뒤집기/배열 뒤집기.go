// 배열 뒤집기
func solution(num_list []int) []int {
	n := len(num_list)

	for i := 0; i < n/2; i++ {
		p := n - i - 1
		num_list[i], num_list[p] = num_list[p], num_list[i] // 값 교환
	}
	return num_list
}
