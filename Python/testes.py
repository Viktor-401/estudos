seg = 'chrome#90@facebook#46@whatsapp#89@'
app = 'facebook'
dados = '7893'
teste = seg[seg.find(app):]
print(seg.find(app))
print(teste)
seg = seg.replace(seg[seg.find(app):teste.find('@')+seg.find(app)],str(app) + '#' + str(dados))
print(seg)


