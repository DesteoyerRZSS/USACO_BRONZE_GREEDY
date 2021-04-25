def maximize(a, b, n):
    # Finds the largest amount to use the machine to minimize uses.
    previous_different = False
    machine_uses = 0
    i = 0
    while i < n:
        if a[i] != b[i]:
            a[i] = b[i]
            if previous_different is False:
                machine_uses += 1
                previous_different = True
        else:
            previous_different = False

        i += 1  # go to next char
    print(machine_uses)


# get users input on strings A, B, and String length
N = int(input())  # convert input to a integer
print(N)
A = input()
B = input()
A = A.replace(" ", "")
B = B.replace(" ", "")

if len(A) != N or len(B) != N:
    print(str(len(A)) + str(len(B)))
    print("Strings not equal to specified string length")
    exit(1)  # Error

# convert A and B to lists so that they are easier to work with
A = list(A)
B = list(B)
maximize(A, B, N)

