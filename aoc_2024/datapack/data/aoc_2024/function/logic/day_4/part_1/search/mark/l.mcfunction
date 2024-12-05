scoreboard players add answer aoc_calc 1
execute unless score visualize aoc_calc matches 1 run return 1
execute positioned ~ ~1 ~ run function aoc_lib:api/stack/push_block {name:"day_4",id:"gold_block"}
execute positioned ~-1 ~1 ~ run function aoc_lib:api/stack/push_block {name:"day_4",id:"gold_block"}
execute positioned ~-2 ~1 ~ run function aoc_lib:api/stack/push_block {name:"day_4",id:"gold_block"}
execute positioned ~-3 ~1 ~ run function aoc_lib:api/stack/push_block {name:"day_4",id:"gold_block"}
