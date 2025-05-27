#!/bin/bash

echo "🌐 Starting Grace AI Operating System Deployment..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create default directory structure
mkdir -p logs data pods registry

# Optional: Export config if needed
export ENVIRONMENT=production
export DB_URL=postgresql://grace:yourpassword@localhost:5432/grace_prod
export REDIS_URL=redis://localhost:6379/0

# Run Grace main OS
echo "🚀 Launching Grace AI Core..."
nohup python3 grace_os_complete.py > logs/grace_output.log 2>&1 &

# Wait a moment to ensure boot
sleep 3
echo "✅ Grace launched in background. Logs available in logs/grace_output.log"
