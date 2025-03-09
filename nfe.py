import pandas as pd
import re

# Lista com os dados extraídos
data = [
    {"Nome": "MACA NAC.GALA", "Código": "1825", "Quantidade": "1.7350", "Unidade": "KG9", "Valor Unitário": "10,90", "Valor Total": "18,91"},
    {"Nome": "RF.REQUEIJAO LIGTHT", "Código": "52483", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "8,49", "Valor Total": "25,47"},
    {"Nome": "MANT.ITAMBE C/S POT", "Código": "51059", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "21,90", "Valor Total": "21,90"},
    {"Nome": "IOG.FRUTAP", "Código": "74203", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "8,79", "Valor Total": "8,79"},
    {"Nome": "RF.IOG.ITAMBE", "Código": "91122", "Quantidade": "2.0000", "Unidade": "UND9", "Valor Unitário": "13,99", "Valor Total": "27,98"},
    {"Nome": "PAO QUEIJO TRAD.", "Código": "85080", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "7,90", "Valor Total": "7,90"},
    {"Nome": "PAO FORMA PULLMAN", "Código": "70385", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "11,99", "Valor Total": "11,99"},
    {"Nome": "PAO PULLMAN ARTESANO", "Código": "86252", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "15,99", "Valor Total": "15,99"},
    {"Nome": "CHIMICHURRI NERESCO", "Código": "93130", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "7,59", "Valor Total": "7,59"},
    {"Nome": "CHA LEAO CAMOMILA", "Código": "6455", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "3,99", "Valor Total": "3,99"},
    {"Nome": "MILHO PIP.MICRO YOKI", "Código": "6326", "Quantidade": "2.0000", "Unidade": "PCT9", "Valor Unitário": "5,29", "Valor Total": "10,58"},
    {"Nome": "CHA DR OETKER", "Código": "73287", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "7,99", "Valor Total": "7,99"},
    {"Nome": "OVO BCO GD CINTA", "Código": "21827", "Quantidade": "1.0000", "Unidade": "CXA9", "Valor Unitário": "49,90", "Valor Total": "49,90"},
    {"Nome": "DOCE S.HELENA PACOQ.", "Código": "53387", "Quantidade": "1.0000", "Unidade": "CXA9", "Valor Unitário": "36,90", "Valor Total": "36,90"},
    {"Nome": "PRATO DESC.F.FACIL15", "Código": "22236", "Quantidade": "5.0000", "Unidade": "UND9", "Valor Unitário": "1,99", "Valor Total": "9,95"},
    {"Nome": "MILHO PIP.MICRO YOKI", "Código": "11634", "Quantidade": "2.0000", "Unidade": "PCT9", "Valor Unitário": "5,29", "Valor Total": "10,58"},
    {"Nome": "CAFE 3COR.CAPP.CLASS", "Código": "4716", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "25,99", "Valor Total": "25,99"},
    {"Nome": "CHA LEAO", "Código": "75777", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "4,29", "Valor Total": "12,87"},
    {"Nome": "CHA LEAO CIDREIRA", "Código": "6454", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "3,99", "Valor Total": "3,99"},
    {"Nome": "CHA LEAO", "Código": "85865", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "13,90", "Valor Total": "13,90"},
    {"Nome": "LEITE PO ITAMBE LT", "Código": "91792", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "13,98", "Valor Total": "41,94"},
    {"Nome": "DET.LIQ.LIMPOL", "Código": "6149", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "1,99", "Valor Total": "1,99"},
    {"Nome": "BISCOITO ARROZ KODIL", "Código": "64649", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "5,99", "Valor Total": "17,97"},
    {"Nome": "CHA LEAO COLD BREW", "Código": "64996", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "12,99", "Valor Total": "12,99"},
    {"Nome": "ACUC.CRIST.REI", "Código": "18696", "Quantidade": "1.0000", "Unidade": "PCT9", "Valor Unitário": "6,98", "Valor Total": "6,98"},
    {"Nome": "BISC.BAUDUCCO WAFER", "Código": "39391", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "3,89", "Valor Total": "11,67"},
    {"Nome": "TORRADA BAUDUCCO", "Código": "64596", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "4,69", "Valor Total": "14,07"},
    {"Nome": "FILTRO.CAFE BRIGITTA", "Código": "39425", "Quantidade": "4.0000", "Unidade": "UND9", "Valor Unitário": "4,75", "Valor Total": "19,00"},
    {"Nome": "BISC.SEQUILHO LIMAO", "Código": "82238", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "2,29", "Valor Total": "2,29"},
    {"Nome": "BISC.BAUDUCCO COOKIE", "Código": "83167", "Quantidade": "3.0000", "Unidade": "UND8", "Valor Unitário": "4,89", "Valor Total": "14,67"},
    {"Nome": "BISC.SEQUILHO TRAD.", "Código": "82236", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "2,29", "Valor Total": "6,87"},
    {"Nome": "BISC.SEQUILHO BAUN", "Código": "82235", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "2,29", "Valor Total": "2,29"},
    {"Nome": "BISC.NESTLE BONO", "Código": "83723", "Quantidade": "4.0000", "Unidade": "UND9", "Valor Unitário": "2,29", "Valor Total": "9,16"},
    {"Nome": "AMENDOIM AMINDUS", "Código": "75403", "Quantidade": "1.0000", "Unidade": "EMB4", "Valor Unitário": "47,40", "Valor Total": "47,40"},
    {"Nome": "AMENDOIM S.HELENA CR", "Código": "40268", "Quantidade": "1.0000", "Unidade": "UND8", "Valor Unitário": "22,90", "Valor Total": "22,90"},
    {"Nome": "BISNAGUITO PULLMAN", "Código": "20048", "Quantidade": "2.0000", "Unidade": "PCT9", "Valor Unitário": "6,99", "Valor Total": "13,98"},
    {"Nome": "BISC.LACTA BIS", "Código": "91038", "Quantidade": "2.0000", "Unidade": "UND9", "Valor Unitário": "15,99", "Valor Total": "31,98"},
    {"Nome": "GRANOLA TIA SONIA", "Código": "60972", "Quantidade": "1.0000", "Unidade": "UND9", "Valor Unitário": "38,90", "Valor Total": "38,90"},
    {"Nome": "AVEIA APTI", "Código": "76784", "Quantidade": "3.0000", "Unidade": "UND9", "Valor Unitário": "3,89", "Valor Total": "11,67"},
    {"Nome": "GARFO BIO S/MESA", "Código": "67016", "Quantidade": "8.0000", "Unidade": "UND9", "Valor Unitário": "4,85", "Valor Total": "38,80"},
    {"Nome": "CAFE MELITTA EXT", "Código": "57172", "Quantidade": "2.0000", "Unidade": "UND9", "Valor Unitário": "29,45", "Valor Total": "58,90"},
    {"Nome": "PAO QUEIJO MINI", "Código": "85242", "Quantidade": "0.3180", "Unidade": "KG9", "Valor Unitário": "22,90", "Valor Total": "7,28"},
    {"Nome": "BANANA NANICA", "Código": "1643", "Quantidade": "2.0300", "Unidade": "KG9", "Valor Unitário": "2,99", "Valor Total": "6,07"},
]

# Remove os dígitos que aparecem na coluna "Unidade"
for item in data:
    item["Unidade"] = re.sub(r'\d+', '', item["Unidade"])

# Converte os valores monetários para float (substituindo vírgula por ponto)
for item in data:
    item["Valor Unitário"] = float(item["Valor Unitário"].replace(',', '.'))
    item["Valor Total"] = float(item["Valor Total"].replace(',', '.'))

# Cria o DataFrame com as colunas desejadas
df = pd.DataFrame(data, columns=["Nome", "Código", "Quantidade", "Unidade", "Valor Unitário", "Valor Total"])

# Exporta o DataFrame para um arquivo Excel com formatação de moeda
with pd.ExcelWriter("tabela_itens.xlsx", engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Itens')
    workbook = writer.book
    worksheet = writer.sheets['Itens']
    
    # Define um formato de moeda (R$)
    currency_format = workbook.add_format({'num_format': 'R$ #,##0.00'})
    
    # Aplica o formato para as colunas de Valor Unitário (E) e Valor Total (F)
    worksheet.set_column('E:E', None, currency_format)
    worksheet.set_column('F:F', None, currency_format)

print("Arquivo 'tabela_itens.xlsx' gerado com sucesso!")
