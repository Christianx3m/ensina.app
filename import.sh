#!/bin/bash

# Caminho para o CSV
CSV_FILE="project_seed.csv"

# Número do projeto do GitHub (ajuste este valor)
PROJECT_NUMBER=5

# Ler CSV linha por linha (pulando o cabeçalho)
tail -n +2 "$CSV_FILE" | while IFS=, read -r tarefa status responsavel due
do
  echo "Adicionando tarefa: $tarefa"
  gh project item-add "$PROJECT_NUMBER" \
    --owner "Christianx3m" \
    --format json \
    | gh project item-edit --id "$(jq -r '.id')" \
      --field "Title=$tarefa" \
      --field "Status=$status" \
      --field "Responsável=$responsavel" \
      --field "Due=$due"

done
