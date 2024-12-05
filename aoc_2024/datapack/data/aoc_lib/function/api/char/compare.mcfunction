# compares two char values
#...
# input:  a: char location
#         b: char location
#...
# output: -1 if a <  b
#          1 if a >  b
#          0 if a == b
#...
# mutate: score lib.compare.res aoc_calc equals output

$data modify storage aoc:register lib.char.a.val set from storage aoc:register $(a)
$data modify storage aoc:register lib.char.b.val set from storage aoc:register $(b)
return run function aoc_lib:char/compare
