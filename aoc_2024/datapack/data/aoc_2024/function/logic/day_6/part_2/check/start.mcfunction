# check if there's already an obstacle here
execute if score d aoc_calc matches 0 if block ~ ~ ~-1 red_concrete run return 0
execute if score d aoc_calc matches 1 if block ~1 ~ ~ red_concrete run return 0
execute if score d aoc_calc matches 2 if block ~ ~ ~1 red_concrete run return 0
execute if score d aoc_calc matches 3 if block ~-1 ~ ~ red_concrete run return 0

execute if score d aoc_calc matches 0 if block ~ ~3 ~-1 gold_block run return 0
execute if score d aoc_calc matches 1 if block ~1 ~3 ~ gold_block run return 0
execute if score d aoc_calc matches 2 if block ~ ~3 ~1 gold_block run return 0
execute if score d aoc_calc matches 3 if block ~-1 ~3 ~ gold_block run return 0

# check if obstacle blocks path
execute if score d aoc_calc matches 0 if block ~ ~-1 ~-1 gray_concrete run return 0
execute if score d aoc_calc matches 1 if block ~1 ~-1 ~ gray_concrete run return 0
execute if score d aoc_calc matches 2 if block ~ ~-1 ~1 gray_concrete run return 0
execute if score d aoc_calc matches 3 if block ~-1 ~-1 ~ gray_concrete run return 0

# place new obstacle
execute if score d aoc_calc matches 0 run setblock ~ ~1 ~-1 orange_concrete
execute if score d aoc_calc matches 1 run setblock ~1 ~1 ~ orange_concrete
execute if score d aoc_calc matches 2 run setblock ~ ~1 ~1 orange_concrete
execute if score d aoc_calc matches 3 run setblock ~-1 ~1 ~ orange_concrete

# check for cycle
scoreboard players operation dc aoc_calc = d aoc_calc
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/setup {name:"ctx_vis"}
execute if function aoc_2024:logic/day_6/part_2/check/step run function aoc_2024:logic/day_6/part_2/check/mark
function aoc_lib:api/stack/pop_all {name:"ctx",direction:"LIFO"}
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_pause {name:"day_6",time:"1"}
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/extend {to:"day_6",from:"ctx_vis"}

# remove obstacle
execute if score d aoc_calc matches 0 run setblock ~ ~1 ~-1 air
execute if score d aoc_calc matches 1 run setblock ~1 ~1 ~ air
execute if score d aoc_calc matches 2 run setblock ~ ~1 ~1 air
execute if score d aoc_calc matches 3 run setblock ~-1 ~1 ~ air
