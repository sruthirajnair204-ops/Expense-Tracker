categories=[]
amounts=[]
print()
while True:
    print('Main Menu: Please select from below')
    print('    1.Add New Expense\n    2.View Expense\n    3.View Total Spent\n    4.Delete an expense\n    5.Exit program\n')
    print('*' * 50)
    try:
        choice=int(input('Input your choice: '))
    except ValueError:
        print('Invalid selection! Please choose the correct option from 1 to 4\n')
        print('*' * 50)
        continue
    #Add New Expense
    if choice==1:
        expense=input('Enter your expense category: ')
        if expense.isalpha():
            categories.append(expense)
            try:
                amt=float(input('Enter the amount: '))
                amounts.append(amt)
                print('Expense added successfully\n')
                print('*' * 50)
            except ValueError:
                print('Invalid Amount! Please enter only numbers.\n')
                print('*' * 50)
        else:
            print('Please use only letters\n')
            print('*'*50)
    #View the expense
    elif choice==2:
        if len(categories)==0:
            print('There is no expense added yet..\n')
        else:
            print('___Your Expense are___\n')
            for i in range(len(categories)):
                print(f'{i+1}. {categories[i]} - \u20B9{amounts[i]}/-\n')
            print('*' * 50)
    elif choice==3:
        total_spent=sum(list(amounts))
        print('Your Total Spent: ',total_spent,'\n')
    #Delete an expense
    elif choice==4:
        if len(categories)==0:
            print('There are no expenses to delete!\n')
            print('*' * 50)
        else:
            print('___Select the serial number to delete___\n')
            for i in range(len(categories)):
                print(f'{i + 1}. {categories[i]} - \u20B9{amounts[i]}/-')
            print()
            try:
                delete_expense=int(input('Enter number to delete: ')) - 1
                #Check if the entered index is exists in our list.
                if 0 <= delete_expense < len(categories):
                    #Remove from both lists using .pop()
                    removed_cat = categories.pop(delete_expense)
                    removed_amt = amounts.pop(delete_expense)
                    print(f'Successfully deleted: {removed_cat} (\u20B9{removed_amt}/-)\n')
                    print('*' * 50)
                else:
                    print('Invalid item number! Returning to main menu.\n')
                    print('*' * 50)
            except ValueError:
                print('Invalid entry! Please enter a valid number.\n')
                print('*' * 50)
    #Exit
    elif choice==5:
        print('Good Bye, See you again..!\n')
        break
    else:
        print('Invalid selection! Please choose the correct option from 1 to 4\n')
        print('*' * 50)


