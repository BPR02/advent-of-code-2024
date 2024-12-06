execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/setup {name:"day_6"}
function aoc_lib:api/stack/setup {name:"ctx"}
function aoc_2024:logic/day_6/part_2/clean_up
execute positioned 0 64 0 run function aoc_2024:logic/day_6/part_2/build/all
execute if score visualize aoc_calc matches 1 run function aoc_lib:api/stack/push_pause {name:"day_6",time:"5s"}

function aoc_lib:api/stack/pop_value {name:"ctx",out:"temp.start"}
function aoc_2024:logic/day_6/part_2/path/start with storage aoc:register temp
