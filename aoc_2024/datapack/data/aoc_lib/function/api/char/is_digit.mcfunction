# checks if a char is a number
#...
# input:  val: char location
#...
# output: -1 if it is not a number
#          else the integer value
#...
# mutate: score lib.char.is_digit aoc_calc equals output

$data modify storage aoc:register lib.char.val set from storage aoc:register $(val)
return run function aoc_lib:char/is_digit with storage aoc:register lib.char
