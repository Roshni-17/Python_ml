# for i in range(1, 5):
#     for j in range(1,4):
#         print(1, end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(1,4):
#         print('*', end=" ")
#     print()
#
#
# for i in range(1, 5):
#     for j in range(1,4):
#         print(i, end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(1,4):
#         print(j, end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(1,4):
#         print(j+4, end=" ")
#     print()


# for i in range(1, 5):
#     for j in range(i):
#         print(j+1, end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(i):
#         print('*', end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(i, 5):
#         print(i, end=" ")
#     print()

for i in range(1, 7):
    for j in range(1,7):
        if(i==j or i==6 or j==1):
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print()