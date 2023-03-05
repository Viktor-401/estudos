#metas: comando voltar, menu de navegação na parte de visualização, encerrar com todos os 7 dias


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

  ciclo = input('Deseja continuar? Digite " nao " para parar o programar e receber os dados coletados.')

  dia = app = ''
  dados = -1

#variáveis do tratamento

opcao = opcaoapp = info = texto1 = texto2 = texto3 = z = ''
totalBytes = totalTotalBytes= 0

#tratamento de dados para visualização



    #opção 1

# if opcao == '1':
#   while opcaoapp != 'facebook' and opcaoapp != 'whatsapp' and opcaoapp != 'instagram' and opcaoapp != 'chrome' and opcaoapp != 'outros':
#     opcaoapp = input('Digite o aplicativo desejado:\nfacebook \nwhatsapp\ninstagram\nchrome \noutros \n')

    # segunda
for w in ('facebook#whatsapp#instagram#chrome#outros#'):
  if w != '#':
    opcaoapp += w
  else:
    for x in seg:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
      totalTotalBytes += int(dados)
        if app == opcaoapp:
          texto1 += '{} usou {} bytes na segunda-feira.\n'.format(app,dados)
          totalBytes += int(dados)
          break
      #terça
    for x in ter:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalTotalBytes += int(dados)
        if app == opcaoapp:
           texto1 += '{} usou {} bytes na terça-feira.\n'.format(app,dados)
           totalBytes += int(dados)
           break
      #quarta
    for x in qua:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalTotalBytes += int(dados)
        if app == opcaoapp:
           texto1 += '{} usou {} bytes na quarta-feira.\n'.format(app,dados)
           totalBytes += int(dados)
           break
      #quinta
    for x in qui:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalTotalBytes += int(dados)
        if app == opcaoapp:
           texto1 += '{} usou {} bytes na quinta-feira.\n'.format(app,dados)
           totalBytes += int(dados)
           break
      #sexta
    for x in sex:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalTotalBytes += int(dados)
        if app == opcaoapp:
           texto1 += '{} usou {} bytes na sexta-feira.\n'.format(app,dados)
           totalBytes += int(dados)
           break
      #sábado
    for x in sab:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        z = ''
        totalTotalBytes += int(dados)
        if app == opcaoapp:
           texto1 += '{} usou {} bytes no sábado.\n'.format(app,dados)
           totalBytes += int(dados)
           break
      #domingo
    for x in dom:
      if x != '@':
        z += x
      else:
        app = z[:z.index('#')]
        dados = z[z.index('#')+1:]
        totalTotalBytes += int(dados)
        z = ''
        if app == opcaoapp:
           totalBytes += int(dados)
           texto1 += '{} usou {} bytes no domingo.\n'.format(app,dados)
           break
    w = ''
texto1 += '{} usou um total de {} bytes na semana.'.format(app,totalBytes)

while opcao != '1' and opcao != '2' and opcao != '3':
  opcao = input('Escolha a opção desejada:\n1 - Total de dados usados por cada aplicativo por dia e na semana inteira.\n2 - Total de dados totais usados em cada dia e na semana inteira.\n3 - Média diaria de consumo total de dados na semana e por aplicativo.')

if opcao == 1:print(texto1)

  #opção 2

