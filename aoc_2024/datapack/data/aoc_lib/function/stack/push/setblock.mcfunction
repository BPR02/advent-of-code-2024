# run from aoc_lib:api/stack/push_block
# push setblock command onto stack

$data modify storage aoc:register lib.stack._.$(stack_name) append value {"type":"command","command":"setblock $(x) $(y) $(z) $(id)"}