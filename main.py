import json,os,urllib.request as w
U=os.environ["MAKEFUN_ENV_URL"]
O=(-17,-15,-10,-6,6,10,15,17,-9,-8,-7,-1,1,7,8,9)
D=(1,-1,8,-8)
E=(7,-7,9,-9)
T=[0]
I=-10001
Z=KeyError
def p(h,d):
 q=w.Request(U+h,json.dumps(d).encode())
 with w.urlopen(q)as r:return json.load(r)
def A(b,s,c):
 f=s&7;r=s>>3
 for o in(-9,-7)if c>0 else(7,9):
  t=s+o
  if 0<=t<64 and b[t]==c and abs((t&7)-f)==1:return 1
 for i,o in enumerate(O):
  t=s+o
  if 0<=t<64:
   df=(t&7)-f;dr=(t>>3)-r
   if(df*df+dr*dr==5 if i<8 else df*df+dr*dr<3)and b[t]==(2+4*(i>7))*c:return 1
 for o in D+E:
  t=s;j=f;n=r
  while 1:
   t+=o
   if t<0 or t>63:break
   u=t&7;v=t>>3
   if abs(u-j)>1 or abs(v-n)>1:break
   j,n=u,v;q=b[t]
   if q:
    if q==(4*c if o in D else 3*c)or q==5*c:return 1
    break
 return 0
def g(b,c,k,e,y):
 m=[]
 for s in range(64):
  q=b[s]
  if q*c<=0:continue
  a=abs(q);f=s&7;r=s>>3
  if a==1:
   d=8*c;t=s+d;l=r==(6 if c>0 else 1)
   if not b[t] and not y:
    m+=[(s,t,z)for z in(5,2,4,3)]if l else[(s,t,0)]
    if r==(1 if c>0 else 6)and not b[s+2*d]:m.append((s,s+2*d,0))
   for o in(-1,1):
    t=s+d+o
    if 0<=t<64 and(t&7)==f+o and(b[t]*c<0 or t==e):
     m+=[(s,t,z)for z in(5,2,4,3)]if l else[(s,t,0)]
  elif a==2 or a==6:
   for o in(O[:8] if a==2 else O[8:]):
    t=s+o
    if 0<=t<64:
     df=(t&7)-f;dr=(t>>3)-r
     if(df*df+dr*dr==5 if a==2 else df*df+dr*dr<3)and b[t]*c<=0 and(not y or b[t]*c<0):m.append((s,t,0))
   if a==6:
    for o in(2,-2):
     z=(1 if o>0 else 2)if c>0 else(4 if o>0 else 8)
     if k&z and not b[s+o//2]and not b[s+o]and(o>0 or not b[s-3])and all(not A(b,s+u,-c)for u in(0,o//2,o)):m.append((s,s+o,0))
  else:
   for o in(D+E if a==5 else D if a==4 else E):
    t=s+o;j=f;n=r
    while 0<=t<64:
     u=t&7;v=t>>3
     if abs(u-j)>1 or abs(v-n)>1:break
     j,n=u,v
     if b[t]*c>0:break
     if not y or b[t]*c<0:m.append((s,t,0))
     if b[t]:break
     t+=o
 return m
def M(b,m,c,k,e):
 s,t,z=m;n=b[:];q=n[s];v=n[t];n[s]=0
 if q==c and t==e and not v:n[t-8*c]=0;v=-c
 n[t]=z*c if z else q
 if abs(q)==6:
  k&=~3 if c>0 else~12
  if abs(t-s)==2:
   a=t+1 if t%56==6 else t-2
   d=t-1 if t%56==6 else t+1
   n[d],n[a]=n[a],0
 for z in(s,t):k&=~{0:2,7:1,56:8,63:4}.get(z,0)
 return n,k,s+8*c if abs(q)==1 and abs(t-s)==16 else-1,v
def F(b,c):
 t=0;w=0;n=5 not in map(abs,b)
 for i,q in enumerate(b):
  if not q:continue
  a=abs(q)
  w+=(a==3)*(q>0 or-1)
  r=i>>3;j=6-max(abs(2*(i&7)-7),abs(2*r-7))
  v=(0,100+(r if q>0 else 7-r)*10,320+j*8,330+j*4,500+12*(r==1+5*(q>0)),900+j*3,j*(8 if n else-6))[a]
  t+=v if q>0 else-v
 t+=30*((w==2)-(w==-2))
 return t if c>0 else-t
def S(b,c,k,e,d,a,f,y=0):
 T[0]+=1
 if T[0]>3e4:raise Z
 j=b.index(6*c)
 q=d<=0;h=A(b,j,-c)
 if q and not h:
  s=F(b,c)
  if s>=f or y>9:return min(s,f)
  if s>a:a=s
 m=g(b,c,k,e,q and not h)
 m.sort(key=lambda x:b[x[1]]*c)
 t=I;n=0
 for x in m:
  o,p,v,_=M(b,x,c,k,e)
  if A(o,x[1]if x[0]==j else j,-c):continue
  n+=1;s=-S(o,-c,p,v,d-1,-f,-a,y+1 if q else 0)
  if s>t:t=s
  if s>a:a=s
  if a>=f:break
 return-10000 if n==0 and h else a if q else t if n else 0
def X(b,c,k,e,L):
 if len(L)==1:return L[0]
 T[0]=0
 D=sorted(((-F(M(b,m,c,k,e)[0],-c),m)for m in L),reverse=True)
 y=D[0][1]
 for h in range(6):
  try:
   z=[y]+[m for _,m in D if m!=y];t=I;a=I
   for m in z:
    n,o,v,_=M(b,m,c,k,e)
    s=-S(n,-c,o,v,h,I,-a)
    if s>t:t=s;y=m
    if s>a:a=s
  except Z:break
 return y
def u(m):return chr(97+(m[0]&7))+str(m[0]//8+1)+chr(97+(m[1]&7))+str(m[1]//8+1)+(" pnbrqk"[m[2]]if m[2]else"")
def P(f):
 d=f.split();b=[0]*64;i=56
 for j in d[0]:
  if j=="/":i-=16
  elif j.isdigit():i+=int(j)
  else:b[i]=("PNBRQK".index(j.upper())+1)*(j<"a"or-1);i+=1
 c=1 if d[1]=="w"else-1
 k=sum(1<<i for i,j in enumerate("KQkq")if j in d[2])
 e=-1 if d[3]=="-"else ord(d[3][0])-97+(int(d[3][1])-1)*8
 return b,c,k,e
while(G:=p("/game",{}))["status"]!="done":
 while G["status"]=="your_move":
  b,c,k,e=P(G["fen"])
  G=p("/move",{"game":G["game"],"move":u(X(b,c,k,e,[(ord(m[0])-97+(ord(m[1])-49)*8,ord(m[2])-97+(ord(m[3])-49)*8,"pnbrqk".index(m[4])+1 if m[4:]else 0)for m in G["legal_moves"]]))})