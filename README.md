# Word_replace
****
Простая функция для замены одного слова в фразе на другое.

### Сначала происходит объявление переменных.
```
  default_phrase = "Hello world, i'm Ilya" - Фраза, которую будем менять
  is_word = True - Флаг несовпадения
  word_to_replace = '' - Слово, которое собираемся менять
  word_replacement = '' - Слово, на которое собираемся менять
```
### Работа функции.
*****
Сначала функция запросит слово, которое хотите поменять и запишет ее в переменную **word_to_replace**.

За это отвечает данный участок кода:
```
word_to_replace = input("Enter the word to replace: ")
```

Фунция произведет нужные проверки на наличе введенного слова в input. 
**Важно!!** - слово должно четко совпадать со словом в изначальной фразе.

Если слово не было введено, то последует предупреждение о необходимости ввода.
За это отвечает данный участок кода:
```
  while len(word_to_replace) == 0:
    print("Need choose the word")
    word_to_replace = input("Enter the word to replace: ")
```

Далее функция запросит слово, на которое хотите поменять и запишет ее в переменную **word_replacement**

За это отвечает данный участок кода:
```
word_replacement = input("Enter the word replacement: ")
```
Фунция произведет нужные проверки на наличе введенного слова в input. 

Если слово не было введено, то последует предупреждение о необходимости ввода.
За это отвечает данный участок кода:
```
  while len(word_replacement) == 0:
    print("Need choose the word")
    word_replacement = input("Enter the word replacement: ")
```
Функция, получив две необходимые переменные проверит изначальную фразу на совпадение слова, которое мы хотим заменить.
За это отвечает данный участок кода:
```
default_phrase_list = default_phrase.replace(',', '').split()

  for word in default_phrase_list:
    if word_to_replace == word:
      word_to_replace = word
      is_word = False
    else:
      pass
```
### Вывод фунции
*****
В итоге функция на основе, в каком положении стоит флаг **is_word** вернет результат.

- В случае если слово не совпало вернется фраза, что нет совпадений.
- Если совпадение было, то измененная фраза успешно выведется.

За это отвечает данный участок кода
```
  if is_word == True:
    print("There is no match")
  else: 
    replace_phrase = print(default_phrase.replace(word_to_replace, word_replacement))
    return replace_phrase
```
