import random

with open("text.txt") as myFile:
    message=myFile.read()
    print("В файле написано- ", message)
    key = input("Введите ключ (Enter - ключ сгенерируется автоматически):")

    if not key:
        key = "".join(
            random.choice(
                "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            )
            for i in range(random.randint(1, len(message)))
        )
        print(f"Вы не ввели ключ, поэтому мы его придумали сами:\n{key}")

    result = bytearray()
    if type(message) == str:
        message = bytearray(message, "utf-8")
    key = bytearray(key, "utf-8")

    for i in range(len(message)):
        result.append(message[i] ^ key[i % len(key)])

with open('text.txt','wb') as FileMy:
    FileMy.write(result)