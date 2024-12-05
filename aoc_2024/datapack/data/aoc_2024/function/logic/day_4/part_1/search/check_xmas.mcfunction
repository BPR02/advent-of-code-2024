# right
execute if block ~1 ~ ~ yellow_concrete if block ~2 ~ ~ orange_concrete if block ~3 ~ ~ red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/r
# left
execute if block ~-1 ~ ~ yellow_concrete if block ~-2 ~ ~ orange_concrete if block ~-3 ~ ~ red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/l
# up
execute if block ~ ~ ~1 yellow_concrete if block ~ ~ ~2 orange_concrete if block ~ ~ ~3 red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/u
# down
execute if block ~ ~ ~-1 yellow_concrete if block ~ ~ ~-2 orange_concrete if block ~ ~ ~-3 red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/d
# diagonal right down
execute if block ~1 ~ ~-1 yellow_concrete if block ~2 ~ ~-2 orange_concrete if block ~3 ~ ~-3 red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/s1
# diagonal right up
execute if block ~1 ~ ~1 yellow_concrete if block ~2 ~ ~2 orange_concrete if block ~3 ~ ~3 red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/s2
# diagonal left down
execute if block ~-1 ~ ~-1 yellow_concrete if block ~-2 ~ ~-2 orange_concrete if block ~-3 ~ ~-3 red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/s3
# diagonal left up
execute if block ~-1 ~ ~1 yellow_concrete if block ~-2 ~ ~2 orange_concrete if block ~-3 ~ ~3 red_concrete run function aoc_2024:logic/day_4/part_1/search/mark/s4
