data modify storage aoc:register temp.char set string storage aoc:register temp.line 0 1
scoreboard players set ret aoc_calc 0
execute store result score ret aoc_calc if data storage aoc:register {temp:{char:'X'}} run setblock ~ ~ ~ lime_concrete
execute if score ret aoc_calc matches 0 store result score ret aoc_calc if data storage aoc:register {temp:{char:'M'}} run setblock ~ ~ ~ yellow_concrete
execute if score ret aoc_calc matches 0 store result score ret aoc_calc if data storage aoc:register {temp:{char:'A'}} run setblock ~ ~ ~ orange_concrete
execute if score ret aoc_calc matches 0 store result score ret aoc_calc if data storage aoc:register {temp:{char:'S'}} run setblock ~ ~ ~ red_concrete

execute if score visualize aoc_calc matches 1 if block ~ ~ ~ lime_concrete run function aoc_lib:api/stack/push_block {name:"day_4",id:"lime_concrete"}
execute if score visualize aoc_calc matches 1 if block ~ ~ ~ yellow_concrete run function aoc_lib:api/stack/push_block {name:"day_4",id:"yellow_concrete"}
execute if score visualize aoc_calc matches 1 if block ~ ~ ~ orange_concrete run function aoc_lib:api/stack/push_block {name:"day_4",id:"orange_concrete"}
execute if score visualize aoc_calc matches 1 if block ~ ~ ~ red_concrete run function aoc_lib:api/stack/push_block {name:"day_4",id:"red_concrete"}

data modify storage aoc:register temp.line set string storage aoc:register temp.line 1
scoreboard players remove line_len aoc_calc 1
execute if score line_len aoc_calc matches 1.. positioned ~1 ~ ~ run function aoc_2024:logic/day_4/part_2/build/line
