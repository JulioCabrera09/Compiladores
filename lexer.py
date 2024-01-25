import ply.lex as lex
import tkinter as tk

tokens = [
    'IDENTIFICADOR',
    'TIPO_DE_DATO',
    'ASIGNACION',
    'ENTERO',
    'FLOTANTE',
    'CADENA',
    'PALABRA_RESERVADA',
    'OPERADOR_ARITMETICO',
    'DOS_PUNTOS',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'PUNTO_COMA',
    'SIMBOLOS', 
]

t_IDENTIFICADOR = r'[a-z][a-z0-9_]*'
t_TIPO_DE_DATO = r'UwU-(int|float|var)'
t_ASIGNACION = r'='
t_ENTERO = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_CADENA = r'\".*?\"'
t_PALABRA_RESERVADA = r'UwU-(def|if|else|for|print)'
t_OPERADOR_ARITMETICO = r'\+|\-'
t_DOS_PUNTOS = r':'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_PUNTO_COMA = r';'
t_SIMBOLOS = r'<|>|<=|>=|==|!='

t_ignore = ' \t'

caracteres_no_validos = set()

def t_error(t):
    caracteres_no_validos.add(t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def analizar_cadena(input_string):
    lexer.input(input_string)
    tokens_y_lexemas = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens_y_lexemas.append((token.type, token.value))
    return tokens_y_lexemas

def analizar_entrada():
    result_text.delete("1.0", tk.END)

    input_text = input_entry.get("1.0", tk.END)
    lexer.input(input_text)

    tokens_y_lexemas = []
    caracteres_no_validos.clear()

    while True:
        token = lexer.token()
        if not token:
            break
        tokens_y_lexemas.append((token.type, token.value))

    primer_caracter_no_valido = True

    for i, (token, lexema) in enumerate(tokens_y_lexemas, start=1):
        result_text.insert(tk.END, f"{i}. Token: {token}, Lexema: {lexema}\n")

    if caracteres_no_validos:
        result_text.insert(tk.END, "\nCaracteres no válidos: \n")
        for caracter_no_valido in caracteres_no_validos:
            result_text.insert(tk.END, f"{caracter_no_valido}\n")

# interfaz gráfica
root = tk.Tk()
root.title("Analizador Léxico")

root.geometry("500x600")

input_label = tk.Label(root, text="Ingrese una cadena:")
input_label.pack(pady=5)

input_entry = tk.Text(root, height=2, width=50)
input_entry.pack(pady=5)

analizar_button = tk.Button(root, text="Analizar", command=analizar_entrada)
analizar_button.pack(pady=5)

result_text = tk.Text(root, height=25, width=50)
result_text.pack(pady=5)

root.mainloop()
