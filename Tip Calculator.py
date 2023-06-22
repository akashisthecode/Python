#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Tip Calculator:")
total_bill = input("What was the Total Bill: ")
tip_percentage = input("What percentage tip would you like to give: ")
split = input("How many people to split the Bill? ")
split_amount = int(total_bill) / int(split)
try:
  tip_amount = float(split_amount)*float(tip_percentage)
  final_amount = round(tip_amount/100, 2)
  pay_bill = float(split_amount) + float(final_amount)
  round(pay_bill,2)
  print("The Amount payable by each person is: {}".format(round(pay_bill,2)))
except ZeroDivisionError:
  tip_amount = float(split_amount)

