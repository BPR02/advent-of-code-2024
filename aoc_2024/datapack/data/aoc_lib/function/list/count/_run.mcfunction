# run from aoc_lib:api/list/count
# checks each element in the list

# check each element
scoreboard players set lib.list.count aoc_calc 0
execute store result score lib.list.count.len aoc_calc run data get storage aoc:register lib.list.count.list
function aoc_lib:list/count/loop
return run scoreboard players get lib.list.count aoc_calc
