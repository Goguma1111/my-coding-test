func solution(price int) int {
    var answer int

    if price >= 500000 {
        answer = int(float64(price) * 0.8)
    } else if price >= 300000 {
        answer = int(float64(price) * 0.9)
    } else if price >= 100000 {
        answer = int(float64(price) * 0.95)
    } else {
        answer = price
    }

    return answer
}