# sorts a list of characters from least to greatest
# input:  list: list
# output: none
#         list becomes sorted

$data modify storage aoc:register lib.list.to_sort set from storage aoc:register $(list)
scoreboard players set lib.list.type aoc_calc 2
function aoc_lib:list/merge_sort/_run
$data modify storage aoc:register $(list) set from storage aoc:register lib.list.to_sort
