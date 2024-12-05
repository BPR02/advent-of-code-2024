$data modify storage aoc:register lib.stack.vis.dir set value $(direction)
$data modify storage aoc:register lib.stack.target set from storage aoc:register lib.stack._.$(name)
$data remove storage aoc:register lib.stack._.$(name)
execute store result score lib.stack.len aoc_calc run data get storage aoc:register lib.stack.target
function aoc_lib:stack/visualize/schedule {time:"5s"}
