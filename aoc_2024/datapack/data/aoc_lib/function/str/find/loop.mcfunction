# run from aoc_lib:str/find/_run
# check each "slice" of string

# check if substring matches
data modify storage aoc:register lib.str.find.check set from storage aoc:register lib.str.find.match
$execute store result score diff aoc_calc run data modify storage aoc:register lib.str.find.check set string storage aoc:register lib.str.find.in $(start) $(end)

# return if substring is found
execute if score diff aoc_calc matches 0 run return 1

# move one char over
execute store result storage aoc:register lib.str.find.start int 1 run scoreboard players add lib.str.find.start aoc_calc 1
execute store result storage aoc:register lib.str.find.end int 1 run scoreboard players add lib.str.find.end aoc_calc 1

# continue until entire string has been checked
execute if score lib.str.find.end aoc_calc > lib.str.find.in_len aoc_calc run return 0
return run function aoc_lib:str/find/loop with storage aoc:register lib.str.find
