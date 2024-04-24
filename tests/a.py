def calculate_average(numbers):

    assert len(numbers) > 0, "List must not be empty"

    total = sum(numbers)

    average = total / len(numbers)

    return average




data = []

result = calculate_average(data)