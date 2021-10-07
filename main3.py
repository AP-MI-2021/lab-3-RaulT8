from typing import List

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in (2,n//2+1):
        if n%i == 0:
            return False
    return True

def bits(n):
    ones=0
    while(n>0):
        if n%2 == 1:
            ones = ones+1
        
        n=n//2
    return ones


def secvPrime(l):
    for x in l:
        if isPrime(x) == False:
            return False
    return True


def get_longest_all_primes(l): #Determina cea mai lunga secventa din l de nr prime
    secvMax= []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if secvPrime(l[i:j+1]) and len(l[i:j+1]) > len(secvMax):
                secvMax = l[i:j+1]
    return secvMax

def get_longest_same_bit_counts(l):
    secvMax=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if bits(l[i]) == bits(l[j]) and len(l[i:j]) > len(secvMax):
                secvMax = l[i:j+1]
    return secvMax



def test_get_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([1,2,3]) == [2,3]
    assert get_longest_all_primes([2,3,5,7,8]) == [2,3,5,7]
    assert get_longest_all_primes([11,13,17,19,20]) == [11,13,17,19]

def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([1,1,2]) == [1,1]
    assert get_longest_same_bit_counts([3,3,3,6,7]) == [3,3,3,6]
    assert get_longest_same_bit_counts([5,6,7,8]) == [5,6]
    assert get_longest_same_bit_counts([7,7,8,9]) == [7,7]
    assert get_longest_same_bit_counts([]) == []
    
def printMenu():
    print("1. Introduceti termenii sirului: ")
    print("2. Determinare cea mai lunga subsecventa cu proprietatea: ")
    print("3. Determinare cea mai lunga subsecventa cu proprietatea: ")
    print("x. Iesire")

def citireLista():
    l = []
    givenString = input("Dati nr de elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    test_get_longest_all_primes()
    test_get_longest_same_bit_counts()

    l=[]
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")
        if optiune =="1":
            l=citireLista()
        elif optiune =="2":
            print(get_longest_all_primes(l))
        elif optiune =="3":
            print(get_longest_same_bit_counts(l))
        elif optiune =="x":
            break

main()

