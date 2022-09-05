
scores = []
print(scores)

scores.append(30)
print(scores)




for i in range(len(scores)):
    print(i, scores[i])

for i in range(len(scores)):
    scores[i] = "안녕"
    print(i, scores[i])
