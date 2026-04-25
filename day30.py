'''File Handling:
----------------
-->File handler is an object of file to maintain several functions of file such as creating,
reading,writing, and update also deleting the file.

How to open a file:
------------------
1. open():
---------
-->This open() function take 2 parameters and inthis we have to close the file by calling
close() function after program..
(i)file name, (ii)mode
2. with open():
--------------

Modes("r","w","a","x","t"):
-----
1."r"--read--To read the file we will use this mode and if no file it will through error.
___________________________________________________________________________________________
2."w"--write--To write the text into the file we will use this mode and it will create
the file if it doesn't exist.
___________________________________________________________________________________________
3."a"--append--To add the text into the file this is used and it will create the file if
it doesn't exist
'''
any = open("demo.txt","a")
any.write("this is line 4")
any.close()
