class Assignment:
    def triangle():
        h = int(input("height = "))
        b= int(input("breadth = "))
        print("Area formula: (height*breath)/2")
        print("Area of Triangle:",(h*b)/2)
        h1 = int(input("height1 = "))
        h2 = int(input("height2 = "))
        b= int(input("breadth = "))
        print("perimeter formula: height1+height2+breath")
        print("perimeter of Triangle:",h1+h2+b)
        
    def percentage():
        s1 = int(input("subject1 = "))
        s2 = int(input("subject2 = "))
        s3 = int(input("subject3 = "))
        s4 = int(input("subject4 = "))
        s5 = int(input("subject5 = "))
        total=s1+s2+s3+s4+s5
        print("total:",total)
        percentage= total/5
        print("percentage",percentage)
        
    def marriage():
        gender= input("enter gender:")
        if gender == "male" or "Male":
            Age = int(input("Enter any age = "))
            if Age >=21:
                print("eligible for marriage")
            else:
                print("not eligible")
        elif gender == "female"or "Female":
            Age = int(input("Enter any age = "))
            if Age >=18:
                print("eligible for marriage")
            else:
                print("not eligible")
        else:
            print("give correct input")
            
 
    def oddeven():
        i = int(input("Enter any number = "))
        if i%2 == 0:
            print("Number is even")
        else:
            print("Number is even")
            
       
    def subfields():
        List=["sub-fields in Ai are;","machine learing","Neural Networks","vision","robotics","speech processing","natural language processing"]
        for i in List:
            print(i)