#
# input:  day:  puzzle day [1..25]
#         part: puzzle part [1..2]
#

scoreboard players reset * aoc_calc
scoreboard players set visualize aoc_calc 1
$scoreboard players set day aoc_calc $(day)
$scoreboard players set part aoc_calc $(part)
$function aoc_2024:load_input/day_$(day)
execute store result score line_count aoc_calc run data get storage aoc:register input
$function aoc_2024:logic/day_$(day)/part_$(part)/run
$function aoc_2024:logic/day_$(day)/part_$(part)/clean_up
$schedule function aoc_2024:logic/day_$(day)/part_$(part)/visualize 5s
