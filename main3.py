from typing import List
import math

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in (2,n//2+1):
        if n%i == 0:
            return False
    return True

def secvPrime(l):
    for x in l:
        if isPrime(x) == False:
            return False
    return True


def bits(n):
    ones=0
    while(n>0):
        if n%2 == 1:
            ones = ones+1
        
        n=n//2
    return ones

def cresc(l):
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            return False
    return True

def get_longest_all_primes(l):
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

def get_longest_sorted_asc(l):
    secvMax = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if cresc(l[i:j+1]) and len(l[i:j+1]) > len(secvMax):
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

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1,2,3,4,1]) == [1,2,3,4]
    assert get_longest_sorted_asc([5,6,4,3]) == [5,6]
    assert get_longest_sorted_asc([2,3,4,2,1]) == [2,3,4]


    
def printMenu():
    print("1. Introduceti termenii sirului: ")
    print("2. Determinare cea mai lunga subsecventa de nr prime : ")
    print("3. Determinare cea mai lunga subsecventa de numere care au acelasi nr de 1 in scrierea binara: ")
    print("4. Determinare cea mai lunga secventa de pperfecte: ")
    print("x. Iesire")

def citire_Lista():
    l = []
    givenString = input("Dati nr de elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    test_get_longest_all_primes()
    test_get_longest_same_bit_counts()
    test_get_longest_sorted_asc()

    l=[]
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")
        if optiune =="1":
            l=citire_Lista()
        elif optiune =="2":
            print(get_longest_all_primes(l))
        elif optiune =="3":
            print(get_longest_same_bit_counts(l))
        elif optiune =="4":
            print(get_longest_sorted_asc(l))
        elif optiune =="x":
            break
        else:
            print("Optiune invalida! Reincercati: ")

main()

