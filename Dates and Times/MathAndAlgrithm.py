import time

def SequencesV1(n):
    totel = 0
    for i in range(n):
        totel += (i+1)
    return(totel)

def SequencesV2(n):
    if n == 1:
        return 1
    return n + SequencesV2(n-1)

def SequencesV3(n):
    return int(n/2*(2+(n-1)))

n = int(input())

start = time.time()
print("answer 1:",SequencesV1(n))
print("time 1:",(time.time()-start)*1000)

start = time.time()
print("answer 3:",SequencesV3(n))
print("time 3:",(time.time()-start)*1000)