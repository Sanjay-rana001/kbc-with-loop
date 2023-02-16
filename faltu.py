Questions=[["1. Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
"A. Virat Kohli","B. Sunil Gavaskar","C. VVS laxman","D. Rahul Dravid","D"],
["2. Ranthambore, Sariska and Keoladeo Ghana are all names of what?",
"A. National Parks",
"B. Goosebumps",
"C. Mountains",
"D. Rivers","D"],
["3. India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?",
"A. Hindi",
"B. Punjabi",
"C. Kannada",
"D. Malayalam","D"],
["4. In terms of production, which of these is the largest train coach manufacturing unit in the world?",
"A. Integral Coach Factory, Bangalore",
"B. Integral Coach Factory, Mumbai",
"C. Integral Coach Factory, Chennai",
"D. Integral Coach Factory, Kolkata","C"],
["5. In 2020, Louise Gluck won the Nobel Prize in which category?",
"A. Music",
"B. Sports",
"C. Literature",
"D. Dance","A"],
["6. Which of the following companies was originally started as a loom manufacturing unit in 1909?",
"A. Suzuki",
"B. CEAT",
"C. Honda",
"D. Mercedes","A"]]
levels=[10000,20000,40000,80000,160000,320000]
for i in range(0,len(Questions)):
    Question=Questions[i]
    print(f"Question for Rs {levels[i]}",)
    print(Question[0])
    print("",Question[1],"\n",Question[2],"\n",Question[3],"\n",Question[4])
    Answer=input("your answer is: ").upper()

    if (Answer==Question[5]):
        print(f"Options {Question[5]} is correct answers-you won {levels[i]}Rs","""
        """)
    else:
        print(f"""option {Answer} is wrong answer
   Better Luck Next Time!!!!""") 
    
        break
    
         

        
       

 


