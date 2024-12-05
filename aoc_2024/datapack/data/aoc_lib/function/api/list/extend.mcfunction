# adds all values from list 2 into list 1
#...
# input:  l1: list location
#         l2: list location
#...
# output: none
#...
# mutate: l1 contains all elements


$data modify storage aoc:register lib.list.in1 set from storage aoc:register $(l1)
$data modify storage aoc:register lib.list.in2 set from storage aoc:register $(l2)
function aoc_lib:list/extend
$data modify storage aoc:register $(l1) set from storage aoc:register lib.list.in1
