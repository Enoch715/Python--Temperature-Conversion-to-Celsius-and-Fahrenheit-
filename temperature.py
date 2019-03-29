choice = input ('請選擇所要轉換的溫標(攝氏or華氏): ')
if choice == '攝氏':
	C = input ('請輸入攝氏溫度: ')
	C = float (C)
	F = C * 9/5 + 32 
	print('華氏溫度為: ', F)
else:
	F = input ('請輸入華氏溫度: ')
	F = float (F)
	C = 5/9 * (F - 32)
	print ('攝氏溫度為: ', C)