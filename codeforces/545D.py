from collections import Counter

s = input()
t = input()

s_count = Counter(s)
t_count = Counter(t)

lop = 0
used_one = 0
used_zero = 0

for i in range(len(t) // 2 + len(t)%2, 0, -1):
    if t[-i:] == t[:i]:
        lop = i
        break

if len(t) == 1:
    lop = 0

if len(s) < len(t):
    print(s)
else:
    
    if '0' not in t_count:
        one = s_count['1'] // t_count['1']
        if one> 0:
            res = [t]
            used_one += t_count['1']
            used_zero += t_count['0']
            truncated_t = t[lop:]
            t_count = Counter(truncated_t)
            one = (s_count['1']-used_one) // t_count['1']
            res_add = [truncated_t for i in range(one)]
            res.extend(res_add)
            used_one += one * t_count['1']
            used_zero += one * t_count['0']
            zero_re = s_count['0']
            one_re = s_count['1'] - used_one
            remainders = ['0' for i in range(zero_re)]
            remainders.extend(['1' for i in range(one_re)])
            res.extend(remainders)
            print("".join(res))
        else:
            print(s)
            
    elif '1' not in t_count:
        zero = s_count['0'] // t_count['0']
        if zero >0:
            res = [t]
            used_one += t_count['1']
            used_zero += t_count['0']
            truncated_t = t[lop:]
            t_count = Counter(truncated_t)
            zero = (s_count['0']-used_zero) // t_count['0']
            res_add = [truncated_t for i in range(zero)]
            res.extend(res_add)
            used_one += zero * t_count['1']
            used_zero += zero * t_count['0']
            zero_re = s_count['0'] - used_zero
            one_re = s_count['1']
            remainders = ['0' for i in range(zero_re)]
            remainders.extend(['1' for i in range(one_re)])
            res.extend(remainders)
            print("".join(res))
        else:
            print(s)
    else:
        zero = s_count['0'] // t_count['0']
        one = s_count['1'] // t_count['1']
        if zero >0 and one> 0:
            res = [t]
            used_one += t_count['1']
            used_zero += t_count['0']
            truncated_t = t[lop:]
            t_count = Counter(truncated_t)
            one = (s_count['1']-used_one) // t_count['1']
            zero = (s_count['0']-used_zero) // t_count['0']
            res_add = [truncated_t for i in range(min(one, zero))]
            res.extend(res_add)
            used_one += (min(one, zero)) * t_count['1']
            used_zero += (min(one, zero)) * t_count['0']
            zero_re = s_count['0'] - used_zero
            one_re = s_count['1'] - used_one
            remainders = ['0' for i in range(zero_re)]
            remainders.extend(['1' for i in range(one_re)])
            res.extend(remainders)
            print("".join(res))
        else:
            print(s)

    
    
    
    