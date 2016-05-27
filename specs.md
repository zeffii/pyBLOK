# PyBLOK

A preliminary attempt at a library for generating BLOK patches. I'm doing this to quickly mash together layouts that may be trickier to connect by hand

## Specs for the components of BLOK ( 2015 edition )

## GENERATE 

```
OSC
   - TYPE: 	"4"
   - POS: 	( 0...n , DAG position, or Z position? )     
   - ID:	given at creation time
   - P0:    semitone	0.0 ... 1.0  // default 0.5
   - P1:    amp      	0.0 ... 1.0  // default 0.5
   - P2:	shape 					 // default 0.5
   			- Sine 		"0.000000" 				 
   			- Tri 		"0.333333"
   			- Saw		  "0.500000"
   			- Square	"1.000000"
```

