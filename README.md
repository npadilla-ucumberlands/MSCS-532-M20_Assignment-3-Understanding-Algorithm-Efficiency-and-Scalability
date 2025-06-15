# MSCS-532-M20_Assignment-3-Understanding-Algorithm-Efficiency-and-Scalability

Part 1: Randomized Quicksort

Files:

    quicksort_benchmark.py

Description:
This script implements Randomized Quicksort and compares it with a deterministic version using various input distributions:

    Random

    Sorted

    Reverse-sorted

    Duplicate-heavy

The program generates performance graphs and saves them as .png files.

How to run:

python quicksort_benchmark.py

Output:

    Graphs: quicksort_random.png, quicksort_sorted.png, etc.

    Runtime trends show Randomized Quicksort maintains O(n log n) performance even on adversarial inputs.

Part 2: Hashing with Chaining

Files:

    hash_table_chaining.py

Description:
A hash table implementation using chaining for collision resolution. Includes operations for:

    Insert

    Search

    Delete

Also includes a basic performance benchmark simulating increased load factors.

How to run:

python hash_table_chaining.py

Output:

    Terminal output confirms correctness and prints insertion time for 100–5000 elements.

    Insertion time remained low even with high load factors, confirming O(1 + α) behavior.

Summary of Findings

    Randomized Quicksort performs more reliably than deterministic pivot selection, especially on sorted or duplicate-heavy inputs.

    Hashing with chaining handles collisions gracefully and maintains near-constant performance with good hash function distribution.

    The combination of theoretical rigor and empirical testing provides strong validation for both algorithmic strategies.

References

Bentley, J. L., & McIlroy, M. D. (1993). Engineering a sort function. Software: Practice and Experience, 23(11), 1249–1265. https://doi.org/10.1002/spe.4380231105
Carter, J. L., & Wegman, M. N. (1979). Universal classes of hash functions. Journal of Computer and System Sciences, 18(2), 143–154. https://doi.org/10.1016/0022-0000(79)90044-8
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms (3rd ed.). MIT Press.
Knuth, D. E. (1998). The art of computer programming, volume 3: Sorting and searching (2nd ed.). Addison-Wesley.
Motwani, R., & Raghavan, P. (1995). Randomized algorithms. Cambridge University Press.
Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley.
