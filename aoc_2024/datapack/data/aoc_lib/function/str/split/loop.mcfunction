# run from aoc_lib:str/split/_run
# split at each delimiter

# find delimiter
execute store result storage aoc:register lib.str.split.end int 1 run function aoc_lib:str/find/_run

# extract everything before the delimiter
execute if score lib.str.find.index aoc_calc matches -1 run function aoc_lib:str/split/extract_last with storage aoc:register lib.str.split
execute unless score lib.str.find.index aoc_calc matches -1 run function aoc_lib:str/split/extract with storage aoc:register lib.str.split
data modify storage aoc:register lib.str.split.res append from storage aoc:register lib.str.split.extract

# continue until all delimiters are found
execute if score lib.str.find.index aoc_calc matches -1 run return 1
execute store result storage aoc:register lib.str.split.start int 1 run scoreboard players operation lib.str.find.start aoc_calc = lib.str.find.end aoc_calc
function aoc_lib:str/split/loop
