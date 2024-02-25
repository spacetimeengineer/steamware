

### *What is steamware?*
Lets be clear from the start, steamware is fun and cool, they are toys, tools and utilities all at the same time. Now that we have that covered lets talk serious becasue this is a serious technology. Science-technology-engineering-art-mathematics ware; (**steamware**) refers to an open source modular part family or hardware assembly language (much like legos) and the software utilities which generate them. **steamware** aims to become a fully open source defacto baseline solution for high integrity-hardware generation for 3D print or otherwise. steamware is very potent in particular in terms of a creation, constructability, deconstructability, manufactuing, maintnence quotient. The hope is that this style of manufacturing will act as a catalyst to overwhelm traditional manufacturing schools of thought and will reveal decentralized manufactured a more serious approach in the arena of manufacturing. These parts are hyper modular and carry infinite permutations that can be imagined, designed and generated on the fly (in seconds!). 


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/steamware_picture_0.jpg" width="300"/>
</p>


### *Self-Evidence Element Identity*
**Steamware** posesses an extremely useful property known as identity-self-evidence where the configurations can be visually discerned, encoded, measured and calculated. No need for bar codes or labels! Infact parts can be designed or imagined in your head and on the fly.

### *How does steamware work?*
This steamware.py script generates openscad code, .stl renderings, images and metadata so the user has the resources to modify, showcase or manufacture the steamware element.

### *Why was it built?*
I thought it would be good for kids. In some part it was a cost-reduction play. An ode to open source. There were alot of reasons behind steamware but when the track string concept clicked I thought it was worth building.

 ### Super Binding
Steamware is fractal like and basis unit centric and this affects the way steamware approaches physical binding or joining of multiple elements. The shafts will often provide space for a basis unit 1/3 the size to fit. 

### No Illegal Operations
Steamware was made to be utility grade, maliable, cheap and recreational. The square holes were designed to act as bolt shafts or shafts for other steamware of lower basis units or whatever... If one looks close enough all steamware is built from basis unit blocks with fit padding applied.

### Material Independence
Steamware is a geometry, not a material (ofcourse unless you are talking 3D printing material but thats the point!) many new filiments are becoming available as time move on anyhow. 3D printing is a quickly growing field.

### *Can I make money off steamware?*
Sure! but your better off adding your own flavor to it. It is about creation and steamware is just step in the right direction. I am here to support all commerce! I am also interested in what people can create!


## **bu** : Basis Unit
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
 
## **fp** : Fit Padding

**fp** is the total amount of distance subtracted from a basis unit per block for the exterior profile and the interior shaft. Without a fit-padding it would be extrememly dificult to bind objects together, especially within a narrow shaft. The fit padding is a variable and must be set by the user to suit thier needs. A recomended starting point is a ***fp = 0.139 (mm)*** and shift from thier but this particular value is tride and tru and is set as default if not specified by user. Defaults to ***fp = 0.139 (mm)***. ***WARNING*** make sure your slicer is set to mm!

## **ts** : Track String
The **ts** variable is the track string. Each transition character in the track string represents a transition from a previous block. It is for this reason there is alwasys one assumed block at the origin that needs no track character. The track string acts as an instruction to build steamware elements and garentee modularity. Due to the discrete cubic nature, all blocks of an identical or mathematically related basis unit express modular poroperties. The translation instruction characters are *(X, Y, Z, A, B, C)* which map to translations in the *( X , Y , Z , -X , -Y , -Z )* directions of euclidian space in basis unit steps. The basis unit can change scale by **1/3** or **3** along the track if the scale modifier instruction characters *'S'(Shrink)* or  *'G' (Grow)* are invoked respectively. Next we have style modification characters *(T, U, V, W)* which respectively map to four separate styles : *(fully cropped)* , *(fully uncropped)*, *(edges cropped / uncropped corners)* and *(cropped corners / uncropped edges)*.




### Track Characters


Track Character | Spatial Transition Instructions  |  Scale Transform Instructions  |  Type Modifier Instructions  |  Special Transform Instructions | Style Modifier Instruction |
| :-----: | :-------------------------: | :----------------: | :-------------: | :-----------: | :-----: |
|    A    |    -x translation : 1 bu    |                    |                 |               |         |
|    B    |    -y translation : 1 bu    |                    |                 |               |         |
|    C    |    -z translation : 1 bu    |                    |                 |               |         |
|    D    |                             |                    |                 |     divide*   |         |
|    E    |                             |                    |                 |               |         |
|    F    |                             |                    |     filled(Currently 'S')      |               |         |
|    G    |                             |   grow bu x 3      |                 |               |         |
|    H    |                             |                    |                 |               |         |
|    I    |                             |                    |                 |               |         |   
|    J    |                             |                    |                 |               |         |
|    K    |                             |                    |                 |               |         |
|    L    |                             |                    |                 |               |         |
|    M    |                             |                    |                 |    multiply*  |         | 
|    N    |                             |                    |                 |               |         |
|    O    |                             |                    |      open       |               |         |
|    P    |                             |                    |    protected*   |               |         |
|    Q    |                             |                    |                 |               |         |
|    R    |                             |                    |                 |               |         |
|    S    |                             |  shrink bu ÷ 3     |                 |               |         |
|    T    |                             |                    |                 |               |      fully cropped*     |
|    U    |                             |                    |                 |               |     fully uncropped*    |
|    V    |                             |                    |                 |               |    (edges cropped / uncropped corners)*    |
|    W    |                             |                    |                 |               |    (cropped corners / uncropped edges)*    |
|    X    |    x translation : 1 bu     |                    |                 |               |         |
|    Y    |    y translation : 1 bu     |                    |                 |               |         |
|    Z    |    z translation : 1 bu     |                    |                 |               |         |



## **mt** : Mass Type
Defaults to 'O' for open which is identical to the diagram above. 'P' is protected which is hollow but covered; for this track-string acts like a pipe extention function. 'F' is for filled and it is not hollow at all. In this case filled just means that open scad interprets a solid object. **WARNING:** The slicer may print at whastever density it wants. 

## **en** : Export Name

**en** is the baseline-name for the files which will be generated without specifying the extentions. They will be placed inside a directory of the same name which will be written to the **export-directory** Any generated files will have this name plus whatever extension the file requires. If left blank, **en** defaults to unnamed_steamware_<n>.

## **ep** : Export Path

**ep** is the path where the export will be writen too; <export_path>+'/'+<export_name> upon execution of **steamware.py**. If left blank, **ep** defaults to the current path.

## Examples

**WARNING** All numerical values are unitless stricly speaking. This is becasue open scad operates this way. Phyical units of distance are applied afterwards with things like slicers. For this reason we say that millimeters are assumed but if you are working with inches you must reassign fit padding especially.

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="500"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="500"/>
<em>image_caption</em>
</p>


    $ python3 steamware.py --en example_part --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --mt O --ts XXSXXX

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/example_part.png#gh-dark-mode-only" width="500"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/example_part.png#gh-light-mode-only" width="500"/>
<em>image_caption</em>
</p>


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/dougnut.png#gh-dark-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/dougnut.png#gh-light-mode-only" width="600"/>
</p>

    $ python3 steamware.py --en dougnut --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --mt O --ts XXXBBAAAYY

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2D.png#gh-dark-mode-only" width="625"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2L.png#gh-light-mode-only" width="625"/>
</p>

    $ python3 steamware.py --en cross --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --ts XXXXAAYYBBBB

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/cross.png#gh-dark-mode-only" width="600"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/cross.png#gh-light-mode-only" width="600"/>
</p>
Each Call creates an .scad file, .stl file and a a .png file of the same filename.


### FUTURE OF STEAMWARE
- Power Transmission
    - Gears (modular) / Snap In
    - Gearboxes (modular) / Snap In
- Computer Housing / General Housing
    - Housing track string constructor algorithms.
- 3D Printed Bearings / Embedded in steamware
- Mechanical Linkage Schemes / New Genberation Scripts
- Make robotics more acessible generally.
- Integrate with mupy *POSSIBLY*

### STEAMWARE WISHLISTS
- Low density space robots
- Atomic Computers
- Wind energy circuts.
- Differential circuts.
- Modular space stations.
- More pull requests.
- More parts available.
- More users who create funtioning businesses or operations.
- New frameworks for technology development.