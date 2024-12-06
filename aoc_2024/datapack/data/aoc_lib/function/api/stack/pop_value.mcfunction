# pop a value from the end of the stack
#...
# input:  name: stack name
#         out: location to put value into
#...
# output: none
#...
# mutate: last stack element is deleted

$function aoc_lib:stack/pop/value {stack_name:$(name)}
$data modify storage aoc:register $(out) set from storage aoc:register lib.stack.val
