nome = input('Insira seu nome:')
nota1 = float(input('Sua primeira nota:'))
nota2 = float(input('Sua segunda nota:'))

print(f'Olá{nome} suas notas foram:')
print(nota1, 'e', nota2)

#Definição da média da escola
def verificar_aprovacao():
  media = calcular_media([nota1, nota2])

  if media >= 6:
    print('Você foi aprovado. Parabéns!')
  else:
    print('Você foi reprovado. Procure seu professor.')

#Definindo como calcular média
def calcular_media(notas):
  quantidade = len(notas)

  soma = 0
  for nota in notas:
    soma = soma + nota
  media = soma / quantidade
  return media
#Verificando aprovação
verificar_aprovacao()
