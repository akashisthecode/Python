import math
def loan_emi():
  amount = int(input("what is the total amount of laon you want? \n"))
  duration = int(input("what is the time period in months? \n"))
  rate_percent = int(input("the rate at which you want the loan? \n"))
  down_payment = int(input("the down payment you are willing to do \n"))
  rate = rate_percent/100   
  loan_amount = amount - down_payment
  try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
  except ZeroDivisionError:
        emi = loan_amount / duration
  emi = math.ceil(emi)
  print("The EMI for your amount as per your duration and downpayment is:\nRs.{}".format(emi))
