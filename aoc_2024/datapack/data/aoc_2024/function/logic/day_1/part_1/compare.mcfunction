
# get values
execute store result score a aoc_calc run data get storage aoc:register temp.l1[-1]
execute store result score b aoc_calc run data get storage aoc:register temp.l2[-1]

# add difference to total
scoreboard players operation a aoc_calc -= b aoc_calc
execute if score a aoc_calc matches ..-1 run scoreboard players operation a aoc_calc *= -1 aoc_const
scoreboard players operation answer aoc_calc += a aoc_calc

# loop for every value
data remove storage aoc:register temp.l1[-1]
data remove storage aoc:register temp.l2[-1]
scoreboard players remove len aoc_calc 1
execute if score len aoc_calc matches 1.. run function aoc_2024:logic/day_1/part_1/compare
