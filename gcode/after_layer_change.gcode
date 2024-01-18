;AFTER_LAYER_CHANGE
; after layer change start
G1 E-1 F2100 ; retract 1mm before photo to avoid oozing

; take a photo start
G1 X{round(print_bed_size[0]/2)} Y{print_bed_size[1]} F{travel_speed*60} ; move head back in the middle
G4 S0 ; Wait for move to finish

G1 X{print_bed_size[0]} Y{print_bed_size[1]} F{travel_speed*60} ; trigger button activation
G4 S0 ; Wait for move to finish
G4 P3500 ; Wait for image capture in miliseconds

G1 X{round(print_bed_size[0]/2)} Y{print_bed_size[1]} F{travel_speed*60} ; move head back in the middle
G4 S0 ; Wait for move to finish
; take a photo end
G1 E1 F2100 ; revert rectraction after photo
;after layer change end

;[layer_z]
