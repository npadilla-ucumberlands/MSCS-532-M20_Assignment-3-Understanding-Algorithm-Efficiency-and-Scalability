import random
import time
import sys
import matplotlib.pyplot as plt

# Increase recursion limit to allow large recursive calls
sys.setrecursionlimit(10000)

# --- Quicksort Implementations ---

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# --- Benchmarking Function ---

def time_sort(sort_fn, arr):
    start = time.perf_counter()
    sort_fn(arr.copy())  # Ensure sorting doesn't mutate original
    end = time.perf_counter()
    return end - start

# --- Input Generators ---

def generate_inputs(size):
    return {
        "Random": [random.randint(0, 10000) for _ in range(size)],
        "Sorted": list(range(size)),
        "Reversed": list(range(size, 0, -1)),
        "Duplicates": [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
    }

# --- Main Benchmark Routine ---

def benchmark():
    input_sizes = [100, 250, 500, 750, 1000]  # Reduced sizes to avoid recursion depth issues
    input_types = ["Random", "Sorted", "Reversed", "Duplicates"]

    results = { "Randomized": {}, "Deterministic": {} }

    for input_type in input_types:
        results["Randomized"][input_type] = []
        results["Deterministic"][input_type] = []

        for size in input_sizes:
            test_input = generate_inputs(size)[input_type]

            # Time randomized quicksort
            r_time = time_sort(randomized_quicksort, test_input)

            # Time deterministic quicksort
            try:
                d_time = time_sort(deterministic_quicksort, test_input)
            except RecursionError:
                d_time = None  # Log failure due to recursion

            results["Randomized"][input_type].append(r_time)
            results["Deterministic"][input_type].append(d_time)

    return input_sizes, results

# --- Plotting Function ---

def plot_results(sizes, results):
    for input_type in results["Randomized"]:
        plt.figure()
        r_times = results["Randomized"][input_type]
        d_times = results["Deterministic"][input_type]

        plt.plot(sizes, r_times, label="Randomized Quicksort", marker='o')
        if None not in d_times:
            plt.plot(sizes, d_times, label="Deterministic Quicksort", marker='x')
        else:
            clean_sizes = [s for s, t in zip(sizes, d_times) if t is not None]
            clean_times = [t for t in d_times if t is not None]
            plt.plot(clean_sizes, clean_times, label="Deterministic Quicksort (partial)", marker='x')

        plt.title(f"Quicksort Performance on {input_type} Input")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"quicksort_{input_type.lower()}.png")
        plt.show()

# --- Run All ---

if __name__ == "__main__":
    sizes, results = benchmark()
    plot_results(sizes, results)
