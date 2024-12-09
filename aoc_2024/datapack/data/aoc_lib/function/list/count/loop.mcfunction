# run from aoc_lib:list/count/_run

# check if matching
execute store result score diff aoc_calc run data modify storage aoc:register lib.list.count.list[-1] set from storage aoc:register lib.list.count.find
execute if score diff aoc_calc matches 0 run scoreboard players add lib.list.count aoc_calc 1

# loop for each element
data remove storage aoc:register lib.list.count.list[-1]
scoreboard players remove lib.list.count.len aoc_calc 1
execute if score lib.list.count.len aoc_calc matches 1.. run function aoc_lib:list/count/loop
