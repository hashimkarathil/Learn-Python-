# test 1

numbers = list(map(int, input().split()))
for i  in range(1, max(numbers)+1):
    if i not in numbers:
        print(i)
        break


# output: 1 2 4 5
# 3

# ......................

# test 2

a = list(map(int, input().split()))

if a == sorted(a):
    print("sorted")
else:
    print("not sorted")


# output: 1 2 5 8 10 15
# sorted

# 1 2 8 5 10 15
# not sorted
