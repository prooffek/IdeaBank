# Ideabank

## Story

You have a brilliant mind and you come up with better and better ideas every day.
The problem is, you would forget them quickly, so you decided to write a script that
helps you keep track of them.

## What are you going to learn?

- use loops
- ask for user input
- work with files
- use command line arguments
- handle errors

## Tasks

1. Create a program in which you can add ideas and it lists them after addition.
    - The program asks for a new idea with printing out the phrase `What is your new idea?` until the user exit with `Ctrl+C`
    - After adding a new idea the list of the ideas is printed out with leading numbers (e.g. `1. first idea`)
    - If the user restarts the program, the ideas added earlier still remain

2. Add the option to list all the existing ideas without adding a new one with command line argument `--list`.
    - Calling the program with the command line argument `--list` prints out the list of the ideas with leading numbers (e.g. `1. first idea`)
    - Giving more command line arguments is ignored by the program

3. Add an option to remove an idea by the leading number. Use console arguments like `--delete 2`.
    - Calling the program with the command line argument `--delete` and a number deletes the idea corresponding to the number and prints out the list of the ideas with leading numbers (e.g. `1. first idea`)
    - Not giving any arguments after the `--delete` argument prints out the error message `Specify a number after --delete`
    - Giving non-number arguments after the `--delete` argument prints out the error message `Specify a number after --delete`
    - Giving more command line arguments is ignored by the program

## General requirements

None

## Hints

- Use a txt file to save data in order to have the ideas after restart as well.
- For deleting an idea you probably want to use some data structure in your program :)


## Starting your project



## Background materials

- <i class="far fa-exclamation"></i> [Strings](project/curriculum/materials/pages/python/strings.md)
- <i class="far fa-exclamation"></i> [Control structures](project/curriculum/materials/pages/python/control-structures.md)
- <i class="far fa-exclamation"></i> [Functions](project/curriculum/materials/pages/python/functions.md)
- <i class="far fa-exclamation"></i> [Tutorial about command line arguments in Python](https://www.pythonforbeginners.com/system/python-sys-argv)
- <i class="far fa-exclamation"></i> [Error handling in Python](https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html)

