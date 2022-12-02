from math import floor

def subir(A, i, x):
    A[i] = x
    j = floor(i/2)
    if j>=0:
        if A[i] > A[j]:
            A[j], A[i] = A[i], A[j]
            subir(A, j, x)

def descer(A, i, n):
    j = (2*i)+1
    if j < n:
        if j+1 < n:
            if A[j+1] > A[j]:
                    j = j+1
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
            descer(A, j, n)

def inserir(A, x):
    A.append(x)
    i = len(A)-1
    subir(A, i, x)

def remover(A):
    n = len(A)
    x = A[-1]
    y = A[0]

    A[0] = x
    descer(A, 0, n-1)
    A.pop()

    return y

def constroi_heap(A):
    n = len(A)
    i= floor(n/2)-1
    while (i>=0):
        descer(A, i, n)
        i = i-1

def pop(A, n):
 
    if n <= 0:
        return -1
 
    top = A[0]

    A[0] = A[n - 1]
 
    descer(A, 0, n - 1)
 
    return top

def heapsort(A):
    n = len(A)

    i = (floor((n - 2)/2))-1
    while i >= 0:
        descer(A, i, n)
        i = i - 1
 
    while n:
        A[n - 1] = pop(A, n)
        n = n - 1
