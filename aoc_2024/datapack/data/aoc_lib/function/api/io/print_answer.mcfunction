# prints the answer
# input:  score | answer, day, part
#         score | #type (aoc_calc), set to 1 for big_int, 2 for strings
# output: none

tellraw @a ["",{"text":"AoC by BPR","color":"red"}]
execute unless score #type aoc_calc matches 1..2 run tellraw @a ["",{"text":"Day ","color":"dark_green"},{"score":{"name":"day","objective":"aoc_calc"},"color":"aqua"},{"text":" Part ","color":"dark_green"},{"score":{"name":"part","objective":"aoc_calc"},"color":"aqua"},{"text":": ","color":"aqua"},{"score":{"name":"answer","objective":"aoc_calc"},"color":"green"},{"text":" "},{"nbt":"lib.time","storage":"aoc:register","interpret":true}]
# execute if score #type aoc_calc matches 1 run function aoc_library:big_int/as_string
execute if score #type aoc_calc matches 1 run tellraw @a ["",{"text":"Day ","color":"dark_green"},{"score":{"name":"day","objective":"aoc_calc"},"color":"aqua"},{"text":" Part ","color":"dark_green"},{"score":{"name":"part","objective":"aoc_calc"},"color":"aqua"},{"text":": ","color":"aqua"},{"nbt":"big_int_string","storage":"aoc:library","interpret":true,"color":"green"},{"text":" "},{"nbt":"lib.time","storage":"aoc:register","interpret":true}]
# execute if score #type aoc_calc matches 2 run function aoc_library:string/join
execute if score #type aoc_calc matches 2 run tellraw @a ["",{"text":"Day ","color":"dark_green"},{"score":{"name":"day","objective":"aoc_calc"},"color":"aqua"},{"text":" Part ","color":"dark_green"},{"score":{"name":"part","objective":"aoc_calc"},"color":"aqua"},{"text":": ","color":"aqua"},{"nbt":"joined_string","storage":"aoc:library","interpret":true,"color":"green"},{"text":" "},{"nbt":"lib.time","storage":"aoc:register","interpret":true}]
