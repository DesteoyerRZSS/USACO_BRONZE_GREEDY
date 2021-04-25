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
numchars = N
i = 0
strchanges = 0
arraystrs = []
previousdifferent = False
while i < N:
    if A[i] != "G" or A[i] != "H":
        exit(1)
    if B[i] != "G" or B[i] != "H":
        exit(1)
    if A[i] != B[i]:
        A[i] = B[i]
        if previousdifferent is False:
            #            buffer = buffer[i:] + B[i]
            strchanges += 1
            previousdifferent = True
    else:
        previousdifferent = False

    i += 1  # go to next char

#print(arraystrs)
print(strchanges)
print(A)
print(B)
