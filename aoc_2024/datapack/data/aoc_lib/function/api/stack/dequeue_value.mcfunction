# pop a value from the beginning of stack
#...
# input:  name: stack name
#         out: location to put value into
#...
# output: none
#...
# mutate: first stack element is deleted

$function aoc_lib:stack/dequeue/value {stack_name:$(name)}
$data modify storage aoc:register $(out) set from storage aoc:register lib.stack.val
