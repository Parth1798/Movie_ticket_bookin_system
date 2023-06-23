#!/usr/bin/env python
# coding: utf-8



import psycopg2
import psycopg2.extras
import pandas as pd
import pandas.io.sql as sqlio
from IPython.display import display


conn = psycopg2.connect(database ="movie_db",user = "postgres",password = "1234",
                       host ="localhost", port = "5432")
w = conn.cursor(cursor_factory= psycopg2.extras.DictCursor) 

x = 10
z = 1
y = 1
a = 1
e = 1
seat_1_to_5=90
seat_5_to_7=150
seat_7_to=180
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
Row = 10
Seats = 10
Total_seat = Row*Seats
#ticket_no = 0
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]











movie='''CREATE TABLE IF NOT EXISTS movies ( movie_id int NOT NULL primary key, movie_name varchar(40) unique, length int DEFAULT NULL, language varchar DEFAULT NULL, show_start date DEFAULT NULL, show_end date DEFAULT NULL ) '''
movies = w.execute(movie)
conn.commit()

q1='''INSERT INTO movies (movie_id, movie_name,length, language, show_start,show_end) VALUES (1, 'Bhediya', 125, 'Hindi', '2022-11-25', '2022-01-31'), (2, 'ઓમ મંગલમ સિંગલમ', 112, 'gujarati', '2022-11-18', '2022-01-31'), (3, 'Avatar 2', 176, 'English', '2022-12-16', '2022-02-28') '''
w.execute(q1)
conn.commit()

screen='''CREATE TABLE if not exists screen (
 screen_id int NOT NULL primary key,
 screen_no int
)'''
screen=w.execute(screen)
conn.commit()

bookedticket = '''CREATE TABLE IF NOT EXISTS public.booked_tickets (
  Ticket_no serial primary key,
  Seat_no int,
  movie_name varchar references movies(movie_name),
  screen_id int references screen(screen_id),
  Name varchar,
  Gender varchar(10),
  Age int,
  Phone_no bigint,
  seat_type varchar,
  Ticket_price int
)'''
booked_ticket=w.execute(bookedticket)
conn.commit()


# In[6]:


q3='''INSERT INTO screen (screen_id) VALUES
(1),
(2),
(3)'''

#w.execute(q3)
#conn.commit()


# In[7]:


sign_up='''CREATE TABLE if not exists signup (
        name varchar NOT NULL,
        phone_no bigint primary key,
        city varchar default null,
        state varchar default null,
        em varchar DEFAULT NULL,
        passw varchar not null)'''
signup=w.execute(sign_up)
conn.commit()

        





print("\n******************  WELCOME TO DAIICT CINEMAS  *********************")

def signin_user():
    o='select * from signup'
    w.execute(o)
    r=w.fetchall()
    list1=[]
    list2=[]
    e = 'select count(*) from booked_tickets'
    w.execute(e)
    conn.commit()
    a = w.fetchall()
    Booked_seat=int(a[0][0])
    v = 'select sum(Ticket_price) from booked_tickets'
    w.execute(v)
    conn.commit()
    n = w.fetchall()
    ku=n[0][0]
    print(type(ku))
    
    
    for h in r:
        list1.append(h[1])
        list2.append(h[5])
    
    while True:
        ck = int(input('enter id or phone no -'))
        passw = input('enter password - ')
        
        if ck in list1 and passw in list2:
            ll = 'select name from signup where phone_no={}'.format(ck)
            w.execute(ll)
            conn.commit()
            kl = w.fetchall()
            print("-------WELCOME {}-------".format(kl[0][0]))
            break
        
        else:
            print('invalid id or password')


class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat/Total_seat)*100
        return percentage

class_call = chart
table_of_chart = class_call.chart_maker()



while True:
    print('\n1. SIGN UP''\n2. SIGN IN\n3. About US')
    acc=int(input('Select Option - '))

    if acc == 1:
        name = str(input("\nENTER YOUR FULL NAME:-"))
        pn = int(input("\nENTER YOUR PHONE NO:-"))
        city = input("\nENTER YOUR CITY NAME:-")
        state = input("\nENTER YOUR STATE:-")
        em = input("\nENTER YOUR EMAIL ID:-")
        passw = input("\nENTER YOUR PASSWORD:-")
        q5 = "insert into signup values('{}',{},'{}','{}','{}','{}') ".format(name,pn,city,state,em,passw) 
        w.execute(q5)
        conn.commit()

    if acc == 2:
        print('\n\nLOG IN AS \n 1. Admin \n 2. user')
        z = int(input('\nSelect Option - '))
        if z < 2 :
            while True:
                admin_id = input('\nEnter Admin Id - ')  # parth,#ganesh
                password = int(input('Enter Password - '))  # 1234
            
                if admin_id == 'parth'or'ganesh' or password == '1234':
                    print('\n\n \tWelcome {}'.format(admin_id))
                    break
        
                else:
                    print('\ninvalid Adminid or Password')
                
            print('\n1. Change Number of Seats(Layout)''\n2. Statistics', '\n3. Show Booked Tickets User Info','\n4. Show Total Booked Tickets In Tabular Form','\n0. Log Out' )
            y = int(input('\nSelect Option - '))
            while y != 0:
                if y == 1:
                    Row = int(input('\nEnter number of Row - \n'))
                    Seats = int(input('Enter number of seats in a Row - \n'))
                    Total_seat = Row * Seats
                    Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]
                    print('\nSeat Layout Changed Successfully''\n\nNow ToTal Number Of sear is %d' %Total_seat)
                    class chart:
                        @staticmethod
                        def chart_maker():
                            seats_chart = {}
                            for i in range(Row):
                                seats_in_row = {}
                                for j in range(Seats):
                                    seats_in_row[str(j + 1)] = 'S'
                                seats_chart[str(i)] = seats_in_row
                            return seats_chart
                        @staticmethod
                        def find_percentage():
                            percentage = (Booked_seat / Total_seat) * 100
                            return percentage

                    class_call = chart
                    table_of_chart = class_call.chart_maker()

                    print('\n1. Change Number of Seats(layout)''\n2. Statistics''\n3. Show booked Tickets User Info''\n4. show total booked tickets in tabular form''\n0. Log Out')
                    y = int(input('\nSelect Option - '))

                elif y == 2:
                    print('\nNumber of purchased Ticket - ', Booked_seat)
                    print('Percentage - ', class_call.find_percentage())
                    print('Current  Income - ', 'Rs', prize_of_ticket)
                    print('Total Income - ', 'Rs', Total_Income)
                    print()
                    print('\n1. Change Number of Seats(layout)''\n2. Statistics''\n3. Show booked Tickets User Info''\n4. show total booked tickets in tabular form''\n0. Log Out')
                    y = int(input('\nSelect Option - '))

                elif y == 3:
                    Enter_row = int(input('\nEnter Row number - \n'))
                    Enter_column = int(input('Enter Column number - \n'))
                    if Enter_row in range(1, Row + 1) and Enter_column in range(1, Seats + 1):
                        if table_of_chart[str(Enter_row - 1)][str(Enter_column)] == 'B':
                            person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                            print('\nName - ', name)
                            print('Gender - ', gender)
                            print('Age - ', age)
                            print('Phone number - ', phone_no)
                            print('Ticket Prize - ', 'Rs', ticket_price)
                            print('\n1. Change Number of Seats(layout)''\n2. Statistics''\n3. Show booked Tickets User Info''\n4. show total booked tickets in tabular form''\n0. Log Out')
                            y = int(input('\nSelect Option - '))
                        else:
                            print()
                            print('\n \t---**---  Vacant seat  ---**---')
                            print('\n1. Change Number of Seats(layout)''\n2. Statistics''\n3. Show booked Tickets User Info''\n4. show total booked tickets in tabular form''\n0. Log Out')
                            y = int(input('\nSelect Option - '))
                    else:
                        print()
                        print('\n \t***  Invalid Input  ***')
                    print()
                    print('\n1. Change Number of Seats(layout)''\n2. Statistics''\n3. Show booked Tickets User Info''\n4. show total booked tickets in tabular form''\n0. Log Out')
                    y = int(input('\nSelect Option - '))
                elif y == 4:
                    e = 'select * from booked_tickets'
                    w.execute(e)
                    conn.commit()
                    a = w.fetchall()
                    fn= pd.read_sql_query('select * from booked_tickets',conn)
                    display(fn)
                elif y == 0:
                    break


                else:
                    print()
                    print('\n \t***  Invalid Input  ***')
                print()
                print('\n1. Change Number of Seats(layout)''\n2. Statistics''\n3. Show booked Tickets User Info''\n4. show total booked tickets in tabular form''\n0. Log Out')
                y = int(input('\nSelect Option - '))
        
        if z == 2:
            signin_user()
            while True:
                print('1. Show seats layout \n2. Buy a Ticket \n3. Ticket Cancellation \n0 Exit')
                x = int(input('Select Option - '))
                if x == 1:
                    if Seats < 10:
                        for seat in range(Seats):
                            print(seat, end='  ')
                        print(Seats)
                    else:
                        for seat in range(10):
                            print(seat, end='  ')
                        for seat in range(10, Seats):
                            print(seat, end=' ')
                        print(Seats)
                    if Seats < 10:
                        for num in table_of_chart.keys():
                            print(int(num) + 1, end='  ')
                            for no in table_of_chart[num].values():
                                print(no, end='  ')
                            print()
                    else:
                        count_num = 0
                        for num in table_of_chart.keys():
                            if int(list(table_of_chart.keys())[count_num]) < 9:
                                print(int(num) + 1, end='  ')
                            else:
                                print(int(num) + 1, end=' ')
                            count_key = 0
                            for no in table_of_chart[num].values():
                                if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                                    print(no, end='  ')
                                else:
                                    print(no, end='  ')
                                count_key += 1
                            count_num += 1
                            print()
                    print('Vacant Seats = ', Total_seat - Booked_seat)
                    print()

                elif x == 2:
                    m = 'select * from movies'
                    w.execute(m)
                    conn.commit()

                    m = w.fetchall()
                    fn = pd.read_sql_query('select * from movies', conn)
                    display(fn)
                    l = int(input('select movie id -'))
                    print('select the row number from 1 to ', Row)
                    Row_number = int(input('Enter Row Number - '))
                    while x == 2:
                        if Row_number < Row:
                            break
                        else:
                            print('please enter valid input')
                        Row_number = int(input('Enter Row Number - '))
                    print('select the column number from 1 to %d' % Seats)
                    Column_number = int(input('Enter Column Number - '))
                    if Column_number < Seats:
                        print('enter value between range from 1 to %d' % Seats)
                    else:
                        print('please enter valid input')
                        print('select the column number from 1 to %d' % Seats)
                    if l == 1:
                        movie_name = 'Bhediya'
                        screen_id = 1

                    elif l == 2:
                        movie_name = 'ઓમ મંગલમ સિંગલમ'
                        screen_id = 2

                    elif l == 3:
                        movie_name = 'Avatar 2'
                        screen_id = 3

                    if Row_number in range(1, Row + 1) and Column_number in range(1, Seats + 1):
                        if table_of_chart[str(Row_number - 1)][str(Column_number)] == 'S':
                            if Row_number < 4:
                                prize_of_ticket = 90
                                seat_type = 'Silver'
                            elif Row_number >= 4 and Row_number <= 7:
                                prize_of_ticket = 120
                                seat_type = 'Gold'
                            else:
                                prize_of_ticket = 150
                                seat_type = 'platinum'

                            print('prize_of_ticket - ', 'Rs', prize_of_ticket)
                            conform = input('yes for booking and no for Stop booking - ')
                            person_detail = {}
                            if conform == 'yes' or 'y' or 'Y' or "YES":
                                name = input('Enter Name -')
                                gender = input('enter gender -')
                                age = int(input('enter age -'))
                                phone_no = int(input('enter phone no -'))
                                ticket_price = prize_of_ticket
                                table_of_chart[str(Row_number - 1)][str(Column_number)] = 'B'
                                Booked_seat += 1
                                Total_Income += prize_of_ticket
                                seatno = Row_number * Column_number
                                ticket_no = ticket_no+1

                                q6 = "insert into booked_tickets values({},'{}',{},'{}','{}',{},{},'{}') ".format(
                                                                                                             seatno,
                                                                                                             movie_name,
                                                                                                             screen_id,
                                                                                                             name,
                                                                                                             gender,
                                                                                                             age,
                                                                                                             phone_no,
                                                                                                             seat_type)
                                w.execute(q6)
                                conn.commit()
                                jk = 'select ticket_no from booked_tickets where phone_no={}'.format(phone_no)
                                w.execute(jk)
                                conn.commit()
                                jl = w.fetchall()
                                ticket_no=jl[0][0]


                            else:
                                continue
                            Booked_ticket_Person[Row_number - 1][Column_number - 1] = person_detail
                            print('Booking Successful Your Ticket Number Is {}'.format(ticket_no))
                        else:
                            print('This seat already booked by some one')
                    else:
                        print()
                        print('***  Invalid Input  ***')
                    print()
                elif x == 3:
                    tic=int(input('Enter Ticket Number -'))
                    q7='delete from booked_tickets where ticket_no={}'.format(tic)
                    w.execute(q7)
                    conn.commit()
                    print('Ticket Number {} Has Been Cancelled'.format(tic))
                elif x == 0:
                    break

    if acc==3:
        DAIICT_Cinema = open(r"C:\Users\parth\OneDrive\Desktop\DAIICT_Cinema.txt", "rt")
        fv = []
        for vv in DAIICT_Cinema.readlines():
            fv.append(vv.rstrip())
        for l in range(0,9):
            print(fv[l])
        DAIICT_Cinema.close()
if Enter_row in range(1, Row + 1) and Enter_column in range(1, Seats + 1):
    if table_of_chart[str(Enter_row - 1)][str(Enter_column)] == 'B':
        person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]