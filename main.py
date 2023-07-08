import random

def Character_Generate():
    list = ['Word','Crow','Apple']
    global ran_word
    ran_word = random.choice(list)
    replaced_word = ran_word
    word_len = [*range(0,len(ran_word))]
    for i in range(len(ran_word)):
        replaced_word = replaced_word.replace(replaced_word[i],'_')
    if len(ran_word) >= 5:
        rand_num = random.choices(word_len,k=2)
        for i in rand_num:
            replaced_word = replaced_word[:i] + ran_word[i] + replaced_word[i+1:]
    else:
        rand_num = random.choice(word_len)
        for i in [rand_num]:
            replaced_word = replaced_word[:i] + ran_word[i] + replaced_word[i+1:]
    
    return replaced_word

def hangman_game():
    word = Character_Generate()
    print('The Word is: %s' % word)
    print(ran_word)
    count = 0
    while True:
        suggest_word = input('Please guess the word: ')
        count += 1
        if count > 4:
            print('You Lose')
            break
        if suggest_word.lower() == ran_word.lower():
            print('Congratulations the word is: %s' % ran_word)
            break

if __name__ == '__main__':
    hangman_game()