#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Challenge-1:-Tuples" data-toc-modified-id="Challenge-1:-Tuples-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Challenge 1: Tuples</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Do-you-know-you-can-create-tuples-with-only-one-element?" data-toc-modified-id="Do-you-know-you-can-create-tuples-with-only-one-element?-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>Do you know you can create tuples with only one element?</a></span></li><li><span><a href="#Print-the-type-of-tup." data-toc-modified-id="Print-the-type-of-tup.-1.0.2"><span class="toc-item-num">1.0.2&nbsp;&nbsp;</span>Print the type of <code>tup</code>.</a></span></li><li><span><a href="#Now-try-to-append-the-following-elements-to-tup." data-toc-modified-id="Now-try-to-append-the-following-elements-to-tup.-1.0.3"><span class="toc-item-num">1.0.3&nbsp;&nbsp;</span>Now try to append the following elements to <code>tup</code>.</a></span></li><li><span><a href="#How-about-re-assign-a-new-value-to-an-existing-tuple?" data-toc-modified-id="How-about-re-assign-a-new-value-to-an-existing-tuple?-1.0.4"><span class="toc-item-num">1.0.4&nbsp;&nbsp;</span>How about re-assign a new value to an existing tuple?</a></span></li><li><span><a href="#Split-tup-into-tup1-and-tup2-with-4-elements-in-each." data-toc-modified-id="Split-tup-into-tup1-and-tup2-with-4-elements-in-each.-1.0.5"><span class="toc-item-num">1.0.5&nbsp;&nbsp;</span>Split <code>tup</code> into <code>tup1</code> and <code>tup2</code> with 4 elements in each.</a></span></li><li><span><a href="#Add-tup1-and-tup2-into-tup3-using-the-+-operator." data-toc-modified-id="Add-tup1-and-tup2-into-tup3-using-the-+-operator.-1.0.6"><span class="toc-item-num">1.0.6&nbsp;&nbsp;</span>Add <code>tup1</code> and <code>tup2</code> into <code>tup3</code> using the <code>+</code> operator.</a></span></li><li><span><a href="#Count-the-number-of-elements-in-tup1-and-tup2.-Then-add-the-two-counts-together-and-check-if-the-sum-is-the-same-as-the-number-of-elements-in-tup3." data-toc-modified-id="Count-the-number-of-elements-in-tup1-and-tup2.-Then-add-the-two-counts-together-and-check-if-the-sum-is-the-same-as-the-number-of-elements-in-tup3.-1.0.7"><span class="toc-item-num">1.0.7&nbsp;&nbsp;</span>Count the number of elements in <code>tup1</code> and <code>tup2</code>. Then add the two counts together and check if the sum is the same as the number of elements in <code>tup3</code>.</a></span></li><li><span><a href="#What-is-the-index-number-of-&quot;h&quot;-in-tup3?" data-toc-modified-id="What-is-the-index-number-of-&quot;h&quot;-in-tup3?-1.0.8"><span class="toc-item-num">1.0.8&nbsp;&nbsp;</span>What is the index number of <code>"h"</code> in <code>tup3</code>?</a></span></li><li><span><a href="#Now,-use-a-FOR-loop-to-check-whether-each-letter-in-the-following-list-is-present-in-tup3:" data-toc-modified-id="Now,-use-a-FOR-loop-to-check-whether-each-letter-in-the-following-list-is-present-in-tup3:-1.0.9"><span class="toc-item-num">1.0.9&nbsp;&nbsp;</span>Now, use a FOR loop to check whether each letter in the following list is present in <code>tup3</code>:</a></span></li><li><span><a href="#How-many-times-does-each-letter-in-letters-appear-in-tup3?" data-toc-modified-id="How-many-times-does-each-letter-in-letters-appear-in-tup3?-1.0.10"><span class="toc-item-num">1.0.10&nbsp;&nbsp;</span>How many times does each letter in <code>letters</code> appear in <code>tup3</code>?</a></span></li></ul></li></ul></li><li><span><a href="#Challenge-2:-Sets" data-toc-modified-id="Challenge-2:-Sets-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Challenge 2: Sets</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#First,-import-the-Python-random-library." data-toc-modified-id="First,-import-the-Python-random-library.-2.0.1"><span class="toc-item-num">2.0.1&nbsp;&nbsp;</span>First, import the Python <code>random</code> library.</a></span></li><li><span><a href="#In-the-cell-below,-create-a-list-named-sample_list_1-with-80-random-values." data-toc-modified-id="In-the-cell-below,-create-a-list-named-sample_list_1-with-80-random-values.-2.0.2"><span class="toc-item-num">2.0.2&nbsp;&nbsp;</span>In the cell below, create a list named <code>sample_list_1</code> with 80 random values.</a></span></li><li><span><a href="#Convert-sample_list_1-to-a-set-called-set1.-Print-the-length-of-the-set.-Is-its-length-still-80?" data-toc-modified-id="Convert-sample_list_1-to-a-set-called-set1.-Print-the-length-of-the-set.-Is-its-length-still-80?-2.0.3"><span class="toc-item-num">2.0.3&nbsp;&nbsp;</span>Convert <code>sample_list_1</code> to a set called <code>set1</code>. Print the length of the set. Is its length still 80?</a></span></li><li><span><a href="#Create-another-list-named-sample_list_2-with-80-random-values." data-toc-modified-id="Create-another-list-named-sample_list_2-with-80-random-values.-2.0.4"><span class="toc-item-num">2.0.4&nbsp;&nbsp;</span>Create another list named <code>sample_list_2</code> with 80 random values.</a></span></li><li><span><a href="#Convert-sample_list_2-to-a-set-called-set2.-Print-the-length-of-the-set.-Is-its-length-still-80?" data-toc-modified-id="Convert-sample_list_2-to-a-set-called-set2.-Print-the-length-of-the-set.-Is-its-length-still-80?-2.0.5"><span class="toc-item-num">2.0.5&nbsp;&nbsp;</span>Convert <code>sample_list_2</code> to a set called <code>set2</code>. Print the length of the set. Is its length still 80?</a></span></li><li><span><a href="#Identify-the-elements-present-in-set1-but-not-in-set2.-Assign-the-elements-to-a-new-set-named-set3." data-toc-modified-id="Identify-the-elements-present-in-set1-but-not-in-set2.-Assign-the-elements-to-a-new-set-named-set3.-2.0.6"><span class="toc-item-num">2.0.6&nbsp;&nbsp;</span>Identify the elements present in <code>set1</code> but not in <code>set2</code>. Assign the elements to a new set named <code>set3</code>.</a></span></li><li><span><a href="#Identify-the-elements-present-in-set2-but-not-in-set1.-Assign-the-elements-to-a-new-set-named-set4." data-toc-modified-id="Identify-the-elements-present-in-set2-but-not-in-set1.-Assign-the-elements-to-a-new-set-named-set4.-2.0.7"><span class="toc-item-num">2.0.7&nbsp;&nbsp;</span>Identify the elements present in <code>set2</code> but not in <code>set1</code>. Assign the elements to a new set named <code>set4</code>.</a></span></li><li><span><a href="#Now-Identify-the-elements-shared-between-set1-and-set2.-Assign-the-elements-to-a-new-set-named-set5." data-toc-modified-id="Now-Identify-the-elements-shared-between-set1-and-set2.-Assign-the-elements-to-a-new-set-named-set5.-2.0.8"><span class="toc-item-num">2.0.8&nbsp;&nbsp;</span>Now Identify the elements shared between <code>set1</code> and <code>set2</code>. Assign the elements to a new set named <code>set5</code>.</a></span></li><li><span><a href="#What-is-the-relationship-among-the-following-values:" data-toc-modified-id="What-is-the-relationship-among-the-following-values:-2.0.9"><span class="toc-item-num">2.0.9&nbsp;&nbsp;</span>What is the relationship among the following values:</a></span></li><li><span><a href="#Create-an-empty-set-called-set6." data-toc-modified-id="Create-an-empty-set-called-set6.-2.0.10"><span class="toc-item-num">2.0.10&nbsp;&nbsp;</span>Create an empty set called <code>set6</code>.</a></span></li><li><span><a href="#Add-set3-and-set5-to-set6-using-the-Python-Set-update-method." data-toc-modified-id="Add-set3-and-set5-to-set6-using-the-Python-Set-update-method.-2.0.11"><span class="toc-item-num">2.0.11&nbsp;&nbsp;</span>Add <code>set3</code> and <code>set5</code> to <code>set6</code> using the Python Set <code>update</code> method.</a></span></li><li><span><a href="#Check-if-set1-and-set6-are-equal." data-toc-modified-id="Check-if-set1-and-set6-are-equal.-2.0.12"><span class="toc-item-num">2.0.12&nbsp;&nbsp;</span>Check if <code>set1</code> and <code>set6</code> are equal.</a></span></li><li><span><a href="#Check-if-set1-contains-set2-using-the-Python-Set-issubset-method.-Then-check-if-set1-contains-set3.*" data-toc-modified-id="Check-if-set1-contains-set2-using-the-Python-Set-issubset-method.-Then-check-if-set1-contains-set3.*-2.0.13"><span class="toc-item-num">2.0.13&nbsp;&nbsp;</span>Check if <code>set1</code> contains <code>set2</code> using the Python Set <code>issubset</code> method. Then check if <code>set1</code> contains <code>set3</code>.*</a></span></li><li><span><a href="#Using-the-Python-Set-union-method,-aggregate-set3,-set4,-and-set5.-Then-aggregate-set1-and-set2." data-toc-modified-id="Using-the-Python-Set-union-method,-aggregate-set3,-set4,-and-set5.-Then-aggregate-set1-and-set2.-2.0.14"><span class="toc-item-num">2.0.14&nbsp;&nbsp;</span>Using the Python Set <code>union</code> method, aggregate <code>set3</code>, <code>set4</code>, and <code>set5</code>. Then aggregate <code>set1</code> and <code>set2</code>.</a></span></li><li><span><a href="#Check-if-the-aggregated-values-are-equal." data-toc-modified-id="Check-if-the-aggregated-values-are-equal.-2.0.15"><span class="toc-item-num">2.0.15&nbsp;&nbsp;</span>Check if the aggregated values are equal.</a></span></li><li><span><a href="#Using-the-pop-method,-remove-the-first-element-from-set1." data-toc-modified-id="Using-the-pop-method,-remove-the-first-element-from-set1.-2.0.16"><span class="toc-item-num">2.0.16&nbsp;&nbsp;</span>Using the <code>pop</code> method, remove the first element from <code>set1</code>.</a></span></li><li><span><a href="#Remove-every-element-in-the-following-list-from-set1-if-they-are-present-in-the-set.-Print-the-remaining-elements." data-toc-modified-id="Remove-every-element-in-the-following-list-from-set1-if-they-are-present-in-the-set.-Print-the-remaining-elements.-2.0.17"><span class="toc-item-num">2.0.17&nbsp;&nbsp;</span>Remove every element in the following list from <code>set1</code> if they are present in the set. Print the remaining elements.</a></span></li></ul></li></ul></li><li><span><a href="#Challenge-3:-Dictionaries" data-toc-modified-id="Challenge-3:-Dictionaries-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Challenge 3: Dictionaries</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Sort-the-keys-of-word_freq-ascendingly." data-toc-modified-id="Sort-the-keys-of-word_freq-ascendingly.-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>Sort the keys of <code>word_freq</code> ascendingly.</a></span></li><li><span><a href="#Sort-the-values-of-word_freq-ascendingly." data-toc-modified-id="Sort-the-values-of-word_freq-ascendingly.-3.0.2"><span class="toc-item-num">3.0.2&nbsp;&nbsp;</span>Sort the values of <code>word_freq</code> ascendingly.</a></span></li></ul></li></ul></li></ul></div>

# ## Challenge 1: Tuples
# 
# #### Do you know you can create tuples with only one element?
# 
# **In the cell below, define a variable `tup` with a single element `"I"`.**
# 
# *Hint: you need to add a comma (`,`) after the single element.*

# In[4]:


# Your code here

tup = ("I",)


# #### Print the type of `tup`. 
# 
# Make sure its type is correct (i.e. *tuple* instead of *str*).

# In[5]:


# Your code here

type(tup)


# #### Now try to append the following elements to `tup`. 
# 
# Are you able to do it? Explain.
# 
# ```
# "r", "o", "n", "h", "a", "c", "k',
# ```

# In[6]:


# Your code here
tup.append("r", "o", "n", "h", "a", "c", "k")

# Your explanation here
# Una de las características de una tupla es que una vez está creada no es modificable, no se pueden ni añadir ni borrar ni cambiar elementos.


# #### How about re-assign a new value to an existing tuple?
# 
# Re-assign the following elements to `tup`. Are you able to do it? Explain.
# 
# ```
# "I", "r", "o", "n", "h", "a", "c", "k"
# ```

# In[7]:


# Your code here
tup["I"] = ("I", "r", "o", "n", "h", "a", "c", "k")

# Your explanation here
# Una de las características de una tupla es que una vez está creada no es modificable, no se pueden ni añadir ni borrar ni cambiar elementos.


# #### Split `tup` into `tup1` and `tup2` with 4 elements in each. 
# 
# `tup1` should be `("I", "r", "o", "n")` and `tup2` should be `("h", "a", "c", "k")`.
# 
# *Hint: use positive index numbers for `tup1` assignment and use negative index numbers for `tup2` assignment. Positive index numbers count from the beginning whereas negative index numbers count from the end of the sequence.*
# 
# Also print `tup1` and `tup2`.

# In[8]:


# Your code here
tup = ["I", "r", "o", "n", "h", "a", "c", "k"]

tup1 = tuple(tup[:4])
tup2 = tuple(tup[-4:])


print(tup1)
print(tup2)


# #### Add `tup1` and `tup2` into `tup3` using the `+` operator.
# 
# Then print `tup3` and check if `tup3` equals to `tup`.

# In[9]:


# Your code here
tup3 = tup1 + tup2
print(tup3)

if tup3 == tup:
    print("tup3 es igual a tup")
else:
    print("tup3 no es igual a tup")


# #### Count the number of elements in `tup1` and `tup2`. Then add the two counts together and check if the sum is the same as the number of elements in `tup3`.

# In[10]:


# Your code here

a = len(tup1)
b = len(tup2)

if a + b == len(tup3):
    print("Tienen el mismo número de elementos")
else:
    print("No tienen el mismo número de elementos")


# #### What is the index number of `"h"` in `tup3`?

# In[11]:


# Your code here
c = tup3.index("h")
f'El index es {c}'


# #### Now, use a FOR loop to check whether each letter in the following list is present in `tup3`:
# 
# ```
# letters = ["a", "b", "c", "d", "e"]
# ```
# 
# For each letter you check, print `True` if it is present in `tup3` otherwise print `False`.
# 
# *Hint: you only need to loop `letters`. You don't need to loop `tup3` because there is a Python operator `in` you can use. See [reference](https://stackoverflow.com/questions/17920147/how-to-check-if-a-tuple-contains-an-element-in-python).*

# In[12]:


# Your code here
letters = ["a", "b", "c", "d", "e"]

for let in letters:
    if let in tup3:
        print("True")
    else:
        print("False")
        


# #### How many times does each letter in `letters` appear in `tup3`?
# 
# Print out the number of occurrence of each letter.

# In[16]:


# Your code 

[[i, tup.count(i)] for i in letters]


# ## Challenge 2: Sets
# 
# There are a lot to learn about Python Sets and the information presented in the lesson is limited due to its length. To learn Python Sets in depth you are strongly encouraged to review the W3Schools tutorial on [Python Sets Examples and Methods](https://www.w3schools.com/python/python_sets.asp) before you work on this lab. Some difficult questions in this lab have their solutions in the W3Schools tutorial.
# 
# #### First, import the Python `random` library.

# In[17]:


import random


# #### In the cell below, create a list named `sample_list_1` with 80 random values. 
# 
# Requirements:
# 
# * Each value is an integer falling between 0 and 100.
# * Each value in the list is unique.
# 
# Print `sample_list_1` to review its values
# 
# *Hint: use `random.sample` ([reference](https://docs.python.org/3/library/random.html#random.sample)).*

# In[18]:


# Your code here

sample_list_1 = random.sample(range(0,100), 80)
print(sample_list_1)
                            


# #### Convert `sample_list_1` to a set called `set1`. Print the length of the set. Is its length still 80?

# In[19]:


# Your code here

set1 = set(sample_list_1)
len(set1)


# #### Create another list named `sample_list_2` with 80 random values.
# 
# Requirements:
# 
# * Each value is an integer falling between 0 and 100.
# * The values in the list don't have to be unique.
# 
# *Hint: Use a FOR loop.*

# In[20]:


# Your code here
sample_list_2 = []

for i in range(80):
    a = random.randint(0,100)
    sample_list_2.append(a)
                      
print(sample_list_2)


# #### Convert `sample_list_2` to a set called `set2`. Print the length of the set. Is its length still 80?

# In[21]:


# Your code here


set2 = set(sample_list_2)
len(set2)


# #### Identify the elements present in `set1` but not in `set2`. Assign the elements to a new set named `set3`.

# In[22]:


# Your code here
set3 = set1 - set2 
set(set3)
print(set3)


# #### Identify the elements present in `set2` but not in `set1`. Assign the elements to a new set named `set4`.

# In[23]:


# Your code here

set4 = set2 - set1
set(set4)
print(set4)


# #### Now Identify the elements shared between `set1` and `set2`. Assign the elements to a new set named `set5`.

# In[24]:


# Your code here

set5 = set1.intersection(set2)
set(set5)
print(set5)


# #### What is the relationship among the following values:
# 
# * len(set1)
# * len(set2)
# * len(set3)
# * len(set4)
# * len(set5)
# 
# Use a math formular to represent that relationship. Test your formular with Python code.

# In[25]:


# Your code here

len(set1) + len(set2) - len(set5) == len(set3) + len(set4) + len(set5)


# #### Create an empty set called `set6`.

# In[26]:


# Your code here

set6 = set()


# #### Add `set3` and `set5` to `set6` using the Python Set `update` method.

# In[27]:


# Your code here

set6.update(set3, set5)
print(set6)


# #### Check if `set1` and `set6` are equal.

# In[28]:


# Your code here

set1 == set6


# #### Check if `set1` contains `set2` using the Python Set `issubset` method. Then check if `set1` contains `set3`.*

# In[29]:


# Your code here

set1.issubset(set2)


# In[30]:


set1.issubset(set3)


# #### Using the Python Set `union` method, aggregate `set3`, `set4`, and `set5`. Then aggregate `set1` and `set2`. 

# In[31]:


# Your code here

agr1 = set3 | set4 | set5
agr2 = set1 | set2


# #### Check if the aggregated values are equal.

# In[32]:


# Your code here

agr1 == agr2


# #### Using the `pop` method, remove the first element from `set1`.

# In[33]:


# Your code here

set1.pop(1)
print(set1)

#No se puede borrar un elemento específico en los sets


# #### Remove every element in the following list from `set1` if they are present in the set. Print the remaining elements.
# 
# ```
# list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
# ```

# In[34]:


# Your code here

list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
list_final = []

for elm in list_to_remove:
    if elm in set1:
        set1.remove(elm)

print(set1)
        
        


# ## Challenge 3: Dictionaries
# 
# In this challenge you will practice how to manipulate Python dictionaries. Before starting on this challenge, you are encouraged to review W3School's [Python Dictionary Examples and Methods](https://www.w3schools.com/python/python_dictionaries.asp).
# 
# First thing you will practice is how to sort the keys in a dictionary. Unlike the list object, Python dictionary does not have a built-in *sort* method. You'll need to use FOR loops to to sort dictionaries either by key or by value.
# 
# The dictionary below is a summary of the word frequency of Ed Sheeran's song *Shape of You*. Each key is a word in the lyrics and the value is the number of times that word appears in the lyrics.

# In[35]:


word_freq = {'love': 25, 'conversation': 1, 'every': 6, "we're": 1, 'plate': 1, 'sour': 1, 'jukebox': 1, 'now': 11, 'taxi': 1, 'fast': 1, 'bag': 1, 'man': 1, 'push': 3, 'baby': 14, 'going': 1, 'you': 16, "don't": 2, 'one': 1, 'mind': 2, 'backseat': 1, 'friends': 1, 'then': 3, 'know': 2, 'take': 1, 'play': 1, 'okay': 1, 'so': 2, 'begin': 1, 'start': 2, 'over': 1, 'body': 17, 'boy': 2, 'just': 1, 'we': 7, 'are': 1, 'girl': 2, 'tell': 1, 'singing': 2, 'drinking': 1, 'put': 3, 'our': 1, 'where': 1, "i'll": 1, 'all': 1, "isn't": 1, 'make': 1, 'lover': 1, 'get': 1, 'radio': 1, 'give': 1, "i'm": 23, 'like': 10, 'can': 1, 'doing': 2, 'with': 22, 'club': 1, 'come': 37, 'it': 1, 'somebody': 2, 'handmade': 2, 'out': 1, 'new': 6, 'room': 3, 'chance': 1, 'follow': 6, 'in': 27, 'may': 2, 'brand': 6, 'that': 2, 'magnet': 3, 'up': 3, 'first': 1, 'and': 23, 'pull': 3, 'of': 6, 'table': 1, 'much': 2, 'last': 3, 'i': 6, 'thrifty': 1, 'grab': 2, 'was': 2, 'driver': 1, 'slow': 1, 'dance': 1, 'the': 18, 'say': 2, 'trust': 1, 'family': 1, 'week': 1, 'date': 1, 'me': 10, 'do': 3, 'waist': 2, 'smell': 3, 'day': 6, 'although': 3, 'your': 21, 'leave': 1, 'want': 2, "let's": 2, 'lead': 6, 'at': 1, 'hand': 1, 'how': 1, 'talk': 4, 'not': 2, 'eat': 1, 'falling': 3, 'about': 1, 'story': 1, 'sweet': 1, 'best': 1, 'crazy': 2, 'let': 1, 'too': 5, 'van': 1, 'shots': 1, 'go': 2, 'to': 2, 'a': 8, 'my': 33, 'is': 5, 'place': 1, 'find': 1, 'shape': 6, 'on': 40, 'kiss': 1, 'were': 3, 'night': 3, 'heart': 3, 'for': 3, 'discovering': 6, 'something': 6, 'be': 16, 'bedsheets': 3, 'fill': 2, 'hours': 2, 'stop': 1, 'bar': 1}


# #### Sort the keys of `word_freq` ascendingly.
# 
# Please create a new dictionary called `word_freq2` based on `word_freq` with the keys sorted ascedingly.
# 
# There are several ways to achieve that goal but many of the ways are beyond what we have covered so far in the course. There is one way that we'll describe employing what you have learned. Please feel free to use this way or any other way you want.
# 
# 1. First extract the keys of `word_freq` and convert it to a list called `keys`.
# 
# 1. Sort the `keys` list.
# 
# 1. Create an empty dictionary `word_freq2`.
# 
# 1. Use a FOR loop to iterate each value in `keys`. For each key iterated, find the corresponding value in `word_freq` and insert the key-value pair to `word_freq2`.
# 
# Print out `word_freq2` to examine its keys and values. Your output should be:
# 
# ```python
# {'a': 8, 'about': 1, 'all': 1, 'although': 3, 'and': 23, 'are': 1, 'at': 1, 'baby': 14, 'backseat': 1, 'bag': 1, 'bar': 1, 'be': 16, 'bedsheets': 3, 'begin': 1, 'best': 1, 'body': 17, 'boy': 2, 'brand': 6, 'can': 1, 'chance': 1, 'club': 1, 'come': 37, 'conversation': 1, 'crazy': 2, 'dance': 1, 'date': 1, 'day': 6, 'discovering': 6, 'do': 3, 'doing': 2, "don't": 2, 'drinking': 1, 'driver': 1, 'eat': 1, 'every': 6, 'falling': 3, 'family': 1, 'fast': 1, 'fill': 2, 'find': 1, 'first': 1, 'follow': 6, 'for': 3, 'friends': 1, 'get': 1, 'girl': 2, 'give': 1, 'go': 2, 'going': 1, 'grab': 2, 'hand': 1, 'handmade': 2, 'heart': 3, 'hours': 2, 'how': 1, 'i': 6, "i'll": 1, "i'm": 23, 'in': 27, 'is': 5, "isn't": 1, 'it': 1, 'jukebox': 1, 'just': 1, 'kiss': 1, 'know': 2, 'last': 3, 'lead': 6, 'leave': 1, 'let': 1, "let's": 2, 'like': 10, 'love': 25, 'lover': 1, 'magnet': 3, 'make': 1, 'man': 1, 'may': 2, 'me': 10, 'mind': 2, 'much': 2, 'my': 33, 'new': 6, 'night': 3, 'not': 2, 'now': 11, 'of': 6, 'okay': 1, 'on': 40, 'one': 1, 'our': 1, 'out': 1, 'over': 1, 'place': 1, 'plate': 1, 'play': 1, 'pull': 3, 'push': 3, 'put': 3, 'radio': 1, 'room': 3, 'say': 2, 'shape': 6, 'shots': 1, 'singing': 2, 'slow': 1, 'smell': 3, 'so': 2, 'somebody': 2, 'something': 6, 'sour': 1, 'start': 2, 'stop': 1, 'story': 1, 'sweet': 1, 'table': 1, 'take': 1, 'talk': 4, 'taxi': 1, 'tell': 1, 'that': 2, 'the': 18, 'then': 3, 'thrifty': 1, 'to': 2, 'too': 5, 'trust': 1, 'up': 3, 'van': 1, 'waist': 2, 'want': 2, 'was': 2, 'we': 7, "we're": 1, 'week': 1, 'were': 3, 'where': 1, 'with': 22, 'you': 16, 'your': 21}
# ```

# In[36]:


# Your code here
keys = list(word_freq.keys())
keys.sort()
print(keys)


# In[37]:


word_freq2 = {}

for k in keys:
    word_freq2[k]= word_freq[k]
        
print(word_freq2)


# #### Sort the values of `word_freq` ascendingly.
# 
# Sorting the values of a dictionary is more tricky than sorting the keys because a dictionary's values are not unique. Therefore you cannot use the same way you sorted dict keys to sort dict values.
# 
# The way to sort a dict by value is to utilize the `sorted` and `operator.itemgetter` functions. The following code snippet is provided to you to try. It will give you a list of tuples in which each tuple contains the key and value of a dict item. And the list is sorted based on the dict value ( [reference](http://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/)
# ).
# 
# ```python
# import operator
# sorted_tups = sorted(word_freq.items(), key=operator.itemgetter(1))
# print(sorted_tups)
# ```
# 
# Therefore, the steps to sort `word_freq` by value are:
# 
# * Using `sorted` and `operator.itemgetter`, obtain a list of tuples of the dict key-value pairs which is sorted on the value.
# 
# * Create an empty dictionary named `word_freq2`.
# 
# * Iterate the list of tuples. Insert each key-value pair into `word_freq2` as an object.
# 
# Print `word_freq2` to confirm your dictionary has its values sorted. Your output should be:
# 
# ```python
# {'conversation': 1, "we're": 1, 'plate': 1, 'sour': 1, 'jukebox': 1, 'taxi': 1, 'fast': 1, 'bag': 1, 'man': 1, 'going': 1, 'one': 1, 'backseat': 1, 'friends': 1, 'take': 1, 'play': 1, 'okay': 1, 'begin': 1, 'over': 1, 'just': 1, 'are': 1, 'tell': 1, 'drinking': 1, 'our': 1, 'where': 1, "i'll": 1, 'all': 1, "isn't": 1, 'make': 1, 'lover': 1, 'get': 1, 'radio': 1, 'give': 1, 'can': 1, 'club': 1, 'it': 1, 'out': 1, 'chance': 1, 'first': 1, 'table': 1, 'thrifty': 1, 'driver': 1, 'slow': 1, 'dance': 1, 'trust': 1, 'family': 1, 'week': 1, 'date': 1, 'leave': 1, 'at': 1, 'hand': 1, 'how': 1, 'eat': 1, 'about': 1, 'story': 1, 'sweet': 1, 'best': 1, 'let': 1, 'van': 1, 'shots': 1, 'place': 1, 'find': 1, 'kiss': 1, 'stop': 1, 'bar': 1, "don't": 2, 'mind': 2, 'know': 2, 'so': 2, 'start': 2, 'boy': 2, 'girl': 2, 'singing': 2, 'doing': 2, 'somebody': 2, 'handmade': 2, 'may': 2, 'that': 2, 'much': 2, 'grab': 2, 'was': 2, 'say': 2, 'waist': 2, 'want': 2, "let's": 2, 'not': 2, 'crazy': 2, 'go': 2, 'to': 2, 'fill': 2, 'hours': 2, 'push': 3, 'then': 3, 'put': 3, 'room': 3, 'magnet': 3, 'up': 3, 'pull': 3, 'last': 3, 'do': 3, 'smell': 3, 'although': 3, 'falling': 3, 'were': 3, 'night': 3, 'heart': 3, 'for': 3, 'bedsheets': 3, 'talk': 4, 'too': 5, 'is': 5, 'every': 6, 'new': 6, 'follow': 6, 'brand': 6, 'of': 6, 'i': 6, 'day': 6, 'lead': 6, 'shape': 6, 'discovering': 6, 'something': 6, 'we': 7, 'a': 8, 'like': 10, 'me': 10, 'now': 11, 'baby': 14, 'you': 16, 'be': 16, 'body': 17, 'the': 18, 'your': 21, 'with': 22, "i'm": 23, 'and': 23, 'love': 25, 'in': 27, 'my': 33, 'come': 37, 'on': 40}
# ```

# In[38]:


# Your code here

import operator
sorted_tups = sorted(word_freq.items(), key=operator.itemgetter(1))
print(sorted_tups)


# In[39]:


word_freq2 = {}

for t in sorted_tups:
    key = t[0]
    value = t[1]
    word_freq2[key] = value
    
print(word_freq2)
    


# In[ ]:




