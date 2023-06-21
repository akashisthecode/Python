#!/usr/bin/env python
# coding: utf-8

# In[2]:


try:
  a = int(input("Enter the First Number: "))
  b = int(input("Enter the Second Number: "))
  operation = input(
  "Select operation: \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n Your Operation Number: "
)
  if operation == "1":
    c = a + b
    print("The Sum is: {}".format(c))
  elif operation == "2":
    c = a - b
    print("The Difference is: {} ".format(c))
  elif operation == "3":
    c = a * b
    print("The Multiplication is: {} ".format(c))
  elif operation == "4":
    c = a / b
    print("The Division is: {} ".format(c))
  else:
    print("Enter the Valid Data")
except ValueError:
  print("Please Enter Numerical Data")


# In[ ]:





# In[ ]:





# In[ ]:




