import random



#global gameboard is a dictionary, keys are diffrent places to put a token and values are x or o token
board = {0: ' ' , 1: ' ' , 2: ' ' ,
 
         3: ' ' , 4: ' ' , 5: ' ' ,

         6: ' ' , 7: ' ' , 8: ' ' }



#global varable turn, a player starts a game with x 
turn='x'
#global varable game_end, firsti its value is false
game_end=False



#function checks whose turn is and shows the board to a player or calls function, which generates GoPiGo's move
def check_turn():

    if(turn!='o'):
        print_board()
        ask_players_move()
    else:
        print("GoPiGon vuoro")
        generate_gopigos_move()
  
  
  
#function generates GoPiGo's random move until the place is free 
def generate_gopigos_move():

    while True:
    
        gopigos_move=random.randint(1,9)
                   
        if(check_place(gopigos_move)):
            set_place(gopigos_move)
            break
        else:
            
            continue



#function changes the turn between a player and the GoPiGo
def change_turn():

    global turn
    if(turn=='x'):
        
        turn='o'
    else:
        turn='x'



#function prints the gameboard
def print_board():

    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

            

#function checks if the players input is int type and between 1 and 9 and asks new values if it is needed
def check_input():
   
    while True:
        try:
            value=int(input())
           
        except ValueError:
            print ("Anna luku")
            continue
        
        if(value < 1 or value > 9):
            print ("Luvun tulee olla valilla 1-9")
            continue
        
        else:
            break
        
    return value



#function asks players move until the place is free and calls a function to set token to that place  
def ask_players_move():

    print("Sinun vuorosi", turn , "Valitse ruutu (1-9) mihin haluat lisätä merkin ")
   
    while True:
        value=check_input()
    
        if(check_place(value)):
            set_place(value)
            break
        
        else:
            print("Paikka on varattu. Tee uusi valinta")
      


#the place to which player or GoPiGo wants to move is checked
def check_place(value):
       
    if(board[value-1]==' '):
        return True
    else:
        return False
    


#function adds token to its place in the board 
def set_place(value):
 
    board[value-1]=turn
    check_situation() 
    


#function resets the turn and board variables and starts a new game by calling the play_new_game function
def start_new_game():
    
    global turn
    turn='x'
    for key in board.keys():
        board[key]=' '
        
    play_new_game()



#function asks player if she or he wants to play a new game
def ask_new_game():
    
    global game_end
    print("Haluatko pelata uuden pelin? K=kyllä, E=ei ")
   
    while True:
        
        new_game=input()
        if(new_game=='k' or new_game=='K'):
            start_new_game()
            break
         
        elif(new_game=='e' or new_game=='E'):
            game_end=True
            print("Hei hei!")
            break
        
        else:
            print ("Anna kirjain k/e tai K/E ")
            continue



#fuction checks all the diffrent rows where could be a win in the board from dictionary
#and returns true in there is one 
def check_win():
  
    winning_rows ={0: (0,1,2), 1:(3,4,5), 2:(6,7,8), 3: (0,3,6), 4: (1,4,7), 5: (2,5,8), 6: (0,4,8), 7: (2,4,6)}
    for values in winning_rows.values():
        counter=0
        for value in values:
             
            if(board[value]==turn):
                counter+=1
                if(counter==3):
                    return True
                
    return False    
     


#fuction checks if board is full and if it is, it returns true which means that there is a tie in the game
def check_tie():
    
    for key in board:
        if(board[key]==' '):
            return False
       
    return True




#fuction checks if there is a win or tie in the board and tells that to the player.
#Otherwise it changes the turn of the player.
def check_situation():
    
    if(check_win()):
        print_board()
        print( turn, " voitti.")
        ask_new_game()
        
    elif(check_tie()):
        print_board()
        print("Peli paattyi tasapeliin.")
        ask_new_game()
        
    else:
        change_turn() 
        
  

#first function checks game_end variable and if it is false the game begins or continues by
#calling check_turn() function. Otherwise the game ends.
def play_new_game():

    while True:
        if(game_end==False):
            check_turn()
        else:
            break
  
 
 
#program starts from main function when you run it
if __name__ == "__main__":
    
    play_new_game()
