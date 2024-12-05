# run from aoc_lib:list/merge_sort/merge_loop
# merge the two arrays into a sorted list

# compare values
execute store result score lib.compare.a aoc_calc run data get storage aoc:register lib.list.sort.merging1[0]
execute store result score lib.compare.b aoc_calc run data get storage aoc:register lib.list.sort.merging2[0]
execute if score lib.list.sort.type aoc_calc matches 1 run function aoc_lib:int/compare

# move smallest value
execute if score lib.compare.res aoc_calc matches -1 run data modify storage aoc:register lib.list.sort.temp append from storage aoc:register lib.list.sort.merging1[0]
execute if score lib.compare.res aoc_calc matches -1 run data remove storage aoc:register lib.list.sort.merging1[0]
execute unless score lib.compare.res aoc_calc matches -1 run data modify storage aoc:register lib.list.sort.temp append from storage aoc:register lib.list.sort.merging2[0]
execute unless score lib.compare.res aoc_calc matches -1 run data remove storage aoc:register lib.list.sort.merging2[0]

# check if either list is empty
execute if score lib.compare.res aoc_calc matches -1 run scoreboard players remove lib.list.sort.len1 aoc_calc 1
execute unless score lib.compare.res aoc_calc matches -1 run scoreboard players remove lib.list.sort.len2 aoc_calc 1
execute if score lib.list.sort.len1 aoc_calc matches 0 run return run data modify storage aoc:register lib.list.sort.temp append from storage aoc:register lib.list.sort.merging2[]
execute if score lib.list.sort.len2 aoc_calc matches 0 run return run data modify storage aoc:register lib.list.sort.temp append from storage aoc:register lib.list.sort.merging1[]

# continue until either list is empty
function aoc_lib:list/merge_sort/merge
