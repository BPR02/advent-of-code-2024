# converts a string to it's integer value
#...
# input:  val: string location
#...
# output: -1 if it is not a number
#          else the integer value
#...
# mutate: score lib.str.to_int aoc_calc equals output

$data modify storage aoc:register lib.str.to_int.val set from storage aoc:register $(val)
return run function aoc_lib:str/to_int/_run
