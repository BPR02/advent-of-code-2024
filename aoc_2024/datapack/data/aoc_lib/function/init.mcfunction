gamerule maxCommandChainLength 2147483647

scoreboard objectives add aoc_calc dummy
scoreboard objectives add aoc_const dummy

scoreboard players set 10 aoc_const 10
scoreboard players set 100 aoc_const 100
scoreboard players set -1 aoc_const -1
scoreboard players set 2 aoc_const 2
scoreboard players set 1000 aoc_const 1000
scoreboard players set max_int aoc_const 2147483647
scoreboard players set min_int aoc_const -2147483648

#declare storage aoc:register
data modify storage aoc:register static.char.to_ascii set value {a:97,b:98,c:99,d:100,e:101,f:102,g:103,h:104,i:105,j:106,k:107,l:108,m:109,n:110,o:111,p:112,q:113,r:114,s:115,t:116,u:117,v:118,w:119,x:120,y:121,z:122,A:65,B:66,C:67,D:68,E:69,F:70,G:71,H:72,I:73,J:74,K:75,L:76,M:77,N:78,O:79,P:80,Q:81,R:82,S:83,T:84,U:85,V:86,W:87,X:88,Y:89,Z:90}
data modify storage aoc:register static.char.to_lower set value {a:'a',b:'b',c:'c',d:'d',e:'e',f:'f',g:'g',h:'h',i:'i',j:'j',k:'k',l:'l',m:'m',n:'n',o:'o',p:'p',q:'q',r:'r',s:'s',t:'t',u:'u',v:'v',w:'w',x:'x',y:'y',z:'z',A:'a',B:'b',C:'c',D:'d',E:'e',F:'f',G:'g',H:'h',I:'i',J:'j',K:'k',L:'l',M:'m',N:'n',O:'o',P:'p',Q:'q',R:'r',S:'s',T:'t',U:'u',V:'v',W:'w',X:'x',Y:'y',Z:'z'}
data modify storage aoc:register static.char.to_upper set value {a:'A',b:'B',c:'C',d:'D',e:'E',f:'F',g:'G',h:'H',i:'I',j:'J',k:'K',l:'L',m:'M',n:'N',o:'O',p:'P',q:'Q',r:'R',s:'S',t:'T',u:'U',v:'V',w:'W',x:'X',y:'Y',z:'Z',A:'A',B:'B',C:'C',D:'D',E:'E',F:'F',G:'G',H:'H',I:'I',J:'J',K:'K',L:'L',M:'M',N:'N',O:'O',P:'P',Q:'Q',R:'R',S:'S',T:'T',U:'U',V:'V',W:'W',X:'X',Y:'Y',Z:'Z'}
data modify storage aoc:register static.char.digits set value {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,0:0}
