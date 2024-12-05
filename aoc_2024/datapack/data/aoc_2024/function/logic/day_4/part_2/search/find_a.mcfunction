execute if block ~ ~ ~ orange_concrete store result score match aoc_calc run function aoc_2024:logic/day_4/part_2/search/check_x-mas

execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_pause {name:"day_4",time:"1"}
execute unless block ~1 ~ ~ air positioned ~1 ~ ~ run function aoc_2024:logic/day_4/part_2/search/find_a
execute if block ~1 ~ ~ air unless block 0 ~ ~1 air positioned 0 ~ ~1 run function aoc_2024:logic/day_4/part_2/search/find_a
