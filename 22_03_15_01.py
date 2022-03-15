



# def say_hello(name,msg):
#     print("안녕하세요"+name)

# say_hello("강대권")

def get_sum(start,end):
    hap = 0
    for i in range(start,end+1):
        hap+=1
        return hap
    
    
result = get_sum(1,10)
print(result)