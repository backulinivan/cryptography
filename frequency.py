import random

class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # FIXME

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        pass

def frequency(f):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    file = open(f, 'r')
    letter_frequence = {letter:0 for letter in alphabet}
    length = 0
    frequencies = []
    for char in file.read():
        if char in alphabet:
            length += 1
            letter_frequence[char] += 1
    for letter in letter_frequence:
        letter_frequence[letter] /= length
    letter_frequence = sorted(letter_frequence.items(), key = lambda x:x[1])
    print(letter_frequence)


print(frequency('WarnPeace.txt'))
print(frequency('code.txt'))