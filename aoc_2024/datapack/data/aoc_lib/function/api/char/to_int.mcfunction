# converts a character to it's integer value
#...
# input:  val: char location
#...
# output: -1 if it is not a number
#          else the integer value
#...
# mutate: score lib.char.to_int aoc_calc equals output

$data modify storage aoc:register lib.char.val set from storage aoc:register $(val)
return run function aoc_lib:char/to_int with storage aoc:register lib.char
