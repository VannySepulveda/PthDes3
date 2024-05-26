print("----FILTRO DE BALANCE POR MES----")
print("_________________________________")

monto = int((input("MONTO A FILTRAR :  $")))
ventas=[]
ventas.append({'mes': "Enero", 'venta': 15000,})
ventas.append({ 'mes':"Febrero", 'venta': 22000,})
ventas.append({'mes':"Marzo", 'venta': 12000,})
ventas.append({'mes':"Abril", 'venta': 17000,})
ventas.append({'mes':"Mayo", 'venta': 81000,})
ventas.append({'mes':"Junio", 'venta': 13000,})
ventas.append({'mes':"Julio", 'venta': 21000,})
ventas.append({'mes':"Agosto", 'venta': 41200,})
ventas.append({'mes':"Septiembre", 'venta': 25000,})
ventas.append({'mes':"Octubre", 'venta': 21500,})
ventas.append({'mes':"Noviembre", 'venta': 91000,})
ventas.append({'mes':"Diciembre", 'venta': 21000})
filtro=[]
for v in ventas:
    if int(v['venta']) > monto:
     filtro.append({'mes':(v['mes']),'venta':(v['venta'])})
     print(f"Mes: {v['mes']}     Monto: $ {v['venta']}.-")
         
   