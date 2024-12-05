# run from aoc_lib:list/merge_sort/_run


# create temp array with sorted values
data modify storage aoc:register lib.list.temp set value []

# merge the first two elements
data modify storage aoc:register lib.list.merging1 set from storage aoc:register lib.list.sorting[0]
data modify storage aoc:register lib.list.merging2 set from storage aoc:register lib.list.sorting[1]
execute store result score lib.list.len1 aoc_calc run data get storage aoc:register lib.list.merging1
execute store result score lib.list.len2 aoc_calc run data get storage aoc:register lib.list.merging2
function aoc_lib:list/merge_sort/merge

# move to end of "queue"
data modify storage aoc:register lib.list.sorting append from storage aoc:register lib.list.temp
data remove storage aoc:register lib.list.sorting[0]
data remove storage aoc:register lib.list.sorting[1]

# loop until everything is merged
execute unless data storage aoc:register lib.list.sorting[1] run function aoc_lib:list/merge_sort/merge_loop
