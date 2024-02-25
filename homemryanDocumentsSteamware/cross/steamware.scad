

module general_block( block_unit, shaft_unit )
{

    difference()
    {
        cube([block_unit, block_unit, block_unit], true);

        rotate([0,0,0]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
        rotate([0,90,0]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
        rotate([0,0,90]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
            
        
    }
}

module transform_block( basis_unit, padding )
{
    block_unit = basis_unit - padding;
    shaft_unit = basis_unit/3 + padding;
    difference()
    {
        cube([block_unit, basis_unit + padding, basis_unit + padding], true);

        rotate([0,0,0]) { cube( [ block_unit + padding + 0.01, shaft_unit, shaft_unit ], center = true ); }
        //rotate([0,90,0]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
        //rotate([0,0,90]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
    
        
    }
}

module solid_transform_block( basis_unit, padding )
{
    block_unit = basis_unit - padding;
    difference()
    {
        cube([block_unit, basis_unit + padding, basis_unit + padding], true);

        rotate([0,0,0]) { cube( [ block_unit + padding + 0.01, 0, 0 ], center = true ); }
        //rotate([0,90,0]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
        //rotate([0,0,90]) { cube( [ block_unit + 0.01, shaft_unit, shaft_unit ], center = true ); }
    
        
    }
}





module general_coupler( block_unit, shaft_unit )
{

    difference()
    {
        cube( [ block_unit/2, block_unit, block_unit] , center = true );
        cube( [ block_unit, shaft_unit, shaft_unit ], center = true );
    }
}

module advanced_block( block_unit, shaft_unit )
{

    // <--WARNING DO NOT CHANGE FROM cubic_corner_to_edge_angle = 54.7 -->

    cubic_corner_to_edge_angle = 54.7;
    corner_cropping_constant = 0.5335 * block_unit ;
    edge_cropping_constant = 0.7707;
    
    
    difference()
    {
        general_block( block_unit, shaft_unit );
        
        translate([corner_cropping_constant,corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,45])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([-corner_cropping_constant,corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,135])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([corner_cropping_constant,-corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,315])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }       
        }
        translate([-corner_cropping_constant,-corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,225])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([corner_cropping_constant,corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,45])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
            
        }
        translate([-corner_cropping_constant,corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,135])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([corner_cropping_constant,-corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,315])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([-corner_cropping_constant,-corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,225])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        
        // Edges.
        
        translate([block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        translate([-block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        translate([block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        translate([-block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        
        rotate([90,0,0])
        {
            translate([block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            
            translate([-block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([-block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
        }
        
        rotate([0,90,0])
        {
            translate([block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            
            translate([-block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([-block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
        }
        
    }
}

module advanced_coupler(block_unit, shaft_unit)
{
    // <--WARNING DO NOT CHANGE FROM cubic_corner_to_edge_angle = 54.7 -->
    cubic_corner_to_edge_angle = 54.7;
    corner_cropping_constant = 0.53355 * block_unit ;
    edge_cropping_constant = 0.7707;
    difference()
    {
        general_coupler(block_unit, shaft_unit);
        
        translate([corner_cropping_constant,corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,45])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([-corner_cropping_constant,corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,135])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([corner_cropping_constant,-corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,315])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }       
        }
        translate([-corner_cropping_constant,-corner_cropping_constant,corner_cropping_constant])
        {
            rotate([0,cubic_corner_to_edge_angle,225])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([corner_cropping_constant,corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,45])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
            
        }
        translate([-corner_cropping_constant,corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,135])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([corner_cropping_constant,-corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,315])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        translate([-corner_cropping_constant,-corner_cropping_constant,-corner_cropping_constant])
        {
            rotate([0,-cubic_corner_to_edge_angle,225])
            {
                cube([block_unit/2, block_unit/2, block_unit/2],true);
            }
        }
        
        // Edges.
        
        translate([block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        translate([-block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        translate([block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        translate([-block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
        {
            rotate([0,0,45])
            {
                cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
            }
        }
        
        rotate([90,0,0])
        {
            translate([block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            
            translate([-block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([-block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
        }
        
        rotate([0,90,0])
        {
            translate([block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            
            translate([-block_unit*edge_cropping_constant,block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
            translate([-block_unit*edge_cropping_constant,-block_unit*edge_cropping_constant,0])
            {
                rotate([0,0,45])
                {
                    cube([block_unit+0.01, block_unit+0.01, block_unit+0.01],true);
                }
            }
        }
        
    }
}

module optimized_block(basis_unit, padding)
{

    block_unit = basis_unit - padding;
    shaft_unit = basis_unit/3 + padding;
    advanced_block(block_unit, shaft_unit);
}


module optimized_coupler(basis_unit, padding)
{

    block_unit = basis_unit - padding;
    shaft_unit = basis_unit/3 + padding;
    advanced_coupler(block_unit, shaft_unit);
}

module solid_optimized_coupler(basis_unit, padding)
{

    block_unit = basis_unit - padding;
    shaft_unit = 0;
    advanced_coupler(block_unit, shaft_unit);
}

module solid_optimized_block(basis_unit, padding)
{

    block_unit = basis_unit - padding;
    shaft_unit = 0;
    advanced_block(block_unit, shaft_unit);
}