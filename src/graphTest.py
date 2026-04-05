import random
import string
import time
import matplotlib.pyplot as plt
from hvlcs import hvlcs

def generateTest(length):
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
    return A, B, values

def graphTest():
    sizes = [25, 50, 75, 100, 150, 200, 300, 400, 500, 600]
    times = []

    for size in sizes:
        A, B, values = generateTest(size)
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