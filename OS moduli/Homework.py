# • Papkadagi barcha fayllarni for oqarali os.remove() dan foydalanib o’chiring
          # • Hozirgi yil oy kun dan  foydalanib  Bir nechta katalog yarating
          # • shutil.copytree() foydalanib  Bir nechta kataloglardan nusxa oling





# file = open("matn1.txt", "w")
#
# file.write("Hello, world")
#
# file.close()


# • Papkadagi barcha fayllarni for oqarali os.remove() dan foydalanib o’chiring

# import os
#
# files = ["matn1.txt"]
#
# for x in files:
#     os.remove(x)



# • Hozirgi yil oy kun dan  foydalanib  Bir nechta katalog yarating

# import os
#
# os.makedirs("2024/02/02")





# • shutil.copytree() foydalanib  Bir nechta kataloglardan nusxa oling

import shutil

shutil.copytree("Homework.py", "lesson.py")





import shutil

src = "/Desktop/PycharmProjects/OS_less/sana.txt"
dst = "/Desktop/PycharmProjects/OS_less/sana.txt"

shutil.copy(src, dst)
print("File copied successfully.")
