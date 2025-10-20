t=int(input())
for _ in range(t):
    n=int(input())
    lines = [input().split() for _ in range(3)]
    fe={}
    for index,innerlist in enumerate(lines):
        for elem in innerlist:
                if elem not in fe:
                    fe[elem]=[]
                fe[elem].append(index+1)   
    p1=0
    p2=0
    p3=0
    for key,value in fe.items():
        if len(value)==1:
            match value[0]:
                    case 1:
                        p1 += 3
                    case 2:
                        p2 += 3
                    case 3:
                        p3 += 3
        elif len(value)==2:
            for j in value:
                match j:
                    case 1:
                        p1 += 1
                    case 2:
                        p2 += 1
                    case 3:
                        p3 += 1
    r=str(p1)+" "+str(p2)+" "+str(p3)
    print(r)
            
                  
