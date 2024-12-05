# run from aoc_lib:api/char/to_int

# check static storage for value mapping
$execute unless data storage aoc:register static.char.digits.$(val) store result score lib.char.to_int aoc_calc run return -1
$execute store result score lib.char.to_int aoc_calc run return run data get storage aoc:register static.char.digits.$(val)
