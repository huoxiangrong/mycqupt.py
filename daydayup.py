#daydayup.py
"""df = 0.01
dayup = pow(1 + df,365)
daydown = pow(1 - df,365)
print("dayup = {:.2f},daydown = {:.2f}".format(dayup,daydown))"""
def dayup(df):
    dayup = 1
    for i in range(364):
        if i%7 in[0,6]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayup(dayfactor) < 37.78:
    dayfactor += 0.001
print("每天需要努力：{:.3f}".format(dayfactor))
    
