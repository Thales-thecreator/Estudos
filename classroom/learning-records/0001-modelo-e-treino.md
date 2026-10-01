# Modelo vs. treino: a ideia central está firme

Na aula 1 o Thales acertou 4 de 5 no quiz e explicou com as próprias palavras que o modelo é "o conjunto de regras que fará a previsão" e o treino é o que permite chegar a essas regras a partir de padrões. A base do aprendizado supervisionado (exemplos → treino → modelo → previsão) está entendida; dá para construir a próxima aula em cima dela.

**Evidence:** quiz da aula 0001 (4/5, errou a 5: usar um modelo pronto é previsão, não treino) e a resposta escrita na conversa de 2026-10-01. Na prova oral da M0.6, logo depois, acertou a mesma ideia com as próprias palavras ("o modelo já está treinado, estou colocando em prática") e explicou que a mensagem do salário vira spam porque, nos exemplos, toda mensagem com valor era spam.

**Implications:** ainda há uma imprecisão a acompanhar. Ele disse que o treino possibilita "o modelo escrever as regras", como se o modelo fosse quem aprende; na verdade o modelo é o *resultado* do treino, e o que o treino usa são os exemplos com rótulo. Para corrigir o modelo, ele pensou em mudar a mensagem nova ("é do RH"), não em acrescentar um exemplo rotulado aos dados. Retomar na próxima aula com perguntas de recuperação: o que entra no treino, o que sai dele, e como se conserta um modelo que erra (mais e melhores exemplos com rótulo).
