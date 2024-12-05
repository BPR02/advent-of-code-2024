# run from aoc_lib:list/merge_sort/_run
# split the array into separate single-element lists

# get last value in to_sort array and put into a single element array, then push to sorting array
data modify storage aoc:register lib.list.sort.entry set value []
data modify storage aoc:register lib.list.sort.entry append from storage aoc:register lib.list.sort.to_sort[-1]
data modify storage aoc:register lib.list.sort.sorting append from storage aoc:register lib.list.sort.entry

# remove value from to_sort array, and continue for each value
data remove storage aoc:register lib.list.sort.to_sort[-1]
scoreboard players remove lib.list.sort.len aoc_calc 1
execute if score lib.list.sort.len aoc_calc matches 1.. run function aoc_lib:list/merge_sort/setup
