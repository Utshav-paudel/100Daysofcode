#list of list of questions
questions=[["What is the capital of France?","london","berlin","paris","moscow",3],
["What is the largest planet in our solar system?","Earth","mars","jupiter","neptune",3],
["Who painted the famous artwork \"Mona Lisa\"?","Van Gogh","Monet","da Vinci","Picasso",3],
["What is the currency of Japan?","Dollar","Euro","Yen","Peso",3],
["Who wrote the novel \"To Kill a Mockingbird\"?","J.D Salinger","Harper lee"," Ernest Hemingway","F. Scott Fitzgerald",2],
["What is the highest mountain peak in the world?","Mt Everest","Mt K2","Kangchanjunga","Lhotse",1],
["What is the largest ocean in the world?","Atlantic","Pacific","Indian","Arctic",2],
["Who is the current president of the United States?","Joe Biden","Donald trump","Barack obama","Geroge W.Bush",1],
["Which element is represented by the symbol \"Fe\" on the periodic table?","Gold","Iron","Silver","Mercury",2]]
#creating list of level for money according to kbc
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n Your question for Rs.{level[i]}:")
    print("\n",question[0])
    print(f" 1.{question[1]}  2.{question[2]}  3.{question[3]}  4.{question[4]}")
    answer=int(input("\nEnter option from (1-4) and 0 to quit : "))
    if answer==0:
        money=level[i-1]
        break
    if answer==question[-1]:
        money=level[i]
        print(f"\nCongratulations you have won Rs.{money}")
        if i==4:
            money=10000
        elif(i == 9):
             money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer")
        break
print(f"\nCongratulations you have won RS.{money}")

    
