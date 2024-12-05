# checks if a char is a letter of the alphabet
#...
# input:  val: char location
#...
# output: -1 if a is not a letter
#          else the ascii integer value
#...
# mutate: score lib.char.is_alpha aoc_calc equals output

$data modify storage aoc:register lib.char.val set from storage aoc:register $(val)
return run function aoc_lib:char/is_alpha with storage aoc:register lib.char
