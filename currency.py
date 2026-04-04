#currency in USD

p=int(input('wt do u have left in pesos?'))
s=int(input('wt do u have left in soles?'))
r=int(input('wt do u have left in reais?'))
ep=3710.16
es=3.36 
er=5.39
usd_p=p/ep
usd_s=s/es
usd_r=r/er
usd=usd_p+usd_s+usd_r
print('the total remaining amount in USD is:', usd)
