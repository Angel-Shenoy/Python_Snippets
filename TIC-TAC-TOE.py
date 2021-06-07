#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
board=[' ' for x in range(0,9)]

def draw_board():
# Draw the TIC TAC TOE board 
    print("=======")
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print("=======")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print("=======")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print("=======")
    
def accept_user_input():
# Accept User Input   
    try:
        flag=False
        while not flag:
            user_position= int(input(" Enter the position you want to enter X 1-9 :"))
            if user_position>0 and user_position<10 and board[user_position-1]==' ':
                flag=True
                board[user_position-1]= 'X'
                draw_board()
                check_winner(board)
            elif user_position>=10 or user_position<=0:
                print(" Enter only value between 1-9 ")
                flag=False
            elif board[user_position-1] !=' ':
                print(f"Position {user_position} is already filled up. Please choose the unfilled positions")
                flag=False
    except: 
        print(" Error : Please enter your choice in integer 1-9")
        flag=False
        accept_user_input()
        
def check_winning_losing_positions(available_positions,letter):
# This function checks the winning or losing position 
    temp_board=board.copy()
    for x in available_positions:
        temp_board[x]=letter
        if(check_winner(temp_board)):
            board[x]='O'
            print("System trying to win if possible")
            print (f"Computer inserted O at {x+1} position")
            temp_board[x]=' '
            return(True)
        else:
            temp_board[x]=' '
    return(False)

def enter_computer_input():
# This function enables the system to have a wise move    
   
    computer_move=False
#Find available positions    
    available_positions=[i for i in range(0,9) if board[i]==' ']
    print ("Available Positions are : ", available_positions)
    priority_positions=[]
#Priority is to find the winning position    
    computer_move=check_winning_losing_positions(available_positions,'O')   
# If no winning position was found, Next priority is to find the position that would not enable the user to win   
    if not computer_move:
        computer_move=check_winning_losing_positions(available_positions,'X')  
# If no winning or losing position found, then use priority positions which are the corner positions        
    if not computer_move:    
        priority_positions=[]
        if len(available_positions)==0:
            print("The board is full")
        else:
            for pos in available_positions:
                if pos in[0,2,6,8]:
                    priority_positions.append(pos)
            print ("Priority Positions are : ", priority_positions) 
            
            if priority_positions==[]: # If no priority positions found, then randomly choose any of the available positions
                current_position=find_random_position(available_positions)
                board[current_position]='O'
                print (f"Computer inserted O at {current_position+1} position")
                computer_move=True
            else: # If  priority positions found, then randomly choose any of the priority positions
                current_position=find_random_position(priority_positions)
                board[current_position]='O'
                print (f"Computer inserted O at {current_position+1} position")
                computer_move=True
    draw_board() 
    return check_winner(board)
        
   
                
def find_random_position(position):
# Function that returns the random number from the list    
    return(random.choice(position))
   # return(random.choice(position))
    
    
def check_winner(my_board):
 #  This function checks the winner  
    first_row =my_board[0]==my_board[1] and my_board[2] == my_board[0]
    second_row=my_board[3]==my_board[4] and my_board[5] == my_board[3]
    third_row=my_board[6]==my_board[7] and my_board[8] == my_board[6]
    first_column=my_board[0]==my_board[3] and my_board[6] == my_board[0]
    second_column=my_board[1]==my_board[4] and my_board[7] == my_board[1]
    third_column=my_board[2]==my_board[5] and my_board[8] == my_board[2]
    first_diagonal=my_board[0]==my_board[4] and my_board[8] == my_board[0]
    second_diagonal=my_board[2]==my_board[4] and my_board[6] == my_board[2]
    # Check if any of the rows, columns or diagonals are filled with same letter
    if((first_row and my_board[0]!=' ') or(second_row and my_board[3]!=' ') or(third_row and my_board[6]!=' ') or (first_column and my_board[0]!=' ') or (second_column and my_board[1]!=' ' ) or (third_column and my_board[2]!=' ')or (first_diagonal and my_board[0]!=' ') or (second_diagonal and my_board[2]!=' ')):
        return True
    else:
        for i in range(0,9):
            if(my_board[i]==' '):
                return False
        print("Its a Tie")
        return True    

def main():
   # board=[' ' for x in range(0,9)]
     
    wish_to_play=True
    print("Welcome to the game of TIC-TAC-TOE")
    while wish_to_play:
        draw_board()
        game_end=False
        while not game_end:
            accept_user_input()
            game_end=enter_computer_input()
            first_row =board[0]==board[1] and board[2] == board[0]
            second_row=board[3]==board[4] and board[5] == board[3]
            third_row=board[6]==board[7] and board[8] == board[6]
            first_column=board[0]==board[3] and board[6] == board[0]
            second_column=board[1]==board[4] and board[7] == board[1]
            third_column=board[2]==board[5] and board[8] == board[2]
            first_diagonal=board[0]==board[4] and board[8] == board[0]
            second_diagonal=board[2]==board[4] and board[6] == board[2]
         
        if game_end:
            if(first_row and board[0]=='X'):
                print("You won as you successfully filled first row with X")
            elif(second_row and board[3]=='X'):
                print ("You won as you successfully filled second row with X")
            elif(third_row and board[6]=='X'):
                print ("You won as you successfully filled third row with X")
            elif(first_column and board[0]=='X'):
                print ("You won as you successfully filled first column with X")
            elif(second_column and board[1]=='X'):
                print ("You won as you successfully filled second column with X")
            elif(third_column and board[2]=='X'):
                print ("You won as you successfully filled third column with X")
            elif(first_diagonal and board[0]=='X'):
                print ("You won as you successfully filled first diagonal with X")
            elif(second_diagonal and board[2]=='X'):
                print ("You won as you successfully filled second diagonal with X")
            if(first_row and board[0]=='O'):
                print("You lost as system successfully filled first row with O")
            elif(second_row and board[3]=='O'):
                print ("You lost as system successfully filled Second row with O")
            elif(third_row and board[6]=='O'):
                print ("You lost as systemu successfully filled Third row with O")
            elif(first_column and board[0]=='O'):
                print ("You lost as system successfully filled first column with O")
            elif(second_column and board[1]=='O'):
                print ("You lost as system successfully filled second column with O")
            elif(third_column and board[2]=='O'):
                print ("You won as you successfully filled third column with O")
            elif(first_diagonal and board[0]=='O'):
                print ("You lost as system successfully filled first diagonal with O")
            elif(second_diagonal and board[2]=='O'):
                print ("You lost as system successfully filled second diagonal with O")
            
        #print ("Game ended!!"+ str(game_end))    
        my_input=input("Do you want to continue the game:  " )
        #print("My choice is :", my_input )
        wish_to_play=my_input.lower()=='yes' or my_input.lower()=='y'
        for i in range(0,9):
            board[i]=' '
        if(not wish_to_play):
            print("It was nice playing with you! Have a good day ahead!")
       
        


# In[3]:


main()


# In[ ]:





# In[ ]:




