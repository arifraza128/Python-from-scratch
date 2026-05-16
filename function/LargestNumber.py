def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

nums = [3, 7, 2, 9, 5]
result = find_largest(nums)

print("Largest number is:", result)
