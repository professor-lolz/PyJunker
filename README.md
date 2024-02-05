# PyJunker
Python Junker, which generates useless functions, disguises basic functions as generated ones

## Usage:
```bash
python3 PyJunker.py -f [input_file] -o [output_file] -c [count]
```
```-f/--input_file``` - Source .py file to be protected

```-o/--output_file``` - The output file that will be created and where the protected code will be saved

```-c/--count``` - The total number of fake functions that will be generated.

## What is PyJunker for?
PyJunker protects your .py file by creating many fake functions, masking the main ones. This method has proven to work well as protection against function dumps (at the test stage - the injection failed with an error)

![BeforeAndAfter](https://github.com/professor-lolz/PyJunker/blob/main/imgs/present_list.png)
