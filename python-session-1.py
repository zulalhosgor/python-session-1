#!/usr/bin/env python
# coding: utf-8
# In[4]:
type(True)
# In[5]:
int(2.9)
# #
# 
# In[6]:
#the sum of two integers gives an integer.
2 + 2
# In[7]:
type(2+2)
# In[8]:
#the sum of two floats gives an float.
2.4 + 3.5
# In[9]:
type(5.9)
# In[10]:
#when subtracting two integers, the result is an integer.
3.Feb
# In[11]:
#if only one of the objects in the subtraction is float, the result is float. 
5.03.2001
# In[12]:
#if only one of the objects in the multiplication operation is float, the result is float. 
5 * 1.2
# In[13]:
#in division, the result is float regardless of the type of objects.
# // operator (int division) 
# 
# 
# In[18]:
#if even one of the objects being processed is float, the answer will be float.
#shows only the exact part of the result of the division operation.
5 // 2
# In[15]:
5 // 2.5
# % operator (modulus operator)
# In[20]:
#gives the remainder after division.
5%2
# ** operator
# In[22]:
#performs the operation of taking the exponent of the number.
2 ** 3
# print ()
# 
# STRINGS
# 
# In[27]:
#each character specified in quotation marks is called a string.
#strings are non-scalar.
#strings are immutable.
# In[28]:
type("anything.?")
# ESCAPE SEQUENCES
# In[30]:
#by using a backslash, you can tell it to treat the quotation mark after it differently.
HHH \hey\"gg"
# In[31]:
'aleksandra\'s home'
# In[34]:
#new line = \n
print("hey\nwassup")
# In[36]:
#tab = 4 times.
print("hey\twassup")
# In[38]:
print("okay\\")
# In[ ]:
# In[41]:
#variable assignment
hi = "hi!"
print(hi)
# string concatenation
# In[42]:
#string concatenation
# In[43]:
5+"4"
# In[44]:
5+ " "+"4"
# In[45]:
message = "hello"
name = "aleksandra"
message + " " + name
# In[49]:
text = message + " " + name
print(text)
# successive concatenation
# In[50]:
#successive concatenation
4 * "hey"
# In[51]:
hey + "hey" + "hey" + "hey"
# In[52]:
1 + "0" *100
# In[53]:
type("1" + "0" *100)
# # len()
# 
# In[54]:
len("12345")
# In[55]:
len("hahahahhahahhahhaha")
# In[56]:
len(" ")
# # indexing [  ] , starting from 0 
# In[59]:
name = "aleksandra"
name[3]
# In[61]:
#no need to variable assignment always.
aleksandra[3]
# In[62]:
#if you want last element of something.
name[-1]
# In[63]:
name[-2]
# In[68]:
#since strings are immutable you cannot change their elements.
# In[70]:
name = "aleksandra"
# In[71]:
name[0] = b
# # slicing
# In[72]:
name = "aleksandra"
# In[73]:
name[0:3]
# In[74]:
name[:3]
# In[75]:
name[3:]
# In[77]:
#the first typed index number is included, but not the last one.
#if you do not specify the beginning, it operates from the beginning. if you do not specify the last element, it operates until the last element.
# In[78]:
#In the slicing process, if the value we give as the end is greater than our largest index, we will not get an error.
# In[80]:
name[0:50000]
# In[81]:
# start point : ending point : rule
# In[82]:
name[0:500:2]
# In[83]:
name[0:3:2]
# In[84]:
#the same process can also be done backwards. but the last element must be written first.
# In[86]:
name[10:0:-2]
# In[87]:
name[10::-1]
# In[88]:
name[::-1]
# # CASTING IN STRINGS
# In[92]:
a = "5"
int(a)
# In[94]:
a = "hi5"
int(a)
# In[97]:
b = "5.3"
int(b)
# In[98]:
b = "5.1"
float(b)
# In[100]:
b = "5.4"
int(float(b))
# # input
# In[101]:
#input value is string.
# In[104]:
x = input("enter a number")
# In[105]:
type(x)
# In[108]:
#directly casting to integer
x = int(input("enter a number"))
# In[107]:
x + 5
# In[109]:
x=int(input("Ondalık bir sayı giriniz: "))
sonuc=x*4
print(sonuc)
# In[110]:
x = 2 #comment line does not have to be in the different line.
# In[115]:
"""this is also 
a comment line"""
x=2
print(x)
# In[ ]:
