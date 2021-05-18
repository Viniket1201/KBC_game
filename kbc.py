from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == int(question["answer"]) else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    backtwo={}
    f,k,l=1,0,0
    for i in range(1,5):
            if i==ques["answer"]:
                backtwo["option"+str(i)]=ques["option"+str(i)]
                k=i
            elif f==1:
                backtwo["option"+str(i)]=ques["option"+str(i)]
                f-=1
                l=i
            else:
                backtwo["option"+str(i)]=" "
    return [backtwo,k,l]
def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    t_money=0
    l_line=1
    for i in range(15):
        print(f'\tQuestion 1: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        quit_ask=input("do you want to quit?? type quit").lower()
        if quit_ask=="quit":
            if i>0:
                t_money=QUESTIONS[i-1]["money"]
            break
        fl=1
        if l_line==1:
            p=input("do you want to use lifeline...type lifeline").lower()
            if p=="lifeline":
                l_line-=1
                fl=0
                twoans=lifeLine(QUESTIONS[i])
                print(f'\tQuestion 1: {QUESTIONS[i]["name"]}' )
                print(f'\t\tOptions:')
                print(f'\t\t\tOption 1: {twoans[0]["option1"]}')
                print(f'\t\t\tOption 2: {twoans[0]["option2"]}')
                print(f'\t\t\tOption 3: {twoans[0]["option3"]}')
                print(f'\t\t\tOption 4: {twoans[0]["option4"]}')
                print("choose",twoans[1],"or",twoans[2])
        if fl==0:
            fl=1
            ans=input()
        else:
            ans = input('Your choice ( 1-4 ) : ')
        # check for the input validations

        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print("You have won money",QUESTIONS[i]["money"])
            if i==4:
                print("you have crossed level 1")
                t_money=10000
            if i==10:
                print("you have crossed level 2")
                t_money=320000
            if i==14:
                print("you have finished this game.")
                t_money=10000000
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print("correct ans was:",QUESTIONS[i]["answer"])
            break
    print("congrulate! total money you have won:",t_money)
        # print the total money won in the end.


kbc()
