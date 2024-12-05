# converts a letter to it's uppercase letter
#...
# input:  val: char location
#...
# output: -1 if it is not a letter
#          else 1
#...
# mutate: score lib.char.to_upper aoc_calc equals output
#         val is the uppercase char

$data modify storage aoc:register lib.char.val set from storage aoc:register $(val)
return run function aoc_lib:char/to_upper with storage aoc:register lib.char
$data modify storage aoc:register $(val) set from storage aoc:register lib.char.val
