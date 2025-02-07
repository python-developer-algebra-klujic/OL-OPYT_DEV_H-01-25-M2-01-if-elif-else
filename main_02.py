'''
Napišite program koji provjerava pripada li unesena riječ vrsti riječi palindrom.
Palindrom je riječ koja se jednako piše (i čita) s lijeva na desno i s desna na lijevo
'''

word = input('Upisite rijec koju zelite provjeriti: ')
word_reversed = '' # a; a + r; ar + b; ...

word_length = len(word)

for i in range(word_length - 1, -1, -1):
    word_reversed = word_reversed + word[i]

# if word.lower() == word_reversed.lower():
if word.upper() == word_reversed.upper(): # Srđan Golubović
    print(f'Rijec {word} je palindrom!')
else:
    print(f'Rijec {word} NIJE palindrom!')
