# already stored, a cycle has been found
execute if score dc aoc_calc matches 0 if block ~ ~-3 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 1 if block ~ ~-4 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 2 if block ~ ~-5 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 3 if block ~ ~-6 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 0 if block ~ ~-7 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 1 if block ~ ~-8 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 2 if block ~ ~-9 ~ cyan_concrete run return 1
execute if score dc aoc_calc matches 3 if block ~ ~-10 ~ cyan_concrete run return 1

# store turn
execute if score dc aoc_calc matches 0 positioned ~ ~-7 ~ run function aoc_lib:api/stack/push_block {name:"ctx",id:"air"}
execute if score dc aoc_calc matches 0 run setblock ~ ~-7 ~ cyan_concrete

execute if score dc aoc_calc matches 1 positioned ~ ~-8 ~ run function aoc_lib:api/stack/push_block {name:"ctx",id:"air"}
execute if score dc aoc_calc matches 1 run setblock ~ ~-8 ~ cyan_concrete

execute if score dc aoc_calc matches 2 positioned ~ ~-9 ~ run function aoc_lib:api/stack/push_block {name:"ctx",id:"air"}
execute if score dc aoc_calc matches 2 run setblock ~ ~-9 ~ cyan_concrete

execute if score dc aoc_calc matches 3 positioned ~ ~-10 ~ run function aoc_lib:api/stack/push_block {name:"ctx",id:"air"}
execute if score dc aoc_calc matches 3 run setblock ~ ~-10 ~ cyan_concrete

return 0
