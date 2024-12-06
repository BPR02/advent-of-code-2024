# splits a string into a list of strings based on a delimeter
#...
# input:  in: location of string to split
#         match: location of string to split by
#         out: location to put resulting list
#...
# output: none

$data modify storage aoc:register lib.str.split.in set from storage aoc:register $(in)
$data modify storage aoc:register lib.str.split.match set from storage aoc:register $(match)
function aoc_lib:str/split/_run
$data modify storage aoc:register $(out) set from storage aoc:register lib.str.split.res
