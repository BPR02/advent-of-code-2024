# run from aoc_lib:api/list/sort_*
# bottom up merge sort (using a queue instead of separate list)

# get array length
execute store result score lib.list.sort.len aoc_calc run data get storage aoc:register lib.list.sort.to_sort
# return early if the list is already sorted
execute if score lib.list.sort.len aoc_calc matches ..1 run return 1

# split array into list of lists with a single element (reverses it too due to push/pop optimization)
data modify storage aoc:register lib.list.sort.sorting set value []
function aoc_lib:list/merge_sort/setup

# iteratively merge first two elements of array
function aoc_lib:list/merge_sort/merge_loop

# return list
data modify storage aoc:register lib.list.sort.to_sort set from storage aoc:register lib.list.sort.sorting[-1]
