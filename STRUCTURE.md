# Project Structure

```
AI_Real_Estate_Listing_Media_Generator/
│
├── src/                                    # Main application code
│   ├── __init__.py
│   ├── main.py                            # FastAPI app entry point
│   ├── config.py                          # Configuration management
│   │
│   ├── api/                               # API layer
│   │   ├── __init__.py
│   │   ├── routes/                        # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── images.py                  # Image upload/enhancement endpoints
│   │   │   ├── jobs.py                    # Job status endpoints
│   │   │   └── videos.py                  # Video generation endpoints
│   │   ├── schemas/                       # Pydantic models
│   │   │   ├── __init__.py
│   │   │   ├── image.py                   # Image request/response schemas
│   │   │   ├── job.py                     # Job schemas
│   │   │   └── video.py                   # Video schemas
│   │   └── dependencies.py                # FastAPI dependencies
│   │
│   ├── agents/                            # LangGraph agents
│   │   ├── __init__.py
│   │   ├── orchestrator.py                # Main orchestration agent
│   │   ├── nodes/                         # Agent nodes
│   │   │   ├── __init__.py
│   │   │   ├── preprocess.py              # Image preprocessing
│   │   │   ├── enhance.py                 # Image enhancement
│   │   │   ├── stage.py                   # Virtual staging
│   │   │   ├── validate.py                # Quality validation
│   │   │   └── generate_video.py          # Video generation
│   │   └── state.py                       # Agent state definitions
│   │
│   ├── models/                            # AI model wrappers
│   │   ├── __init__.py
│   │   ├── base.py                        # Base model interface
│   │   ├── enhancement.py                 # Stable Diffusion wrapper
│   │   ├── staging.py                     # ControlNet wrapper
│   │   ├── video.py                       # SVD wrapper
│   │   └── clip_validator.py              # CLIP similarity checker
│   │
│   ├── gpu/                               # GPU provider integrations
│   │   ├── __init__.py
│   │   ├── base.py                        # Base GPU provider interface
│   │   ├── kaggle.py                      # Kaggle integration
│   │   ├── colab.py                       # Colab integration
│   │   └── local.py                       # Local GPU fallback
│   │
│   ├── workers/                           # Celery workers
│   │   ├── __init__.py
│   │   ├── celery_app.py                  # Celery configuration
│   │   └── tasks.py                       # Celery tasks
│   │
│   ├── db/                                # Database layer
│   │   ├── __init__.py
│   │   ├── base.py                        # SQLAlchemy base
│   │   ├── models.py                      # Database models
│   │   ├── session.py                     # Database session
│   │   └── repositories/                  # Data access layer
│   │       ├── __init__.py
│   │       ├── job.py                     # Job repository
│   │       └── media.py                   # Media repository
│   │
│   ├── services/                          # Business logic
│   │   ├── __init__.py
│   │   ├── image_service.py               # Image processing service
│   │   ├── job_service.py                 # Job management service
│   │   └── video_service.py               # Video generation service
│   │
│   └── utils/                             # Utilities
│       ├── __init__.py
│       ├── file_handler.py                # File operations
│       ├── logger.py                      # Logging configuration
│       └── validators.py                  # Input validators
│
├── tests/                                 # Test suite
│   ├── __init__.py
│   ├── conftest.py                        # Pytest fixtures
│   ├── unit/                              # Unit tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_services.py
│   │   └── test_validators.py
│   ├── integration/                       # Integration tests
│   │   ├── __init__.py
│   │   ├── test_api.py
│   │   └── test_agents.py
│   └── e2e/                               # End-to-end tests
│       ├── __init__.py
│       └── test_workflow.py
│
├── notebooks/                             # Jupyter notebooks
│   ├── kaggle/                            # Kaggle notebooks
│   │   ├── image_enhancement.ipynb        # Enhancement pipeline
│   │   ├── virtual_staging.ipynb          # Staging pipeline
│   │   └── video_generation.ipynb         # Video pipeline
│   └── experiments/                       # Experimentation notebooks
│       ├── model_comparison.ipynb
│       └── prompt_engineering.ipynb
│
├── scripts/                               # Utility scripts
│   ├── setup_kaggle.py                    # Kaggle setup automation
│   ├── download_models.py                 # Model weight downloader
│   └── seed_db.py                         # Database seeding
│
├── docs/                                  # Documentation
│   ├── architecture.md                    # System architecture
│   ├── setup.md                           # Setup guide
│   ├── api.md                             # API documentation
│   ├── development.md                     # Development guide
│   └── deployment.md                      # Deployment guide
│
├── alembic/                               # Database migrations
│   ├── versions/                          # Migration files
│   └── env.py                             # Alembic configuration
│
├── data/                                  # Local data (gitignored)
│   └── app.db                             # SQLite database
│
├── uploads/                               # User uploads (gitignored)
├── outputs/                               # Generated outputs (gitignored)
├── temp/                                  # Temporary files (gitignored)
│
├── .env                                   # Environment variables (gitignored)
├── .env.example                           # Environment template
├── .gitignore                             # Git ignore rules
├── requirements.txt                       # Python dependencies
├── pyproject.toml                         # Python project config
├── README.md                              # Project overview
└── STRUCTURE.md                           # This file
```

## Key Directories Explained

### `/src`
Main application code organized by layers:
- **api**: REST API endpoints and schemas
- **agents**: LangGraph orchestration logic
- **models**: AI model wrappers
- **gpu**: GPU provider integrations
- **workers**: Background task processing
- **db**: Database models and repositories
- **services**: Business logic layer
- **utils**: Shared utilities

### `/tests`
Comprehensive test suite:
- **unit**: Fast, isolated tests
- **integration**: Component interaction tests
- **e2e**: Full workflow tests

### `/notebooks`
Jupyter notebooks for:
- Kaggle GPU execution
- Model experimentation
- Prompt engineering

### `/docs`
Project documentation:
- Architecture design
- Setup instructions
- API reference
- Development guides

## Design Patterns

### Layered Architecture
```
API Layer (FastAPI)
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Data Access)
    ↓
Database Layer (SQLAlchemy)
```

### Agent Pattern
```
LangGraph Orchestrator
    ↓
Agent Nodes (Preprocess → Enhance → Stage → Validate → Video)
    ↓
Model Wrappers (Diffusion, ControlNet, SVD)
    ↓
GPU Providers (Kaggle, Colab, Local)
```

### Async Task Pattern
```
API Request
    ↓
Create Job (Database)
    ↓
Queue Task (Celery)
    ↓
Return Job ID
    ↓
Background Processing
    ↓
Update Job Status
```

## File Naming Conventions

- **Python files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions**: `snake_case()`
- **Constants**: `UPPER_SNAKE_CASE`
- **Test files**: `test_*.py`

## Import Organization

```python
# Standard library
import os
from typing import List

# Third-party
from fastapi import FastAPI
from pydantic import BaseModel

# Local
from src.config import settings
from src.models.base import BaseModel
```

## Next Steps

1. Implement core API endpoints in `/src/api/routes/`
2. Build LangGraph agent in `/src/agents/`
3. Create model wrappers in `/src/models/`
4. Set up Celery tasks in `/src/workers/`
5. Write tests in `/tests/`
