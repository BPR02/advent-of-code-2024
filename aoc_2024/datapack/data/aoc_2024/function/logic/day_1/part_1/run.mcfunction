data merge storage aoc:register {temp:{l1:[],l2:[]}}

# split input into two lists
function aoc_lib:api/list/iter {list:"input",function:"aoc_2024:logic/day_1/part_1/append"}

# sort each list
function aoc_lib:api/list/sort_int {list:"temp.l1"}
function aoc_lib:api/list/sort_int {list:"temp.l2"}

# for each element, compare
scoreboard players set answer aoc_calc 0
execute store result score len aoc_calc run data get storage aoc:register temp.l1
function aoc_2024:logic/day_1/part_1/compare
