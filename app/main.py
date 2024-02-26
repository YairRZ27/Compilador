from flask import Flask, render_template, url_for, redirect, request
from AnalizadorLexico import def_tokens


app = Flask(__name__)
lt = []
t_simb2 = {
    'dec': ['dec','d','PR'],
    'else':  ['else','E','PR'],
    'endif':  ['endif','EF','PR'],
    'endwhile':  ['endwhile','EW','PR'],
    'endmain':  ['endmain','e','PR'],
    'main':  ['main','m','PR'],
    'int':  ['int','i','PR'], 
    'string':  ['string','s','PR'],
    'out':  ['out','o','PR'],
    'input': ['input','IT','PR'],
    'if': ['if','I','PR'],
    'while': ['while','w','PR'],
    '+': ['+','+','OP'],
    '-':['-','-','OP'],
    '/':['/','/','OP'],
    '*':['*','*','OP'],
    '%':['%','%','OP'],
    '=':['=','=','OP'],
    '<':['<','<','OP'],
    '<:':['<:','<:','OP'],
    '>':['>','>','OP'],
    '>:':['>:','>:','OP'],
    ':':[':',':','OP'],
    '!':['!','!','OP'],
    '_':['_','_','OP'],
    '[':['[','[','SEP'],
    ']':[']',']','SEP'],
    ',':[',',',','SEP'],
    '(':['(','(','SEP'],
    ')':[')',')','SEP']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar',methods=['post'])
def analizar():
    if request.method=='POST':
        data=request.form['data']
        lt.clear()
    def_tokens.errores.clear()    
    def_tokens.t_simb = t_simb2.copy()
    # Give the lexer some input
    def_tokens.lexer.input(data)
    # Set the initial lineno
    def_tokens.lexer.lineno=1

    # Tokenize
    while True:
        tok = def_tokens.lexer.token()
        if not tok: 
            break      # No more input
        lt.append(def_tokens.t_simb.get(tok.value))
    #return render_template('lexico.html', ts=list(def_tokens.t_simb.values()), toks=lt, errores=def_tokens.errores,corrida=corrida,cad=cad)
    return render_template('resultados.html',ts=list(def_tokens.t_simb.values()), toks=lt, errores=def_tokens.errores)


if __name__=='__app__':
    app.run(debug=True)#se habilita el debug para que la app web sea sensible a los cambios
    