# Week - 2

<details>

<summary>

## Reading and writing files

</summary>

> **Accessing an File**

```python
# --- Basic approach for accessing a file ---

# Using open() funtion:
file_obj = open('<file_name>','mode')
file_obj.close()
# You must close the file at the end of your program

# Using 'with' block:
# 'with' block automatically closes the file at the end
with open('<file_name>','mode') as file_obj:
  pass

# --- Some of modes for accessing a file ---

# By default, it's in read-only mode
readonlyfile_obj = open('file_name.txt')

# In write mode, it creates a new file if it didn't exists 
# (or) overwrites the existing content of the specified file
writeonlyfile_obj = open('filename.txt','w')

# In append mode, You can append the content at the end of the file
appendfile_obj = open('filename.txt','a')
```

> file functions

```python
# --- functions for reading files ---
with open('file_name.txt') as readfile_obj:

  # returns a single from the current position
  single_line = readfile_obj.readline()
  print(single_line)

  # returns the whole content from the current position
  all_content_from_current = readfile_obj.read()
  print(all_content_from_current)

# Reads all the lines and returns a list of all lines
readonlyfile_obj = open('file_name.txt')
all_lines = readfile_obj.readlines()
readonlyfile_obj.close()

# --- functions for writing files ---
with open('file_name.txt', 'w') as writefile_obj:
  
  # Overwrites the whole content of existing file with given content
  # (or) adds content if the file is newly created 
  writefile_obj.write('Adding this line by overwrting the previous content (or) adding content if the file is newly created ')
  
with open('file_name.txt', 'a') as appendfile_obj:

  # adds content at the end of the file
  appendfile_obj.write('adding this line at the end of the file')
```

</details>
<details>

<summary>

## Managing Files and Directories

</summary>

> Working with Files

```python
import os

# remove an existing file
os.remove('<file_name>')

# rename an existing file
os.rename('<current_file_name>','<new_file_name>')

# check whether file exists or not i.e, reurn a boolean value
os.path.exists('<file_path>')
```

> More File Information

```python
import os
import datetime

# returns the size of the file
os.path.getsize('<file_path>')

# return data-timestamps of the file
timestamp = os.path.getmtime('<file_path>')

# formating the time stamp into more human-readiable form - requires datetime module
file_creation_details = datetime.datetime.formattimestamp(timestamp)

# returns absolute file path of the relatively specified file path
os.path.abspath('<rel_file_path>')
```

> Directories

```python
import os

# return current working directory
os.getcwd()

# create a new directory
os.mkdir('<dir_name>')

# changes the directory
os.chdir('<dir_name>')

# remove an existing empty directory
os.rmdir('<dir_name>')

# lists all the files & directories within the specified directory
# if the directory is not specifies then it will returns list of all files & directories within the current directory
os.listdir('<dir_name>')

# returns a boolean value to determine whether the given name is a directory or not
os.isdir('<dir_name>')

# used to joined the full path
os.path.join()
```
>> Sample Program:
```python
# This program will determine all content with the current directory either as file or as directory
import os

dir = os.getcwd()
for name in os.listdir(dir):
  fullname = os.path. join(dir, name)
  if os.path.isdir(fullname):
    print("{} is a directory.".format(fullname))
  else:
    print("{} is a file.".format(fullname))
```

</details>
  
<details>
  
<summary>

## Reading and Writing CSV Files

</summary>

> Reading CSV Files

```python
import csv

with open('csv_file.txt') as cf:
  
  # reader parses the input file and return item in its respective order
  cf_reader = csv.reader(cf)
  
  # we use an simple for-loop to iterative over all data items
  for itemset in cf_reader:
    item1, item2, item3, ... = itemset
```
  
> Generating CSV

```python
import csv

# Consider the following datasets
dataset1 = [ ['user1','address1'] ]
dataset2 = [ ['user2','address2'], ['user3','address3'], ['user4','address4'] ]  

# writing the content into the a csv file 
with open('csv_file.txt','w') as cf:

  # made an writer instance of csv class for the file object 'cf'
  writer = csv.writer(cf)
  
  # writes a single row into the file
  writer.writerow(dataset1)
  
  # writes all rows into the file
  writer.writerow(dataset2)  
```

> Reading and Writing CSV Files with Dictionaries
>
>> We should use this approach when the data inside the csv file starts with headers like keys of dictionaries.

```python
# --- Reading from CSV files using Dicionaries ---
import csv

with open('sample_dict_csv.csv') as sdcf:
  
  # creating an reader instance for the file
  reader = csv.DictReader(sdcf)
  
  # now we can access them using the header values (or) keyvalues
  for data in reader:
    user, address = data['user'], data['address']

# --- Writing from CSV files using Dicionaries ---

# Consider the following datasets
dataset = { 'user1':'address1', 'user2':'address2', 'user3':'address3', 'user4':'address4' }
keys = [ 'user1', 'user2', 'user3', 'user4' ]

with open('sample_dict_csv.csv') as sdcf:
  
  # creating an writer instance for the file
  writer = csv.DictWriter(sdcf, fieldnames=keys)
  
  # first adding the header (or) keys for the csv file
  writer.writeheader()
  
  # now adding data values
  writer.writerows(dataset)
```
  
</details>
