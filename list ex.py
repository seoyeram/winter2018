def add():
      num = int(input("num:"))
      num2 = int(input("num2:"))
      print(num + num2)
def sub():
      num = int(input("num:"))
      num = int(input("num:"))
      print(num - num2)
def multiply():
      num = int(input("num:"))
      num2 = int(input("num2:"))
      print(num * num2)
def divide():
      num = int(input("num:"))
      num2 = int(input("num2:"))
      if num ==0 or num2 ==0:
            print("Error")
            return
      print(num / num2)
def mock():
      num = int(input("num:"))
      num2 = int(input("num2:"))
      if num ==0 or num2 ==0:
            print("Error")
            return
      result = num // num2
      print(result)
def nameoji():
      num = int(input("num:"))
      num2 = int(input("num2:"))
      if num ==0 or num2 ==0:
            print("Error")
            return
      print(num % num2)

while True:
      print("Menu")
      print("=====================================")
      print("1:add")
      print("2:sub")
      print("3:multiply")
      print("4:divide")
      print("5:mock")
      print("6:nameoji")
      sel = int(input(":"))

      if(sel ==1):
            add()
      elif(sel==2):
            sub()
      elif(sel==3):
            multiply()
      elif(sel==4):
            divide()
      elif(sel==5):
            mock()
      elif(sel==6):
            nameoji()
      elif(sel==7):
            break
      else:
            print("Wrong input, please input again")
