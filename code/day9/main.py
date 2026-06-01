import heapq

def maxDiamonds(arr, k):

    # Create max heap using negative values
    max_heap = []

    for num in arr:
        heapq.heappush(max_heap, -num)

    total = 0

    # Perform k operations
    for i in range(k):

        # Get maximum diamonds bag
        max_diamond = -heapq.heappop(max_heap)

        # Add diamonds to total
        total += max_diamond

        # Remaining diamonds after taking
        remaining = max_diamond // 2

        # Push remaining back into heap
        heapq.heappush(max_heap, -remaining)

    return total


# INPUT SECTION
arr = list(map(int, input("Enter bag diamonds: ").split()))

k = int(input("Enter minutes: "))

# FUNCTION CALL
result = maxDiamonds(arr, k)

# OUTPUT
print("Maximum Diamonds:", result)