import random

def rand_temp(size):
    temp = []
    for i in range(size):
        temp.append(random.randint(0,100))
    print(f"The original temperature list is: \n {temp}")
    return temp

def selection_sort(data):
    for i in range(len(data)):
        min = i
        for j in range(i+1, len(data)):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]

def main():
    temp = rand_temp(100)
    selection_sort(temp)
    print(f"The sorted temperature list is: \n {temp}")

main()