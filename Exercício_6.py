number_max_sequences = int(input('Quantas sequências Fibonacci gostaria ver?: \n'))

previous = 0
next = 0
count = 0

while(count < number_max_sequences):
    print(next)
    next = next + previous
    previous = next - previous
    if next == 0:
        next = next + 1
    count += 1
