# Store-Records-and-parallelized-read-analysis-


This project is split into 2 parts but submitted as one python file store_analyze.py 
1. Writing code that will take a file of records to insert into your DB and output all pages of that database      in a directory with one file per page. 
	The program will be called through a terminal with the following command to store the data 
	python store_analyze.py store <location_of_insert_file>
  
  Description:
  
  
  
    a. This will create three directories “Fixed”, “Delimited”, “Offset”. These directories should not exist prior to running this code. So, you will need to delete the directories between different runs of your code. 	
    b. Then it will read in all tuples from the input file that is given as an argument <location_of_insert_file>
    c. The insert file will consist of n tuples with one tuple per line, where each tuple is of the form: (INSERT, attribute_1, attribute_2 , … attribute_m) The number of attributes can be different with different input files, so don’t hard code the number of attributes. The first value of each tuple is INSERT, which will not be stored, it is just the command to say that you should insert this data into your storage. To make things easy, each value will be treated as a string. So, numbers like 65 will be treated like “65” when reading from the input file and writing to your pages (discussed below).
    d. The program will take each tuple from the input file, in the same order that they appear in the input file, and write them to multiple files (pages) in the three created directories using the following format: Each page can only hold 500 tuples. Fill up each page before creating a new one. Label pages sequentially as “page_0”, “page_1”, … “page_t” You do not know how many pages are needed until you know how many tuples there are. Each line in each page holds a single tuple in one of the following formats corresponding to the directory used:



              i. Fixed: In the pages, in this directory, each attribute uses 20 units of space. If they use less than 20 units of space, the concatenate “x” to the end of each value until they are 20 units of space. No values will require more than 20 units of space, so we don’t need to worry about catching those. An example with two attributes would be “012xxxxxxxxxxxxxxxxxKingxxxxxxxxxxxxxxxx” 
              ii. Delimited: In the pages in this directory, attributes are separated by a delimiter ‘$’. For example, a record could be “012$King$Tree$120”, which represent 4 attributes. 
              iii. Offset: In the pages in this directory, each record starts with n fixed length values then say how much of an offset each of their corresponding values are. For example, a record could be “6x9x13012King1200”, where 6x (6 with a space filler) indicates that the value of the first attribute (012) starts at index 6, 9x (9 with a space filler) indicates that “King” starts at index 9, etc. Use a size of 2 spaces for each of the fixed length sections, which will give you the range from 0-99. 

The first line of each page should contain two numbers separated by a comma. The first number indicates the number of attributes and the second number indicates the size each fixed offset section uses (the second number will always be 2). For example, for the example above, the line would be “3,2”. 
All directories will hold the same data, but they will be in different formats.

2. Write code that will run both in serial and in parallel to achieve the following goals. 
The second part of your code will read in the pages from one of your directories (“Fixed”, “Delimited”, “Offset”) and calculate the average value of some attribute. This part of the code is executed by running the following command 
python store_analyze.py analyze <Fixed, Delimited, Offset> <index_of_attribute> <num_processes>” 
Where:

              a. analyze tells the code that you are analyzing the data and not storing, 
              b. < Fixed, Delimited, Offset> determines which directory that you are going to analyze, 
              c. <index_of_attribute> state which attribute that you are going to calculate the average of. The first attribute in a tuple will be attribute 0, and each other attribute’s index increasing by 1 as you go from left to right. Remember, that these numeric values are stored as a string and therefore, to properly calculate the average, you need to convert the string representation to a numeric representation. 
              d. <num_processes> represents the number of processes that you will use to calculate the average. Specifically, the python package multiprocessing will create multiple processes to make the calculations more efficient. Each process will be given a page, or group of pages to read and analyze. Each process’ calculation should be used in the final mean average. 


The program will print out the mean value of the targeted attribute from the targeted directory using the indicated number of processes in the following format: 
 “<attribute_index> average: <calculated_average>” 
