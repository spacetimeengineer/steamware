#!/usr/bin/env python3
import os, sys
import shutil
import argparse




class CUBX2000:
    """ This class builds digital representations of CUBX2000 hardware elements."""

    def __init__(self, system_code, output_directory): # Runs when object is initialized.

        self.system_code = system_code  # System code.
         
        system_code_list = self.system_code.split("-") # separates simple   
         
        self.VENDOR_CODE = system_code_list[0] # Vendor code.
        self.WORK_CODE = system_code_list[1] # Work code.
        self.ITEM_CODE = system_code_list[2] # Item code.
        
        if len(system_code_list) == 5:
            
            self.CONFIG_CODE = system_code_list[3]
        
        if len(system_code_list) == 4:
            
            self.CONFIG_CODE = ""
            
        self.PROTOCOL_CODE = system_code_list[len(system_code_list)-1] # Protocol code.
        
        self.basis_unit = float(self.ITEM_CODE.split("BU")[1].split("S")[0]) # The units which blocks are measured in and the length of each alphabetic-translation.
        self.padding = float(self.ITEM_CODE.split("S")[1].split("M")[0].replace("P",".")) # Shaft radius for each block.
        
        
        self.mass_state = self.ITEM_CODE.split("M")[1]
        
                
        self.output_directory = output_directory # Directory where resources are delivered.
        self.scad_file_name = output_directory + "/" + self.system_code +".scad" # The actual name of the scad file that is represented by the system code.
        
        self.scad_file = open(self.scad_file_name, 'w+')  # open file in append mode

        os.system("cp -R "+os.path.dirname(__file__)+"/scad/ "+ self.output_directory) # On Linux, copies from relevent scad libraries into 'output directory' to perfrom work and uses system codes and CONFIG CODES in particular to feed parametrization into. Libraries are intented to be removed after function has been fufilled.
            
        self.scad_file.write('use <scad/CUBX2000.scad>;\n\n') # Write library usage. #TODO May need to be plugged in at the end.
            

        self.block_coordinates_tracker = [ 0, 0, 0 ]    
        self.coupler_coordinates_tracker = [ 0, 0, 0 ]
        self.coupler_orientation = [ 0, 0, 0 ]
        self.delta_block_coordinates_tracker = [ 0, 0, 0 ]
        self.delta_coupler_coordinates_tracker = [ 0, 0, 0 ]
        
        
        self.scad_file.write('translate( [ 0, 0, 0 ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')

        self.INSTRUCTION_SET = []
        
        for i in list(self.CONFIG_CODE):
            print(i)
            if i == "S":
                
                self.mass_state = "S"
            
            if i =="O":
                
                self.mass_state = "O"
            
            if i != "S" and i != "O": 
                
                self.INSTRUCTION_SET.append([ i, self.mass_state ]) 

        for i in range(len(self.INSTRUCTION_SET)):

            INSTRUCTION = self.INSTRUCTION_SET[i]
            
            if i != len(self.INSTRUCTION_SET)-1: # If not the last element.
                
                NEXT_INSTRUCTION = self.INSTRUCTION_SET[i+1][0]
                
            else:
                
                NEXT_INSTRUCTION = None
                
            if i == 0:
                    
                PREVIOUS_INSTRUCTION = None
                    
            else:
                    
                PREVIOUS_INSTRUCTION = self.INSTRUCTION_SET[i-1][0]
 
 
 
 
            self.transcribe_configuration(INSTRUCTION, NEXT_INSTRUCTION, PREVIOUS_INSTRUCTION) 
                  

                
            
        
        
        self.scad_file.close() # Finish writing scad script.
        

    
    def transcribe_configuration(self, INSTRUCTION, NEXT_INSTRUCTION, PREVIOUS_INSTRUCTION):

        self.previous_block_coordinates_tracker = self.block_coordinates_tracker    
        self.previous_coupler_coordinates_tracker = self.coupler_coordinates_tracker
        
        self.mass_state = INSTRUCTION[1]
        
        
        
        
        
        
        if (INSTRUCTION[0] =="A"):
            
            if (PREVIOUS_INSTRUCTION == "U"):
                
                pass
            
            else:
                
                if (NEXT_INSTRUCTION == "D"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "D"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
                    
                    self.coupler_orientation = [ 0, 0, 0 ]
                    self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit/2, 0, 0 ])))
                    self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit, 0, 0 ])))
                                    
                    bx = self.block_coordinates_tracker[0]
                    by = self.block_coordinates_tracker[1]
                    bz = self.block_coordinates_tracker[2]
                    
                    cx = self.coupler_coordinates_tracker[0]
                    cy = self.coupler_coordinates_tracker[1]
                    cz = self.coupler_coordinates_tracker[2]
                    
                    cox = self.coupler_orientation[0]
                    coy = self.coupler_orientation[1]
                    coz = self.coupler_orientation[2]

                    if (self.mass_state == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                    if (self.mass_state == "S"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')

        if (INSTRUCTION[0] =="B"):
            
            if (PREVIOUS_INSTRUCTION == "U"):
                
                pass
            
            else:
                    
                if (NEXT_INSTRUCTION == "D"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "D"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                        
                    self.coupler_orientation = [ 0, 0, -90]
                    self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit/2, 0 ])))
                    self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit, 0 ])))
                    
                    bx = self.block_coordinates_tracker[0]
                    by = self.block_coordinates_tracker[1]
                    bz = self.block_coordinates_tracker[2]
                    
                    cx = self.coupler_coordinates_tracker[0]
                    cy = self.coupler_coordinates_tracker[1]
                    cz = self.coupler_coordinates_tracker[2]
                    
                    cox = self.coupler_orientation[0]
                    coy = self.coupler_orientation[1]
                    coz = self.coupler_orientation[2]

                    if (self.mass_state == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                    if (self.mass_state == "S"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
        if (INSTRUCTION[0] =="C"):
            
            if (PREVIOUS_INSTRUCTION == "U"):
                
                pass
            
            else:
                    
                if (NEXT_INSTRUCTION == "D"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "D"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
                    self.coupler_orientation = [ 0, -90, 0]
                    self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit/2 ])))
                    self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit ])))
                    
                    bx = self.block_coordinates_tracker[0]
                    by = self.block_coordinates_tracker[1]
                    bz = self.block_coordinates_tracker[2]
                    
                    cx = self.coupler_coordinates_tracker[0]
                    cy = self.coupler_coordinates_tracker[1]
                    cz = self.coupler_coordinates_tracker[2]
                    
                    cox = self.coupler_orientation[0]
                    coy = self.coupler_orientation[1]
                    coz = self.coupler_orientation[2]

                    if (self.mass_state == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                    if (self.mass_state == "S"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                                
                
        if (INSTRUCTION[0] =="X"):
            
            
            if (PREVIOUS_INSTRUCTION == "U"): # if (PREVIOUS_INSTRUCTION == "U" or (PREVIOUS_INSTRUCTION == "S" or PREVIOUS_INSTRUCTION == "O") and PREVIOUS_PREVIOUS_INSTRUCTION == "U"):
                
                pass
            
            else:
            
                if (NEXT_INSTRUCTION == "D"):
                    
                    pass
                    

                    
                    
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "D"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
                    self.coupler_orientation = [ 0, 0, 0 ]
                    self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit/2, 0, 0 ])))
                    self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit, 0, 0 ])))
                    
                    
                    bx = self.block_coordinates_tracker[0]
                    by = self.block_coordinates_tracker[1]
                    bz = self.block_coordinates_tracker[2]
                    
                    cx = self.coupler_coordinates_tracker[0]
                    cy = self.coupler_coordinates_tracker[1]
                    cz = self.coupler_coordinates_tracker[2]
                    
                    cox = self.coupler_orientation[0]
                    coy = self.coupler_orientation[1]
                    coz = self.coupler_orientation[2]

                    
                    if (self.mass_state == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                    if (self.mass_state == "S"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')           
                

            
        if (INSTRUCTION[0] =="Y"):
            
            if (PREVIOUS_INSTRUCTION == "U"):
                
                pass
            
            else:
                    
                if (NEXT_INSTRUCTION == "D"):
                    
                    pass
                    
                    
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "D"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
                    self.coupler_orientation = [ 0, 0, 90]
                    self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit/2, 0 ])))
                    self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit, 0 ])))
                    
                    bx = self.block_coordinates_tracker[0]
                    by = self.block_coordinates_tracker[1]
                    bz = self.block_coordinates_tracker[2]
                    
                    cx = self.coupler_coordinates_tracker[0]
                    cy = self.coupler_coordinates_tracker[1]
                    cz = self.coupler_coordinates_tracker[2]
                    
                    cox = self.coupler_orientation[0]
                    coy = self.coupler_orientation[1]
                    coz = self.coupler_orientation[2]

                    if (self.mass_state == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                    if (self.mass_state == "S"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                            
        if (INSTRUCTION[0] =="Z"):
            
            if (PREVIOUS_INSTRUCTION == "U"):
                
                pass
            
            else:        
                    
                if (NEXT_INSTRUCTION == "D"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "D"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
                    self.coupler_orientation = [ 0, 90, 0]
                    self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit/2 ])))
                    self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit ])))
                    
                    
                    bx = self.block_coordinates_tracker[0]
                    by = self.block_coordinates_tracker[1]
                    bz = self.block_coordinates_tracker[2]
                    
                    cx = self.coupler_coordinates_tracker[0]
                    cy = self.coupler_coordinates_tracker[1]
                    cz = self.coupler_coordinates_tracker[2]
                    
                    cox = self.coupler_orientation[0]
                    coy = self.coupler_orientation[1]
                    coz = self.coupler_orientation[2]

                    if (self.mass_state == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                    if (self.mass_state == "S"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')

                
            
            
            
            
            
            
            
                    
        
        if (INSTRUCTION[0] == "U"):
            
            if NEXT_INSTRUCTION == "A":

                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit/2, 0, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit, 0, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit/2, 0, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit, 0, 0 ])))
                self.basis_unit = self.basis_unit * 3
                
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
                
            if NEXT_INSTRUCTION == "B":

                
                self.coupler_orientation = [ 0, 0, -90]
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit/2, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]
                
                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit/2, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit, 0 ])))
                self.basis_unit = self.basis_unit * 3
                
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
            if NEXT_INSTRUCTION == "C":

                self.coupler_orientation = [ 0, -90, 0]
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit/2 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit/2 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit ])))
                self.basis_unit = self.basis_unit * 3
                
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
                
                
                
                
                
                
                
                
            if NEXT_INSTRUCTION == "X":

                self.coupler_orientation = [ 0, 0, 0 ]
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit/2, 0, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit, 0, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit/2, 0, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit, 0, 0 ])))
                self.basis_unit = self.basis_unit * 3
                
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
                
            if NEXT_INSTRUCTION == "Y":

                self.coupler_orientation = [ 0, 0, 90 ]
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit/2, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit/2, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit, 0 ])))
                self.basis_unit = self.basis_unit * 3
                
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
            if NEXT_INSTRUCTION == "Z":

                self.coupler_orientation = [ 0, 90, 0]
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit/2 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit/2 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit])))
                self.basis_unit = self.basis_unit * 3
                
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                    
                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); }\n')
                
                
      
                
                
                
        if (INSTRUCTION[0] =="D"):
            
                
            if NEXT_INSTRUCTION == "A":

                self.coupler_orientation = [ 0, 0, 0]
                self.basis_unit = self.basis_unit / 3
                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit/2, 0, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ -self.basis_unit, 0, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
            if NEXT_INSTRUCTION == "B":

                self.coupler_orientation = [ 0, 0, -90]
                self.basis_unit = self.basis_unit / 3
                
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit/2, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, -self.basis_unit, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
           
            
            if NEXT_INSTRUCTION == "C":

                self.coupler_orientation = [ 0, -90, 0]
                self.basis_unit = self.basis_unit / 3
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit/2 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, -self.basis_unit ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                
                
                
            if NEXT_INSTRUCTION == "X":

                self.coupler_orientation = [ 0, 0, 0 ]
                self.basis_unit = self.basis_unit / 3
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit/2, 0, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ self.basis_unit, 0, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                
            
                
                
            if NEXT_INSTRUCTION == "Y":

                self.coupler_orientation = [ 0, 0, 90 ]
                self.basis_unit = self.basis_unit / 3
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit/2, 0 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, self.basis_unit, 0 ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                
                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')
                

            
            if NEXT_INSTRUCTION == "Z":

                self.coupler_orientation = [ 0, 90, 0]
                self.basis_unit = self.basis_unit / 3
                self.coupler_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit/2 ])))
                self.block_coordinates_tracker = list(map(sum, zip(self.block_coordinates_tracker,[ 0, 0, self.basis_unit ])))
                
                bx = self.block_coordinates_tracker[0]
                by = self.block_coordinates_tracker[1]
                bz = self.block_coordinates_tracker[2]
                
                cx = self.coupler_coordinates_tracker[0]
                cy = self.coupler_coordinates_tracker[1]
                cz = self.coupler_coordinates_tracker[2]
                
                cox = self.coupler_orientation[0]
                coy = self.coupler_orientation[1]
                coz = self.coupler_orientation[2]

                if (self.mass_state == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')

                if (self.mass_state == "S"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.padding)+' ); } }\n')


        self.coupler_orientation = [ 0, 0, 0 ]
        print(PREVIOUS_INSTRUCTION, INSTRUCTION, NEXT_INSTRUCTION, "----> "+str(self.block_coordinates_tracker))

            
            




if __name__ == "__main__":
    
    # System codes to remember :
    
    #CUBX2000("RYANSOL-CUBX2000-BU5S0P12MO-XXXXXXX-SCAD22", "/home/mryan")
    #CUBX2000("RYANSOL-CUBX2000-BU5S0P12MO-XXXXXXXYYYYYYY-SCAD22", "/home/mryan")
    #CUBX2000("RYANSOL-CUBX2000-BU5S0P12MO-XXYYAABBXAZZXXCCZZYYCCZZAACCZZBBXA-SCAD22", "/home/mryan")
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXYYAA-SCAD22", "/home/mryan")
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXXYYAAA-SCAD22", "/home/mryan")

    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXYYAABBXAZXXYYAABBXAZXXYYAABBXAZXXYYAABBXA-SCAD22", "/home/mryan")
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XYBBYXXYBBYXXYBBYXXYBBYX-SCAD22", "/home/mryan")
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-BXXYBXXYBXXYBXXABBXABBYAABYAABYAABYAAXYYAXYXXBBBXXXYYY-SCAD22", "/home/mryan") # RPI3MB+_SLEEVE_WRAP : 6BU X 10BU    
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-BXXYBXXYBXXYBXXABBXABBXABBXABBYAABYAABYAABYAABYAAXYYAXYYAXYYAXYYBXXBBBBBBBXXXXXYYYYYYYXXBBAAAAAAAAABBBXXXXXXXXXAAAAY-SCAD22", "/home/mryan/Desktop/RPI3_SLEEVE") # RPI3MB+_SLEEVE_WRAP : 12BU X 10BU    
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-BXXYBXXYBXXYBXXYBXXABBXABBYAABYAABYAABYAABYAAXYYAXYXXBBBXXYBXXXYYY-SCAD22", "/home/mryan/Desktop/RPI3_SLEEVE") # RPI3MB+_SLEEVE_WRAP : 6BU X 10BU    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXYYAABBXAZZXYZCYBAXXABXCCZZYYCCZZAACCZZBBXXCC XXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAX-SCAD22", "/home/mryan/Desktop/print_set_jan_6_2023_chunk_improved")
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXYYAABBXAZZXYZCYBAXXABXCCZZYYCCZZAACCZZBBXXCC XXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXCCXX XXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXCCXX-SCAD22", "/home/mryan/Desktop/print_set_jan_6_2023_chunk_improved")
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXYYAABBXAZZXYZCYBAXXABXCCZZYYCCZZAACCZZBBXXCCXXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXXXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXXXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXXXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAX-SCAD22", "/home/mryan/Desktop/print_set_jan_6_2023_chunk_improved")

    #CUBX2000("RYANSOL-CUBX2000-BU10S0P135MO-XXYYAABBXAZZXYZCYBAXXABXCCZZYYCCZZAACCZZBBXXCC XXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXCCXX XXXYYAAAXBAXBZAXZAXXYZCYBAXXABXCCZZYYCCZZAAAXCAXCAXZZBAXBAXCCXX-SCAD22", "/home/mryan/Desktop/print_set_jan_6_2023_chunk_improved")
  
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXXYYYYZZZZAAXXBBYYCCZZ-SCAD22", "/home/mryan")
    
    # Create an instance of the CUBX2000 class with a complex "truck-like" track string
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXXYYYYZZZZUUAAAXXBBYYCCZZDDXXXXYYYYZZZZUUAAAXXBBYYCCZZDDXXXXYYYYZZZZUUAAAXXBBYYCCZZDDXXXXYYYYZZZZUUAAAXXBBYYCCZZDD-SCAD22", "/home/mryan")
    # Create an instance of the CUBX2000 class with a complex "truck-like" track string
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXXYYYYZZZZUUXYZZAAXYZZBBXYZZCCXYZZDDXYZZUUXYZZAAXYZZBBXYZZCCXYZZDDXYZZUUXYZZAAXYZZBBXYZZCCXYZZDDXYZZUUXYZZAAXYZZBBXYZZCCXYZZDDXYZZ-SCAD22", "/home/mryan")
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZ-SCAD22", "/home/mryan")
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZ-SCAD22", "/home/mryan")
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZ-SCAD22", "/home/mryan")
    
    #CUBX2000("RYANSOL-CUBX2000-BU10S0P14MO-XXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZXXXYYYZZZAAXBBXCCZ-SCAD22", "/home/mryan")
    
    # q: Make a new track of a 4x4x4 cube with a 1x1x1 cube in the center.      
    # q: Make a new track of a 4x4x4 cube with a 1x1x1 cube in the center.
    # q: Make a new track of a 4x4x4 cube with a 1x1x1 cube in the center.                                                          
    # q: Make a new track of a 4x4x4 cube with a 1x1x1 cube in the center.
    
    
    #q: Make 
    
    
    parser = argparse.ArgumentParser()

    #-db DATABASE -u USERNAME -p PASSWORD -size 20
    parser.add_argument("--ed", "--export_directory", help="File Names", type=str)
    parser.add_argument("--bu", "--basis_unit", help="Basis Unit", type=float)
    parser.add_argument("--fp", "--fit_padding", help="Fit Padding", type=float)
    parser.add_argument("--ts", "--track_string", help="Track String", type=str)

    args = parser.parse_args()

    CUBX2000("RYANSOL-CUBX2000-BU"+args.bu+"S0P14MO-"+args.ts+"-SCAD22", "/home/mryan")
