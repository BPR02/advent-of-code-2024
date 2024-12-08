# update path; check out of bounds
execute if block ~ ~-2 ~ air run return 0
execute if score visualize aoc_calc matches 1 positioned ~ ~-1 ~ run function aoc_lib:api/stack/push_block {name:"day_6",id:"yellow_concrete"}
execute if score visualize aoc_calc matches 1 positioned ~ ~-1 ~ run function aoc_lib:api/stack/push_positioned_function {name:"ctx_vis",function:"aoc_2024:logic/day_6/part_2/check/clear"}

# turn at obstacle
scoreboard players set blocked_c aoc_calc -1
execute if score dc aoc_calc matches 0 if block ~ ~ ~-1 red_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 1 if block ~1 ~ ~ red_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 2 if block ~ ~ ~1 red_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 3 if block ~-1 ~ ~ red_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 0 if block ~ ~1 ~-1 orange_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 1 if block ~1 ~1 ~ orange_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 2 if block ~ ~1 ~1 orange_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score blocked_c aoc_calc matches -1 if score dc aoc_calc matches 3 if block ~-1 ~1 ~ orange_concrete store result score blocked_c aoc_calc run scoreboard players add dc aoc_calc 1
execute if score dc aoc_calc matches 4.. run scoreboard players set dc aoc_calc 0

# store turn result (return if cycle)
scoreboard players set cycle aoc_calc 0
execute unless score blocked_c aoc_calc matches -1 store result score cycle aoc_calc run function aoc_2024:logic/day_6/part_2/check/store_turn
execute if score cycle aoc_calc matches 1 run return 1
execute unless score blocked_c aoc_calc matches -1 run return run function aoc_2024:logic/day_6/part_2/check/step

# step forward
execute if score dc aoc_calc matches 0 positioned ~ ~ ~-1 run return run function aoc_2024:logic/day_6/part_2/check/step
execute if score dc aoc_calc matches 1 positioned ~1 ~ ~ run return run function aoc_2024:logic/day_6/part_2/check/step
execute if score dc aoc_calc matches 2 positioned ~ ~ ~1 run return run function aoc_2024:logic/day_6/part_2/check/step
execute if score dc aoc_calc matches 3 positioned ~-1 ~ ~ run return run function aoc_2024:logic/day_6/part_2/check/step
