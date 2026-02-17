# Notebooks

## Kaggle Notebooks
These notebooks are designed to run on Kaggle with GPU acceleration:

- **image_enhancement.ipynb**: Image enhancement using Stable Diffusion
- **virtual_staging.ipynb**: Virtual staging using ControlNet
- **video_generation.ipynb**: Video generation using Stable Video Diffusion

## Experiments
Notebooks for experimentation and model comparison:

- **model_comparison.ipynb**: Compare different models and parameters
- **prompt_engineering.ipynb**: Test and optimize prompts

## Usage

### Running on Kaggle
1. Upload notebook to Kaggle
2. Enable GPU accelerator (Settings → Accelerator → GPU)
3. Add input datasets if needed
4. Run all cells

### Running Locally (if GPU available)
```bash
jupyter notebook
```

## Tips
- Always save outputs to `/kaggle/working/` on Kaggle
- Use batch processing for multiple images
- Monitor GPU memory usage
