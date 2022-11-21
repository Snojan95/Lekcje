for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line+= '\t%3d' % (x*y)
    print(line)
    
# generalnie prosta sprawa, pamietaj tylko ze najpierw wykonuja sie najbardziej
# zagniezdzone petle (te najbardziej wciete)