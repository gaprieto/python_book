name = 'Harrison'
guess = input("So I'm thinking of person's name. Try to guess it: ")
pos = 0

while guess != name and pos < len(name):
    print("Nope, that's not it! Hint: letter ", end='')
    print(pos + 1, "is", name[pos] + ". ", end='')
    guess = input("Guess again: ")
    pos = pos + 1

if pos == len(name) and name != guess:
    print("Too bad, you couldn't get it.  The name was", name + ".")
else:
    print("\nGreat, you got it in", pos + 1,  "guesses!")

