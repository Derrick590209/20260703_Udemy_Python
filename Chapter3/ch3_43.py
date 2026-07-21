# Structural Pattern Matching 可以上網查
# switch statement ==

# lang = input("你希望學甚麼程式語言?")

# if lang == "JavaScript":
#     print("你會成為網頁前端開發人員")
# elif lang == "PHP":
#     print("你會成為網頁後端開發人員")
# elif lang == "Python":
#     print("你會成為資料科學家")
# elif lang == "Kotlin":
#     print("你會成為Android應用程式開發人員")
# elif lang == "Swift":
#     print("你會成為IOS應用程式開發人員")
# else:
#     print("你會成為其他程式開發人員")


# lang = input("你希望學甚麼程式語言?")
# match lang:
#     case "JavaScript":
#         print("你會成為網頁前端開發人員")
#     case "PHP":
#         print("你會成為網頁後端開發人員")
#     case "Python":
#         print("你會成為資料科學家")
#     case "Kotlin":
#         print("你會成為Android應用程式開發人員")
#     case "Swift":
#         print("你會成為IOS應用程式開發人員")
#     case _:
#         print("你會成為其他程式開發人員")


# day = input("今天星期幾?")
# match day:
#     case "星期日" | "星期一" : # vertical bar == or的語法
#         print("今日公休")
#     case "星期六": 
#         print("今日營業半天")
#     case _:
#         print("今日正常營業")


#  # matching 也支援其他資料型態
# command = input("Where do you wanna go?") # I wanna go home
# print(command.split(" ")) # ['I', 'wanna', 'go', 'home']


command = input("Where do you wanna go?")
match command.split(" "):
    case ["Go", "home"]:
        print("You wanna go home")
    case _:
        print("The system cannot determine where you wanna go?")
