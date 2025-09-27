questions = [["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
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
for i in range (0,len(questions)):
    question = questions[i]
    print(f"\n\n[Question for rupees.{levels[i]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[2]}       d. {question[4]}")
    reply =int(input("Enter your answer in (1-4) form: "))
    money = 0  
    if reply == question[-1]:
        print (f"correct answer, You have won Rs {levels[i]}") 
        if (i ==4):
            money = 10000
        elif(i ==9):
            money =320000 
        elif(i ==14):
            money =10000000    
    else:
        print("Wrong Answer")
        break    
    