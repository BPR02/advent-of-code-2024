# pop everything from stack for visualization
#...
# input:  name: stack name
#         direction: "FIFO" or "LIFO" (queue or stack)
#...
# output: none

$data modify storage aoc:register lib.stack.vis.dir set value $(direction)
$data modify storage aoc:register lib.stack.target set from storage aoc:register lib.stack._.$(name)
$data remove storage aoc:register lib.stack._.$(name)
execute store result score lib.stack.len aoc_calc run data get storage aoc:register lib.stack.target
function aoc_lib:stack/visualize/schedule {time:"5s"}
