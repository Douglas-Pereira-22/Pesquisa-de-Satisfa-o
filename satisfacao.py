n1 =  0
n2 =  0
n3 =  0

for i in range(3):
    print('Queremos saber sua opinião sobre o nosso atendimento')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    opiniao = int((input('Digite 1-Excelente 2-Bom 3-Ruim: ')))
    print('Obrigado por participar!')
    print('*'*30)
    if opiniao == 1:
        n1 += 1
    elif opiniao == 2:
        n2 += 1
    elif opiniao == 3:
        n3 += 1
    else:
        pass
print('*'*30)
print(f'Execelente = {n1}')
#print(f'Bom = {n2}')
print(f'Ruim = {n3}')
