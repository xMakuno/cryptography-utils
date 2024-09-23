phrase = "En el vasto océano de datos, Batman se sumerge como un detective digital, rastreando los rastros de El Acertijo. Cada pista es una clave, cada enigma, un desafío a la integridad del sistema. La seguridad informática no es solo un conjunto de reglas, es una batalla constante contra las mentes criminales que buscan la grieta en la armadura. Y en este juego, Batman sabe que un solo error puede abrir las puertas al caos."
characters = 0
for c in phrase:
    if c != " " and c != "," and c != ";" and c != "." and c != "!":
        characters+=1
print(f"The amount of chars in the phrase is: {characters}")