#hashing 
from typing import Sized


def hash(key):
    return key%size

def probe(H , key):
    index = hash(key)
    i = 0
    while H[(index + i) % size] != 0:
        i+=1
    return (index + i) % size 


def insert(H , key):
    index = hash(key)
    if H[index] != 0 :
        index = probe(H , key)
    H[index] = key

def search(H , key , size):
    index = hash(key)
    i = 0
    while H[(index + i)%size] != key:
        i+=1
    return index
size = 10

H = [0 for i in range(size)]
insert(H , 12)
insert(H , 15)
insert(H , 1)
print(H)
