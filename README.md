# STEAMWare
Hardware Assembly Language
STEAMWare ( Science - Technology - Engineering - Art - Mathematics ) - Ware

*Note from the author*

This is an extremely potent technology. Ill leave it at that. Built it for kids and adults. I want it simple and I want it free and I want the savings to go to the people who matter most. Be a builder. DO with these what YOU want.





What is STEAMWare?
==================

In short, STEAMWare refers to a new (LEGO-like) modular part family and the open-source software utility which generates them. LEGO-Like-apparent but so much more in reality and built to solve the scaling problems.

simply by fit and join; If everything is cubelike then everything should slide into place. The padding which is applied to each block relative to the basis unit is required to make binding less tight. As long as relativcie positioning of blocks is managed by a basis unit coordinate system then everything is great.


OpenSource
==========

Pull requests are appreciated. But bear with me I am slow and dumb as fucking molasis most days. 

*Benefits*

- Not limited to 3D printers but illuminated by them.
- STEAMWare is material independent and hyper non-propietary.
- STEAMWare is far cheaper than anything like it and far more useful.
- Utility and recreation grade.
- Hyper modular
- Infinite Parts
- Illegal operations
- Inventions Wanted
- Developers Wanted
- Believers Wanted

    Replace physical parts with files for print/reference.
    Replace Legos with STEAMWare
    Replace propietary with permissive open source
    Replace finite parts with infinite parts.



Binding
=======

Fit and Join:

Bolt and Nut

Wrap Binding

Friction Binding

On Padding Variance:




Manufacturing
=============

Principly these were built with 3D printers in mind: This is multifold First 


1.) 3D printers cannot compete with traditional manufdactuinr meathods true 

however this is only the case for a subset of all possible design sets which STEAMWare now provides access to. F
rom this viewpoint CNC machnines onyl are better for certsain parts.

2.) 3D Printers are getting way better.

3.) Abstrracted from materials or manufacturing process.




Examples:

    $ python3 sw.py --fn donught --bu 10 --fp 0.134 --ts XYABBBBBZCZZZZZ

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)

    $ python3 sw.py --fn donught --basis_unit 10 --fit_padding 0.134 --track_string XXX

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)

    $ python3 sw.py --fn donught --basis_unit 10 --fit_padding 0.134 --track_string XXXZ

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)

    $ python3 sw.py --fn donught --basis_unit 10 --fit_padding 0.134 --track_string XXXZCXX

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)

    $ python3 sw.py --fn donught --basis_unit 10 --fit_padding 0.134 --track_string XXYYAABBX

![alt text](https://github.com/spacetimeengineer/STEAMWare/blob/master/resources/donught.png)



Each Call creates an .scad file, .stl file and a a .png file of the same filename.