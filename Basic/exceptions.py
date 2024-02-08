#x = 10 / 0


#try:
  #  x = 10 / 0
#except:
  #  print("Well that didn't work!")


try:
    answer = input("What should i divide 10 dy?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:
    print("This code always runs")