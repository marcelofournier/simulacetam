#!/bin/bash
#Busca e elimina linhas de questões duplicadas no arquivo quiz.dat
#Salva as questões removidas do arquivo quiz.dat no arquivo linhas_removidas.txt
#Por fim, salva o arquivo quiz.dat somente com as questões válidas, sem duplicação.


# Verifica se o número de argumentos é válido
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <arquivo>"
    exit 1
fi

# Verifica se o arquivo existe
if [ ! -f "$1" ]; then
    echo "O arquivo '$1' não existe."
    exit 1
fi

# Remove as linhas duplicadas do arquivo e salva em um novo arquivo temporário
temp_file=$(mktemp)
awk '!seen[$0]++' "$1" > "$temp_file"

# Extrai as linhas removidas para um novo arquivo
removed_lines_file="linhas_removidas.txt"
awk 'seen[$0]++' "$1" > "$removed_lines_file"

# Sobrescreve o arquivo original com as linhas únicas
mv "$temp_file" "$1"

echo "Linhas duplicadas removidas com sucesso do arquivo '$1'."
echo "Linhas removidas foram salvas no arquivo '$removed_lines_file'."