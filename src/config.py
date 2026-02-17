"""Application configuration using pydantic-settings"""

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Application
    app_name: str = "AI Real Estate Media Generator"
    environment: Literal["development", "staging", "production"] = "development"
    debug: bool = True
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 4

    # Database
    database_url: str = "sqlite:///./data/app.db"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # File Storage
    upload_dir: Path = Path("./uploads")
    output_dir: Path = Path("./outputs")
    temp_dir: Path = Path("./temp")
    max_upload_size_mb: int = 50

    # GPU Processing
    gpu_provider: Literal["kaggle", "colab", "local"] = "kaggle"
    batch_processing: bool = True
    max_batch_size: int = 10

    # Kaggle API
    kaggle_username: str = ""
    kaggle_key: str = ""

    # Model Configuration
    image_enhancement_model: str = "stabilityai/stable-diffusion-2-1"
    staging_model: str = "lllyasviel/control_v11p_sd15_canny"
    video_model: str = "stabilityai/stable-video-diffusion-img2vid"

    # Generation Parameters
    image_width: int = 1024
    image_height: int = 768
    inference_steps: int = 30
    guidance_scale: float = 7.5
    video_frames: int = 24
    video_fps: int = 8

    # Quality Assurance
    clip_similarity_threshold: float = 0.75
    max_retries: int = 3

    # LangGraph Agent
    agent_max_iterations: int = 10
    agent_timeout_seconds: int = 300

    # Monitoring
    enable_metrics: bool = True
    metrics_port: int = 9090

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create directories if they don't exist
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)


# Global settings instance
settings = Settings()
