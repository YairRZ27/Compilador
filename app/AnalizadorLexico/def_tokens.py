# Construyendo el analizador léxico
import ply.lex as lex
reservadas = {
    'dec': 'd',
    'else': 'E',
    'endif': 'EF',
    'endwhile': 'EW',
    'endmain': 'e',
    'main': 'm',
    'int': 'i', 
    'string': 's',
    'out': 'o',
    'input':'IT',
    'if':'I',
    'while':'w'
}
tokens = [
    'PARIZQ','PARDER','MEN','MAY','MEN_IG','MAY_IG',
    'IGUAL_A','DIFERENTE_DE','CORIZQ','CORDER',
    'MAS','MENOS','POR','DIVIDIDO','MODULO',
    'DEC','INT','V','T','PR','IGUAL',
    'COMA','GBAJO','STRING','COMMENT'
] + list(reservadas.values())
# Tokens
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_MEN = r'<'
t_MAY = r'>'
t_MEN_IG = r'<:'
t_MAY_IG = r'>:'
t_IGUAL_A = r':'
t_DIFERENTE_DE = r'!'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_IGUAL = r'='
t_DIVIDIDO = r'/'
t_MODULO = r'%'
t_GBAJO = r'\_'
t_COMA = r','

#cuenta el orden de las reglas 
#van de las mas restrictivas (más lasgas) a las mas permisivas (mas cortas)
def t_COMMENT(t):
    r'\{.*\}'
    pass

def t_DEC(t):
    r'\#\d+\.\d+'
    if t_simb.get(t.value) == None:
        #t_simb[t.value] = [t.value, t.type, 'dec']
        t_simb[t.value] = [t.value, 'num', 'DEC']
    return t

def t_INT(t):
    r'\#\d+'
    if t_simb.get(t.value) == None:
        #t_simb[t.value] = [t.value, t.type, 'INT']
        t_simb[t.value] = [t.value, 'num', 'INT']
    return t

def t_V(t):
    r'@(\w)+@'
    if t_simb.get(t.value) == None:
        t_simb[t.value] = [t.value, 'V', 'VAR']
    return t

def t_PR(t):
    r'(\w)+'
    # Check for reserved words
    if reservadas.get(t.value.lower()) != None:
        t.type = reservadas.get(t.value.lower(), 'PR')
        return t
    t_error(t)

def t_T(t):
    #r'\".+\"' #\. es el meta caracter de las ER de python para cualquier simbolo
    r'\"[^\"]+\"' # con lo corchetes se define un grupo que con eel  êxcluye solo al caracter de ", que necesia la secuencia de escape
    if t_simb.get(t.value) == None:
        t_simb[t.value] = [t.value, t.type, 'TXT']
    return t

# Caracteres ignorados
t_ignore = " \t\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    print("Error '%s'" % t.value , " en la linea " , t.lineno)
    errores.append(t)
    print(t)
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
#estructuras de datos
errores=[]
t_simb = {}
