
# count
function aoc_lib:api/list/count {list:"temp.l2",find:"temp.l1[-1]"}

# add similarity to total
execute store result score a aoc_calc run data get storage aoc:register temp.l1[-1]
scoreboard players operation a aoc_calc *= lib.list.count aoc_calc
scoreboard players operation answer aoc_calc += a aoc_calc

# loop for every value
data remove storage aoc:register temp.l1[-1]
scoreboard players remove len aoc_calc 1
execute if score len aoc_calc matches 1.. run function aoc_2024:logic/day_1/part_2/count
