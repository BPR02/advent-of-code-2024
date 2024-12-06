# run from aoc_lib:str/to_int/_run
# convert first char to digit

# get first char
data modify storage aoc:register lib.char.val set string storage aoc:register lib.str.to_int.val 0 1
function aoc_lib:char/to_int with storage aoc:register lib.char

# add to current value (shift current over by mulitplying 10)
scoreboard players operation lib.str.to_int aoc_calc *= 10 aoc_const
scoreboard players operation lib.str.to_int aoc_calc += lib.char.to_int aoc_calc

# stop if all digits counted
scoreboard players remove lib.str.to_int.len aoc_calc 1
execute if score lib.str.to_int.len aoc_calc matches ..0 run return 1

# continue for next digit
data modify storage aoc:register lib.str.to_int.val set string storage aoc:register lib.str.to_int.val 1
function aoc_lib:str/to_int/loop
