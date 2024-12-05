# run from aoc_lib:api/char/to_ascii

# check static storage for value mapping
$execute unless data storage aoc:register static.char.to_ascii.$(val) store result score lib.char.to_ascii aoc_calc run return -1
$execute store result score lib.char.to_ascii aoc_calc run return run data get storage aoc:register static.char.to_ascii.$(val)
