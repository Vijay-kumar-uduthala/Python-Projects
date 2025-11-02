#!/usr/bin/env python
# coding: utf-8

# In[2]:


Name= input("Enter your name")
Weight= int(input("Enter your weight in pounds"))
Height= int(input("Enter your height in inches"))
BMI=Weight * 703 / (Height * Height)
print(BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are very underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("Congrats! You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else: 
        print("You are very overweight")
else:
    print("enter valid details")

