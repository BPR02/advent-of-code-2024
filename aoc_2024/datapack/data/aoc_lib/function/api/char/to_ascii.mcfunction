# converts a letter to it's ascii integer value
#...
# input:  val: char location
#...
# output: -1 if it is not a letter
#          else the ascii integer value
#...
# mutate: score lib.char.to_ascii aoc_calc equals output

$data modify storage aoc:register lib.char.val set from storage aoc:register $(val)
return run function aoc_lib:char/to_ascii with storage aoc:register lib.char
