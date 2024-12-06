# run from aoc_lib:api/stack/dequeue_value
# pop value from stack (FIFO)

$data modify storage aoc:register lib.stack.val set from storage aoc:register lib.stack._.$(stack_name)[0].value
$data remove storage aoc:register lib.stack._.$(stack_name)[0]
