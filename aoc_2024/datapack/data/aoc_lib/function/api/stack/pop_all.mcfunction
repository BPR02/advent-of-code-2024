# pop everything from stack for visualization
#...
# input:  name: stack name
#         direction: "FIFO" or "LIFO" (queue or stack)
#...
# output: none

$data modify storage aoc:register lib.stack.pop.dir set value $(direction)
$data modify storage aoc:register lib.stack.target set from storage aoc:register lib.stack._.$(name)
$data modify storage aoc:register lib.stack._.$(name) set value []
execute store result score lib.stack.len aoc_calc run data get storage aoc:register lib.stack.target
function aoc_lib:stack/pop_all/_run
