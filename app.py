import sys
def calculate (m1,m2,m3):
    total = m1+m2+m3
    average = total / 3
    percentage = (total / 300) * 100
    return total,average,percentage
m1 = int(sys.argv[1])
m2 = int(sys.argv[2])
m3 = int(sys.argv[3])
total,percentage,average = calculate(m1,m2,m3)
print("total : ",total)
print("average : ",average)
print("percentage : ",percentage)
