while True:
    s=str(input("Enter your Email: "))
    count=0
    for i in range(0,len(s)):
        if s[i]=="@":
            count+=1;
            break
        count+=1
    print("Username:"+s[:(count-1)],"and domain:"+(s[count:]).upper())
    r=input("DO you want to slice your email again?(Type 'y' for yes 'n' for no): ")
    if r=='y':
        pass
    else: 
        print("Thank you. See you again !")
        break
