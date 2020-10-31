Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lux={'health':490,'mana':334,'melee':550,'armor':18.72}
>>> lux
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux={'health':490,'health':800,'mana':334,'melee':550,'armor':18.72}
>>> lux['health']
800
>>> x={100:'hundred', False:0, 3.5:[3.5,3.5]}
>>> x
{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
>>> x[3.5]
[3.5, 3.5]
>>> x[100]
'hundred'
>>> x['False']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x['False']
KeyError: 'False'
>>> x[False]
0
>>> y={9:{9:9}}
>>> y[9]
{9: 9}
>>> x={}
>>> x
{}
>>> x=dict()
>>> x
{}
>>> lux1=dict(health=490,mana=334,melee=550,armor=18.72)
>>> lux1
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux2=dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
>>> lux2
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux3=dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
>>> lux3
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> lux4=dict({'health':490,'mana':334,'melee':550,'armor':18.72})
>>> lux4
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> 
>>> 
>>> 
>>> 
>>> 12-2
10
>>> 
>>> lux={'health':490,'mana':334,'melee':550,'armor':18.72}
>>> lux['health']
490
>>> lux['armor']
18.72
>>> lux['health']=2037
>>> lux['mana']=1184
>>> lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}
>>> lux['mana_regen']=3.28
>>> lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}
>>> ;ix['attack_speed']
SyntaxError: invalid syntax
>>> lux['attack_speed']
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lux['attack_speed']
KeyError: 'attack_speed'
>>> 'health'in lux
True
>>> 'attack_speed'in lux
False
>>> 'attack_speed'not in lux
True
>>> type(lux)
<class 'dict'>
>>> 'health' not in lux
False
>>> 0==0
True
>>> 1==1.=
SyntaxError: cannot assign to comparison
>>> 1==1.0
True
>>> 1 is 1.0
False
>>> len(lux)
5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 연습문제
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    연습문제
NameError: name '연습문제' is not defined
>>> camille={zip[('health','health_regen','mana','mana_regen','melee','attack_damage','attack_speed','armor','magic_resistance','movement_speed'),(575.6,1.7,338.8,1.63,125,60,0.625,26,32.1,340)]}
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    camille={zip[('health','health_regen','mana','mana_regen','melee','attack_damage','attack_speed','armor','magic_resistance','movement_speed'),(575.6,1.7,338.8,1.63,125,60,0.625,26,32.1,340)]}
TypeError: 'type' object is not subscriptable
>>> camille=dict(zip[('health','health_regen','mana','mana_regen','melee','attack_damage','attack_speed','armor','magic_resistance','movement_speed'),(575.6,1.7,338.8,1.63,125,60,0.625,26,32.1,340)])
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    camille=dict(zip[('health','health_regen','mana','mana_regen','melee','attack_damage','attack_speed','armor','magic_resistance','movement_speed'),(575.6,1.7,338.8,1.63,125,60,0.625,26,32.1,340)])
TypeError: 'type' object is not subscriptable
>>> camille=dict(zip(['health','health_regen','mana','mana_regen','melee','attack_damage','attack_speed','armor','magic_resistance','movement_speed'],[575.6,1.7,338.8,1.63,125,60,0.625,26,32.1,340]))
>>> camille
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63, 'melee': 125, 'attack_damage': 60, 'attack_speed': 0.625, 'armor': 26, 'magic_resistance': 32.1, 'movement_speed': 340}
>>> print(camille[health])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(camille[health])
NameError: name 'health' is not defined
>>> print(camille['health'])
575.6
>>> print(camille['movement_speed'])
340
>>> 
==================================== RESTART: C:/Users/TETRA/Desktop/12.5심사문제.py ====================================
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
{'health': '575.6', 'health_regen': '1.7', 'mana': '338.8', 'mana_regen': '1.63'}
>>> 
==================================== RESTART: C:/Users/TETRA/Desktop/12.5심사문제.py ====================================

==================================== RESTART: C:/Users/TETRA/Desktop/12.5심사문제.py ====================================
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
{'health': 575.6, 'health_regen': 1.7, 'mana': 338.8, 'mana_regen': 1.63}
>>> 