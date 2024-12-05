# run from aoc_lib:api/char/compare

# convert to ascii integer value
execute store result score lib.compare.a aoc_calc run function aoc_lib:char/to_ascii with storage aoc:register lib.char.a
execute store result score lib.compare.b aoc_calc run function aoc_lib:char/to_ascii with storage aoc:register lib.char.b
# compare the integers
return run function aoc_lib:int/compare
