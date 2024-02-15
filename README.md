Note frome the author
=====================
I dont mean to sound korny but here we are... I have so many rthings I want to share when I think about wwhy I made steamware but it doesn t wreally matter.  It was always aqbout a catalyst for kindness. Nothing more. All other reasons pail in comparison to this one. We need to be better. I need to be better. I think we can build things if we work together. I think its the only way. Talking doesnt matter unless it reflects something real. We need to begin finding wways to solve problems. We nedd to be better. We need hiugh integrety. We need free. we need freedom to roam with no exceptions for all. We need tools to coordinate and work together and I assertt this is one. This is my offering so you know I am for real when say I am part of the solution. I ask for nothing more than you adknowledge this from me. I ask for your trust and one day mabye friendship. I am in this for the *adventure* and if you are like me and you seek *adventure* then help me. If you dont know what I am saying then you need to learn to read between the lines and look deeper. Nothing is what it seems.


What is steamware?
==================

Science-technology-engineering-art-mathematics ware; (**steamware**) refers to an open source modular part family or hardware assembly language (much like legos) and the software utilities which generate them. **steamware** aims to become a fully open source defacto baseline solution for high integrity-hardware generation for 3D print or otherwise. steamware is very potent in particular in terms of a creation, constructability, deconstructability, manufactuing, maintnence quotient. The hope is that this style of manufacturing will act as a catalyst to overwhelm traditional manufacturing schools of thought and will reveal decentralized manufactured a more serious approach in the arena of manufacturing. These parts are hyper modular and carry infinite permutations that can be imagined, designed and generated on the fly (in seconds!). Also **steamware** posesses an extremely useful property known as identity-self-evidence where the configurations can be visually discerned, encoded, measured and calculated. No need for bar codes or labels! This saves alot of time.



How does steamware work?
=======================
This steamware.py script generates openscad code.

Why was it built?
=================
There were a multitude of reasons behind steamware. Check out my mupy library. steamware was built as an optimized part library after spending a while on that library.

Recursion Binding
=================
Steamware is fractal like and basis unit centric and this affects the way steamware approaches physical binding or joining of multiple elements. The shafts will often provide space for a basis unit 1/3 the size to fid. 

No Illegal Operations
=====================
Steamware was made to be utility grade, maliable, cheap and recreational. The square holes were designed to act as bolt shafts or shafts for other steamware of lower basis units. If one looks close enough all steamware currently is built from basis unit blocks with fit padding applied.

Material Independence
=====================
Steamware is a geometry, not a material (ofcourse unless you are talking 3D printing material but thats the point!) many new filiments are becoming available as time move on anyhow. 3D printing is a quickly growing field.

Can I make money off steamware?
===============================
You may sell this steamware any way you see fit! I am here to support all commerce! I am also interested in what people can create.


**bu** : Basis Unit
===============
**bu** makes reference to the 'basis-unit' and essentially defines the initial scale of the part within the track string. Specifically it makes reference to the length, width and hieght of each block unit within the **steamware** coordinate system assuming a scale modiier instruction was applied which would yield a basis unit as three times greater or one third the size. Basis-units are not physical, they are the frame in which a track-string defines a **steamware** element. The *block units* themselves are physical and derive from **basis units** but are slightly smaller due to the **fit-padding** which is subtracted however upon transitions, a coupler mesh is applied for every spatial transition instruction character in a track string so that the padding wont interfere with binding intentions. It is important to note that binding is not ensured becasue blocks are adjacent, only if there is a track string.


    $ python3 steamware.py

When you run steamware.py nothing particularly interesting happens and the generated directory will be unnamed and placed in the current directory of execution. All of the defaults are activated but with no track string entered by the user only a single basis unit block is available and it represents our primordial origin block.

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" width="600"/>
</p>
<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" width="600"/>
</p>
<em align="center" width="200">This is a block unit and is roughly the size of the basis unit but minus some padding.</em>


The basis unit defaults to 10 which is *assumed* to millimeters becasue slicing software ultimatly determines this so check your slicing configurations. Also openscad whjich this tech is built on is relies on unitless measures of space. The fit padding (~0.139) is the only clue that millimetrs were intended since in inches the fit padding would be less optimized.

    $ python3 steamware.py --en example_part --ed /home/mryan/Documents/steamware

**fp** : Fit Padding
==============
**fp** is the total amount of distance subtracted from a basis unit per block for the exterior profile and the interior shaft. Without a fit-padding it would be extrememly dificult to bind objects together, especially within a narrow shaft. The fit padding is a variable and must be set by the user to suit thier needs. A recomended starting point is a fp = 0.139 (mm) and shift from thier but this particular value is tride and tru and is set as default if not specified by user. 

**ts** : Track String
==============
The **ts** variable is the track string. Each character in the track string represents a transition from a previous block. It is for this reason there is alwasys one assumed block at the origin that needs no track character. The track string acts as an instruction to build steamware elements and express garenteed modularity. Due to the discrete cubic nature, all blocks of an identical or mathematically related basis unit have garenteed modular poroperties. The translation instruction characters are *X, Y, Z, A, B, C* which map to translations in the *( X , Y , Z , -X , -Y , -Z )* directions of euclidian space at basis unit steps. It can change scale by 1/3 or 3 depending on the scale modifyer instruction  characters: U, D

track characters
================



=============
| Spatial Transition Instructions  |  Scale Transform Instructions  |  Type Modifier Instructions  |  Special Transform Instructions | Style Modifier Instruction |
| --- | --- | --- | --- |
|   <p style="text-align: center;">A</p>    |      |      |         |     |
|   <p style="text-align: center;">B</p>    |      |      |         |     | 
|   <p style="text-align: center;">C</p>    |      |      |         |     |  
|       |      |     |   <p style="text-align: center;">D</p>       |     |
|       |      |     |        |
|       |      |        <p style="text-align: center;">F</p>   |        |    |
|       |  <p style="text-align: center;">G</p>    |     |        |      |
|       |      |      |        |        |
|       |      |      |        |        |   
|       |      |      |        |        |
|       |      |      |        |        |
|       |      |      |        |        |
|       |      |      |    <p style="text-align: center;">M</p>     |   |        |
|       |      |      |        |        |
|       |      |   <p style="text-align: center;">O</p>   |        |        |
|       |      |   <p style="text-align: center;">P</p>   |        |        |
|       |      |      |        |        |       <p style="text-align: center;">T</p>     |
|       |      |      |        |        |       <p style="text-align: center;">U</p>     |
|       |      |      |        |        |       <p style="text-align: center;">V</p>     |
|       |      |      |        |        |       <p style="text-align: center;">W</p>     |
|   <p style="text-align: center;">X</p>    |      |      |         |        |
|   <p style="text-align: center;">Y</p>    |      |      |         |        |
|   <p style="text-align: center;">Z</p>    |      |      |         |        |



**it** : Initial Type
Defaults to 'O' for open which is identical to the diagram above. 'P' is protected which is hollow but covered; for this track-string acts like a pipe extention function. 'F' is for filled and it is not hollow at all. In this case filled just means that open scad interprets a solid object. **WARNING:** The slicer may print at whastever density it wants. 

**en** : Export Name
====================
**en** is the baseline-name for the files which will be generated without specifying the extentions. They will be placed inside a directory of the same name which will be written to the **export-directory** Any generated files will have this name plus whatever extension the file requires. If left blank, **en** defaults to unnamed_steamware_<n>.

**ep** : Export Path
====================
**ep** is the path where the export will be writen too; <export_path>+'/'+<export_name> upon execution of **steamware.py**. If left blank, **ep** defaults to the current path.

Examples
========
**WARNING** All numerical values are unitless stricly speaking. This is becasue open scad operates this way. Phyical units of distance are applied afterwards with things like slicers. For this reason we say that millimeters are assumed but if you are working with inches you must reassign fit padding especially.

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="500"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="500"/>
<em>image_caption</em>
</p>fro bolts and pins but strings and wires are ok too! Even the steamware itself is material independent.


    $ python3 steamware.py --en example_part --ep \home\mryan\Documents\steamware --bu 10 --fp 0.134 --it O --ts XXSXXX


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
- Linkage Schemes
- Make robotics more acessible generally.

STEAMWARE WISHLISTS
===================
- Low density space robots
- Atomic Computers
- Wind energy circuts.
- Modular space stations.
- More pull requests.
- More parts available.
- More users who create funtioning businesses or operations.
- New frameworks for technology development.