
# split the string
data modify storage aoc:register temp.delim set value "   "
function aoc_lib:api/str/split {in:"lib.list.e",match:"temp.delim",out:"temp.strings"}

# convert each string to int
execute store result storage aoc:register temp.int1 int 1 run function aoc_lib:api/str/to_int {val:"temp.strings[0]"}
execute store result storage aoc:register temp.int2 int 1 run function aoc_lib:api/str/to_int {val:"temp.strings[1]"}

# add the two ints to separate lists
data modify storage aoc:register temp.l1 append from storage aoc:register temp.int1
data modify storage aoc:register temp.l2 append from storage aoc:register temp.int2
