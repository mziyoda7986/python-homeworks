def enrollment_stats(uni):
    num = [int(val[1]) for val in uni]
    tuition = [int(val[2]) for val in uni]
    return num, tuition

def mean(x):
    xsum = sum(x)
    return round(xsum/len(x), 2)

def median(x):
    x.sort()
    return x[len(x)//2] if len(x) % 2 else (x[len(x)//2-1] + x[len(x)//2])/2

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
print("******************************")
print("Total students:", sum(val[1] for val in universities))
print("Total tuition: $", sum(val[2] for val in universities), '\n')
num, tuit = enrollment_stats(universities)
print("Student mean:", mean(num))
print("Student median:", median(num), '\n')
print("Tuition mean: $", mean(tuit))
print("Tuition median: $", median(tuit))
print("******************************")