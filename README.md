*Note from the author*

This is an extremely potent technology. Ill leave it at that. Built it for kids, adults and robots. I want it simple and I want it free and I want to reinvest the value of this tech into itself and the benefits go to us all. Be a builder. DO with these what YOU want. 





What is STEAMWare?
==================

STEAMWare refers to a modular part family and the software utility which generates them. It is open source. It is LE



fn : File Name(s)
=================
fn is the baseline-name for the files which will be generated without the extention. Any generated files will have this name plus whatever extension the file requires.

bu : Basis Unit
===============
bu is just the name of the files which will be generated without the extention. Any generated files will have this name plus whatever extension it requires.

<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" />
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" />

fp : Fit Padding
==============
fp is the total amount of distance subtracted from a basis unit per block for the exterior profile and the interior shaft. Without a fit-padding it would be extrememly dificult to bind objects together, especially within a narrow shaft. The fit padding is a variable and must be set by the user to suit thier needs. A recomended starting point is a fp = 0.139 (mm) and shift from thier but this particular value is tride and tru and is set as default if not specified by user. 

ts : Track String
==============
ts is the track string. It is an instruction which builds objects wwith ensured modularity. Due to the discrete cubic nature, All blocks of an identical or mathematically reklated basis unit have garenteed modular poroperties. It uses Translation Instruction X, Y, Z, A, B, C Scale Modifyer Instruction U, D, and Type Modifies Instruction.




<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" />
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" />
Examples:

    $ python3 sw.py --fn donught --bu 10 --fp 0.134 --ts XYABBBBBZCZZZZZ




Each Call creates an .scad file, .stl file and a a .png file of the same filename.


