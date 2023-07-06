# pip install requests
#https://www.youtube.com/watch?v=QkDiBWJ8Row

import requests
import json
link="https://eduardotestedoerner-default-rtdb.firebaseio.com/" #https://eltondoerner1-default-rtdb.firebaseio.com/"
dados=[{'Cliente':'Eduardo','Qtd':123,'Cor':'Vermelho'},{'Cliente':'Maria','Qtd':123,'Cor':'Vermelho'}]

#post
req=requests.post(f'{link}/Clientes/.json',data=json.dumps(dados))
print(req)
print(req.text)

# #patch
# dados={'cliente':'EltonEdited'}
# req=requests.patch(f'{link}/Vendas/-NT73tVeINcqVygvBRbh/.json',data=json.dumps(dados))

# #get
# dados={'cliente':'EltonEdited'}
# req=requests.get(f'{link}/Vendas/.json',data=json.dumps(dados))
# print(req)
# print(req.text)
# r=req.json()
# print(r['-NT73tVeINcqVygvBRbh']['Qtd'])

# idBusca=None
# for id in r:
#     v=r[id]['cliente']
#     if v=="EltonEdited":
#         idBusca=id
#         print(id)

# print(r[id]['Qtd'])
