# update path
execute if block ~ ~-2 ~ air run return 1
execute unless block ~ ~-1 ~ gold_block run scoreboard players add answer aoc_calc 1
execute unless block ~ ~-1 ~ gold_block if score visualize aoc_calc matches 1 positioned ~ ~-1 ~ run function aoc_lib:api/stack/push_block {name:"day_6",id:"gold_block"}
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_pause {name:"day_6",time:"1"}
setblock ~ ~-1 ~ gold_block

# turn at obstacle
scoreboard players set blocked aoc_calc 0
execute if score d aoc_calc matches 0 if block ~ ~ ~-1 red_concrete store result score blocked aoc_calc run scoreboard players add d aoc_calc 1
execute if score blocked aoc_calc matches 0 if score d aoc_calc matches 1 if block ~1 ~ ~ red_concrete store result score blocked aoc_calc run scoreboard players add d aoc_calc 1
execute if score blocked aoc_calc matches 0 if score d aoc_calc matches 2 if block ~ ~ ~1 red_concrete store result score blocked aoc_calc run scoreboard players add d aoc_calc 1
execute if score blocked aoc_calc matches 0 if score d aoc_calc matches 3 if block ~-1 ~ ~ red_concrete store result score blocked aoc_calc run scoreboard players add d aoc_calc 1
execute if score d aoc_calc matches 4.. run scoreboard players set d aoc_calc 0

# step forward
scoreboard players add _i aoc_calc 1
execute if score blocked aoc_calc matches 1 run return run function aoc_2024:logic/day_6/part_1/path/step
execute if score d aoc_calc matches 0 positioned ~ ~ ~-1 run return run function aoc_2024:logic/day_6/part_1/path/step
execute if score d aoc_calc matches 1 positioned ~1 ~ ~ run return run function aoc_2024:logic/day_6/part_1/path/step
execute if score d aoc_calc matches 2 positioned ~ ~ ~1 run return run function aoc_2024:logic/day_6/part_1/path/step
execute if score d aoc_calc matches 3 positioned ~-1 ~ ~ run return run function aoc_2024:logic/day_6/part_1/path/step
