try: 
    file = open("./Assignments/A4/Task1/sample.txt", "r")
    print("Line 1:",file.readline())
    print("Line 2:",file.readline())
    file.close()
except FileNotFoundError:
    print("The File 'sample.txt' was not found")
