# run from aoc_lib:api/str/find
# finds a substring in the string

# setup search indices
execute store result storage aoc:register lib.str.find.start int 1 run scoreboard players get lib.str.find.start aoc_calc
execute store result score lib.str.find.end aoc_calc run data get storage aoc:register lib.str.find.match
execute store result storage aoc:register lib.str.find.end int 1 run scoreboard players operation lib.str.find.end aoc_calc += lib.str.find.start aoc_calc

# get index of first match
execute store result score lib.str.find.in_len aoc_calc run data get storage aoc:register lib.str.find.in
execute store result score lib.str.find.res aoc_calc run function aoc_lib:str/find/loop with storage aoc:register lib.str.find

# return result (-1 if not in string, else the index of the found substring)
execute if score lib.str.find.res aoc_calc matches 0 store result score lib.str.find.index aoc_calc run return -1
return run scoreboard players operation lib.str.find.index aoc_calc = lib.str.find.start aoc_calc
