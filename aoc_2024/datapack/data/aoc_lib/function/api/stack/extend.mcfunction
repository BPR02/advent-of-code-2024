# copy everything from one stack and to another
#...
# input:  to: target stack name
#         from: source stack name
#...
# output: none
#...
# mutate: "to" stack contains everything from "from" stack

$data modify storage aoc:register lib.stack._.$(to) append from storage aoc:register lib.stack._.$(from)[]
