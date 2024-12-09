# counts the number of values that exist in a list
#...
# input:  list: list location
#         find: value location
#...
# output: number of found elements
#...
# mutate: score lib.list.count is set to output

$data modify storage aoc:register lib.list.count.list set from storage aoc:register $(list)
$data modify storage aoc:register lib.list.count.find set from storage aoc:register $(find)
return run function aoc_lib:list/count/_run
