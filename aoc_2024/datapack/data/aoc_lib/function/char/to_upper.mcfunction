$execute unless data storage aoc:register static.char.to_upper.$(val) store result score lib.char.to_upper aoc_calc run return -1
$data modify storage aoc:register lib.char.val set from storage aoc:register static.char.to_upper.$(val)
return run scoreboard players set lib.char.to_upper aoc_calc 1
