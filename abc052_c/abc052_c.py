import math


def __sieve(num):
    sieved_set = set()
    for i in range(2, num + 1):
        sieved_set.add(i)

    # エラトステネスの篩法で素数を計算する
    for i in range(2, int(math.sqrt(num)) + 1):
        for j in range(2, num + 1):
            if (j % i == 0) and (j != i) and (j in sieved_set):
                sieved_set.remove(j)

    return sieved_set


def __calc_divisor(num, prime_count_array):
    for prime in prime_count_array:
        count = 0
        temp_divided = num
        while temp_divided % prime == 0:
            count += 1
            temp_divided /= prime
        prime_count_array[prime] += count


n = int(input())

# 素数を計算
primes = __sieve(n)

# N! の各項について、素因数分解する
prime_count_array = {}
for i in primes:
    prime_count_array[i] = 0
for i in range(2, n + 1):
    __calc_divisor(i, prime_count_array)

# 素因数分解結果から約数の個数を計算
divisor_count = 1
for divisor_count_of_prime in prime_count_array.values():
    divisor_count *= (divisor_count_of_prime + 1)

# 出力用に余りを算出
print(divisor_count % (10 ** 9 + 7))
