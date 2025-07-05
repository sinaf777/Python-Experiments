glist = ["nn", "bb", "mm","uu"]
glist.append("vv")
glist.insert(1,"cc")
glist.pop()
for i  in range(len(glist)-1, -1, -1):
    print(glist[i], i)
#list example