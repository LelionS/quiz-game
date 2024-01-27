a=input("whats your name? ")
b=input("hello "+a+", would you wish to play a quiz game(y/n)").lower()
if b=="y":
  print("get ready to start in a few!")
elif b=="n":
  print("thank you, you can try other times for more fun")
else:
  print("Invalid data entry, try again!")
  print("Welcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
if b == 'y':
    question_no += 1
    quiz = input(f"\n{question_no}.who's the powerful person in human history ").lower()
    if quiz == 'muhammad':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is: 	Muhammad')

# ------1
    question_no += 1
    quiz = input(f'\n{question_no}. How long did world war one last ').lower()
    
    if quiz == 'four years' or "4 years":
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is: Four years')

# -----2
    question_no += 1
    quiz = input(f'\n{question_no}. Name of one of the founder members of Apple ').lower()
    
    if quiz == 'Steve Job'or'Ronald Wayne'or'Steve Wozniak':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer can either be: Steve Job, Steve Wozniak or Ronald wayne')

# -----3
    question_no += 1
    quiz = input(f'\n{question_no}. Who among the disciples of jesus lived till old age    ').lower()
    
    if quiz == 'john':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is: power supply unit')


# -----4
    question_no += 1
    quiz = input(f'\n{question_no}. what was one of three possible causes for the death of Alexander the Great ').lower()
    
    if quiz == 'Malaria'or'liver disease'or'Typhoid':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> read only memory')


# ------5 

else:
    print('thank you you are out of a game.')
    quit()

# ------score
print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')
