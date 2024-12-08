# run from aoc_lib:api/stack/pop_all
# pop from stack in either FIFO or LIFO order

# get direction
scoreboard players set lib.stack.fifo aoc_calc -1
execute if data storage aoc:register {lib:{stack:{pop:{dir:"FIFO"}}}} store result score lib.stack.fifo aoc_calc run data modify storage aoc:register lib.stack.pop.next set from storage aoc:register lib.stack.target[0]
execute if score lib.stack.fifo aoc_calc matches -1 run data modify storage aoc:register lib.stack.pop.next set from storage aoc:register lib.stack.target[-1]

# get next element
execute if score lib.stack.fifo aoc_calc matches -1 run data remove storage aoc:register lib.stack.target[-1]
execute unless score lib.stack.fifo aoc_calc matches -1 run data remove storage aoc:register lib.stack.target[0]

# execute stack command
execute if data storage aoc:register {lib:{stack:{pop:{next:{type:"command"}}}}} run function aoc_lib:stack/pop_all/run_command with storage aoc:register lib.stack.pop.next

# run for every element in the stack
scoreboard players remove lib.stack.len aoc_calc 1
execute unless score lib.stack.len aoc_calc matches 1.. run return 1
function aoc_lib:stack/pop_all/_run
