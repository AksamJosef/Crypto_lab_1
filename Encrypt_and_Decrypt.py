
# Вариант 22.

# Функция шифровки и записи в файл
def Encrypt (A, B, M): # для алгоритма шифровки будем использовать входные параметры a, b, m из варианта
    try:
        path_to_file = input ("Введите путь к файлу, который хотите зашифровать: \n")
        with open(path_to_file, 'rb') as SFile: # открываем файл для чтения побайтово
            FileContain = bytearray(SFile.read()) # создаем байтовый массив
            for i, byte in enumerate(FileContain):
                FileContain[i] = (A * byte + B) % M # шифровка по алгоритму. для каждого i-го элемента
                                                    # меняем его байтовое значение

        # открываем файл заново, иначе зашифрованное содержимое записывается в конец файла, а не вместо
        # исходного содержимого
        with open(path_to_file, "wb") as OFile:
            OFile.write (FileContain)
            print("Программа завершена успешно, файл зашифрован,"
                  " попробуйте его открыть и убедитесь, что он теперь битый :)")
    except FileNotFoundError: # на всякий случай обрабатываем исключение в случае, если файл не найден
                              # или прописан неверный путь к файлу
        print("Файл не найден, запустите заново программу и введите корректно")

# Функция дешифровки и запись в файл, устроена похожим образом как и функция шифровки,
# но алгоритм дешифровки уже обратный
def Decrypt (invA, B, M):
    try:
        path_to_file = input("Введите путь к файлу, который хотите зашифровать: \n")
        with open(path_to_file, 'rb') as SFile:
            FileContain = bytearray(SFile.read())
            for i, byte in enumerate(FileContain):
                FileContain[i] = (invA * (byte - B)) % M

        with open(path_to_file, 'wb') as OFile:
            OFile.write(FileContain)
            print("Файл расшифрован. Попробуйте его открыть, и он откроется :)")
    except FileNotFoundError:
        print("Файл не найден, запустите заново программу и введите корректно")


# вывел в отдельную функцию поиск a ^ (-1)
def inv (A, M):
    for i in range(M):
        if (A * i) % M == 1:
            return i

### CONST
M = 256
A = 47
B = 61
###

Selected = input("Введите 1 или 2, чтобы выбрать функцию программы:\n"
                 "1: Шифровка\n"
                 "2: Дешифровка\n")
if Selected == '1':
    Encrypt(A, B, M)

elif Selected == '2':
    invA = inv(A, M)
    Decrypt(invA, B, M)

else:
    print("Вы ввели неправильный параметр. Запустите программу еще раз и введите правильно!\n")