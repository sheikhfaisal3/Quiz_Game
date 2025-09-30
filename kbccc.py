questions = [["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["what is the full form of HTML ?","Hyper Text Markup Language","Hi To My Life","Hello Text Me Later","Hell To This Life",1],
             ["Who is the most followed person on instagram?","Messi","khabib","neymar","Ronaldo",4],
             ["full form of ngl?","not going to laugh","not gonna lie","new gene located","nice game lional",2],
             ["who among these is a bird?","lion","cheetah ","eagle","dog",3],
             ["who is the father of history?","manmohan sing","bill gates","herodots","ishowspeed ",3],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ]
levels =[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,]
money = 0 
for i in range (0,len(questions)):
    question = questions[i]
    print(f"\nQuestion for rupees.{levels[i]}")
    print(question[0])
    print(f"1. {question[1]}       2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")
    reply =int(input("Enter your answer 1-4 or 0 for quit: "))
    if reply == 0:
        money = levels[i-1]
        print("you have choosed to quit")
        break
    if reply == question[-1]:
        print (f"\ncorrect answer, You have won Rs {levels[i]}") 
        if (i ==4):
            money = 10000
        elif(i ==9):
            money =320000 
        elif(i ==14):
            money =10000000    
    else:
        print("Wrong Answer .")
        break

print(f"your take home money is Rs{money}")   