*Note from the author*

Steamware is a potent technology. 




What is STEAMWare?
==================

**steamware** refers to an open source modular part family and the software utilities which generates them. STEAMWare aims to make a fully open source baseline solution for high integrity-hardware generation for 3D print or otherwise. The hope of the author that this style of manufacturing will overwhelm traditional manufacturing schools of thought. These parts are hyper modular and carry infinite permutations wehich can be designed and generated on the fly. **steamware** has a very useful property where the configurations can be visually discerned or mentally encoded. This makes labeling with an infinite permutation set a non-issue.

You may think of **steamware** as in many ways similar to the LEGO company except a few key differences.

**steamware** is not a company but a repository which provides free parts. The only cost is the material for 3D prining or otherwise and the energy needeed to make it. The desing and labeling component is taken care of from the outset.

LEGO provides parts that they manufacturte and it is not legal to manufacture LEGOs yourself and it in any event is not appreciated by the LEGO company.


**steamware** provides infinite parts and all with garenteed modular properties.

**steamware** is a python s ript which builds openSCAD files that point to parts.

How does Steameare work?
=======================
This steamware.py script generates openscad code.

Why was it built?
=================
There were a multitude of reasons behind steamware. Check out my mupy library. steamware was built as an optimized part library after spending a while on that library.

Recursion Binding
=================

No Illegal Operations
=====================
Steamware was made to be useful and maliable. The holes wer designed fro bolts and pins but strings and wires are ok too! Even the steamware itself is material independent.

Material Independence
=====================
Steamware is geometry, not material ofcourse unless you are talking 3D printing material but thats the point! many new filiments are becoming available as time move on. 3D printing is a quickly growing field.


**fn** : File Name(s)
=================
**fn** is the baseline-name for the files which will be generated without the extention. Any generated files will have this name plus whatever extension the file requires.

**bu** : Basis Unit
===============
**bu** makes reference to the 'basis-unit' and essentially defines the initial scale of the part within the track string. Specifically it makes reference to the length, width and hieght of each block unit within the STEAMWare coordinate system. Basis-units are not physical, they are the frame in which track strings define a STEAMWare element. The block units themselves are physical and derive from basis units but are slightly smaller due to the padding which is subtracted however a coupler mesh is applied for every character in a track string so that said padding wont undermine binding intentions. It is important to note that binding is not ensured becasue blocks are adjacent. Binding is only applied for each character in the track string. 

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" width="600"/>
</p>
<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" width="600"/>
</p>
<em align="center">This is a block unit and is roughly the size of the basis unit but minus some padding.</em>

**fp** : Fit Padding
==============
**fp** is the total amount of distance subtracted from a basis unit per block for the exterior profile and the interior shaft. Without a fit-padding it would be extrememly dificult to bind objects together, especially within a narrow shaft. The fit padding is a variable and must be set by the user to suit thier needs. A recomended starting point is a fp = 0.139 (mm) and shift from thier but this particular value is tride and tru and is set as default if not specified by user. 

**ts** : Track String
==============
The **ts** variable is the track string. Each character in the track string represents a transition from a previous block. It is for this reason there is alwasys one assumed block at the origin that needs no track character. The track string acts as an instruction to build steamware elements and express garenteed modularity. Due to the discrete cubic nature, all blocks of an identical or mathematically related basis unit have garenteed modular poroperties. The translation instruction characters are *X, Y, Z, A, B, C* which map to translations in the *( X , Y , Z , -X , -Y , -Z )* directions of euclidian space at basis unit steps. It can change scale by 1/3 or 3 depending on the scale modifyer instruction  characters: U, D




<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="500"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="500"/>
<em>image_caption</em>
</p>


    $ python3 steamware.py --fn example_part --bu 10 --fp 0.134 --ts XXDXXX


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1D.png#gh-dark-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1L.png#gh-light-mode-only" width="600"/>
</p>

    $ python3 steamware.py --fn donught --bu 10 --fp 0.134 --ts XXXBBAAAYY


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2D.png#gh-dark-mode-only" width="625"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2L.png#gh-light-mode-only" width="625"/>
</p>

    $ python3 steamware.py --fn cross --bu 10 --fp 0.134 --ts XXXXAAYYBBBB


Each Call creates an .scad file, .stl file and a a .png file of the same filename.


FUTURE OF STEAMWARE
===================
- Power Transmission
    - Gears (modular) / Snap In
    - Gearboxes (modular) / Snap In
- Computer Housing
    - Housing track string constructor algorithms.
- 3D Printed Bearings / Embedded in steamware