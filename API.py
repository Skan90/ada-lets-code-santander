import requests

url = 'https://v6.exchangerate-api.com/v6/6afaa31933281c47c0e38a75/latest/USD'

requisition = requests.get(url)

print(requisition.status_code)

data = requisition.json()

print(data)

value_reais = float(input("Inform the value in R$ to be converted\n"))
exchange_rate = data['conversion_rates']['BRL']
print( f'R${value_reais} in dolar is US${(value_reais / exchange_rate):.2f}' )