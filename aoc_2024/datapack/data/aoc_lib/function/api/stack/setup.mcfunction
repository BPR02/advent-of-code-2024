# create a new stack
#...
# input:  name: stack name (id)
#...
# output: none

$data modify storage aoc:register lib.stack._.$(name) set value []
