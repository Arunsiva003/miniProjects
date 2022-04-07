def new_game():
    i = 1
    mark = 0
    for key in questions:
        print(f"{i}) {key}")
        for j in answers[i - 1]:
            print(j)
        guess = input("enter your option: ")
        guess = guess.upper()
        if guess == questions.get(key):
            print("CORRECT!")
            mark += 1
        else:
            print(questions.get(key))
            print("WRONG!!")
        print("----------------------------")
        i += 1
    print(f"Your score: {mark}/3")


questions = {
"Python Designed by?": "B",
"Python has how many standard datatypes": "C",
"Python First Appeared in the year": "D"
}

answers = [
["A)Ritchie", "B)Guido van Rossum", "C)James Gosling", "D)NOTA"],
["A)7", "B)4", "C)6", "D)5"],
["A)1996", "B)1995", "C)1990", "D)1991"]
]
new_game()


