# append a position to the stack
#...
# input:  name: stack name
#         function: function name
#...
# output: none
#...
# mutate: absolute coordinates added to the stack

# get block pos
summon marker ~ ~ ~ {Tags:["aoc_lib.stack.marker"]}
data modify storage aoc:register lib.stack.temp.abs set from entity @e[type=marker,tag=aoc_lib.stack.marker,limit=1,distance=..0.1] Pos
kill @e[type=marker,tag=aoc_lib.stack.marker,limit=1,distance=..0.1]
data modify storage aoc:register lib.stack.temp.x set from storage aoc:register lib.stack.temp.abs[0]
data modify storage aoc:register lib.stack.temp.y set from storage aoc:register lib.stack.temp.abs[1]
data modify storage aoc:register lib.stack.temp.z set from storage aoc:register lib.stack.temp.abs[2]
# store pos function in stack
$data modify storage aoc:register lib.stack.temp.stack_name set value $(name)
$data modify storage aoc:register lib.stack.temp.function_name set value "$(function)"
function aoc_lib:stack/push/positioned_function with storage aoc:register lib.stack.temp
