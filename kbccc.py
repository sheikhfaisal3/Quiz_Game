questions = [["1.which building is the tallest building in the world?","Burj khalifa","taj mahal","qutub minar","red fort",1],
             ["2,what is the full form of HTML ?","Hyper Text Markup Language","Hi To My Life","Hello Text Me Later","Hell To This Life",1],
             ["3.Who is the most followed person on instagram?","Messi","khabib","neymar","Ronaldo",4],
             ["4.full form of ngl?","not going to laugh","not gonna lie","new gene located","nice game lional",2],
             ["5.who among these is a bird?","lion","cheetah ","eagle","dog",3],
             ["6.speed of light?","3*10^7 m/s","3*10^3 m/s","3*10^9 m/s ","3*10^8 m/s",4],
             ["7.identify the footballer among these players?","michal jordan","virat kholi","rodrygogoes","cena",3],
             ["8.famous place in kashmir?","Burj khalifa","taj mahal","qutub minar","gulmarg",4],
             ["9.what is the full form of ik?"," i know","i knew","inside kashmir","i'm king",1],
             ["10.find the missing word in \"Samsng\"?","a","j","e","u",4],
             ["11.shah jahan built?","Burj khalifa","taj mahal","ifel tower","statue of liberty",2],
             ["12.what was titanic","ship","plane","car","bus",1],
             ["13.identify the harry potter chracter?","charles","vinod","malfoy","pokemon",3],
             ["14.how many states are there in india (consider j&k as a state )?","22","29","8","10",2],
             ["15.kashmir is well known for its?","rudeness","racisim","beauty & hospitality","theifs",3],
             ["16.what was the name of the actress in titanic?","pooja","mary","elizabeth","rose",4]
            ]

levels =[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0 
print(len(levels))
for i in range (0,len(questions)):
    question = questions[i]
    print(f"\nQuestion for {levels[i]} Rupees")
    print(question[0])
    print(f"1. {question[1]}       2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")
    reply =int(input("Enter your answer 1-4 or 0 for quit: "))
    if reply == 0:
        money = levels[i-1]
        print("you have choosed to quit:")
        break
    if reply == question[-1]:
        print (f"\ncorrect answer, You have won Rs {levels[i]}") 
        if (i ==5):
            money = 10000
        elif(i ==10):
            money =320000     
        elif(i ==15):
            money =10000000
            print("Congratulations You have won this Game❤️")
                
    else:
        print("Wrong Answer .")
        break

print(f"your take home money is Rs{money}")   