import PySimpleGUI as sg

# ===== LAYOUT =====
layout = [

    [sg.Text(" Sistema Escolar", font=("Arial black", 20))],

    # PROFESSOR
    [sg.Text("Nome do Professor")],
    [sg.Input(key="professor")],

    # ALUNO
    [sg.Text("Nome do Aluno")],
    [sg.Input(key="aluno")],

    # DADOS
    [sg.Text ("Meses de Aula")],
    [sg.Input(key="meses")],

    [sg.Text("Aulas por Mês")],
    [sg.Input(key="aulas_mes")],

    [sg.Text("Faltas")],
    [sg.Input(key="faltas")],

    [sg.Text ("Primeira Nota")],
    [sg.Input(key="nota1")],

     [sg.Text ("Segunda Nota")],
    [sg.Input(key="nota2")],

    # BOTÃO
    [sg.Button("Calcular")],

    # RESULTADO
    [sg.Text("", key="resultado")]
]

# ===== JANELA =====
janela = sg.Window("EduLogic System", layout)

# ===== LOOP =====
while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break

    if evento == "Calcular":
        try:

            #Calculo Frequencia
            meses = int(valores["meses"])
            aulas_mes = int(valores["aulas_mes"])
            faltas = int(valores["faltas"])

            total_aulas = meses * aulas_mes
            presencas = total_aulas - faltas

            frequencia = (presencas / total_aulas) * 100 
            
            #Calculo Notas

            nota1 = float(valores["nota1"])
            nota2 = float(valores["nota2"])
            
            media = (nota1 + nota2) / 2

            if frequencia >= 75 and media >= 7:
                status = "Aprovado"
            elif frequencia >= 75 and media <= 5 or media < 7:
                status = "Recuperação"
            else:
                status = "Reprovado"    

            resultado = f"""
Aluno: {valores['aluno']}
Frequência: {frequencia:.2f}%
Situação: {status}
"""

            janela["resultado"].update(resultado)

        except:
            sg.popup("Preencha os campos corretamente!")

janela.close()