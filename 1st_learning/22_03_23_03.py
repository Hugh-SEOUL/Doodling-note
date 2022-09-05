

# double_list = [
#                 [1,2,3,4,5],
#                 [6,7,8,9,10],
#                 [11,12,13,14,15]    
# ]

# print(double_list)
# print(double_list[0])


# for i in range(len(double_list)):
#     for j in range(len(double_list[i])):
#         print(double_list[i][j],end="\t")
#     print()


rows = int(input("원하는 행을 입력해주세요:"))
cols = int(input("원하는 열을 입력해주세요:"))
li1 = []
for row in range(rows):
    li1 += [[0]* cols]
print(li1)