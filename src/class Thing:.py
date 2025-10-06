class Thing:
    def __repr__(self):
        return "REPR!"
    
    def __str__(self):
        return "STR!"
    
t = Thing()

print(t)
t
print(str(t))
print(repr(t))