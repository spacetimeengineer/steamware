# STEAMWare
Hardware Assembly Language
STEAMWare ( Science - Technology - Engineering - Art - Mathematics ) - Ware




*Note from the author*

This is an extremely potent technology. Ill leave it at that. Built it for kids, adults and robots. I want it simple and I want it free and I want to reinvest the value of this tech into itself and the benefits go to us all. Be a builder. DO with these what YOU want. 





What is STEAMWare?
==================

In short, STEAMWare refers to a new (LEGO-like) modular part family and the open-source software utility which generates them.

<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" width="700" />
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" width="700" />
    

Instructions
============

fn : File Name
==============
This is just the name of the files which will be generated without the extention. Any generated files will have this name plus whatever extension it requires.

bu : Basis Unit
===============
This is just the name of the files which will be generated without the extention. Any generated files will have this name plus whatever extension it requires.

fn : Fit Padding
==============
This is the total amount of distance subtracted from a basis unit per block across one dimension. This variable ensures variability so that joinery can be loose or tight. 

ts : Track String
==============
This is the definition of a track. It uses Translation Instruction X, Y, Z, A, B, C Scale Modifyer Instruction U, D, and Type Modifies Instruction

<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="1000" />
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="1000" />
Examples:

    $ python3 sw.py --fn donught --bu 10 --fp 0.134 --ts XYABBBBBZCZZZZZ

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)

    $ python3 sw.py --fn donught --basis_unit 10 --fit_padding 0.134 --track_string XXX

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)

    $ python3 sw.py --fn donught --basis_unit 10 --fit_padding 0.134 --track_string XXXZ

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)




Each Call creates an .scad file, .stl file and a a .png file of the same filename.


