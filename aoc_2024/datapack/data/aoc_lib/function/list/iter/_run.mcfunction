# run from aoc_lib:api/list/iter
# runs a command for each element in the list

# loop each element
execute store result score lib.list.iter.len aoc_calc run data get storage aoc:register lib.list.iter.list
function aoc_lib:list/iter/loop
