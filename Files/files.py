def main():

  #  myflie = open("textfile.txt", "w+")

  #  myflie = open("textfile.txt", "a+")

  #  for i in range(10):
  #      myflie.write("นี้คือข้อความบางส่วนใหม่\n")

  #  myflie.close()
    myflie = open("textfile.txt", "r")
    if myflie.mode == 'r':
        #contents = myflie.read()
        #print(contents)
        fl = myflie.readlines()
        for x in fl:
            print(x)

if __name__ == "__main__":
    main()