data modify storage aoc:register temp.line set from storage aoc:register input[0]
execute store result score line_len aoc_calc run data get storage aoc:register temp.line
function aoc_2024:logic/day_4/part_1/build/line

data remove storage aoc:register input[0]
scoreboard players remove line_count aoc_calc 1
execute if score line_count aoc_calc matches 1.. positioned ~ ~ ~1 run function aoc_2024:logic/day_4/part_1/build/all
