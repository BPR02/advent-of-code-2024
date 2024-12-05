# run from aoc_lib:api/char/is_alpha

# check static storage for value mapping
$execute unless data storage aoc:register static.char.to_digit.$(val) store result score lib.char.is_alpha aoc_calc run return -1
$execute store result score lib.char.is_alpha aoc_calc run return run data get storage aoc:register static.char.to_digit.$(val)
