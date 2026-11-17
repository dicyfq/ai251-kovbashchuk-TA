def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n):
    comparisons = 0
    assignments = 0
    k = i
    assignments += 1

    while True:
        j = 2 * k + 1
        assignments += 1
        comparisons += 1
        if j >= n:
            break

        comparisons += 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
            assignments += 1

        comparisons += 1
        if arr[k] >= arr[j]:
            break

        swap(arr, k, j)
        assignments += 3
        k = j
        assignments += 1

    return comparisons, assignments

def heapsort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 1

    for i in range(n // 2 - 1, -1, -1):
        c, a = sink(arr, i, n)
        comparisons += c
        assignments += a

    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        assignments += 3
        c, a = sink(arr, 0, i)
        comparisons += c
        assignments += a

    return arr, comparisons, assignments

my_list = [90, 10, 15, 80, 100, 6, 57, 5, 29]
print("оригінальний масив:", my_list)

sorted_list, comps, assigs = heapsort(my_list.copy())

print("відсортований масив:", sorted_list)
print(f"кількість порівнянь: {comps}")
print(f"кількість присвоєнь: {assigs}")
