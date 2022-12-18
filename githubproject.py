matrix = [    [True, 34, 5, 'School'],
    [8, 23, 20, 11, 37, 55, 17],
    ['book', 'mosh', 'arc', 'photo'],
    [-1, 'Mani']
]

all_strings = []

for row in matrix:
    all_strings1 = True
    strings2= []
    for element in row:
        if not isinstance(element, str):
            all_strings1= False
            break
        else:
            strings2.append(element)
    if all_strings1:
        all_strings.extend(strings2)

print(' '.join(all_strings).upper())  # Output: BOOK MOSH ARC PHOTO
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
primes = []
for row in matrix:
    all_numbers1 = True
    numbers2 = []
    for element in row:
        if not isinstance(element, int):
            all_numbers1 = False
            break
        else:
            numbers2.append(element)
    if all_numbers1:
        for number in numbers2:
            if is_prime(number):
                primes.append(number)

primes.reverse()
print(primes)  # Output: [37, 23, 17, 11]
