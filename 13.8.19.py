total=0
count=0
list_age=[]
try:
    tickets = int(input('Input the desired number of tickets: '))
    if int(tickets) <= 0 or int(tickets)>100:
        raise ValueError("You entered the wrong amount tickets")
    else:
        try:
            while count < tickets:
                count+=1
                print (f"Input the age of {count} visitor!")
                age = int(input("Input the age: "))
                if age > 100 or age <= 0:
                    raise ValueError("You entered the wrong age")
                if age < 18:
                    print("Enter is free")
                elif 18<=age<25:
                    print("Cost 990 RUB for ticket")
                else:
                    print("Cost 1390 RUB for ticket")
                list_age.append(age)

            for i in list_age: 
                if int(i) < 18:
                    total+=0
                elif 18<=int(i)<25:
                    total+=990
                else:
                    total+=1390
                
            if tickets > 3:
                print(f'---\nTo pay: {total*0.9} RUB\nYou discount 10%')
            else:
                print(f'---\nTo pay: {total} RUB')
        except ValueError as error:
            print(error)
            print("End of Programm!")
        else:
            print(f"You reserved {tickets} tickets")
            print(f"Congratulation reservation was successful!")
except ValueError as error:
    print(error)
    print("End of Programm!")
    
   
