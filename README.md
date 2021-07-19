# redhat-task

## Author
Andrey Grigorenko

## Usage
```python
#Usage will print
python3 RedHatTask.py

#Script will search for pattern abc in input from STDIN
python3 RedHatTask.py -r abc

#Script will search for pattern abc in all files with extension .txt
python3 RedHatTask.py -r abc *.txt

#Script will search for pattern abc in all files with extension .txt and color matched pattern with provided color
python3 RedHatTask.py -r abc *.txt -c red

#Script will search for pattern abc in all files with extension .txt and color matched pattern with provided color and underline it
python3 RedHatTask.py -r abc *.txt -c red -u underline

#Script will search for pattern abc in all files with extension .txt and print it in the following format
python3 RedHatTask.py -r abc *.txt -c red -u underline -m True
	file.name:line number:start index:matched string
	text.txt :  2  : 0 : abc
	
```