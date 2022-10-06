from operator import truediv
from pickle import TRUE


conta_normal = True
conta_universitaria = True

saldo = 2000
saque = 3000
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print(f'saque no valor de {saque}  realizado com sucesso')
    elif saque <= (saldo - cheque_especial):
        print('saque realizado com uso do cheque especial')
    else:
        print('não foi possivel realizar o saque, saldo insuficiente!')
        
status = "sucesso" if saldo >= saque else 'vc nao vai sacar'
print(status)
        