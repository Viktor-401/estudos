#metas: comando voltar, menu de navegação na parte de visualização.


#variáveis gerais
seg = ter = qua = qui = sex = sab = dom = dia = app = ciclo = ''
dados = -1

#programa

input('Este é o programa de monitoramento de dados. \nEm cada etapa digite as informações necessárias. \nCaso digite valores inválidos o programa requesitará os dados novamentes. \nCaso digite e envie valores indesejados, apenas digite: " voltar "\nPressione enter para continuar.')

while ciclo != 'nao':
  #coleta de dados
  while dia != 'seg' and dia != 'ter' and dia != 'qua' and dia != 'qui' and dia != 'sex' and dia != 'sab' and dia != 'dom':

    dia = input('Digite o dia de uso: \nseg -> segunda \nter -> terça \nqua -> quarta \nqui -> quinta \nsex -> sexta \nsab -> sábado \ndom -> domingo \n')

  while app != '1' and app != '2' and app != '3' and app != '4' and app != '5':

    app = input('Digite o aplicativo usado: \n1 - facebook \n2 - whatsapp\n3 - instagram\n4 - chrome \n5 - outros \n')

  while int(dados) < 0:
    try:
      dados = int(input('Digite a quantidade de dados, em bytes, utilizada:'))
    except: print
  #atribuições aos dias
  if dia == 'seg':seg += '#a' + str(app) + '#d' + str(dados)
  if dia == 'ter':ter += '#a' + str(app) + '#d' + str(dados)
  if dia == 'qua':qua += '#a' + str(app) + '#d' + str(dados)
  if dia == 'qui':qui += '#a' + str(app) + '#d' + str(dados)
  if dia == 'sab':sab += '#a' + str(app) + '#d' + str(dados)
  if dia == 'sex':sex += '#a' + str(app) + '#d' + str(dados)
  if dia == 'dom':dom += '#a' + str(app) + '#d' + str(dados)

  ciclo = input('Deseja continuar? Digite " nao " para parar o programar e receber os dados coletados.')

  dia = app = ''
  dados = -1

#variáveis do tratamento

opcao = ''

#tratamento de dados para visualização

while opcao != '1' and opcao != '2' and opcao != '3':
  opcao = input('Escolha a opção desejada:\n1 - Total de dados usados por cada aplicativo por dia e na semana inteira.\n2 - Total de dados totais usados em cada dia e na semana inteira.\n3 - Média diaria de consumo total de dados na semana e por aplicativo.')



print(dia, app , dados , seg , ter , qua , qui , sex , sab , dom)