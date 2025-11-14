# original list
data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

# no high outliers
# data = [104, 101, 4, 105, 103, 5, 107, 100, 106, 102, 108]

# no low outliers
# data = [104, 101, 105, 308, 103, 107, 100, 306, 106, 102, 108]

# no high and low outliers
# data = [104, 101, 105, 103, 107, 100, 106, 102, 108]

# empty list
# data = []

# including border values
# data = [104, 101, 4, 105, 200, 308, 99, 199, 103, 101, 201, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
#
# print(data)

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
