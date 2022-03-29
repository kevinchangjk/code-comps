T = int(input())
refla = ['00', '11', '88', '25', '52']
reflb = ['01', '02', '05', '08', '12', '15', '18', '22', '28', '58', '55']
reflc = ['10', '50', '20', '80', '51', '21', '81', '55', '85', '82', '22']

def reflhc(h, m):
    reflat = [refla[i] for i in range(5) if (int(refla[i]) < h) and (int(refla[i]) < m)]
    reflbt = [reflb[i] for i in range(11) if (int(reflb[i]) < h) and (int(reflc[i]) < m)]
    reflct = [reflc[i] for i in range(11) if (int(reflc[i]) < h) and (int(reflb[i]) < m)]
    reflat.extend(reflbt)
    reflat.extend(reflct)
    return reflat

def reflmc(h, m):
    reflat = [refla[i] for i in range(5) if (int(refla[i]) < h) and (int(refla[i]) < m)]
    reflbt = [reflb[i] for i in range(11) if (int(reflc[i]) < h) and (int(reflb[i]) < m)]
    reflct = [reflc[i] for i in range(11) if (int(reflb[i]) < h) and (int(reflc[i]) < m)]
    reflat.extend(reflbt)
    reflat.extend(reflct)
    return reflat

def addd(hm):
    if hm // 10 == 0:
        return str('0'+str(hm))
    else:
        return str(hm)

for i in range(T):
    h, m = list(map(int, input().split()))
    sh, sm = input().split(":")
    reflht = reflhc(h, m)
    reflmt = reflmc(h, m)
    resh = 0
    resm = 0
    
    if sh in reflht:
        if sm in reflmt:
            resh = sh
            resm = sm
        else:
            reflanm = [int(reflmt[i]) - int(sm) for i in range(len(reflmt)) if int(reflmt[i]) - int(sm) > 0]
            if len(reflanm) != 0:
                resh = sh
                resm = addd(int(sm) + min(reflanm))
                
    if resh == 0:
        reflanh = [int(reflht[i]) - int(sh) for i in range(len(reflht)) if int(reflht[i]) - int(sh) > 0]
        if len(reflanh) != 0:
            resh = addd(int(sh)+min(reflanh))
            resm = '00'
        else:
            resh = '00'
            resm = '00'
            
    print(f"{resh}:{resm}")
    
    