# Setup Guide

## Prerequisites

- Python 3.11+
- Redis (for Celery)
- Git
- Kaggle account (for GPU processing)

## Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd AI_Real_Estate_Listing_Media_Generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
# Copy example env file
cp .env.example .env

# Edit .env with your settings
# Minimum required:
# - KAGGLE_USERNAME
# - KAGGLE_KEY
```

### 5. Initialize Database
```bash
# Create data directory
mkdir data

# Run migrations (when implemented)
# alembic upgrade head
```

### 6. Start Redis
```bash
# Windows (using WSL or Docker)
docker run -d -p 6379:6379 redis:latest

# Linux
sudo systemctl start redis

# Mac
brew services start redis
```

## Running the Application

### Development Mode

#### Terminal 1: FastAPI Server
```bash
python -m src.main
```
Server runs at: http://localhost:8000

#### Terminal 2: Celery Worker
```bash
celery -A src.workers.celery_app worker --loglevel=info
```

### Production Mode
```bash
# Use gunicorn or uvicorn with workers
uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Kaggle Setup

### 1. Get API Credentials
1. Go to https://www.kaggle.com/settings
2. Scroll to "API" section
3. Click "Create New API Token"
4. Download `kaggle.json`

### 2. Configure Credentials
```bash
# Windows
mkdir %USERPROFILE%\.kaggle
copy kaggle.json %USERPROFILE%\.kaggle\

# Linux/Mac
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### 3. Add to .env
```
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_key
```

## Verification

### Check API
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "gpu_provider": "kaggle",
  "batch_processing": true
}
```

### Check Celery
```bash
celery -A src.workers.celery_app inspect ping
```

## Troubleshooting

### Redis Connection Error
- Ensure Redis is running: `redis-cli ping` (should return PONG)
- Check REDIS_URL in .env

### Import Errors
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Kaggle API Errors
- Verify credentials in ~/.kaggle/kaggle.json
- Check KAGGLE_USERNAME and KAGGLE_KEY in .env

## Next Steps

1. Read [architecture.md](architecture.md) to understand system design
2. Explore API documentation at http://localhost:8000/docs
3. Run tests: `pytest tests/`
4. Start building! See [development.md](development.md)

## Development Tools

### Code Formatting
```bash
black src/ tests/
```

### Linting
```bash
ruff check src/ tests/
```

### Type Checking
```bash
mypy src/
```

### Run All Checks
```bash
black src/ tests/ && ruff check src/ tests/ && mypy src/ && pytest tests/
```
