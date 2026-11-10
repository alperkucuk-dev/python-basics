numbers = [12, 7, 3, 25, 8, 19, 4, 16]
summation_ = 0
maximum = numbers[0]
count = 0

evens = []

for i in numbers: 
    summation_ += i
    count +=1

    if i % 2 == 0:
          evens.append(i)

    if i > maximum:
            maximum =i

average = summation_ / count 



txt =f"Summation of numbers: {summation_} , maximum number: {maximum} , size of numbers: {count}, average : {average}"
print(txt)

summation_func = sum(numbers)
maximum_func = max(numbers)
size_func = len(numbers)
average_func =sum(numbers)/len(numbers)

txt2 = f"Summation of numbers: {summation_func} , maximum number: {maximum_func} , size of numbers: {size_func}, average : {average_func}"
print(txt2)

print(evens)

