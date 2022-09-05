def main():
    string = input("문자열:")
    acr = ""
    
    for word in string.upper().split():
        print(word)
        acr += word[0]
    
    print("머리문자열:", acr)

if __name__ == "__main__":
    main()