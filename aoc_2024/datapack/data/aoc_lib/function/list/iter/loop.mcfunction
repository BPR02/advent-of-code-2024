# run from aoc_lib:list/iter/_run

data modify storage aoc:register lib.list.e set from storage aoc:register lib.list.iter.list[0]
function aoc_lib:list/iter/run_function with storage aoc:register lib.list.iter

# loop for each element
data remove storage aoc:register lib.list.iter.list[0]
scoreboard players remove lib.list.iter.len aoc_calc 1
execute if score lib.list.iter.len aoc_calc matches 1.. run function aoc_lib:list/iter/loop
