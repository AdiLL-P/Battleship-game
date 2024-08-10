import random
class battleship:
    def __init__(self,ship_coloumn,ships_row):
        self.ship = ship_coloumn
        self.ship_row = ships_row

    def input_user(self):
       a = (0,0,0,0,0)
       b = (0,0,0,0,0)
       c = (0,0,0,0,0)
       d = (0,0,0,0,0)
       e = (0,0,0,0,0)
       response = ""
       print(f"""This is the grid please use your move within this :
       ---------------------------      
       |   | 1 | 2 | 3 | 4 | 5 |   | 
       ---------------------------
       | A | {a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | A |
       ---------------------------
       | B | {b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]} | B |
       ---------------------------
       | C | {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | C |
       ---------------------------
       | D | {d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]} | D |
       ---------------------------
       | E | {e[0]} | {e[1]} | {e[2]} | {e[3]} | {e[4]} | E |
       ---------------------------
       |   | 1 | 2 | 3 | 4 | 5 |   | 
       ---------------------------
       """)
       print("""
rows are a,b,c,d,e
coloumns 1,2,3,4,5""")
       print("you will get 10 tries")
      
       ship = self.ship
       ship_row = self.ship_row 
       
       flag = True
       lives = 11
       while flag:
        if lives == 0:
            print(f"""alas!!! ship was at 
row : {ship_row}  
coloumn : {ship}""")
            break
        while lives > 0:
            try:
                input1 = input("enter the row : ")
                input2 = int(input("enter coloumn : "))
                if input1 == "a" or input1 == "A":
                    for i in range(1,6):
                        if i == input2:
                            a = list(a)
                            a[i-1] = 1
                            if i == ship :
                                if ship_row == "a" or ship_row == "A" :
                                    response =("Congratulations !! that was the position of ship")
                                    lives = 0
                                    flag = False
                                    break
                            else:
                                    lives = lives-1
                                    response =f"Ship Not here mate!! \nremaining tries : {lives}"

                    a = tuple(a)
                elif input1 == "b" or input1 == "B":
                    for i in range(1,6):
                        if i == input2:
                            b = list(b)
                            b[i-1] = 1
                            if i == ship :
                                if ship_row == "b" or ship_row == "B" :
                                    response =("Congratulations !! that was the position of ship")
                                    lives = 0
                                    flag = False
                                    break
                            else:
                                    lives = lives-1
                                    response =f"Ship Not here mate!! \nremaining tries : {lives}"

                    b = tuple(b)
                elif input1 == "c" or input1 == "C":
                    for i in range(1,6):
                        if i == input2:
                            c = list(c)
                            c[i-1] = 1
                            if i == ship :
                                if ship_row == "c" or ship_row == "C" :
                                    response =("Congratulations !! that was the position of ship")
                                    lives = 0
                                    flag = False
                                    break
                            else:
                                    lives = lives-1
                                    response =f"Ship Not here mate!! \nremaining tries : {lives}"
                    c = tuple(c)
                elif input1 == "d" or input1 == "D":
                    for i in range(1,6):
                        if i == input2:
                            d = list(d)
                            d[i-1] = 1
                            if i == ship :
                                if ship_row == "d" or ship_row == "D" :
                                    response =("Congratulations !! that was the position of ship")
                                    lives = 0
                                    flag = False
                                    break
                            else:
                                    lives = lives-1
                                    response =f"Ship Not here mate!! \nremaining tries : {lives}"
                    d = tuple(d)
                elif input1 == "e" or input1 == "E":
                    for i in range(1,6):
                        if i == input2:
                            e = list(e)
                            e[i-1] = 1
                            if i == ship :
                                if ship_row == "e" or ship_row == "e" :
                                    response =("Congratulations !! that was the position of ship")
                                    lives = 0
                                    flag = False
                                    break
                            else:
                                    lives = lives-1
                                    response =f"Ship Not here mate!! \nremaining tries : {lives}"
                    e = tuple(e)
                print(f"""
        ---------------------------      
        |   | 1 | 2 | 3 | 4 | 5 |   | 
        ---------------------------
        | A | {a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | A |
        ---------------------------
        | B | {b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]} | B |
        ---------------------------
        | C | {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | C |
        ---------------------------
        | D | {d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]} | D |
        ---------------------------
        | E | {e[0]} | {e[1]} | {e[2]} | {e[3]} | {e[4]} | E |
        ---------------------------
        |   | 1 | 2 | 3 | 4 | 5 |   | 
        ---------------------------
        """)
                print(response)
            except ValueError:
                print("Wrong input try")


ship = random.randint(1,5)
ship_row =random.choice(("a","b","c","d","e"))
a = battleship(ship,ship_row)
a.input_user()