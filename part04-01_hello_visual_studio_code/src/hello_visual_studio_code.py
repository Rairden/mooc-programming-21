while True:
    editor = input("Editor: ")
    str = editor.lower()
    if str == "word":
        print("awful")
    elif str == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
