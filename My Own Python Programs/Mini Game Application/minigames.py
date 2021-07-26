import os
import json
import re
import pyautogui
import random
import turtle
import time
import threading
import mttkinter as mt
from tkinter import messagebox as mb
from functools import partial
from PIL import Image, ImageTk

#Start of Sign In Part
with open('signupdetails.json', 'r+') as jsondata:
    if os.stat('signupdetails.json').st_size > 0:
        python_signup_details = json.load(jsondata)
    else:
        python_signup_details = {'users': [{}]}

signin = mt.mtTkinter.Tk()
signin.geometry('350x125')
signin.title('Sign in - Mini Game')
signin.resizable(0, 0)
signin.update()

signedin_guy = {}

def submit():
    global signedin_guy
    username = pyautogui.prompt('Enter account username')
    password = pyautogui.password('Enter account password')
    for i in range(0, (len(python_signup_details['users']))):
        if (python_signup_details['users'][i]['username'] == username) and (python_signup_details['users'][i]['password'] == password):
            signedin_guy = python_signup_details['users'][i]
            mb.showinfo('confirmation', 'Correct username and password!')
            signin.destroy()
            startapp()
            return
    mb.showinfo('confirmation', 'Wrong username password')

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z])                       # at least one capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9])                        # at least one numeric digit
    (?=.*[a-z])                        # at least one lower case letters
    .{8,}                              # at least 8 total digits
    $
    )''', re.VERBOSE)   

def forgotpass():
    username = pyautogui.prompt('Enter username')
    new_pass = pyautogui.password('Enter new password')
    con_pass = pyautogui.password('Re-enter new password')

    userexists = False
    for x in range(0, (len(python_signup_details['users']))):
        x -= 1
        if python_signup_details['users'][x]['username'] == username:
            userexists = True
            break

    if userexists == False:
        mb.showinfo('confirmation', 'Invalid username')
        return

    if new_pass != con_pass:
        mb.showinfo('confirmation', 'New password and confirmed password don\'t match')
        return

    mo = passwordRegex.search(new_pass)
    if not mo:
        mb.showinfo('confirmation', 'Password is not strong. Make sure to include at least 8 digits, one capital and lower case letter, one number and one of !@#&*')
        return

    j = 0
    for i in range(0, (len(python_signup_details['users'])-1)):
        j += 1
        if python_signup_details['users'][j]['username'] == username:
            break

    python_signup_details['users'][j]['password'] = new_pass
    with open('signupdetails.json', 'r+') as jsondata:
        json.dump(python_signup_details, jsondata, indent=4)
    mb.showinfo('confirmation', 'Password changed!')

def signup():
    global signedin_guy
    new_mail = pyautogui.prompt('Enter email address')
    new_fname = pyautogui.prompt('Enter your firstname')
    new_lname = pyautogui.prompt('Enter your lastname')
    new_username = pyautogui.prompt('Enter username for new account')
    new_password = pyautogui.password('Enter password for new account')
    con_password = pyautogui.password('Re-enter password for new account')

    for x in range(0, (len(python_signup_details['users']))):
        if python_signup_details['users'][x]['username'] == new_username:
            mb.showinfo('confirmation', 'Username taken!')
            return

    if new_password != con_password:
        mb.showinfo('confirmation', 'Password and Confirmation of password don\'t match')
        return

    mo = passwordRegex.search(new_password)
    if not mo:
        mb.showinfo('confirmation', 'Password is not strong. Make sure to include at least 8 digits, one capital and lower case letter, one number and one of !@#&*')
        return
    
    python_signup_details['users'].append({'username': new_username,
                                           'password': new_password,
                                           'fname': new_fname,
                                           'lname': new_lname,
                                           'email': new_mail,
                                           'gameScores': {
                                               'tictactoe': {
                                                  'matches': 0,
                                                   'wins': 0,
                                                   'loses': 0},
                                               'hangman': {
                                                   'matches': 0,
                                                   'wins': 0,
                                                   'loses': 0},
                                               'rockpaperscissor': {
                                                   'matches': 0,
                                                   'wins': 0,
                                                   'loses': 0},
                                               'whackamole': {
                                                   'matches': 0,
                                                   'wins': 0,
                                                   'loses': 0}}})

    signedin_guy = {'username': new_username,
                    'password': new_password,
                    'fname': new_fname,
                    'lname': new_lname,
                    'email': new_mail,
                    'gameScores': {
                        'tictactoe': {
                            'matches': 0,
                            'wins': 0,
                            'loses': 0},
                        'hangman': {
                            'matches': 0,
                            'wins': 0,
                            'loses': 0},
                        'rockpaperscissor': {
                            'matches': 0,
                            'wins': 0,
                            'loses': 0},
                        'whackamole': {
                            'matches': 0,
                            'wins': 0,
                            'loses': 0}}}
    
    with open('signupdetails.json', 'r+') as jsondata:
        json.dump(python_signup_details, jsondata, indent=4)
    mb.showinfo('confirmation', 'Account Created!')
    signin.destroy()
    startapp()
    
mt.mtTkinter.Button(signin, text='Sign In', command=submit).grid(row=2, column=1)
mt.mtTkinter.Button(signin, text='Forgot Password', command=forgotpass).grid(row=3, column=1)
mt.mtTkinter.Button(signin, text='Don\'t have an account? Sign up!', command=signup).grid(row=4, column=1)

#Start of Main App Part
mainapp = None

def refresh():
    global mainapp
    global signedin_guy

    hangman_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    hangman_textarea.place(x=20, y=300)
    hangman_scores = f"Matches: {signedin_guy['gameScores']['hangman']['matches']} \nWins: {signedin_guy['gameScores']['hangman']['wins']} \nLoses: {signedin_guy['gameScores']['hangman']['loses']}"
    hangman_textarea.insert(mt.mtTkinter.END, hangman_scores)

    tictactoe_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    tictactoe_textarea.place(x=230, y=300)
    tictactoe_scores = f"Matches: {signedin_guy['gameScores']['tictactoe']['matches']} \nWins: {signedin_guy['gameScores']['tictactoe']['wins']} \nLoses: {signedin_guy['gameScores']['tictactoe']['loses']}"
    tictactoe_textarea.insert(mt.mtTkinter.END, tictactoe_scores)

    rockpaperscissor_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    rockpaperscissor_textarea.place(x=470, y=300)
    rockpaperscissor_scores = f"Matches: {signedin_guy['gameScores']['rockpaperscissor']['matches']} \nWins: {signedin_guy['gameScores']['rockpaperscissor']['wins']} \nLoses: {signedin_guy['gameScores']['rockpaperscissor']['loses']}"
    rockpaperscissor_textarea.insert(mt.mtTkinter.END, rockpaperscissor_scores)

    whackamole_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    whackamole_textarea.place(x=710, y=300)
    whackamole_scores = f"Matches: {signedin_guy['gameScores']['whackamole']['matches']} \nWins: {signedin_guy['gameScores']['whackamole']['wins']} \nLoses: {signedin_guy['gameScores']['whackamole']['loses']}"
    whackamole_textarea.insert(mt.mtTkinter.END, whackamole_scores)

def signout():
    global signin
    global signedin_guy
    global mainapp

    signedin_guy = {}
    mainapp.destroy()

    signin = mt.mtTkinter.Tk()
    signin.geometry('350x125')
    signin.title('Sign in - Mini Game')
    signin.resizable(0, 0)
    signin.update()

    mt.mtTkinter.Button(signin, text='Sign In', command=submit).grid(row=2, column=1)
    mt.mtTkinter.Button(signin, text='Forgot Password', command=forgotpass).grid(row=3, column=1)
    mt.mtTkinter.Button(signin, text='Don\'t have an account? Sign up!', command=signup).grid(row=4, column=1)

def startapp():
    global mainapp
    global signedin_guy

    mainapp = mt.mtTkinter.Tk()
    mainapp.geometry('900x650')
    mainapp.title('Mini Games! Choose Game')
    mainapp.resizable(0, 0)
    mainapp.update()

    canvas = mt.mtTkinter.Canvas(mainapp, width=900, height=650)
    canvas.place(x=0, y=0)
    signout_btn = mt.mtTkinter.Button(mainapp, text='Sign Out?', fg='red', command=signout)
    signout_btn.place(x=0, y=0)
    welcome_label = mt.mtTkinter.Label(mainapp, text=f'Hello, {signedin_guy["username"]}')
    welcome_label.place(x=700, y=0)
    canvas.create_rectangle(0, 40, 900, 200, fill='blue')
    canvas.pack()

    refresh_btn = mt.mtTkinter.Button(mainapp, text='Refresh your game scores', command=refresh)
    refresh_btn.place(x=0, y=615)

    hangman_btn = mt.mtTkinter.Button(mainapp, text='Hangman!', command=hangman_start)
    hangman_btn.place(x=20, y=250)
    tic_tac_toe_btn = mt.mtTkinter.Button(mainapp, text='Tic Tac Toe', command=tic_tac_toe_setup)
    tic_tac_toe_btn.place(x=230, y=250)
    rock_paper_scissor_btn = mt.mtTkinter.Button(mainapp, text='Rock Paper Scissor', command=rock_paper_scissor)
    rock_paper_scissor_btn.place(x=470, y=250)
    whackamole_btn = mt.mtTkinter.Button(mainapp, text='Whack-a-Mole', command=whackamole)
    whackamole_btn.place(x=710, y=250)

    hangman_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    hangman_textarea.place(x=20, y=300)
    hangman_scores = f"Matches: {signedin_guy['gameScores']['hangman']['matches']} \nWins: {signedin_guy['gameScores']['hangman']['wins']} \nLoses: {signedin_guy['gameScores']['hangman']['loses']}"
    hangman_textarea.insert(mt.mtTkinter.END, hangman_scores)

    tictactoe_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    tictactoe_textarea.place(x=230, y=300)
    tictactoe_scores = f"Matches: {signedin_guy['gameScores']['tictactoe']['matches']} \nWins: {signedin_guy['gameScores']['tictactoe']['wins']} \nLoses: {signedin_guy['gameScores']['tictactoe']['loses']}"
    tictactoe_textarea.insert(mt.mtTkinter.END, tictactoe_scores)

    rockpaperscissor_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    rockpaperscissor_textarea.place(x=470, y=300)
    rockpaperscissor_scores = f"Matches: {signedin_guy['gameScores']['rockpaperscissor']['matches']} \nWins: {signedin_guy['gameScores']['rockpaperscissor']['wins']} \nLoses: {signedin_guy['gameScores']['rockpaperscissor']['loses']}"
    rockpaperscissor_textarea.insert(mt.mtTkinter.END, rockpaperscissor_scores)

    whackamole_textarea = mt.mtTkinter.Text(mainapp,height=3,width=15,bg="#FFFF99")
    whackamole_textarea.place(x=710, y=300)
    whackamole_scores = f"Matches: {signedin_guy['gameScores']['whackamole']['matches']} \nWins: {signedin_guy['gameScores']['whackamole']['wins']} \nLoses: {signedin_guy['gameScores']['whackamole']['loses']}"
    whackamole_textarea.insert(mt.mtTkinter.END, whackamole_scores)

#Hangman
hangman_sel_tk = None
t = None

def hang_wrong1():
    t.up()
    t.backward(150)
    t.left(90)
    t.backward(150)
    t.down()
    t.forward(435)
    t.right(90)
    t.forward(230)
    t.right(45)
    t.forward(130)
    t.right(45)

def hang_wrong2():
    t.up()
    t.backward(3)
    t.right(90)
    t.forward(5)
    t.down()
    t.circle(50)

def hang_wrong3():
    t.up()
    t.left(90)
    t.forward(100)
    t.down()
    t.forward(150)

def hang_wrong4():
    t.up()
    t.right(180)
    t.forward(145)
    t.left(150)
    t.down()
    t.forward(115)

def hang_wrong5():
    t.up()
    t.right(180)
    t.forward(115)
    t.right(115)
    t.down()
    t.forward(115)

def hang_wrong6():
    t.up()
    t.right(180)
    t.forward(115)
    t.right(215)
    t.forward(145)
    t.right(35)
    t.down()
    t.forward(120)

def hang_wrong7():
    t.up()
    t.right(180)
    t.forward(120)
    t.right(120)
    t.down()
    t.forward(120)

def hangman_maingame(wordlist):
    global t
    global python_signup_details
    global signedin_guy

    hangman_sel_tk.destroy()
    temp = random.choice(wordlist)
    word = temp.lower()
    turtle.title('Hangman - Mini Games')
    t = turtle.Pen()

    answerArray = []
    for i in range(len(word)):
        answerArray.append('_')

    wrongs = 0
    remLetters = len(word)

    while remLetters > 0:
        stringAnswer = ''
        for j in answerArray:
            stringAnswer += j + ' '
        mb.showinfo('confirmation', stringAnswer)

        temp_guess = pyautogui.prompt('Enter one letter guess')
        guess = temp_guess.lower()
        prevRem = remLetters

        if len(guess) != 1:
            mb.showinfo('Enter one letter ONLY')
            continue
        else:
            for l in range(0, len(word)):
                if word[l] == guess:
                    answerArray[l] = guess
                    remLetters -= 1
            if prevRem == remLetters:
                wrongs = wrongs + 1
                if wrongs == 1:
                    hang_wrong1()
                elif wrongs == 2:
                    hang_wrong2()
                elif wrongs == 3:
                    hang_wrong3()
                elif wrongs == 4:
                    hang_wrong4()
                elif wrongs == 5:
                    hang_wrong5()
                elif wrongs == 6:
                    hang_wrong6()
                else:
                    hang_wrong7()
                    break

    if wrongs < 7:
        signedin_guy['gameScores']['hangman']['matches'] += 1
        signedin_guy['gameScores']['hangman']['wins'] += 1
        mb.showinfo('confirmation', 'You win!')
    else:
        signedin_guy['gameScores']['hangman']['matches'] += 1
        signedin_guy['gameScores']['hangman']['loses'] += 1
        mb.showinfo('confirmation', 'You lose.')

    j = 0
    for i in range(0, (len(python_signup_details['users'])-1)):
        j += 1
        if python_signup_details['users'][j]['username'] == signedin_guy['username']:
            break

    python_signup_details['users'][j] = signedin_guy
    with open('signupdetails.json', 'r+') as jsondata:
        json.dump(python_signup_details, jsondata, indent=4)

    mb.showinfo('confirmation', f'The word was {word}')
    turtle.bye()

def hangman_start():
    global hangman_sel_tk
    hangman_sel_tk = mt.mtTkinter.Tk()
    hangman_sel_tk.geometry('400x300')
    hangman_sel_tk.title('Select word for Hangman')
    hangman_sel_tk.resizable(0, 0)
    hangman_sel_tk.update()

    food = ['Chicken', 'Pizza', 'Pasta', 'Dimsum', 'Quesadilla', 'Nachos', 'Hamburger', 'Cheeseburger', 'Noodles', 'Taco', 'Fish', 'Lasagna', 'Brownie', 'Cookie', 'Salad']
    fruits = ['Apple', 'Mango', 'Strawberry', 'Kiwi', 'Banana', 'Orange', 'Pear', 'Watermelon', 'Muskmelon', 'Papaya', 'Plum', 'Grapes', 'Avocado', 'Durian', 'Cherry']
    countries = ['India', 'China', 'England', 'Canada', 'Singapore', 'Thailand', 'Pakistan', 'Australia', 'Spain', 'France', 'Germany', 'Switzerland', 'Mexico', 'Brazil', 'Cuba']
    sports = ['Cricket', 'Football', 'Basketball', 'Handball', 'Volleyball', 'Baseball', 'Karate', 'Boxing', 'Tennis', 'Rugby', 'Hockey', 'Golf', 'Cycling', 'Running', 'Archery']
    vegetables = ['Onion', 'Potato', 'Tomato', 'Capsicum', 'Chilli', 'Brinjal', 'Lettuce', 'Cabbage', 'Carrot', 'Coriander', 'Bottleguard', 'Fenugreek', 'Cauliflower', 'Radish', 'Spinach']
    naruto = ['Obito', 'Kakashi', 'Naruto', 'Sasuke', 'Madara', 'Hashirama', 'Jiraiya', 'Orochimaru', 'Minato', 'Tobirama', 'Hiruzen', 'Guy', 'Danzo', 'Itachi', 'Nagato']
    languages = ['English', 'Hindi', 'French', 'Spanish', 'Japanese', 'German', 'Chinese', 'Hebrew', 'Arabic', 'Bengali', 'Russian', 'Latin', 'Portuguese', 'Greek', 'Punjabi']
    animals = ['Lion', 'Tiger', 'Elephant', 'Zebra', 'Giraffe', 'Jaguar', 'Cheetah', 'Dog', 'Cat', 'Rabbit', 'Camel', 'Deer', 'Panda', 'Monkey', 'Gorilla']
    colors = ['Green', 'Red', 'Blue', 'Yellow', 'Orange', 'Violet', 'Black', 'White', 'Gray', 'Indigo', 'Pink', 'Golden', 'Silver', 'Brown', 'Turquoise']

    mt.mtTkinter.Button(hangman_sel_tk, text=' Food ', command=partial(hangman_maingame, food)).grid(row=0, column=0)
    mt.mtTkinter.Button(hangman_sel_tk, text='Fruits', command=partial(hangman_maingame, fruits)).grid(row=0, column=1)
    mt.mtTkinter.Button(hangman_sel_tk, text='Sports', command=partial(hangman_maingame, sports)).grid(row=0, column=2)
    mt.mtTkinter.Button(hangman_sel_tk, text='Countries', command=partial(hangman_maingame, countries)).grid(row=1, column=0)
    mt.mtTkinter.Button(hangman_sel_tk, text='  Naruto ', command=partial(hangman_maingame, naruto)).grid(row=1, column=1)
    mt.mtTkinter.Button(hangman_sel_tk, text='Languages', command=partial(hangman_maingame, languages)).grid(row=1, column=2)
    mt.mtTkinter.Button(hangman_sel_tk, text=' Animals  ', command=partial(hangman_maingame, animals)).grid(row=2, column=0)
    mt.mtTkinter.Button(hangman_sel_tk, text='  Colors  ', command=partial(hangman_maingame, colors)).grid(row=2, column=1)
    mt.mtTkinter.Button(hangman_sel_tk, text='Vegetables', command=partial(hangman_maingame, vegetables)).grid(row=2, column=2)

#Tic Tac Toe
ttt_tk = None
turns = 0
theBoard = {'top-L': ' ',
                'top-M': ' ',
                'top-R': ' ',
                'mid-L': ' ',
                'mid-M': ' ',
                'mid-R': ' ',
                'low-L': ' ',
                'low-M': ' ',
                'low-R': ' '}

def ttt_endgame():
    global turns
    global ttt_tk
    global python_signup_details
    global signedin_guy

    if (theBoard['top-L'] == 'x' and theBoard['top-M'] == 'x' and theBoard['top-R'] == 'x') \
    or (theBoard['mid-L'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['mid-R'] == 'x') \
    or (theBoard['low-L'] == 'x' and theBoard['low-M'] == 'x' and theBoard['low-R'] == 'x') \
    or (theBoard['top-L'] == 'x' and theBoard['mid-L'] == 'x' and theBoard['low-L'] == 'x') \
    or (theBoard['top-M'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['low-M'] == 'x') \
    or (theBoard['top-R'] == 'x' and theBoard['mid-R'] == 'x' and theBoard['low-R'] == 'x') \
    or (theBoard['top-L'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['low-R'] == 'x') \
    or (theBoard['top-R'] == 'x' and theBoard['mid-M'] == 'x' and theBoard['low-L'] == 'x'):
        signedin_guy['gameScores']['tictactoe']['matches'] += 1
        signedin_guy['gameScores']['tictactoe']['wins'] += 1
        j = 0
        for i in range(0, (len(python_signup_details['users'])-1)):
            j += 1
            if python_signup_details['users'][j]['username'] == signedin_guy['username']:
                break

        python_signup_details['users'][j] = signedin_guy
        with open('signupdetails.json', 'r+') as jsondata:
            json.dump(python_signup_details, jsondata, indent=4)

        ttt_tk.destroy()
        mb.showinfo('confirmation', 'You win!')
        return True
    elif (theBoard['top-L'] == 'o' and theBoard['top-M'] == 'o' and theBoard['top-R'] == 'o') \
    or (theBoard['mid-L'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['mid-R'] == 'o') \
    or (theBoard['low-L'] == 'o' and theBoard['low-M'] == 'o' and theBoard['low-R'] == 'o') \
    or (theBoard['top-L'] == 'o' and theBoard['mid-L'] == 'o' and theBoard['low-L'] == 'o') \
    or (theBoard['top-M'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['low-M'] == 'o') \
    or (theBoard['top-R'] == 'o' and theBoard['mid-R'] == 'o' and theBoard['low-R'] == 'o') \
    or (theBoard['top-L'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['low-R'] == 'o') \
    or (theBoard['top-R'] == 'o' and theBoard['mid-M'] == 'o' and theBoard['low-L'] == 'o'):
        signedin_guy['gameScores']['tictactoe']['matches'] += 1
        signedin_guy['gameScores']['tictactoe']['loses'] += 1
        j = 0
        for i in range(0, (len(python_signup_details['users'])-1)):
            j += 1
            if python_signup_details['users'][j]['username'] == signedin_guy['username']:
                break

        python_signup_details['users'][j] = signedin_guy
        with open('signupdetails.json', 'r+') as jsondata:
            json.dump(python_signup_details, jsondata, indent=4)

        ttt_tk.destroy()
        mb.showinfo('confirmation', 'You lose')
        return True
    elif turns >= 9:
        signedin_guy['gameScores']['tictactoe']['matches'] += 1
        j = 0
        for i in range(0, (len(python_signup_details['users'])-1)):
            j += 1
            if python_signup_details['users'][j]['username'] == signedin_guy['username']:
                break

        python_signup_details['users'][j] = signedin_guy
        with open('signupdetails.json', 'r+') as jsondata:
            json.dump(python_signup_details, jsondata, indent=4)

        ttt_tk.destroy()
        mb.showinfo('confirmation', 'Draw')
        return True

def ttt_oturn():
    poslist = list(theBoard.keys())
    randPos = None
    while True:
        randPos = random.choice(poslist)
        if theBoard[randPos] == ' ':
            break

    theBoard[randPos] = 'o'
    if ttt_endgame():
        return
    tic_tac_toe()

def ttt_maingame(pos):
    global turns
    turns += 1
    theBoard[pos] = 'x'
    if ttt_endgame():
        return
    ttt_oturn()

def tic_tac_toe_setup():
    global ttt_tk
    ttt_tk = mt.mtTkinter.Tk()
    ttt_tk.title('Tic Tac Toe - Mini Games')
    ttt_tk.geometry('450x450')
    ttt_tk.resizable(0, 0)
    ttt_tk.update()
    tic_tac_toe()

def tic_tac_toe():
    global ttt_tk
    mt.mtTkinter.Button(ttt_tk, text=theBoard['top-L'], command=partial(ttt_maingame, 'top-L'), height=5, width=15).grid(row=0, column=0)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['top-M'], command=partial(ttt_maingame, 'top-M'), height=5, width=15).grid(row=0, column=1)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['top-R'], command=partial(ttt_maingame, 'top-R'), height=5, width=15).grid(row=0, column=2)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['mid-L'], command=partial(ttt_maingame, 'mid-L'), height=5, width=15).grid(row=1, column=0)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['mid-M'], command=partial(ttt_maingame, 'mid-M'), height=5, width=15).grid(row=1, column=1)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['mid-R'], command=partial(ttt_maingame, 'mid-R'), height=5, width=15).grid(row=1, column=2)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['low-L'], command=partial(ttt_maingame, 'low-L'), height=5, width=15).grid(row=2, column=0)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['low-M'], command=partial(ttt_maingame, 'low-M'), height=5, width=15).grid(row=2, column=1)
    mt.mtTkinter.Button(ttt_tk, text=theBoard['low-R'], command=partial(ttt_maingame, 'low-R'), height=5, width=15).grid(row=2, column=2)

#Rock Paper Scissor
rps_tk = None

def rps_choice_tonum(choice):
    rps_action_tonum = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps_action_tonum[choice]

def rps_maingame(action):
    global rps_tk
    global signedin_guy
    global python_signup_details

    user_choice = ''
    if action == 'rock':
        user_choice = 'rock'
    elif action == 'paper':
        user_choice = 'paper'
    elif action == 'scissor':
        user_choice = 'scissor'
    comp_choice = random.choice(['rock', 'paper', 'scissor'])

    comp_num = rps_choice_tonum(comp_choice)
    user_num = rps_choice_tonum(user_choice)

    res = ''
    if user_num == comp_num:
        signedin_guy['gameScores']['rockpaperscissor']['matches'] += 1
        res = 'Tie'
    elif (user_num-comp_num) % 3 == 1:
        res = 'You Win'
        signedin_guy['gameScores']['rockpaperscissor']['matches'] += 1
        signedin_guy['gameScores']['rockpaperscissor']['wins'] += 1
    else:
        res = 'You lose'
        signedin_guy['gameScores']['rockpaperscissor']['matches'] += 1
        signedin_guy['gameScores']['rockpaperscissor']['loses'] += 1

    rps_resarea = mt.mtTkinter.Text(rps_tk, height=12, width=30, bg='#FFFF99')
    rps_resarea.grid(row=3, column=0)
    rps_resarea_text = f'Your choice: {user_choice} \nComp choice: {comp_choice} \nResult: {res}'
    rps_resarea.insert(mt.mtTkinter.END, rps_resarea_text)

    j = 0
    for i in range(0, (len(python_signup_details['users'])-1)):
        j += 1
        if python_signup_details['users'][j]['username'] == signedin_guy['username']:
            break

    python_signup_details['users'][j] = signedin_guy
    with open('signupdetails.json', 'r+') as jsondata:
        json.dump(python_signup_details, jsondata, indent=4)

def rock_paper_scissor():
    global rps_tk
    rps_tk = mt.mtTkinter.Tk()
    rps_tk.geometry('400x300')
    rps_tk.title('Rock Paper Scissor - Mini Games')
    rps_tk.resizable(0, 0)
    rps_tk.update()

    button_rock = mt.mtTkinter.Button(rps_tk, text='     Rock     ', bg='skyblue', command=partial(rps_maingame, 'rock'))
    button_rock.grid(row=0, column=0)
    button_paper = mt.mtTkinter.Button(rps_tk, text='    Paper     ', bg='pink', command=partial(rps_maingame, 'paper'))
    button_paper.grid(row=1, column=0)
    button_scissor = mt.mtTkinter.Button(rps_tk, text='   Scissor    ', bg='lightgreen', command=partial(rps_maingame, 'scissor'))
    button_scissor.grid(row=2, column=0)

#Whack-a-Mole
whackamole_tk = None
imgBtn = None
tkimg = None
whack_tarea = None
whack_display = None
points = 0

class Whack:
    def repos(self):
        global whackamole_tk
        global imgBtn
        global tkimg

        imgBtn.place_forget()

        xpos = random.randint(0, 340)
        ypos = random.randint(0, 340)

        imgBtn = mt.mtTkinter.Button(whackamole_tk, image=tkimg, command=self.maingame_whackamole)
        imgBtn.place(x=xpos, y=ypos)

    def update_points(self):
        global whack_tarea
        global whack_display
        global whackamole_tk
        global points

        whack_tarea = mt.mtTkinter.Text(whackamole_tk, height=3, width=12, bg='#FFFF99')
        whack_tarea.place(x=350, y=350)
        whack_display = f'Score: {points}'
        whack_tarea.insert(mt.mtTkinter.END, whack_display)

    def maingame_whackamole(self):
        global imgBtn
        global points
        global whackamole_tk

        points += 1
        self.update_points()
        if points >= 10:
            mb.showinfo('Confirmation', 'You Win!')
            signedin_guy['gameScores']['whackamole']['matches'] += 1
            signedin_guy['gameScores']['whackamole']['wins'] += 1

            j = 0
            for i in range(0, (len(python_signup_details['users'])-1)):
                j += 1
                if python_signup_details['users'][j]['username'] == signedin_guy['username']:
                    break

            python_signup_details['users'][j] = signedin_guy
            with open('signupdetails.json', 'r+') as jsondata:
                json.dump(python_signup_details, jsondata, indent=4)
            return
        self.repos()

    def point_decrease(self):
        global whackamole_tk
        global points
        while True:
            time.sleep(1.5)
            points -= 1
            self.update_points()
            if points <= -10:
                mb.showinfo('confirmation', 'You lose')
                signedin_guy['gameScores']['whackamole']['matches'] += 1
                signedin_guy['gameScores']['whackamole']['loses'] += 1

                j = 0
                for i in range(0, (len(python_signup_details['users'])-1)):
                    j += 1
                    if python_signup_details['users'][j]['username'] == signedin_guy['username']:
                        break

                python_signup_details['users'][j] = signedin_guy
                with open('signupdetails.json', 'r+') as jsondata:
                    json.dump(python_signup_details, jsondata, indent=4)
                return
            self.repos()

def whackamole():
    global whackamole_tk
    global imgBtn
    global tkimg
    global whack_tarea
    global whack_display
    global points
    
    whackamole_tk = mt.mtTkinter.Toplevel()
    whackamole_tk.geometry('450x450')
    whackamole_tk.title('Whack-a-mole - Mini Games')
    whackamole_tk.resizable(0, 0)
    whackamole_tk.update()

    tkimg = ImageTk.PhotoImage(Image.open('montymole.png'))
    xpos = random.randint(0, 340)
    ypos = random.randint(0, 340)

    whack = Whack()

    imgBtn = mt.mtTkinter.Button(whackamole_tk, image=tkimg, command=whack.maingame_whackamole)
    imgBtn.place(x=xpos, y=ypos)

    whack_tarea = mt.mtTkinter.Text(whackamole_tk, height=3, width=12, bg='#FFFF99')
    whack_tarea.place(x=350, y=350)
    whack_display = f'Score: {points}'
    whack_tarea.insert(mt.mtTkinter.END, whack_display)

    threadObj = threading.Thread(target=whack.point_decrease)
    threadObj.setDaemon(True)
    threadObj.start()
