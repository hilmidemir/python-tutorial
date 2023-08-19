import mod

#result = help(Modules)
#result = help(Modules.func)
result = mod.person['name']
result = mod.person['age']

print(result)

p = mod.Person()
p.speak()


