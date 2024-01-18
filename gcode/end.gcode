; put below section after 'Move print head up' and before 'park print head'

;;
; final screenshot start
G1 X{round(print_bed_size[0]/2)} Y{print_bed_size[1]} F{travel_speed*60} ; move head back in the middle
G4 S0 ; Wait for move to finish
G1 X{print_bed_size[0]} Y{print_bed_size[1]} F{travel_speed*60} ; trigger button activation
G4 S0 ; Wait for move to finish
G4 P3500 ; Wait for image capture in miliseconds
; final screenshot end
;;
