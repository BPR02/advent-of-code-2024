# obstacle already placed
execute if score d aoc_calc matches 0 if block ~ ~3 ~-1 gold_block run setblock ~ ~4 ~-1 coal_block
execute if score d aoc_calc matches 0 if block ~ ~3 ~-1 gold_block run return 0
execute if score d aoc_calc matches 1 if block ~1 ~3 ~ gold_block run setblock ~1 ~4 ~ coal_block
execute if score d aoc_calc matches 1 if block ~1 ~3 ~ gold_block run return 0
execute if score d aoc_calc matches 2 if block ~ ~3 ~1 gold_block run setblock ~ ~4 ~1 coal_block
execute if score d aoc_calc matches 2 if block ~ ~3 ~1 gold_block run return 0
execute if score d aoc_calc matches 3 if block ~-1 ~3 ~ gold_block run setblock ~-1 ~4 ~ coal_block
execute if score d aoc_calc matches 3 if block ~-1 ~3 ~ gold_block run return 0

# place obstacle
scoreboard players add answer aoc_calc 1
execute if score d aoc_calc matches 0 run setblock ~ ~3 ~-1 gold_block
execute if score d aoc_calc matches 1 run setblock ~1 ~3 ~ gold_block
execute if score d aoc_calc matches 2 run setblock ~ ~3 ~1 gold_block
execute if score d aoc_calc matches 3 run setblock ~-1 ~3 ~ gold_block

execute if score visualize aoc_calc matches 1 if score d aoc_calc matches 0 positioned ~ ~-1 ~-1 run function aoc_lib:api/stack/push_block {name:"day_6",id:"gold_block"}
execute if score visualize aoc_calc matches 1 if score d aoc_calc matches 1 positioned ~1 ~-1 ~ run function aoc_lib:api/stack/push_block {name:"day_6",id:"gold_block"}
execute if score visualize aoc_calc matches 1 if score d aoc_calc matches 2 positioned ~ ~-1 ~1 run function aoc_lib:api/stack/push_block {name:"day_6",id:"gold_block"}
execute if score visualize aoc_calc matches 1 if score d aoc_calc matches 3 positioned ~-1 ~-1 ~ run function aoc_lib:api/stack/push_block {name:"day_6",id:"gold_block"}
return 1
