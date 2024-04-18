total = 0
count = 0

with open("numbers.txt", "r") as file:

    for line in file:
        mark = float(line.strip())  # strip() removes the newline character at the end
        total += mark
        count += 1


print(total)