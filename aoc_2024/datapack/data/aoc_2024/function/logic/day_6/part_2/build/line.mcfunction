data modify storage aoc:register temp.char set string storage aoc:register temp.line 0 1
scoreboard players set ret aoc_calc 0
setblock ~ ~ ~ light_gray_concrete
execute store result score ret aoc_calc if data storage aoc:register {temp:{char:'#'}} run setblock ~ ~2 ~ red_concrete
execute if score ret aoc_calc matches 0 store result score ret aoc_calc if data storage aoc:register {temp:{char:'^'}} run setblock ~ ~2 ~ magenta_glazed_terracotta[facing=south]
execute if block ~ ~2 ~ magenta_glazed_terracotta positioned ~ ~2 ~ run function aoc_lib:api/stack/push_pos {name:"ctx"}

execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_block {name:"day_6",id:"light_gray_concrete"}
execute if score visualize aoc_calc matches 1 if block ~ ~2 ~ red_concrete positioned ~ ~1 ~ run function aoc_lib:api/stack/push_block {name:"day_6",id:"red_concrete"}
execute if score visualize aoc_calc matches 1 if block ~ ~2 ~ magenta_glazed_terracotta positioned ~ ~2 ~ run function aoc_lib:api/stack/push_block {name:"day_6",id:"magenta_glazed_terracotta[facing=south]"}

data modify storage aoc:register temp.line set string storage aoc:register temp.line 1
scoreboard players remove line_len aoc_calc 1
execute if score line_len aoc_calc matches 1.. positioned ~1 ~ ~ run function aoc_2024:logic/day_6/part_2/build/line
