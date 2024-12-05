# run from aoc_lib:api/char/to_upper

# check static storage for value mapping
$execute unless data storage aoc:register static.char.to_upper.$(val) store result score lib.char.to_upper aoc_calc run return -1
$execute store result score lib.char.to_upper aoc_calc run return run data modify storage aoc:register lib.char.val set from storage aoc:register static.char.to_upper.$(val)
