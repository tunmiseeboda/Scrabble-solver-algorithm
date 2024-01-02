from itertools import product

def load_dictionary():
  dictionary = set()
  with open('dictionary.txt', 'r') as file:
    for word in file:
      dictionary.add(word.strip())
  return dictionary

def permute_letters(letters, dictionary):
  words = []
  for r in range(1, len(letters) + 1):
    perms = [''.join(perm) for perm in product(letters, repeat=r)]
    for word in perms:
      if word in dictionary:
        words.append(word)
  return words

def valid_words(words):
    with open('valid_words.txt', 'w') as file:
        for word in words:
            file.write(word + "\n")
        

letters = []
letter_amount = 0
while letter_amount < 7:
  letter = input('Enter a letter: ')
  if len(letter) > 1:
    print('Please enter only one letter at a time.')
  else:
    letters.append(letter)
    letter_amount += 1
    
dictionary = load_dictionary()
permutations_list = permute_letters(letters, dictionary)


for list in permutations_list:
  print(list)
  
    
    
