# converts a letter to it's uppercase letter
#...
# input:  val: char location
#...
# output: -1 if it is not a letter
#         1 upon success
#         0 if the letter is already uppercase
#...
# mutate: score lib.char.to_upper aoc_calc equals output
#         val is the uppercase char

$data modify storage aoc:register lib.char.val set from storage aoc:register $(val)
function aoc_lib:char/to_upper with storage aoc:register lib.char
execute if score lib.char.to_upper aoc_calc matches -1 run return -1
$return run data modify storage aoc:register $(val) set from storage aoc:register lib.char.val
