import random
import string
import time
import matplotlib.pyplot as plt
from hvlcs import hvlcs
import os


def generateTest(length, fileName, folder="tests/q1Tests"):
    alphabet = ['a', 'b', 'c', 'd', 'e']
    values = {}
    for ch in alphabet:
        values[ch] = random.randint(1, 10)

    A = ""
    for i in range(length):
        A += random.choice(alphabet)

    B = ""
    for i in range(length):
        B += random.choice(alphabet)
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    filePath = os.path.join(folder, fileName)

    with open(filePath, 'w') as f:
        f.write(f"{len(alphabet)}\n")
        for character, value in values.items():
            f.write(f"{character} {value}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")

    return A, B, values

def graphTest():
    sizes = [25, 50, 75, 100, 150, 200, 300, 400, 500, 600]
    times = []

    for size in sizes:
        A, B, values = generateTest(size, f"testSize{size}.in")
        start_time = time.time()
        hvlcs(A, B, values)
        end_time = time.time()
        runtime = end_time - start_time
        times.append(runtime)
        print(f"Size: {size} | Time: {runtime} seconds")

    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("String Length")
    plt.ylabel("Runtime (seconds)")
    plt.title("HVLCS Runtime vs Input Size")
    plt.grid()
    plt.savefig("runtime_graph.png")
    plt.show()

if __name__ == "__main__":
    graphTest()