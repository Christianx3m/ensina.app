Write-Host "🚀 Iniciando ambiente Ensina.app" -ForegroundColor Cyan

# 1️⃣ Ativar ambiente virtual
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    Write-Host "🟡 Ativando ambiente virtual..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
} else {
    Write-Host "❌ Ambiente virtual não encontrado. Criando novo..." -ForegroundColor Red
    python -m venv venv
    & .\venv\Scripts\Activate.ps1
}

# 2️⃣ Instalar dependências
if (Test-Path "requirements.txt") {
    Write-Host "📦 Instalando dependências..." -ForegroundColor Yellow
    pip install -r requirements.txt
} else {
    Write-Host "⚠️ Arquivo requirements.txt não encontrado!" -ForegroundColor Red
}

# 3️⃣ Verificar arquivo .env
if (Test-Path ".env") {
    $apiKey = Select-String -Path ".env" -Pattern "OPENAI_API_KEY" -ErrorAction SilentlyContinue
    if ($apiKey) {
        Write-Host "✅ Chave OpenAI encontrada." -ForegroundColor Green
    } else {
        Write-Host "⚠️ Nenhuma chave OPENAI_API_KEY encontrada no .env!" -ForegroundColor Red
    }
} else {
    Write-Host "⚠️ Arquivo .env não encontrado!" -ForegroundColor Red
}

# 4️⃣ Iniciar servidor e abrir navegador
Write-Host "🌐 Iniciando servidor Uvicorn..." -ForegroundColor Green
Start-Process "http://127.0.0.1:8000"
uvicorn main:app --reload
