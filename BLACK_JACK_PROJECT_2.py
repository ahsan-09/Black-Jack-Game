import random

class Deck:
    def __init__(self,category,rank):
        self.deck=[]
        self.rank=rank
        self.category=category
        for i in self.category:
            for k in self.rank:
                self.deck.append([i,k])

class shuffle:
    def __init__(self,rank_values):
        self.rank_values=rank_values
        random.shuffle(self.rank_values)
        
class deal_cards:
    dealer_card=[]
    dealer_other_card=[]
    player_card=[]
    player_other_card=[]
    def __init__(self,li):
        self.random_list=li
        
    def dealer_player_cards(self):
        for i in range(0,2):
            self.dealer_card.append(self.random_list[i])
            self.player_card.append(self.random_list[i+2])
        
        for i in range(4,50,1):
            self.player_other_card.append(self.random_list[i])
            self.dealer_other_card.append(self.random_list[i+2])
            
    def check_card_player(self):
        for k in range(0,2):
            if(self.player_card[k][1]=='ace'):
                while True:
                    self.a=int(input("player! Do you want to count ace as 1 or 11? : "))
                    if self.a==1:
                        break
                    elif self.a==11:
                        self.player_card[k][1]='aces'
                        break   
                    print(" Please enter a valid value")
    
    def check_player_other_card(self,i):
        for k in range(i-1,i):
            if(self.player_other_card[k][1]=='ace'):
                while True:
                    self.a=int(input("player! Do you want to count ace as 1 or 11? : "))
                    if self.a==1:
                        break
                    elif self.a==11:
                        self.player_other_card[k][1]='aces'
                        break   
                    print(" Please enter a valid value")       

    def check_dealer_other_card(self,i):
        for k in range(i-1,i):
            if(self.dealer_other_card[k][1]=='ace'):
                self.dealer_other_card[k][1]=='aces'

    def check_dealer_card(self,sum):
        for k in range(0,2):
            if(self.dealer_card[k][1]=='ace') and (sum<17):
                self.dealer_card[k][1]=='aces'

                
    def __str__(self):
        return (f'dealer card 1 is {self.dealer_card[0][1]} of {self.dealer_card[0][0]}\nplayer card 1 is {self.player_card[0][1]} of {self.player_card[0][0]}\nplayer card 2 is {self.player_card[1][1]} of {self.player_card[1][0]}')


class Money_Bank:
    def __init__(self,player_balance,player_bet):
        self.player_balance=player_balance
        self.player_bet=player_bet
        self.dealer_money=0
    
    def player_deposit_win(self):
        self.player_balance=self.player_balance+(self.player_bet*2)
        print(f'\nPlayer!You have won the game and your Balance is Rs.{self.player_balance}.You can withdraw it')
    
    def player_withdrawl_loose(self):
        self.player_balance=self.player_balance-self.player_bet
        print(f'\nYou have lost the game and your Balance is Rs.{self.player_balance}')
        self.dealer_money=self.dealer_money+self.player_bet
        print(f'\nDealer You have won the game and you have players bet money.Your Balance is Rs.{self.dealer_money}')    

category=['Spades','Hearts','Diamonds','Clubs']
rank=['ace','Jack','King','Queen','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
value={'ace':1,'aces':11,'Jack':10,'King':10,'Queen':10,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10}
d=Deck(category,rank)
play=True
again=0
while play==True: 
    s=shuffle(d.deck)     
    #print(value['aces'])
    if (again==0):
        while True:
            try:
                balance=int(input("Player!Please enter your total balance : Rs."))
            except:
                print("You have not entered a valid value")
            else:
                break
    while True:
        try:
            bet=int(input("Player!Please enter the amount of your bet : Rs."))
            if(bet>balance):
                print("Your balance is less than your bet.")
                a=1/0
        except:
            print("You have entered a invalid value")
        else:
            break
    money=Money_Bank(balance,bet)
    print("\n\nCards are going to be dealt now.After dealing cards following are your cards\n")
    h=deal_cards(s.rank_values)
    h.dealer_player_cards()
    print(h)
    h.check_card_player()
    sum_of_dealer_card=value[h.dealer_card[0][1]]+value[h.dealer_card[1][1]]
    h.check_dealer_card(sum_of_dealer_card)
    sum_of_dealer_card=value[h.dealer_card[0][1]]+value[h.dealer_card[1][1]]
    sum_of_players_card=value[h.player_card[0][1]]+value[h.player_card[1][1]] # to get value from dictionary
    lost=0
    p=0
    k=0
    val=0
    val2=0
    while True: 
        choise=input("\nPlayer! Do You want to stay or Hit? ").upper()
        if(choise=='HIT'):
            print(f'\nPlayer! Your new card is {h.player_other_card[p][1] } of {h.player_other_card[p][0]}')
            val+=1
            h.check_player_other_card(val)
            sum_of_players_card=sum_of_players_card+value[h.player_other_card[p][1]]
            print(f'\nPlayer! Sum of Your Cards is : {sum_of_players_card}')
            if (sum_of_players_card>21):
                money.player_withdrawl_loose()
                balance=money.player_balance
                lost =1
                break
            p+=1
        elif (choise=='STAY'):
            break 
        else:
            print("Please enter a valid option")

    if(lost==0):
        print(f'\nDealer card 2 is {h.dealer_card[1][1]} of {h.dealer_card[1][0]}')
        while True:
            if (sum_of_dealer_card<17):
                print("\nDealer is getting a new card")
                print(f'\nDealer! Your new card is {h.dealer_other_card[k][1] } of {h.dealer_other_card[k][0]}')
                val2+=1
                h.check_dealer_other_card(val2)
                sum_of_dealer_card=sum_of_dealer_card+value[h.dealer_other_card[k][1]]
                if(sum_of_dealer_card>21):
                    print(f'\nDealer! Sum of Your Cards is : {sum_of_dealer_card}')
                    money.player_deposit_win()
                    balance=money.player_balance
                    break
                k+=1
            elif(sum_of_dealer_card>sum_of_players_card):
                print(f'\nDealer! Sum of Your Cards is : {sum_of_dealer_card}')
                money.player_withdrawl_loose()
                balance=money.player_balance
                break
            else:
                print(f'\nDealer! Sum of Your Cards is : {sum_of_dealer_card}')
                money.player_deposit_win()
                balance=money.player_balance
                break
    while True:
        Play_again=input("\nPlayer! Do you want to play again?Yes or No: ").upper()
        if(Play_again=='YES'):
            h.dealer_card.clear()
            h.player_card.clear()
            h.dealer_other_card.clear()
            h.player_other_card.clear()
            if(money.player_balance==0):
                print("Soryy your balance is RS.0 .You cannot play anymore")
                break
            again=1
            break
        elif(Play_again=='NO'):
            play=False
            break
        else:
            print("Please enter a valid option")