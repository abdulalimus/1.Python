class Class2MultipleFunctions ():
    def Subfields():
        lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Subfields in AI are: ")
        for domain in lists:
            print (domain)
             
    def OddEven(num):
        if (num%2 == 0):
           Message = f"{num} is Even Number"
        else:
           Message = f"{num} is Odd Number"
        return Message 

    def Eligible(gender,age):
        if (gender == "Male"):
            if (age >= 21):
                eligibility = "ELIGIBLE"
            else:
                eligibility = "NOT ELIGIBLE"
        else:
            if (age >= 18):
                eligibility = "ELIGIBLE"
            else:
                eligibility = "NOT ELIGIBLE"
        return eligibility

    def percentage(subject1,subject2,subject3,subject4,subject5):
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percent = total / 500 * 100
        return percent

    def triangle(height,breadth,height1,height2,breadth1):
        area = (height * breadth) / 2 
        perimeter = height1 + height2 + breadth1
        return area, perimeter

            
    