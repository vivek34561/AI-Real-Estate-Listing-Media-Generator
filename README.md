# AI Real Estate Listing Media Generator

## Overview
An AI-powered system that transforms basic real estate photos into professional-grade listing media, including enhanced images, virtually staged rooms, and walkthrough videos.

## Business Problem
- Real estate agents lose leads due to poor quality photos and lack of walkthrough videos
- Professional photography shoots are expensive ($300-$500) and time-consuming
- Quick turnaround needed for competitive listings

## Solution
Upload room images with style preferences, and the system automatically:
- Enhances image quality
- Virtually stages rooms with furniture and decor
- Generates short walkthrough videos

## Tech Stack
- **Backend**: FastAPI
- **Agent Orchestration**: LangGraph
- **Image Generation**: Stable Diffusion, ControlNet
- **Video Generation**: Image-to-Video models
- **Quality Assurance**: CLIP similarity checks
- **GPU**: Kaggle/Colab (batch processing)

## Project Status
🚧 Under Development

## Getting Started
See [docs/setup.md](docs/setup.md) for installation and setup instructions.

## Architecture
See [docs/architecture.md](docs/architecture.md) for system design details.
