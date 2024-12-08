# run from aoc_lib:api/stack/push_positioned_function
# push positioned function command onto stack

$data modify storage aoc:register lib.stack._.$(stack_name) append value {"type":"command","command":"execute positioned $(x) $(y) $(z) run function $(function_name)"}
