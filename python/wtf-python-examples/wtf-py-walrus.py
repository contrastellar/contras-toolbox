def demo_func():
    return 5

b = demo_func()
if b: # I'm pretty sure this ~= "(1==1)" or some such. "does b exist?" is probably more accurate
    print(b)

print("\n")

if a := demo_func():
    print(a)
