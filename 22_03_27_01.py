
# from traceback import print_tb


# partya = {"신은혁","김연아","손연재","김철수"}
# partyb = {"최양락","김기훈","손연재","안철수"}

# print(partya & partyb)

# print(partya.intersection(partyb))


dic1 = {1: "사과", 2:"토마토", 3:"딸기", 4:"바나나"}

# a= dic1.values()
# print(a)
# b= sorted(dic1.values())
# print(b)
 
 
print(sorted(dic1.values(), values=dic1.__getitem__))