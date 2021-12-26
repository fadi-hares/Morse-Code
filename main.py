morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.","0": "-----"
}

def encrypt(sentence):
    encrypted_sentence = ''
    words = sentence.upper().split()
    for word in words:
        letter_list = list(word)
        encrypted_words = ''
        for letter in letter_list:
            encrypted_words += morse_code[letter] + ' '
        encrypted_sentence += encrypted_words + ','
    print(f"Please copy and save the line below:\n{encrypted_sentence}")

    
def decrypt(sentence):
    decrypted_sentence = ''
    words = sentence.split(',')
    for word in words[:-1]:
        letters = word.split()
        decrypted_words = ''
        for item in letters:
            #check if the letter is a valid morse code
            if item in morse_code.values():
                for key, value in morse_code.items():
                    if value == item:
                        decrypted_words += key
            else:
                print('Please insert a valid morse code')
        decrypted_sentence += decrypted_words + " "
    print(f"Your text is\n{decrypted_sentence.lower()}")

while True:
    user_choice = input('\nPlease Choose what do you want to do? "e" for encrypt or "d" for decrypt, "x" for exit:\n')

    if user_choice == 'e':
        user_encrypt_letter = input('\nPlease put the text you want to encrypt:\n')
        encrypt(user_encrypt_letter)
    elif user_choice == 'd':
        user_decrypt_letter = input('\nPlease put the text you want to decrypt:\n')
        decrypt(user_decrypt_letter)
    elif user_choice == 'x':
        break
    else:
        print('Please choose a valid option')
        