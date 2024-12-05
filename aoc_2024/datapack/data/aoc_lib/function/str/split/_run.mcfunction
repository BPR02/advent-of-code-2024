# run from aoc_lib:api/str/split
# splits a string into a list according to a delimiter

# setup list of split strings
data modify storage aoc:register lib.str.split.res set value []

# setup delimiter search
data modify storage aoc:register lib.str.find.in set from storage aoc:register lib.str.split.in
data modify storage aoc:register lib.str.find.match set from storage aoc:register lib.str.split.match
scoreboard players set lib.str.find.start aoc_calc 0

# search and split at delimiter
data modify storage aoc:register lib.str.split.start set value 0
function aoc_lib:str/split/loop
