import math

source = [0., 0.045, 0.09, 0.13, 0.175, 0.22]


def lumi_cal(dist, point, source, batch):

    tot_lumi = 0
    

    for m in range(0,6):

        single_lumi = 0
        source_inte = 0

        if batch[m] == 'w':
            source_inte = 20000
        elif batch[m] == 'r':
            source_inte = 2000

        btw_dis = math.sqrt(math.pow(dist,2)+math.pow(source[m]-point,2))
        #print(f'{m+1}th source dist effect : {round(btw_dis,2)}')
        single_lumi = source_inte/(math.pow(1+btw_dis,2))

        #print(f'{m+1}th source effect : {round(single_lumi,2)}')

        tot_lumi = tot_lumi + single_lumi

    #print(f'total source effect : {tot_lumi}')

    return tot_lumi


def get_tot_lumi(batch):
    point = [0.,0.03,0.06,0.09,0.13,0.16,0.19,0.22]

    for n in range(0,8):
        lumi = lumi_cal(0.4, point[n], source, batch)
        print(f'{n+1}th point lumi = {round(lumi,2)}\n')

batch1 = ['w','r','w','w','r','w']
batch2 = ['w','w','r','r','w','w']

print('batch 1 result')
get_tot_lumi(batch1)
print('-----------------')
print('batch 2 result')
get_tot_lumi(batch2)
