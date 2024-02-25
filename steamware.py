#!/usr/bin/env python3
import os, sys
import shutil
import argparse
from loguru import logger



class STEAMWare:
    """ This class builds digital representations of STEAMWare elements."""
    def __init__(self, basis_unit, fit_padding, track_string, mass_type, export_name, export_directory): # Runs when object is initialized.

        self.track_string = track_string # The string of configuration codes that are used to build the steamware element.    
            
        
        self.basis_unit = basis_unit # The initial basis unit that the steamware element is built on.
        self.fit_padding = fit_padding # The initial fit padding that the system is built on.
        
       
        self.mass_type = mass_type # The initial type of mass state that the system is in.
        if mass_type is None: # If no mass type is given, the system defaults to "O" (Open).
            mass_type = "O" # Default mass type is "O" (Open).
                            
        self.export_directory = export_directory # Directory where resources are delivered.
        self.export_name = export_name # Name of the export file/directory.
        
        self.steamware_element_directory = self.export_directory + "/" +  self.export_name # The directory where the steamware element is stored.
        if not os.path.exists(self.export_directory):
            
            logger.info("Creating export directory : " + self.export_directory ) # Log export directory creation.   
            
            os.system("mkdir "+ self.export_directory) # Create export directory.
            
        else: # If export directory already exists.
            
            logger.info("Export directory : " + self.export_directory + " already exists." ) # Log export directory already exists.
            
        if not os.path.exists(self.steamware_element_directory): # If steamware element directory does not exist.
            
            logger.info("Creating steamware element directory : " + self.steamware_element_directory ) # Log steamware element directory creation.
            os.system("mkdir "+ self.steamware_element_directory) # Create steamware element directory.
            
        else: # If steamware element directory already exists.
            
            logger.info("Steamware element directory : " + self.steamware_element_directory + " already exists." ) # Log steamware element directory already exists.
            
            
        self.scad_file_name = export_directory + "/" + export_name + "/" + export_name +".scad" # The actual name of the scad file that is represented by the system code.
        self.scad_file = open(self.scad_file_name, 'w+')  # open file in append mode


        os.system("cp -R "+os.path.dirname(__file__)+"/steamware.scad "+ self.steamware_element_directory) # On Linux, copies from relevent scad libraries into 'steamware element directory' to perfrom work and uses system codes and CONFIG CODES in particular to feed parametrization into. Libraries are intented to be removed after function has been fufilled.
        self.scad_file.write('\n\n// STEAMWare Export Name: '+str(self.export_name)+'\n') # Write export name to scad file.
        self.scad_file.write('// STEAMWare Export Directory: '+str(self.export_directory)+'\n') # Write export directory to scad file.
        self.scad_file.write('// STEAMWare Track String Identity: '+str(self.track_string)+'\n\n') # Write track string identity to scad file.
        self.scad_file.write('// Initial Basis Unit : '+str(self.basis_unit)+'\n') # Write basis unit to scad file.
        self.scad_file.write('// Fit Padding : '+str(self.fit_padding)+'\n') # Write fit padding to scad file.
        self.scad_file.write('// Initial Mass Type: '+str(self.mass_type)+'\n\n\n') # Write mass type to scad file.
        
        self.scad_file.write('use <steamware.scad>;\n\n') # Write library usage. #TODO May need to be plugged in at the end.
            

        self.block_coordinates_tracker = [ 0, 0, 0 ] # The coordinates of the block that is being tracked.
        self.coupler_coordinates_tracker = [ 0, 0, 0 ] # The coordinates of the coupler that is being tracked.
        self.coupler_orientation = [ 0, 0, 0 ] # The orientation of the coupler that is being tracked.1
        self.delta_block_coordinates_tracker = [ 0, 0, 0 ] # The delta coordinates of the block that is being tracked.
        self.delta_coupler_coordinates_tracker = [ 0, 0, 0 ] # The delta coordinates of the coupler that is being tracked.
        
        if (self.mass_type == "O"): # If the mass type is "O" (Open).
                    
            self.scad_file.write('translate( [ 0, 0, 0 ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n') # Write (Open) origin block to scad file.
                    
        if (self.mass_type == "F"): # If the mass type is "F" (Full/Filled).
                    
            self.scad_file.write('translate( [ 0, 0, 0 ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n') # Write (Filled/Full) origin block to scad file.
        

        self.INSTRUCTION_SET = []
        
        for i in list(self.track_string):
            
            if i == "F": # If the mass type is "F" (Full/Filled).
                
                self.mass_type = "F" # Set the mass type to "F" (Full/Filled).
            
            if i =="O": # If the mass type is "O" (Open).
                
                self.mass_type = "O" # Set the mass type to "O" (Open).
            
            if i != "F" and i != "O":  # If the mass type is not "F" (Full/Filled) or "O" (Open).
                
                self.INSTRUCTION_SET.append([ i, self.mass_type ])  # This is where the instruction set is built.

        for i in range(len(self.INSTRUCTION_SET)): # For each element in the instruction set ; track string identity.

            INSTRUCTION = self.INSTRUCTION_SET[i] # Get the instruction.
            
            if i != len(self.INSTRUCTION_SET)-1: # If not the last element.
                
                NEXT_INSTRUCTION = self.INSTRUCTION_SET[i+1][0] # Get the next instruction.
                
            else: # If the last element of the instruction.
                
                NEXT_INSTRUCTION = None # If the last element.
                
            if i == 0: # If the first element.
                    
                PREVIOUS_INSTRUCTION = None # If the first element.
                    
            else: # If not the first element.
                    
                PREVIOUS_INSTRUCTION = self.INSTRUCTION_SET[i-1][0] # Get the previous instruction.
 
            self.transcribe_configuration(INSTRUCTION, NEXT_INSTRUCTION, PREVIOUS_INSTRUCTION) # Transcribe the configuration to the scad file.
        
        self.scad_file.close() # Finish writing scad script.


    
    def transcribe_configuration(self, INSTRUCTION, NEXT_INSTRUCTION, PREVIOUS_INSTRUCTION): # Transcribes the configuration to the scad file.
        """Transcribes the configuration to the scad file.

        Args:
            INSTRUCTION (str): Current track string instruction being processed and interpreted.
            NEXT_INSTRUCTION (str): Next track string instruction being processed and interpreted.
            PREVIOUS_INSTRUCTION (str): Previous track string instruction being processed and interpreted.
        """    
    
        self.previous_block_coordinates_tracker = self.block_coordinates_tracker    
        self.previous_coupler_coordinates_tracker = self.coupler_coordinates_tracker
        
        self.mass_type = INSTRUCTION[1]
        
        
        
        
        
        
        if (INSTRUCTION[0] =="A"):
            
            if (PREVIOUS_INSTRUCTION == "G"):
                
                pass
            
            else:
                
                if (NEXT_INSTRUCTION == "S"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "S"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
                    
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

                    if (self.mass_type == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                    if (self.mass_type == "F"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')

        if (INSTRUCTION[0] =="B"):
            
            if (PREVIOUS_INSTRUCTION == "G"):
                
                pass
            
            else:
                    
                if (NEXT_INSTRUCTION == "S"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "S"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                        
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

                    if (self.mass_type == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                    if (self.mass_type == "F"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
        if (INSTRUCTION[0] =="C"):
            
            if (PREVIOUS_INSTRUCTION == "G"):
                
                pass
            
            else:
                    
                if (NEXT_INSTRUCTION == "S"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "S"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
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

                    if (self.mass_type == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                    if (self.mass_type == "F"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                                
                
        if (INSTRUCTION[0] =="X"):
            
            
            if (PREVIOUS_INSTRUCTION == "G"): # if (PREVIOUS_INSTRUCTION == "G" or (PREVIOUS_INSTRUCTION == "F" or PREVIOUS_INSTRUCTION == "O") and PREVIOUS_PREVIOUS_INSTRUCTION == "G"):
                
                pass
            
            else:
            
                if (NEXT_INSTRUCTION == "S"):
                    
                    pass
                    

                    
                    
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "S"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
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

                    
                    if (self.mass_type == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                    if (self.mass_type == "F"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')           
                

            
        if (INSTRUCTION[0] =="Y"):
            
            if (PREVIOUS_INSTRUCTION == "G"):
                
                pass
            
            else:
                    
                if (NEXT_INSTRUCTION == "S"):
                    
                    pass
                    
                    
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "S"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
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

                    if (self.mass_type == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                    if (self.mass_type == "F"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                            
        if (INSTRUCTION[0] =="Z"):
            
            if (PREVIOUS_INSTRUCTION == "G"):
                
                pass
            
            else:        
                    
                if (NEXT_INSTRUCTION == "S"):
                    
                    pass
                    
                
                if ((NEXT_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z"] or PREVIOUS_INSTRUCTION in ["A", "B", "C", "X", "Y", "Z", "S"]) or (NEXT_INSTRUCTION == None and PREVIOUS_INSTRUCTION == None)):
                    
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

                    if (self.mass_type == "O"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                    if (self.mass_type == "F"):
                        
                        self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                        self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')

                
            
            
            
            
            
            
            
                    
        
        if (INSTRUCTION[0] == "G"):
            
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
                
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
                
                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
                
                
                
                
                
                
                
                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(cx)+', '+str(cy)+', '+str(cz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_optimized_coupler( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                    
                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { solid_optimized_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); }\n')
                
                
      
                
                
                
        if (INSTRUCTION[0] =="S"):
            
                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
           
            
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                
                
                
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                
            
                
                
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

                
                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')
                

            
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

                if (self.mass_type == "O"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')

                if (self.mass_type == "F"):
                    
                    self.scad_file.write('translate( [ '+str(bx)+', '+str(by)+', '+str(bz)+' ] ) { rotate ( [ '+str(cox)+', '+str(coy)+', '+str(coz)+' ] ) { solid_transform_block( '+str(self.basis_unit)+' , '+str(self.fit_padding)+' ); } }\n')


        self.coupler_orientation = [ 0, 0, 0 ]
        print(PREVIOUS_INSTRUCTION, INSTRUCTION, NEXT_INSTRUCTION, "----> "+str(self.block_coordinates_tracker))

            
            
if __name__ == "__main__": 

    """ Main Program """
    
    parser = argparse.ArgumentParser() # Create Argument Parser Object
    parser.add_argument("--en", "--export_name", help="Export Name", type=str) # Add the export name argument which is a string that descrribes the name of the file/directory to be exported.
    parser.add_argument("--ed", "--export_directory", help="Export Directory", type=str) # Add the export directory argument which is a string that describes the directory where the file/directory will be exported.   
    parser.add_argument("--bu", "--basis_unit", help="Basis Unit", type=float) # Add the basis unit argument which is a float that describes the basis unit of the block.
    parser.add_argument("--fp", "--fit_padding", help="Fit Padding", type=float) # Add the fit padding argument which is a float that describes the fit padding of the block.
    parser.add_argument("--ts", "--track_string", help="Track String", type=str) # Add the track string argument which is a string that describes the track string of the block.
    parser.add_argument("--mt", "--mass_type", help="Mass Type", type=str) # Add the mass type argument which is a string that describes the mass type of the initial block(s).
    args = parser.parse_args() # Parse the arguments and store them in the args variable.

    STEAMWare(args.bu, args.fp, args.ts, args.mt, args.en, args.ed) # Create a STEAMWare object with the basis unit, fit padding, track string, mass type, export name, and export directory arguments.
    
"""Examples:
    # Windows: python steamware.py --en "test" --ed "C:/Users/JohnDoe/Desktop" --bu 10 --fp 0.1 --mt "O" --ts "UABCD" 
    # Linux: python steamware.py --en "test" --ed "/home/JohnDoe/Desktop" --bu 10 --fp 0.1 --mt "O" --ts "UABCD"
"""