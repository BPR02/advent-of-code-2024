# run from aoc_lib:api/stack/pop_value
# pop value from stack (LIFO

$data modify storage aoc:register lib.stack.val set from storage aoc:register lib.stack._.$(stack_name)[-1].value
$data remove storage aoc:register lib.stack._.$(stack_name)[-1]
