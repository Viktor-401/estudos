
#metas: ***comando voltar, ***encerrar com todos os 7 dias(com poossibilidade de voltar), ***reescrever dados, ***separar resultados opção 1

#variáveis gerais

seg = ter = qua = qui = sex = sab = dom = dia = app = ciclo = ''
dados = -1

#programa

input('Este é o programa de monitoramento de dados. \nEm cada etapa digite as informações necessárias. \nCaso digite valores inválidos o programa requesitará os dados novamentes. \nCaso digite e envie valores indesejados, apenas digite: " voltar "\nPressione enter para continuar.')

while ciclo != 'nao':

  #coleta de dados

  while dia != 'seg' and dia != 'ter' and dia != 'qua' and dia != 'qui' and dia != 'sex' and dia != 'sab' and dia != 'dom':

    dia = input('Digite o dia de uso: \n seg -> segunda \n ter -> terça \n qua -> quarta \n qui -> quinta \n sex -> sexta \n sab -> sábado \n dom -> domingo \n')

  while app != 'facebook' and app != 'whatsapp' and app != 'instagram' and app != 'chrome' and app != 'outros':

    app = input('Digite o aplicativo usado: \n facebook \n whatsapp \n instagram \n chrome \n outros \n')

  while int(dados) < 0:
    try:
      dados = int(input('Digite a quantidade de dados, em bytes, utilizada:'))
    except: pass

  #atribuições aos dias

  if dia == 'seg':seg += str(app) + '#' + str(dados) + '@'
  if dia == 'ter':ter += str(app) + '#' + str(dados) + '@'
  if dia == 'qua':qua += str(app) + '#' + str(dados) + '@'
  if dia == 'qui':qui += str(app) + '#' + str(dados) + '@'
  if dia == 'sab':sab += str(app) + '#' + str(dados) + '@'
  if dia == 'sex':sex += str(app) + '#' + str(dados) + '@'
  if dia == 'dom':dom += str(app) + '#' + str(dados) + '@'
  print(seg, ter, qua, qui, sex, sab , dom)
  ciclo = input('Deseja continuar? Digite " nao " para parar o programar e receber os dados coletados.')

  dia = app = ''
  dados = -1

#variáveis do tratamento

opcao = opcaoapp = info = texto1 = texto2 = texto3 = z = ''
totalBytes = totalTotalBytes = totalBytesDia = 0

#tratamento de dados para visualização


for w in ('facebook#whatsapp#instagram#chrome#outros#'):
  if w != '#':
    opcaoapp += w
  else:

    # segunda

    for x in seg:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalBytesDia += int(dados)
        if app == opcaoapp:
          texto1 += '{} : {} bytes, segunda-feira.\n'.format(app,dados)
          totalTotalBytes += int(dados)
          totalBytes += int(dados)
    texto2 += '#Segunda-feira : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0

    #terça

    for x in ter:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalBytesDia += int(dados)
        if app == opcaoapp:
           texto1 += '{} : {} bytes, terça-feira.\n'.format(app,dados)
           totalTotalBytes += int(dados)
           totalBytes += int(dados)
    texto2 += 'Terça-feira : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0

    #quarta

    for x in qua:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalBytesDia += int(dados)
        if app == opcaoapp:
           texto1 += '{} : {} bytes, quarta-feira.\n'.format(app,dados)
           totalTotalBytes += int(dados)
           totalBytes += int(dados)
    texto2 += 'Quarta-feira : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0

    #quinta

    for x in qui:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalBytesDia += int(dados)
        if app == opcaoapp:
           texto1 += '{} : {} bytes, quinta-feira.\n'.format(app,dados)
           totalTotalBytes += int(dados)
           totalBytes += int(dados)
    texto2 += 'Quinta-feira : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0

    #sexta

    for x in sex:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalBytesDia += int(dados)
        if app == opcaoapp:
           texto1 += '{} : {} bytes, sexta-feira.\n'.format(app,dados)
           totalTotalBytes += int(dados)
           totalBytes += int(dados)
    texto2 += 'Sexta-feira : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0

    #sábado

    for x in sab:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalBytesDia += int(dados)
        if app == opcaoapp:
           texto1 += '{} : {} bytes, sábado.\n'.format(app,dados)
           totalTotalBytes += int(dados)
           totalBytes += int(dados)
    texto2 += 'Sábado : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0

    #domingo

    for x in dom:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        totalBytesDia += int(dados)
        z = ''
        if app == opcaoapp:
           totalTotalBytes += int(dados)
           totalBytes += int(dados)
           texto1 += '{} : {} bytes, domingo.\n'.format(app,dados)
    texto3 += 'Média {} : {}\n'.format(opcaoapp, str(int(totalBytes/7)))
    texto1 += '{} : {} bytes, na semana.\n'.format(opcaoapp,totalBytes)
    totalBytes = 0
    texto2 += 'No domingo : {} bytes.\n'.format(totalBytesDia)
    totalBytesDia = 0
    texto2 += 'Semana : {} bytes.\n'.format(totalTotalBytes)
    opcaoapp = ''
texto3 += 'Média diária de consumo total : {}\n'.format(str(int(totalTotalBytes/7)))
texto2 = texto2[texto2.rindex('#')+1:]

while opcao != '1' and opcao != '2' and opcao != '3':
  opcao = input('Escolha a opção desejada:\n1 - Total de dados usados por cada aplicativo por dia e na semana inteira.\n2 - Total de dados totais usados em cada dia e na semana inteira.\n3 - Média diária de consumo total de dados na semana e por aplicativo.')

if opcao == '1':print(texto1)
if opcao == '2':print(texto2)
if opcao == '3':print(texto3)
