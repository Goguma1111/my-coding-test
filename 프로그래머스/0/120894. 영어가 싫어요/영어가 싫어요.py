def solution(numbers):
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(n) :

        numbers = numbers.replace(num,str(i))

    return int(numbers)    

print(solution("onetwothreefourfivesixseveneightnine"))        
