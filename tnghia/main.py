c,p = input().split()
cname = []
l = []
level = []
d = []
s = []
b = []
r = []
prl = []
prjn = []
lvlr = []
like = []
disl = []
c = int(c)
p = int(p)
for i in range(c):
    toAppend, amount = input().split()
    cname.append(str(toAppend))
    for i in range(int(amount)):
        toAppend2, lvl = input().split()
        l.append(str(toAppend2))
        level.append(int(lvl))
for i in range(p):
    toAppend, d2, s2, b2, r2 = input().split()
    prjn.append(str(toAppend))
    d.append(int(d2))
    s.append(int(s2))
    b.append(int(b2))
    r.append(int(b2))
    for i in range(int(r2)):
        toAppend2, lvlc = input().split()
        prl.append(str(toAppend2))
        lvlr.append(int(lvlc))

print(p)
for i in range(len(prjn)):
    print(prjn[i])



        

