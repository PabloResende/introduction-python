#1. (n + n) parenteses são executados de dentro para fora
#2. ** (potenciação ou exponenciação)
#3. * / // % (vezes, divisão, divisão completa, módulo)
#4. + - (mais e menos)

conta_1 = 1 + 1 ** 5 + 5 #7
print(conta_1)
#há outras formas de fazer essa mesma conta:
conta_2 = (1 + 1) ** (5 + 5) #1024
print(conta_2)
#essa mudança se dá pela lógica de precedência, isto é, os '()' são calculados primeiro
#outra informação importante a se frisar, '()' é lido de dentro para fora, ou seja
#se houver '(())' os parenteses de dentro serão lidos primeiro 

