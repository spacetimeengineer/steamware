*Note from the author*

STEAMWare is a potent technology built for reasons difficult to explain. It can be very useful.




What is STEAMWare?
==================

STEAMWare refers to an open source modular part family and the software utilities which generates them. STEAMWare aims to make a fully open source baseline solution for high integrity-hardware generation for 3D print or otherwise. The hope of the author that this style of manufacturing will overwhelm traditional manufacturing schools of thought. These parts are hyper modular and carry infinite permutations wehich can be designed and generated on the fly. STEAMWare has a very useful property where the configurations can be visually discerned or mentally encoded. This makes labeling with an infinite permutation set a non-issue.

You may think of STEAMWare as in many ways similar to the LEGO company except a few key differences.

STEAMWare is not a company but a repository which provides free parts. The only cost is the material for 3D prining or otherwise and the energy needeed to make it. The desing and labeling component is taken care of from the outset.

LEGO provides parts that they manufacturte and it is not legal to manufacture LEGOs yourself and it in any event is not appreciated by the LEGO company.


STEAMWare provides infinite parts and all with garenteed modular properties.

STEAMWare is a python s ript which builds openSCAD files that point to parts.


fn : File Name(s)
=================
'fn' is the baseline-name for the files which will be generated without the extention. Any generated files will have this name plus whatever extension the file requires.

bu : Basis Unit
===============
'bu' makes reference to the 'basis-unit' and essentially defines the initial scale of the part within the track string. Specifically it makes reference to the length, width and hieght of each block unit within the STEAMWare coordinate system. Basis-units are not physical, they are the frame in which track strings define a STEAMWare element. The block units themselves are physical and derive from basis units but are slightly smaller due to the padding which is subtracted however a coupler mesh is applied for every character in a track string so that said padding wont undermine binding intentions. It is important to note that binding is not ensured becasue blocks are adjacent. Binding is only applied for each character in the track string. 

<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" width="600"/>

fp : Fit Padding
==============
fp is the total amount of distance subtracted from a basis unit per block for the exterior profile and the interior shaft. Without a fit-padding it would be extrememly dificult to bind objects together, especially within a narrow shaft. The fit padding is a variable and must be set by the user to suit thier needs. A recomended starting point is a fp = 0.139 (mm) and shift from thier but this particular value is tride and tru and is set as default if not specified by user. 

ts : Track String
==============
The 'ts' variable is the track string. Each character in the track string represents a transition from a previous block. It is for this reason there is alwasys one assumed block at the origin that needs no track character. The track string acts as an instruction to build steamware elements and express garenteed modularity. Due to the discrete cubic nature, all blocks of an identical or mathematically related basis unit have garenteed modular poroperties. The translation instruction characters are X, Y, Z, A, B, C which map to translations in the ( X , Y , Z , -X , -Y , -Z ) directions of euclidian space at basis unit steps. It can change scale by 1/3 or 3 depending on the scale modifyer instruction  characters: U, D



, and Type Modifies Instruction.




<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="600"/>

    $ python3 sw.py --fn example_part --bu 10 --fp 0.134 --ts XXDXXX

<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1D.png#gh-dark-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1L.png#gh-light-mode-only" width="600"/>

    $ python3 sw.py --fn donught --bu 10 --fp 0.134 --ts XXXBBAAAYY

<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2D.png#gh-dark-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2L.png#gh-light-mode-only" width="600"/>

    $ python3 sw.py --fn cross --bu 10 --fp 0.134 --ts XXXXAAYYBBBB


Each Call creates an .scad file, .stl file and a a .png file of the same filename.


FUTURE OF STEAMWARE
===================
- Modular Gearboxes / Modular Differentials
- Modular Gears.
- Algorithms that build modular housing for any kind of part. Motors, PCBs, Computers, Devices, Ect, Wires.
- Housing for well known parts.