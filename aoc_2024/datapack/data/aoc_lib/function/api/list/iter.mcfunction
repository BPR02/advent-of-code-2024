# runs a command for each element in the list
#...
# input:  list: list location
#         function: name of function to run for each element
#...
# output: none
#...
# mutate: none (list is unaffected)
#...
# notes: use `lib.list.e` in the function to target the current element
#        e.g. tellraw @a ["",{"nbt":"lib.list.e","storage":"aoc:register"}]

$data modify storage aoc:register lib.list.iter.list set from storage aoc:register $(list)
$data modify storage aoc:register lib.list.iter.function set value "$(function)"
function aoc_lib:list/iter/_run
