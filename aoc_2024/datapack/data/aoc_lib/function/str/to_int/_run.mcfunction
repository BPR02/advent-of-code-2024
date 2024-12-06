# run from aoc_lib:api/str/to_int
# converts the string to an integer

# convert each character
scoreboard players set lib.str.to_int aoc_calc 0
execute store result score lib.str.to_int.len aoc_calc run data get storage aoc:register lib.str.to_int.val
execute if score lib.str.to_int.len aoc_calc matches 0 run return 0
function aoc_lib:str/to_int/loop

# return value
return run scoreboard players get lib.str.to_int aoc_calc
