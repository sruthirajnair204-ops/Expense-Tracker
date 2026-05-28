#Initializing empty lists to store the expense
categories=[]
amounts=[]
print()
#Starting the continuous loop
while True:
    #Display the main menu choices to the user
    print('Main Menu: Please select from below')
    print('    1.Add New Expense\n    2.View Expense\n    3.View Total Spent\n    4.Delete an expense\n    5.Exit program\n')
    print('*'*50)
    #taking the user's choice and validating it
    try:
        choice=int(input('Input your choice: '))
    except ValueError:
        print('Invalid selection! Please choose the correct option from 1 to 5\n')
        print('*'*50)
        continue
    #---CHOICE 1: ADD NEW EXPENSE---
    if choice==1:
        expense=input('Enter your expense category: ')
        #Checking if the category name contains only alphabets
        if expense.isalpha():
            categories.append(expense)
            #taking the amount from the user and validating it
            try:
                amt=float(input('Enter the amount: '))
                amounts.append(amt)
                print('Expense added successfully\n')
                print('*'*50)
            except ValueError:
                print('Invalid Amount! Please enter only numbers.\n')
                print('*'*50)
        else:
            print('Please use only letters\n')
            print('*'*50)
    #---CHOICE 2: VIEW ALL EXPENSES---
    elif choice==2:
        #Checking if the list is empty
        if len(categories)==0:
            print('There is no expense added yet..\n')
        else:
            print('___Your Expense are___\n')
            #Looping through both lists using index positions
            for i in range(len(categories)):
                print(f'{i + 1}. {categories[i]} - \u20B9{amounts[i]}/-\n')
            print('*'*50)
    #---CHOICE 3: CALCULATE TOTAL SPENT---
    elif choice==3:
        #Calculating the total spent
        total_spent=sum(list(amounts))
        print(f'Your Total Spent: \u20B9{total_spent:.2f}\n')
        print('*'*50)
    #---CHOICE 4: DELETE AN EXPENSE---
    elif choice==4:
        #Checking if there are any entries available to delete
        if len(categories)==0:
            print('There are no expenses to delete!\n')
            print('*'*50)
        else:
            #Displaying current items to identify the number to delete
            for i in range(len(categories)):
                print(f'{i+1}. {categories[i]} - \u20B9{amounts[i]}/-')
            print()
            try:
                delete_expense=int(input('Enter number to delete: ')) - 1
                #Checking if the entered index exists in our list.
                if 0<=delete_expense<len(categories):
                    #Removeing from both the lists
                    removed_cat=categories.pop(delete_expense)
                    removed_amt=amounts.pop(delete_expense)
                    print(f'Successfully deleted: {removed_cat} (\u20B9{removed_amt}/-)\n')
                    print('*'*50)
                else:
                    print('Invalid item number! Returning to main menu.\n')
                    print('*'*50)
            except ValueError:
                print('Invalid entry! Please enter a valid number.\n')
                print('*'*50)

    #---CHOICE 5: EXIT PROGRAM---
    elif choice==5:
        print('Good Bye, See you again..!\n')
        break  #Exiting from the While loop

    #---ERROR HANDLING FOR OUT OF OPTION NUMBERS---
    else:
        print('Invalid selection! Please choose the correct option from 1 to 5\n')
        print('*'*50)




