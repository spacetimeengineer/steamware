

// STEAMWare Export Name: example_part
// STEAMWare Export Directory: homemryanDocumentsSteamware
// STEAMWare Track String Identity: XXSXXX

// Initial Basis Unit : 10.0
// Fit Padding : 0.134
// Initial Mass Type: O


use <steamware.scad>;

translate( [ 0, 0, 0 ] ) { optimized_block( 10.0 , 0.134 ); }
translate( [ 5.0, 0, 0 ] ) { rotate ( [ 0, 0, 0 ] ) { optimized_coupler( 10.0 , 0.134 ); } }
translate( [ 10.0, 0, 0 ] ) { optimized_block( 10.0 , 0.134 ); }
translate( [ 15.0, 0, 0 ] ) { rotate ( [ 0, 0, 0 ] ) { optimized_coupler( 10.0 , 0.134 ); } }
translate( [ 20.0, 0, 0 ] ) { optimized_block( 10.0 , 0.134 ); }
translate( [ 23.333333333333332, 0, 0 ] ) { rotate ( [ 0, 0, 0 ] ) { transform_block( 3.3333333333333335 , 0.134 ); } }
translate( [ 25.0, 0, 0 ] ) { rotate ( [ 0, 0, 0 ] ) { optimized_coupler( 3.3333333333333335 , 0.134 ); } }
translate( [ 26.666666666666664, 0, 0 ] ) { optimized_block( 3.3333333333333335 , 0.134 ); }
translate( [ 28.333333333333332, 0, 0 ] ) { rotate ( [ 0, 0, 0 ] ) { optimized_coupler( 3.3333333333333335 , 0.134 ); } }
translate( [ 29.999999999999996, 0, 0 ] ) { optimized_block( 3.3333333333333335 , 0.134 ); }
translate( [ 31.666666666666664, 0, 0 ] ) { rotate ( [ 0, 0, 0 ] ) { optimized_coupler( 3.3333333333333335 , 0.134 ); } }
translate( [ 33.33333333333333, 0, 0 ] ) { optimized_block( 3.3333333333333335 , 0.134 ); }
