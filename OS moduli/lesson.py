# import os
#
#
# file = os.listdir()
#
# print(file)


# import os
# with os.scandir(os.getcwd()) as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)





# import os
#
#
# file = os.listdir()

#
# with os.scandir(os.getcwd()) as dir_contents:
#     for entry in dir_contents:
#         for i in file:
#             info = entry.stat()
#             print()
#             print(f"{i} --> {info.st_mtime}")
#             print()





# import os
#
#
# file = os.listdir()
#
# count = 0
# with os.scandir(os.getcwd()) as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#
#         print(f"{file[count]} --> {info.st_size}")
#         count += 1





#papka yaratish

# from pathlib import Path
#
# file = Path("NewFile") #create file
#
# file.mkdir()





#papka ichida papka yaratish
# import os
#
# os.makedirs("2024/02/01")



# import os
#
# print(os.getcwd())
# file = os.getcwd() + "/lesson4.py"
# os.remove(file)