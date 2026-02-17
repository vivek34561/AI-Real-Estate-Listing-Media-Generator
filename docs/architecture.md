# System Architecture

## Overview
The AI Real Estate Media Generator uses a **decoupled, batch-processing architecture** designed to work with limited GPU resources while maintaining professional-grade output quality.

## High-Level Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Client    │─────▶│  FastAPI     │─────▶│  LangGraph  │
│  (Upload)   │      │  Backend     │      │   Agent     │
└─────────────┘      └──────────────┘      └─────────────┘
                            │                      │
                            ▼                      ▼
                     ┌──────────────┐      ┌─────────────┐
                     │   Database   │      │   Celery    │
                     │  (Job State) │      │ Task Queue  │
                     └──────────────┘      └─────────────┘
                                                  │
                                                  ▼
                                          ┌─────────────┐
                                          │   GPU       │
                                          │ Processing  │
                                          │ (Batch)     │
                                          └─────────────┘
```

## Components

### 1. FastAPI Backend
- **Purpose**: REST API for client interactions
- **Responsibilities**:
  - Accept image uploads
  - Validate inputs
  - Create processing jobs
  - Return job status and results
- **Tech**: FastAPI, Pydantic

### 2. LangGraph Agent
- **Purpose**: Orchestrate multi-step generation pipeline
- **Workflow**:
  1. Image preprocessing
  2. Enhancement generation
  3. Virtual staging
  4. Quality validation (CLIP)
  5. Video generation (optional)
  6. Retry logic on failures
- **Tech**: LangGraph, LangChain

### 3. Celery Task Queue
- **Purpose**: Asynchronous job processing
- **Why**: Decouples API from GPU processing
- **Benefits**:
  - Non-blocking API responses
  - Retry mechanisms
  - Job prioritization
- **Tech**: Celery, Redis

### 4. GPU Processing Layer
- **Purpose**: Run AI models for generation
- **Providers**:
  - **Kaggle**: Batch notebook execution
  - **Colab**: Manual/semi-automated
  - **Local**: If GPU available
- **Models**:
  - Stable Diffusion (enhancement)
  - ControlNet (staging)
  - SVD (video generation)

### 5. Database
- **Purpose**: Store job metadata and state
- **Schema**:
  - Jobs (id, status, created_at, etc.)
  - Images (original, enhanced, staged)
  - Videos (if generated)
- **Tech**: SQLAlchemy, SQLite (dev) / PostgreSQL (prod)

## Data Flow

### User Upload Flow
```
1. User uploads images + style preferences
2. API validates and stores files
3. Job created in database (status: pending)
4. Celery task queued
5. API returns job_id to user
6. User polls /jobs/{job_id} for status
```

### GPU Processing Flow
```
1. Celery worker picks up job
2. LangGraph agent starts orchestration
3. Prepares inputs for GPU
4. Submits to GPU provider (Kaggle/Colab)
5. GPU runs models in batch
6. Outputs downloaded and validated
7. Job status updated (completed/failed)
8. User retrieves results
```

## GPU Strategy

### Why Batch Processing?
- **No persistent GPU**: Free tiers have session limits
- **Cost-effective**: Only use GPU when needed
- **Scalable**: Can switch providers easily

### Kaggle Integration
- **Input**: Upload images + config to Kaggle dataset
- **Processing**: Run notebook with models
- **Output**: Download generated media
- **Automation**: Kaggle API for programmatic control

### Latency Expectations
- **Images only**: 1-3 minutes
- **Images + video**: 3-6 minutes
- **Acceptable for real estate**: Yes (not real-time needed)

## Quality Assurance

### CLIP Similarity Check
- Compare generated image to prompt
- Threshold: 0.75 (configurable)
- Retry if below threshold

### Retry Logic
- Max retries: 3
- Exponential backoff
- Different seeds per retry

## Scalability Considerations

### Current (MVP)
- Single worker
- SQLite database
- Manual Kaggle uploads

### Future (Production)
- Multiple Celery workers
- PostgreSQL with connection pooling
- Automated Kaggle API integration
- CDN for media delivery
- Paid GPU APIs (Replicate, RunPod)

## Security

- Input validation (file types, sizes)
- Rate limiting
- API authentication (future)
- Secure file storage

## Monitoring

- Job success/failure rates
- Processing times
- GPU utilization
- Error tracking

## Technology Choices

| Component | Technology | Why |
|-----------|-----------|-----|
| Backend | FastAPI | Fast, async, type-safe |
| Orchestration | LangGraph | Agent workflows, retries |
| Task Queue | Celery | Industry standard, reliable |
| Database | SQLAlchemy | ORM, migration support |
| GPU | Kaggle/Colab | Free, sufficient for MVP |
| Models | Diffusers | Open-source, flexible |

## Design Principles

1. **Decoupling**: API ≠ GPU processing
2. **Async-first**: Non-blocking operations
3. **Retry-friendly**: Handle GPU failures gracefully
4. **Observable**: Log everything
5. **Testable**: Mock GPU for tests
6. **Scalable**: Easy to add paid GPUs later
