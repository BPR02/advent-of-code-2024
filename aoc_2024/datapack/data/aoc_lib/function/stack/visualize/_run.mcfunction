# run from aoc_lib:api/stack/visualize
# pop from stack in either FIFO or LIFO order

# get direction
scoreboard players set lib.stack.fifo aoc_calc -1
execute if data storage aoc:register {lib:{stack:{vis:{dir:"FIFO"}}}} store result score lib.stack.fifo aoc_calc run data modify storage aoc:register lib.stack.vis.next set from storage aoc:register lib.stack.target[0]
execute if score lib.stack.fifo aoc_calc matches -1 run data modify storage aoc:register lib.stack.vis.next set from storage aoc:register lib.stack.target[-1]

# get next element
execute if score lib.stack.fifo aoc_calc matches -1 run data remove storage aoc:register lib.stack.target[-1]
execute unless score lib.stack.fifo aoc_calc matches -1 run data remove storage aoc:register lib.stack.target[0]

# stop if there's nothing left in stack
scoreboard players remove lib.stack.len aoc_calc 1
execute unless score lib.stack.len aoc_calc matches 1.. run return 1

# execute stack command
scoreboard players set lib.stack.pause aoc_calc -1
execute if data storage aoc:register {lib:{stack:{vis:{next:{type:"pause"}}}}} run scoreboard players set lib.stack.pause aoc_calc 1
execute if score lib.stack.pause aoc_calc matches -1 if data storage aoc:register {lib:{stack:{vis:{next:{type:"command"}}}}} run function aoc_lib:stack/visualize/run_command with storage aoc:register lib.stack.vis.next

# pause if necessary then run again
execute unless score lib.stack.pause aoc_calc matches -1 run function aoc_lib:stack/visualize/schedule with storage aoc:register lib.stack.vis.next
execute if score lib.stack.pause aoc_calc matches -1 run function aoc_lib:stack/visualize/_run
