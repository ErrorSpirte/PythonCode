import random, time

def generate_password():
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    length = int(input("Введите длину случайного пароля: "))
    time.sleep(1)
    print("\nСлучайно созданный пароль:")
    time.sleep(1.5)
    
    for i in range(length):
        password += random.choice(characters)
    
    print(password)
    print(" ")

def display_instructions():
    print("Привет! Это мем-словарь. Если вы встретили новое непонятное слово,")
    time.sleep(1.5)
    print("введите его (большими буквами!), и я расскажу вам, что оно означает.")
    time.sleep(1.5)
    print("Чтобы выйти, введите 'Выход'.")
    time.sleep(1)
    print(" ")

def meme_dictionary():
    meme_dict = {
        "КРИНЖ": "Что-то очень странное или стыдное",
        "РОФЛ": "шутка",
        "ЩИЩ": "одобрение или восторг",
        "КРИПОВЫЙ": "страшный, пугающий",
        "АГРИТЬСЯ": "злиться",
        "ТОПЧИК": "что-то очень крутое или лучшее",
        "ШОК": "сильное удивление или изумление",
        "КЕК": "аналог 'лол', выражение смеха",
        "ХЕЙТ": "негативное отношение, враждебность",
        "ГЕЙМЕР": "человек, увлекающийся видеоиграми",
        "МЕМ": "вирусное изображение или шутка, часто используемая в интернете",
        "ИМБА": "чрезмерно сильный или мощный",
        "ДЕБАГ": "исправление ошибок в программировании",
        "ФРИК": "эксцентричный или странный человек",
        "ДЕДЛАЙН": "срок сдачи работы или проекта",
        "ПРОГА": "программа или приложение",
        "БАГ": "ошибка в программе или системе",
        "ЛОЛ": "Что-то очень смешное"
    }
    
    display_instructions()
    while True:
        word = input("Введите непонятное слово (большими буквами!): ")
        if word.lower() == "выход":
            print("До свидания! До новых встреч!")
            break
        elif word in meme_dict:
            print(meme_dict[word])
            time.sleep(1)
            print(" ")
        else:
            print("Извините, но такого слова нет")
            time.sleep(1)
            print(" ")

def main():
    while True:
        print("Выберите действие:")
        time.sleep(0.5)
        print("1. Генератор случайных паролей")
        time.sleep(0.5)
        print("2. Мем-словарь")
        time.sleep(0.5)
        print("3. Выход")
        time.sleep(0.5)
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            generate_password()
        elif choice == "2":
            meme_dictionary()
        elif choice == "3":
            print("До свидания! До новых встреч!")
            break
        else:
            print("Неправильный выбор, попробуйте снова.")
            time.sleep(1)
            print(" ")

main()
