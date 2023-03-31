# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

vowel_letters = "а, е, ё, и, о, у, ы, э, ю, я".split(", ")

poem = input("Введите стих Винни-Пуха: ").split()

syllables = []
for word in poem:
    count = 0
    for i in word:
        if i in vowel_letters:
            count += 1
    syllables.append(count)

print("Парам пам-пам" if len(set(syllables)) == 1 else "Пам парам")
