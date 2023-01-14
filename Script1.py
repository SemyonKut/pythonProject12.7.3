print('\nРаспределение процентных ставок по вкладам в различных банках:')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}   #распределение процентных ставок по вкладам в различных банках
for key, value in per_cent.items():
  print("{0}: {1}".format(key,value))
print('-' * 80)
moneyStr = input('Введите сумму (целое число), которую планируете положить под проценты:\n')
#print(type(money))
'''   '''
if moneyStr.isnumeric()==True or moneyStr.isdigit()==True:
            print('-'*80)
            money = float(moneyStr)
            print("Ваша сумма: ", money,"руб.")
else: print("Пожалуйста, введите корректную сумму!")

print('Накопленные средства за год вклада в каждом из банков: ')
#deposit = [per_cent(0)*money, per_cent(1)*money, per_cent(2)*money, per_cent(3)*money]  #подсчет годовых выплат
per_centList = list(per_cent.values())  #подсчет годовых выплат
#print(per_centList)
depTKB = round(per_centList[0]*money/100, 2)   #ВЫПЛАТЫ = (СУММА*ПРОЦЕНТ)/100
#print(depTKB)
depSKB = round(per_centList[1]*money/100, 2)
#print(depSKB)
depVTB = round(per_centList[2]*money/100, 2)
#print(depVTB)
depSBER = round(per_centList[3]*money/100, 2)
#print(depSBER)
deposit = {'ТКБ': depTKB, 'СКБ': depSKB, 'ВТБ': depVTB, 'СБЕР': depSBER}
for key, value in deposit.items():
  print("{0}: {1}".format(key,value))
print('-' * 80)

max_viplata = max(deposit.values())
print('Максимальная сумма, которую вы можете заработать', max_viplata)