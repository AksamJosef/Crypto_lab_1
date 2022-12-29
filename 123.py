path_to_file = input ("Введите путь к файлу, который хотите зашифровать: \n")
with open(path_to_file, 'rb') as SFile: # открываем файл для чтения побайтово
    FileContain = bytearray(SFile.read()) # создаем байтовый массив
print (FileContain)
