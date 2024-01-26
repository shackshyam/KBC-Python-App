Questions = [{
    "Question" : "Q1.Which is largest Country in world ?",
    "Option" : ["1.India 2.America 3.Russia 4.China"],
    "Answer" : 3
},{
   "Question" : "Q2.Which is Smallest Country in world ?",
    "Option" : ["1.SriLanka 2.Nepal 3.Russia 4.Indonesia"],
    "Answer" : 1
},{
   "Question" : "Q3.Which is Expensive Country in world ?",
    "Option" : ["1.America 2.Pakistan 3.Dubai 4.China"],
    "Answer" : 1 
},{
   "Question" : "Q4.Which is largest Country in Population in world ?",
    "Option" : ["1.Nepal 2.America 3.Pakistan 4.China"],
    "Answer" : 4 
},{
   "Question" : "Q5.Which is largest Country Across Area in world ?",
    "Option" : ["1.India 2.Bhutan 3.Russia 4.SriLanka"],
    "Answer" : 3 
}]

PriceWon = 0
QuestionIndex = 0
GameOver = False

PlayerName = str(input("Please Enter Your Name : ")).capitalize()
print("So", "Mr/Mrs." + PlayerName, "Let's Begin :>")

while not GameOver:
    Question = Questions[QuestionIndex]
    print(Question["Question"])
    for option in Question["Option"]:
        print(option)
    UserAnswer = int(input("Enter The Number Of Correct Option : "))  
    if UserAnswer == Question["Answer"]:
        print("Congratualtion, You Have Choice Correct Option!")
        PriceWon += 1000
    else:
        print("You Have Chosen Incorrect Option!")
        GameOver = True
            
    QuestionIndex += 1
    if QuestionIndex == len(Questions):
        GameOver = True
        
print("Mr."+PlayerName,"Total Price You Have Won ₹" ,PriceWon)
