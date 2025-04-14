## Important Warnings

- **WARNING:** Steamware is functional but still under development. Some features (marked with a `*`) are not yet implemented. While the parts themselves are stable, the script is not fully stable and may break if misused. Follow the instructions carefully for the best results.
- **WARNING:** Never 3D print with supports!
- **WARNING:** All numerical values are unit-less. Millimeters are assumed, but slicers ultimately determine the units.

---

## What is Steamware?

**Steamware** stands for **Science-Technology-Engineering-Art-Mathematics ware**. It is an open-source modular part family and hardware assembly language, much like Legos, combined with software utilities to generate them. Steamware aims to become a baseline solution for high-integrity hardware generation for 3D printing and beyond. 

Steamware is designed to be:
- Fun and creative (toys, tools, and utilities all in one).
- Modular, with infinite permutations that can be imagined, designed, and generated in seconds.
- A catalyst for decentralized manufacturing, challenging traditional approaches.

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/steamware_picture_0.jpg" width="300"/>
</p>

---

## How Does Steamware Work?

The `steamware.py` script generates:
- OpenSCAD code.
- STL renderings.
- Images and metadata.

These resources allow users to modify, showcase, or manufacture Steamware elements.

---

## Why Was Steamware Built?

Steamware was created with several goals in mind:
- To inspire creativity in kids.
- To reduce costs and promote open-source solutions.
- To explore applications in robotics, wind energy, housing, and even space exploration.
- To replace traditional materials like cardboard with modular, reusable parts.

---

## Key Features

### Self-Evident Identity
Steamware parts have a property called **self-evident identity**, meaning their configurations can be visually discerned, encoded, measured, and calculated without the need for barcodes or labels. Parts can even be designed mentally and on the fly.

### Super Binding
Steamware uses a fractal-like, basis-unit-centric approach to physical binding. Shafts often accommodate smaller basis units (1/3 the size). Binding methods include:
- Joinery-based binding.
- Bolt or string binding.
- Design-specific binding.

### No Illegal Operations
Steamware is designed to be utility-grade, versatile, and cost-effective. Square holes can act as bolt shafts, accommodate smaller basis units, or serve other purposes. All parts are built from basis unit blocks with fit padding applied.

### Material Independence
Steamware is a geometry, not a material. While limited by the capabilities of 3D printers, it provides a starting point for countless applications.

---

## Can I Make Money with Steamware?

Absolutely! Steamware is open-source, and you are free to use it commercially. Adding your own unique touch is encouraged. Steamware is about fostering creativity and innovation, and the possibilities are endless.

## Installation

The `steamware.py` script runs without dependencies, but the generated scripts require an OpenSCAD instance to view, render, or photograph Steamware.

### On Linux

Install OpenSCAD using the following command:

```bash
$ sudo apt-get install openscad
```

### On Windows or macOS

Download OpenSCAD from [https://openscad.org/downloads.html](https://openscad.org/downloads.html).

---

## **bu**: Basis Unit

The **bu** variable defines the initial scale of the part within the track string. It represents the length, width, and height of each block unit in the Steamware coordinate system. Basis units are not physical but serve as a reference frame for defining Steamware elements. 

Block units, derived from basis units, are slightly smaller due to **fit padding**. Coupler meshes are applied for every spatial transition instruction in a track string to ensure padding does not interfere with binding. Note that adjacency of blocks does not guarantee binding unless specified by a track string.

The default basis unit is `10`, assumed to be in millimeters. However, slicing software ultimately determines the units, so check your slicer configurations. OpenSCAD operates with unit-less measures, but the default fit padding (~0.139) suggests millimeters were intended.

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0L.png#gh-light-mode-only" width="600"/>
</p>
<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/legend_0D.png#gh-dark-mode-only" width="600"/>
</p>
<em align="center" width="200">This is a block unit, roughly the size of the basis unit minus padding.</em>

---

## **fp**: Fit Padding

The **fp** variable specifies the distance subtracted from a basis unit per block for the exterior profile and interior shaft. Fit padding ensures proper binding of objects, especially within narrow shafts. 

A recommended starting value is `fp = 0.139 (mm)`, which is the default if not specified. Adjust as needed for your requirements. **WARNING:** Ensure your slicer is set to millimeters for accurate results.

---

## **ts**: Track String

The **ts** variable represents the track string, where each character defines a transition from the previous block. The track string begins with an assumed block at the origin, requiring no transition character. 

### Transition Characters
- **X, Y, Z**: Translate in the positive X, Y, Z directions.
- **A, B, C**: Translate in the negative X, Y, Z directions.

### Scale Modifier Characters
- **S**: Shrink (1/3 the size).
- **G**: Grow (3 times the size).

### Style Modifier Characters
- **T**: Fully cropped.
- **U**: Fully uncropped.
- **V**: Edges cropped, uncropped corners.
- **W**: Cropped corners, uncropped edges.

The track string acts as an instruction set to build Steamware elements while ensuring modularity. Due to the discrete cubic nature, all blocks of identical or mathematically related basis units exhibit modular properties.




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



## **mt**: Mass Type

The **mt** variable defines the mass type of the part:
- **O**: Open (default). Identical to the diagram above.
- **P**: Protected. Hollow but covered, acting like a pipe extension.
- **F**: Filled. Solid with no hollow sections. **WARNING:** The slicer may print at the density set by the user.

## **en**: Export Name

The **en** variable specifies the base name for generated files (excluding extensions). Files are placed in a directory named after this variable. If left blank, **en** defaults to `unnamed_steamware_<n>`.

## **ed**: Export Directory

The **ed** variable defines the path where exports are saved: `<export_path>/<export_name>`. If left blank, **ed** defaults to the current directory.

## Examples

**WARNING:** All numerical values are unit-less. OpenSCAD operates without units, so physical units (e.g., millimeters) are applied later using slicers. If working in inches, adjust fit padding accordingly.

### Example 1: Basic Part

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0D.png#gh-dark-mode-only" width="500"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_0L.png#gh-light-mode-only" width="500"/>
</p>

```bash
$ python3 steamware.py --en example_part --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --mt O --ts XXSXXX
```

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/example_part.png#gh-dark-mode-only" width="1000"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/example_part.png#gh-light-mode-only" width="1000"/>
</p>

### Example 2: Doughnut Shape

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1D.png#gh-dark-mode-only" width="625"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_1L.png#gh-light-mode-only" width="625"/>
</p>

```bash
$ python3 steamware.py --en doughnut --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --mt O --ts XXXBBAAAYY
```

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/dougnut.png#gh-dark-mode-only" width="1000"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/dougnut.png#gh-light-mode-only" width="1000"/>
</p>

### Example 3: Cross Shape

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2D.png#gh-dark-mode-only" width="625"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/instruction_example_2L.png#gh-light-mode-only" width="625"/>
</p>

```bash
$ python3 steamware.py --en cross --ed /directory/where/files/are/exported --bu 10 --fp 0.134 --ts XXXXAAYYBBBB
```

<p align="center">
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/cross.png#gh-dark-mode-only" width="1000"/>
<img src="https://github.com/spacetimeengineer/STEAMWare/blob/main/resources/cross.png#gh-light-mode-only" width="1000"/>
</p>

Each command generates an `.scad` file, an `.stl` file, and a `.png` file with the specified filename.

---

## Future of Steamware

- Power transmission:
    - Modular gears and gearboxes.
- Housing:
    - Algorithms for housing track string construction.
- 3D-printed bearings embedded in Steamware.
- Mechanical linkage schemes and next-generation scripts.
- Increased accessibility for robotics.
- Potential integration with MuPy.

## Steamware Wishlist

- Low-density space robots.
- Atomic computers.
- Wind energy circuits.
- Differential circuits.
- Modular space stations.
- More pull requests and contributions.
- Expanded part library.
- More users creating businesses or operations with Steamware.
- New frameworks for technology development.
- Broader adoption and innovation.
