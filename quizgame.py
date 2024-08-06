#-----------------------------
def new_game():
    question_num = 0
    guesses = []
    correct_answered = 0
    for key in questions :
        print(key)
        for opt in options[question_num]:
            #it's just print the options 
            print(opt)
        guess = str(input('Enter A, B, C or D : ')).upper()
        guesses.append(guess)  
        #then check answers is that correct or not
        correct_answered += check_ans(questions.get(key), guess) 
        question_num += 1
        print('------------------------------------------------------------------------------------------------------------------')
    #we're gonna display the total score 
    display_score(correct_answered, guesses)
     
#--------------------------a
def check_ans(answer, guess):
    if answer == guess :
        print("Correct Answer")
        return 1
    else :
        print('Wrong Answer')
        return 0
    
#---------------------------
def display_score(score, guesses):
    total_score = len(options)
    print("Total Score = ", score , '/', total_score)
    #do you want to play again
    idx = 0
    for key in questions :
       print(key, " == for this your choosed option is : ", guesses[idx])
       if idx < len(guesses):
           idx += 1
            
    play_again()
#----------------------------
def play_again():
    wanna_play = 'No'
    wanna_play = str(input("Hey, wanna play again :")).capitalize()
    if(wanna_play == 'yes'.capitalize()):
           new_game()
    else:
        print("Nope! I'am bored")


questions = {
    "1.What is the primary function of a network switch?":"C",
    "2.Which protocol is used to ensure the reliable delivery of data across a network?":"B",
    "3.In a client-server network architecture, who typically provides resources and services?":"B",
    "4.What does the acronym DNS stand for in the context of computer networks?":"A"
}

options = [
    ["A. To connect different networks", "B. To route data between networks",
     "C. To filter and forward data packets to specific devices within the same network", "D. To manage IP addresses"],
    ["A. IP", "B. TCP", "C. UDP", "D. ICMP"],
    ["A. The client", "B. The server", "C. The switch", "D. The router"],
    ["A. Domain Name System", "B. Digital Network Service", "C. Data Network Server", "D. Direct Network Switch"]
]

#Let's start the game
new_game()
