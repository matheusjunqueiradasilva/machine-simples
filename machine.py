#é um email novo?                         spam
#é de um comércio?                  1 = sim , 0= não
#voce solicitou esse email?

from sklearn.naive_bayes import MultinomialNB

email1 =[1,1,1]
email2 =[1,0,0]
email3 =[1,1,0]
email4 =[0,1,1]
email5 =[0,0,1]

dados = [email1,email2,email3,email4,email5]

marcacoes = [1,0,0,1,1]

modelo = MultinomialNB()

modelo.fit(dados,marcacoes)

misterioso1 =[1,1,0]  #0
misterioso2 =[0,0,0]  #0
misterioso3 =[1,1,1]  #1
misterioso4 =[1,0,1]  #1

teste = [misterioso1,misterioso2,misterioso3,misterioso4]

resultado = modelo.predict(teste)

print(resultado)
