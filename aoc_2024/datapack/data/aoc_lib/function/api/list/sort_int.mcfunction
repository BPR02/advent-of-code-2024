# sorts a list of integers from least to greatest
#...
# input:  list: list location
#...
# output: none
#...
# mutate: list becomes sorted

$data modify storage aoc:register lib.list.sort.to_sort set from storage aoc:register $(list)
scoreboard players set lib.list.sort.type aoc_calc 1
function aoc_lib:list/merge_sort/_run
$data modify storage aoc:register $(list) set from storage aoc:register lib.list.sort.to_sort
