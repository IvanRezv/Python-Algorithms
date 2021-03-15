simv=input("Какой символ посчитать? ")
sentence = input("Вводи строку, щас посчитаем -")
vas=sum(map(lambda x : 1 if simv in x else 0, sentence))
print("Всего символ - ",simv,"Встретился",vas," Раз")