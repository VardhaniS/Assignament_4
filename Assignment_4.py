#!/usr/bin/env python
# coding: utf-8

# 1. What exactly is []?
[] means list representation.
# 2. In a list of values stored in a variable called spam, how would you assign the value  'hello' as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)
We can assign the value by append,insert.
For inserting at a specific position we use the spam.insert
# In[1]:


spam=[2,4,6,8,10]
spam.insert(2,'hello')
print(spam)


# Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.

# 3. What is the value of spam[int(int('3' * 2) / 11)]?
Here the int(int('3'*2)/11) means '3' the string is multipled means 33 it convertes into integer and when divided by 11 the output is 3 .
The 3rd position in the list is displayed
# In[3]:


spam=['a','b','c','d']
print(spam[int(int('3'*2)/11)])


# 4. What is the value of spam[-1]?
# 
-1 index starts from the last of the list. The last index of list is -1.
# In[5]:


print(spam[-1])


# 5. What is the value of spam[:2]?
It prints the from the starting of the list to the position before 2
# In[6]:


print(spam[:2])


# Let's pretend bacon has the list [3.14, 'cat,'  11, 'cat,'  True] for the next three questions.

# 6. What is the value of bacon.index('cat')?
It displays the first index position of 'cat' in list
# In[17]:


bacon=[3.14,'cat',11,'cat',True]
print(bacon.index('cat'))


# 7. How does bacon.append(99) change the look of the list value in bacon?
append(99) is used to insert 99 in the list
# In[19]:


bacon.append(99)
print(bacon)


# 8. How does bacon.remove('cat') change the look of the list in bacon?

# In[ ]:


remove is used remove the specific variable from the list


# In[20]:


bacon.remove('cat')
print(bacon)


# 9. What are the list concatenation and list replication operators?

# In[ ]:


List concatenation is used to add both the list together where as replication reportor used to join and replicate the variable in list


# 10. What is difference between the list methods append() and insert()?
append is used to add the variable at the last of the list.
insert is used to add the variable at specified position 
# 11. What are the two methods for removing items from a list?
remove and pop
# 12. Describe how list values and string values are identical.
list values are the nunber of elements in the list and string value is the number of characters in the string
# 13. What's the difference between tuples and lists?

# In[ ]:


lists are changable where as tuples are unchangable.


# 14. How do you type a tuple value that only contains the integer 42?

# In[1]:


x=(42,)
print(type(x))

15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# In[6]:



X=('vardhani','varu')
y=list(X)
print(y)
z=tuple(y)
print(z)


# 16. Variables that "contain"; list values are not necessarily lists themselves. Instead, what do they contain?
will refer to list values
# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
in copy() if any changes made to reflected copy the original copy is affected
where as deepcopy() if any changes made in reflected copy the orginal copy is not affected.