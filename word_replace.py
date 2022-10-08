#Короткий код для замены слов в фразе
#При запуске функция просит ввести слово, которое нужно поменять
#Потом просит слово, на которое поменять
#Функция возвращает измененную фразу
def replace_word():
  # Объявление всех необходимых переменных
  default_phrase = "Hello world, i'm Ilya" 
  is_word = False
  word_to_replace = ''
  word_replacement = ''

  print(f"Default phrase: {default_phrase}")
  # Запрос слова, которое нужно заменить
  word_to_replace = input("Enter the word to replace: ")
  # Проверка на ввод этого слова
  while len(word_to_replace) == 0:
    print("Need choose the word")
    word_to_replace = input("Enter the word to replace: ")

  # Запрос слова, на которое нужно поменять
  word_replacement = input("Enter the word replacement: ")
  # Проверка на ввод этого слова
  while len(word_replacement) == 0:
    print("Need choose the word")
    word_replacement = input("Enter the word replacement: ")

  default_phrase_list = default_phrase.replace(',', '').split()
  # Проверка на совпадение
  for word in default_phrase_list:
    if word_to_replace == word:
      word_to_replace = word
      is_word = True
    else:
      pass
  # Проверка на наличие совпадений   
  if is_word == False:
    print("There is no match")
  else: 
    replace_phrase = print(default_phrase.replace(word_to_replace, word_replacement))
    return replace_phrase
#Запуск функции
replace_word()