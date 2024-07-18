import os

def clear_console():
    os.system('cls')

input('Hello\nTell me your fund and position data to tell you Reward and Risk of position\nPress Enter to continue . . .')
clear_console()
isRial = input('Wanna calculate Toman too? (Y/N) ')
if isRial.lower().strip() == 'y':
    usdttmn = float(input('Enter USDT to Toman price: '))
clear_console()
fund = float(input('Enter fund in USDT: '))
percent = float(input('Enter percentage of fund that enters this position: '))
type = input('Enter type (Long/Short): ')
print()
entry = float(input('Entry price: '))
tp = float(input('TP price: '))
sl = float(input('SL price: '))
lv = float(input('Leverage: '))
print('\n')
frozen = fund/100*percent
if type.lower() == 'long':
    tpp = (tp-entry)*100/entry*lv
    tpd = frozen*tpp/100
    slp = (entry-sl)*100/entry*lv
    sld = frozen*slp/100
elif type.lower() == 'short':
    tpp = (entry-tp)*100/entry*lv
    tpd = frozen*tpp/100
    slp = (sl-entry)*100/entry*lv
    sld = frozen*slp/100

if isRial.lower() == 'y':
    print('Risk/Reward Raito: ',tpp/slp,'\nProfit: (',tpd,'USDT ) (',tpd*usdttmn,'Toman )',tpp,'%\nLoss: (',sld,'USDT ) (',sld*usdttmn,'Toman )',slp,'%')
else:
    print('Risk/Reward Raito: ',tpp/slp,'\nProfit: (',tpd,'USDT )',tpp,'%\nLoss: (',sld,'USDT ) ',slp,'%')
input('\n\nPress any key to exit . . .')


