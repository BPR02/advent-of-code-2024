# append pause command to the stack
#...
# input:  name: stack name
#         time: length to wait (same as schedule command)
#...
# output: none

$data modify storage aoc:register lib.stack._.$(name) append value {type:"pause",time:$(time)}
