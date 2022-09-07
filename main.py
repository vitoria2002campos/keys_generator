#GERADOR DE SENHA#

#maiusculas e minusculas
#simbolos e espaços



chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "|@"
    elif letra in "Bb":
        senha = senha + "2M"
    elif letra in "Cc":
        senha = senha + "p<"
    elif letra in "Dd":
        senha = senha + "1z"
    elif letra in "Ee":
        senha = senha + "%/"
    elif letra in "Ff":
        senha = senha + "-"
    elif letra in "Gg":
        senha = senha + "&&"
    elif letra in "Hh":
        senha = senha + "#"
    elif letra in "Ii":
        senha = senha + ";"
    elif letra in "Jj":
        senha = senha + "?"
    elif letra in "Kk":
        senha = senha + "'"
    elif letra in "Ll":
        senha = senha + "_."
    elif letra in "Mm":
        senha = senha + "%"
    elif letra in "Nn":
        senha = senha + "("
    elif letra in "Oo":
        senha = senha + "?"
    elif letra in "Pp":
        senha = senha + ")"
    elif letra in "Qq":
        senha = senha + "6n"
    elif letra in "Rr":
        senha = senha + "0_"
    elif letra in "Ss":
        senha = senha + "9l"
    elif letra in "Tt":
        senha = senha + "4M"
    elif letra in "Uu":
        senha = senha + "5q"
    elif letra in "Uu":
        senha = senha + "8p"
    elif letra in "Vv":
        senha = senha + "5N"
    elif letra in "Ww":
        senha = senha + "/&"
    elif letra in "Xx":
        senha = senha + "&?"
    elif letra in "Yy":
        senha = senha + "$*"
    elif letra in "Zz":
        senha = senha + "*="
    else: senha = senha + letra
print(senha)



