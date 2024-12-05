execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/setup {name:"day_4"}
execute positioned 0 64 0 run function aoc_2024:logic/day_4/part_1/build/all
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_pause {name:"day_4",time:"5s"}
execute positioned 0 64 0 run function aoc_2024:logic/day_4/part_1/search/find_x
