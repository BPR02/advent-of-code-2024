scoreboard players set d aoc_calc 0
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_block {name:"day_6",id:"air"}
$execute positioned $(start) run function aoc_2024:logic/day_6/part_2/path/step
