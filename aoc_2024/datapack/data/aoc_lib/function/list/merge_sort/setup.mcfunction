# run from aoc_lib:list/merge_sort/_run

# get last value in to_sort array and put into a single element array, then push to sorting array
data modify storage aoc:register lib.list.entry set value []
data modify storage aoc:register lib.list.entry append from storage aoc:register lib.list.to_sort[-1]
data modify storage aoc:register lib.list.sorting append from storage aoc:register lib.list.entry

# remove value from to_sort array, and continue for each value
data remove storage aoc:register lib.list.to_sort[-1]
scoreboard players remove lib.list.len.t aoc_calc 1
execute if score lib.list.len.t aoc_calc matches 1.. run function aoc_lib:list/merge_sort/setup
