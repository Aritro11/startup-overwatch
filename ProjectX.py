import mysql.connector as sqltor


print('Welcome...\n')
print("This program accesses a table stored in a database containing information about some top Indian startups \
      and enables a user to perform various sql queries to it.\n")
print('Database name: Project')
print('Table name   : Startups \n\n')


#establishing connection to the required mysql database
mycon = sqltor.Connect(host = 'localhost', user = 'root', passwd = 'write_your_own_pass_here', database = 'your_database_name')
cursor = mycon.cursor()
if mycon.is_connected():
    print('Connection Successful!!')
else:
    print('Connecion Unsuccessful!!')


# storing name of all coloumns in table startups in a tuple for later use in displaying output
coloumn_names = ('Startups','Founder','YearFounded','Industry','Valuation(million $)','Headquaters')
    
print('\n\nDisplaying various funtions that you can perform:')
while True:
    
    print('')
    print('-'*30)
    print('1. View table records')
    print('2. Modify table data')
    print('3. Add new record/row')
    print('4. Search/compare records')
    print('5. Exit')
    print('-'*30)
    print('')
    
    ask = int(input('Enter your choice (1/2/3...): '))
    
    if ask == 1:
        cursor.execute('select * from startups')
        record1 = cursor.fetchall()
        print('\nTable records:\n')
        print(coloumn_names)
        for row in record1:
            print(row)
        
        
    elif ask == 2:
        clm_name = input('Enter coloumn name where modification has to be made: ')
        old_value = input('Enter exixting value: ')
        new_value = input('Enter new value: ')
        
        # Writing update query using f-strings whcih allow variables to be used in a string
        query1 = f"UPDATE startups SET {clm_name} = '{new_value}' WHERE {clm_name} = '{old_value}'"
        cursor.execute(query1)
        mycon.commit()
        print('Modification done!!')
        
        
    elif ask == 3:
        # asking user for data of each coloumn of the new row to be added
        stp = input('Enter startup name: ')
        fdr = input('Enter founder name: ')
        yrf = int(input('Enter founding year: '))
        ind = input('Enter industry: ')
        val = int(input('Enter valuation (in million $): '))
        hdqtr = input('Enter headquarters: ')
        
        # inserting new row to the table 
        newrow = "insert into startups(startups,founder,yearfounded,industry,valuation_$,headquarter) \
              values('{}','{}',{},'{}',{},'{}')".format(stp,fdr,yrf,ind,val,hdqtr)
        cursor.execute(newrow)
        mycon.commit()                   # commit to make changes permanent
        print('New record added!!')
          
    
    elif ask == 4:
        # giving user the option to search, view and compare records by different data points
        print('Choose one option amongst the following choices:')
        print('A. Search by startup name')
        print('B. Search by founder')
        print('C. Search by industry')
        print('D. View by year of founding')
        print('E. View by industry')
        print('F. View by highest to lowest valued startups')
        print('G. View total valuation of all startups listed here')
        print('H. View startups having 1 bn $ or more in valuation')
        print('I. View by oldest to newest startup')
        print('J. View by headquater location\n')
        
        # asking user to choose any of desired option
        ask2 = input('Enter your choice (A/B/C....): ')
        ask2 = ask2.lower()
        print('')
        if ask2 == 'a':
            n = input('Enter startup name: ')
            cursor.execute(f"Select * from startups where startups = '{n}'")
        elif ask2 == 'b':
            f = input('Enter founder name: ')
            cursor.execute(f"select * from startups where founder = '{f}'")
        elif ask2 == 'c':
            i = input('Enter industry name: ')
            cursor.execute(f"select * from startups where industry = '{i}'")
        elif ask2 == 'd':
            cursor.execute('select * from startups order by yearfounded')
        elif ask2 == 'e':
            cursor.execute('select * from startups order by industry')
        elif ask2 == 'f':
            cursor.execute('select * from startups order by valuaton_$ desc')
        elif ask2 == 'g':
            cursor.execute('select sum(valuation_$) from startups')
        elif ask2 == 'h':
            cursor.execute('select * from startups where valuation_$ >= 1000')
        elif ask2 == 'i':
            cursor.execute('select * from startups order by yearfounded desc')
        elif ask2 == 'j':
            cursor.execute('select * from startups order by headquaters')
            
        print('')
        record2 = cursor.fetchall()
        # checking if resultset is empty or not
        if len(record2) == 0:
            print('No record found!\n')
        else:
            print('Required records:\n')
            if ask2 == 'g':
                print('Valuaton of all startups(in million $):')
            else:
                print(coloumn_names)
            for row2 in record2:
                print(row2)
         
            
    elif ask == 5:
        print('Exiting...')
        break
        
