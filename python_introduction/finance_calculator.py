monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("your monthly savings are" , monthly_savings)
projected_savings = monthly_savings * 12 * 1.05
print("projected savings after one year, with interest, is: " , projected_savings)


