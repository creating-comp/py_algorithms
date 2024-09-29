input = [2, 5, 3, 0, 2, 3, 0, 3]
print("inputArray = ", input)
m = max(input)
count = (m+1)*[0]
for i in range(len(input)):
    count[input[i]] = input.count(input[i])
print("counterArray = ", count)

out = []
for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            out.append(i)

print(out)
