'''
Adjusting SqzTP and saturation point could result in different best track width pick
'''
import matplotlib.pyplot as plt

def Sqz(tp, a):
    '''set lambda function for Sqz at x TP'''
    return lambda x : a * (x - tp)**2 if x > tp else 0

xl = [x for x in range(1000)]
yl_BER = [1.4*(x - 600)**2 -100 if x < 600 else -100 for x in xl]
combs = [[] for x in range(5)] #different SqzTP from 0 to 500
min_list, min_index = [float('inf') for i in range(5)], [0 for i in range(5)]
for j in range(len(combs)):
    max = float('-inf')
    for i in range(1000):
        combs[j].append(yl_BER[i] + Sqz(j * 150, 0.5)(i))
        if combs[j][i] < min_list[j]:
            min_list[j] = combs[j][i]
            min_index[j] = i
    

figure = plt.figure()
p = figure.add_subplot(111)
p.set(title = 'SqzBER v.s. Changing SqzTP', xlabel = 'SqzTP in nm', ylabel = 'SqzBER in dcd')
for comb in combs:
    p.plot(xl, comb)
    p.legend([0, 150, 300, 450, 600])
    p.plot(min_index, min_list, marker = 'o')
    p.plot()
noSqz = [yl_BER[i] for i in range(1000)]
plt.plot(xl, noSqz)
p.set(xlim = [0,1000], ylim= [-100000, 600000])
plt.show()
