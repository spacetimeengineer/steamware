**WARNING** : Steamware is about ready to go. There are some features that are not in yet (marked by a *) but its working good. You will happy with what we got so far I think. This entire repo needs work including the README.md but this isn't my day job and the parts themselves are stable. Script is stable as far as I can tell but you could break it if you tried. Just a script not a library yet but check it out if you want. 

**WARNING** Never 3D print with supports!

**WARNING** Assume millimeters but all numbers are unit-less. Slicers determine units generally.!



### *What is steamware?*
Lets be clear from the start, **Steamware is fun and cool, they are toys, tools and utilities all at the same time!** Now that we have that covered lets talk serious because this is a serious technology. Science-technology-engineering-art-mathematics ware; (**steamware**) refers to an open source modular part family or hardware assembly language (much like Legos) and the software utilities which generate them. **steamware** aims to become a fully open source defacto baseline solution for high integrity-hardware generation for 3D print or otherwise. **Steamware** is very potent in particular in terms of a creation, constructability, de-constructability, manufacturing, maintenance quotient. The hope is that this style of manufacturing will act as a catalyst to overwhelm traditional manufacturing schools of thought and will reveal decentralized manufactured a more serious approach in the arena of manufacturing. These parts are hyper modular and carry infinite permutations that can be imagined, designed and generated on the fly (in seconds!). 


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/steamware_picture_0.jpg" width="300"/>
</p>


### *How does steamware work?*
This steamware.py script generates openscad code, .stl renderings, images and metadata so the user has the resources to modify, showcase or manufacture the steamware element.

### *Why was it built?*
I thought it would be good for kids. In some part it was a cost-reduction play. An ode to open source. Something about data compression I think and OOOOooo robots and wind energy once the gears are built into steamware. Housing and spaceships and a replacement for cardboard. Also check out the mupy library if you really want to know how nuts I am. There were a lot of reasons behind Steamware. Maybe you can help find new ones.

### Self-Evident Identity*
**Steamware** possesses an extremely useful property known as self-evident-identity where the configurations can be visually discerned, encoded, measured and calculated. No need for bar codes or labels! In fact parts can be designed or imagined in your head and on the fly.

### Super Binding
**Steamware** is fractal like and basis unit centric and this affects the way steamware approaches physical binding or joining of multiple elements. The shafts will often provide space for a basis unit 1/3 the size to fit. Binding is principally joinery based but there are other forms of binding such as bolt or string binding. There can be design binding which is a bind that works by some part being *designed* for some other.

### No Illegal Operations
**Steamware** was made to be utility grade, mailable, cheap and recreational. The square holes were designed to act as bolt shafts or shafts for other steamware of lower basis units or whatever... If one looks close enough all steamware is built from basis unit blocks with fit padding applied.

### Material Independence
Steamware is a geometry, not a material so we are limited to what 3D printers or otherwise could offer. I would argue that with these parts you could at-least get things started! 

### *Can I make money off steamware?*
Sure! but your better off adding your own flavor to it. It is about creation and steamware is just step in the right direction. I am here to support all commerce! I am also interested in what people can create!


## Installation :

The steamware.py script can run without any dependencies but the scripts which it generates do require an an openscad instance to view/render/photograph Steamware.

On Linux :

    $ sudo apt-get install openscad

If you are using Windows or MacOS go to :  https://openscad.org/downloads.html


## **bu** : Basis Unit
The **bu** variable makes reference to the 'basis-unit' and essentially defines the initial scale of the part within the track string. Specifically it makes reference to the length, width and height of each block unit within the **steamware** coordinate system assuming a scale modiier instruction was applied which would yield a basis unit as three times greater or one third the size. Basis-units are not physical, they are the frame in which a track-string defines a **steamware** element. The *block units* themselves are physical and derive from **basis units** but are slightly smaller due to the **fit-padding** which is subtracted however upon transitions, a coupler mesh is applied for every spatial transition instruction character in a track string so that the padding wont interfere with binding intentions. It is important to note that binding is not ensured because blocks are adjacent, only if there is a track string.


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" width="600"/>
</p>
<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" width="600"/>
</p>
<em align="center" width="200">This is a block unit and is roughly the size of the basis unit but minus some padding.</em>


The basis unit defaults to 10 which is *assumed* to millimeters because slicing software ultimately determines this so check your slicing configurations. Also *openscad* which this tech is built on is relies on unit-less measures of space. The fit padding (~0.139) is the only clue that millimeters were intended since in inches the fit padding would be less optimized.

 
## **fp** : Fit Padding

The **fp** variable is the total amount of distance subtracted from a basis unit per block for the exterior profile and the interior shaft. Without a fit-padding it would be extremely difficult to bind objects together, especially within a narrow shaft. The fit padding is a variable and must be set by the user to suit their needs. A recommended starting point is a ***fp = 0.139 (mm)*** and shift from their but this particular value is tried and tru and is set as default if not specified by user. Defaults to ***fp = 0.139 (mm)***. ***WARNING*** make sure your slicer is set to mm!

## **ts** : Track String
The **ts** variable is the track string. Each transition character in the track string represents a transition from a previous block. It is for this reason there is always one assumed block at the origin that needs no track character. The track string acts as an instruction to build steamware elements and grantee modularity. Due to the discrete cubic nature, all blocks of an identical or mathematically related basis unit express modular properties. The translation instruction characters are *(X, Y, Z, A, B, C)* which map to translations in the *( X , Y , Z , -X , -Y , -Z )* directions of euclidean space in basis unit steps. The basis unit can change scale by **1/3** or **3** along the track if the scale modifier instruction characters *'S'(Shrink)* or  *'G' (Grow)* are invoked respectively. Next we have style modification characters *(T, U, V, W)* which respectively map to four separate styles : *(fully cropped)* , *(fully uncropped)*, *(edges cropped / uncropped corners)* and *(cropped corners / uncropped edges)*.




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
Defaults to 'O' for open which is identical to the diagram above. 'P' is protected which is hollow but covered; for this track-string acts like a pipe extension function. 'F' is for filled/full and it is not hollow at all. In this case filled just means that open scad interprets a solid object. **WARNING:** The slicer may print at whatever density the user sets it at. 

## **en** : Export Name

The **en** variable is the baseline-name for the files which will be generated without specifying the extensions. They will be placed inside a directory of the same name which will be written to the **export-directory** Any generated files will have this name plus whatever extension the file requires. If left blank, **en** defaults to unnamed_steamware_<n>.

## **ed** : Export Directory

The **ed** variable is the path where the export will be writen too; <export_path>+'/'+<export_name> upon execution of **steamware.py**. If left blank, **ep** defaults to the current path.

## Examples

**WARNING** All numerical values are unit-less strictly speaking. This is because open scad operates this way. Physical units of distance are applied afterwards with things like slicers. For this reason we say that millimeters are assumed but if you are working with inches you must reassign fit padding especially.


### Example 1 : Just an example part

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="500"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="500"/>
<em></em>
</p>


    $ python3 steamware.py --en example_part --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --mt O --ts XXSXXX

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/example_part.png#gh-dark-mode-only" width="1000"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/example_part.png#gh-light-mode-only" width="1000"/>
<em></em>
</p>

### Example 2 : A (strange) dougnut shape. 

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1D.png#gh-dark-mode-only" width="625"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1L.png#gh-light-mode-only" width="625"/>
</p>

    $ python3 steamware.py --en dougnut --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --mt O --ts XXXBBAAAYY


<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/dougnut.png#gh-dark-mode-only" width="1000"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/dougnut.png#gh-light-mode-only" width="1000"/>
</p>

### Example 3 : A cross-like shape. 

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2D.png#gh-dark-mode-only" width="625"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2L.png#gh-light-mode-only" width="625"/>
</p>

    $ python3 steamware.py --en cross --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --ts XXXXAAYYBBBB

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/cross.png#gh-dark-mode-only" width="1000"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/cross.png#gh-light-mode-only" width="1000"/>
</p>


Each Call creates an .scad file, .stl file* and a a .png* file of the same filename.


### FUTURE OF STEAMWARE
- Power Transmission
    - Gears (modular) / Snap In
    - Gearboxes (modular) / Snap In
- Computer Housing / General Housing
    - Housing track string constructor algorithms.
- 3D Printed Bearings / Embedded in steamware
- Mechanical Linkage Schemes / New Generation Scripts
- Make robotics more accessible generally.
- Integrate with mupy *POSSIBLY*

### STEAMWARE WISHLISTS
- Low density space robots
- Atomic Computers
- Wind energy circuits.
- Differential circuits.
- Modular space stations.
- More pull requests.
- More parts available.
- More users who create functioning businesses or operations.
- New frameworks for technology development.
