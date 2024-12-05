# run from aoc_lib:list/merge_sort/_run
# iteratively merge first two elements in a queue

# create temp array with sorted values
data modify storage aoc:register lib.list.sort.temp set value []

# merge the first two elements
data modify storage aoc:register lib.list.sort.merging1 set from storage aoc:register lib.list.sort.sorting[0]
data modify storage aoc:register lib.list.sort.merging2 set from storage aoc:register lib.list.sort.sorting[1]
execute store result score lib.list.sort.len1 aoc_calc run data get storage aoc:register lib.list.sort.merging1
execute store result score lib.list.sort.len2 aoc_calc run data get storage aoc:register lib.list.sort.merging2
function aoc_lib:list/merge_sort/merge

# move to end of "queue"
data remove storage aoc:register lib.list.sort.sorting[0]
data remove storage aoc:register lib.list.sort.sorting[0]
data modify storage aoc:register lib.list.sort.sorting append from storage aoc:register lib.list.sort.temp

# loop until everything is merged
execute if data storage aoc:register lib.list.sort.sorting[1] run function aoc_lib:list/merge_sort/merge_loop
