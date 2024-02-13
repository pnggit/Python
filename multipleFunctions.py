class libraryFunctions:
    def Subfields():
        aiFields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for aiField in aiFields:
            print(aiField)
            
    def OddEven():
        number=int(input("Enter a number:"))
        if(number%2==0):
            print(number," is Even number")
        else:
            print(number," is Odd number")
            
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<21):
            print("NOT ELIGIBLE")
        else:
            print("Eligible")
            
    def percentage():
        average=0
        total=0
        for number in range(5):
            subject=int(input("Subject"+str(number+1)+"="))
            total=total+subject
            average=total/(number+1)
        print("Total :",total)
        print("Percentage :",average)
        
    def triangle():
        heightForArea=int(input("Height:"))
        breadthForArea=int(input("Breadth:"))
        #Area formula: (Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",((heightForArea*breadthForArea)/2))
        height1ForPerimeter=int(input("Height1:"))
        height2ForPerimeter=int(input("Height2:"))
        breadthForPerimeter=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",height1ForPerimeter+height2ForPerimeter+breadthForPerimeter)