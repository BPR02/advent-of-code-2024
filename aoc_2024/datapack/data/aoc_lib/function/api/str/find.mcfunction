# find a substring in a string
#...
# input:  in: location of string to split
#         find: location of string to find
#         start: index to start search from
#...
# output: index of the substring in the string
#         -1 if substring is not in the string
#...
# mutate: score lib.str.find.index is set to the output
#         score lib.str.find.end is set to the index of the last char of the substring

$data modify storage aoc:register lib.str.find.in set from storage aoc:register $(in)
$data modify storage aoc:register lib.str.find.match set from storage aoc:register $(match)
$scoreboard players set lib.str.find.start set value $(start)
return run function aoc_lib:str/find/_run
