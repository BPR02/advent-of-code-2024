# append a block position to the stack
#...
# input:  name: stack name
#         id: block id
#...
# output: none
#...
# mutate: command with setblock command is added to stack

# get block pos
setblock ~ ~ ~ jukebox
data modify storage aoc:register lib.stack.temp set from block ~ ~ ~
# store setblock function in stack
$setblock ~ ~ ~ $(id)
$data modify storage aoc:register lib.stack.temp.id set value $(id)
$data modify storage aoc:register lib.stack.temp.stack_name set value $(name)
function aoc_lib:stack/push/setblock with storage aoc:register lib.stack.temp
