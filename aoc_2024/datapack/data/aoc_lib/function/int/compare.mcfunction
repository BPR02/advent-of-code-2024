execute if score lib.compare.a aoc_calc < lib.compare.b aoc_calc run return run scoreboard players set lib.compare.res aoc_calc -1
execute if score lib.compare.a aoc_calc > lib.compare.b aoc_calc run return run scoreboard players set lib.compare.res aoc_calc 1
return run scoreboard players set lib.compare.res aoc_calc 0
