from random import randint
num = randint(1,100)
guesses = [0]

while True:
    guess = int(input('Guess the number between 1 and 100: '))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    if guess == num:
        print(f'Nice work you guesses it in {len(guesses)} guesses.')
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
print(guesses)
