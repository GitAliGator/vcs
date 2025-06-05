# VCS Metrics - Video Comprehension Score

[![PyPI version](https://badge.fury.io/py/vcs-metrics.svg)](https://badge.fury.io/py/vcs-metrics)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python library for evaluating narrative similarity between reference and generated text using the Video Comprehension Score (VCS) metric.

## Features

- **Global Alignment Score (GAS)**: Measures semantic similarity at the full-text level
- **Local Alignment Score (LAS)**: Evaluates segment-by-segment semantic similarity  
- **Narrative Alignment Score (NAS)**: Assesses how well narrative flow is preserved
- **Comprehensive Visualizations**: Generate detailed plots and PDF reports
- **Flexible Configuration**: Customizable parameters for different use cases

## Installation

```bash
pip install vcs-metrics
```

### Development Installation

```bash
git clone https://github.com/yourusername/vcs-metrics.git
cd vcs-metrics
pip install -e ".[dev]"
```

## Quick Start

```python
import torch
from vcs import compute_vcs_score

# Example segmenter function (you can use any tokenizer)
def simple_segmenter(text):
    return text.split('.')

# Example embedding function (replace with your preferred model)
def embedding_function(texts):
    # This is a placeholder - use actual embeddings like BERT, SBERT, etc.
    # Should return a torch.Tensor of shape (len(texts), embedding_dim)
    return torch.randn(len(texts), 384)  # Example with 384-dim embeddings

# Compute VCS score
reference_text = "The cat sat on the mat. It was a sunny day."
generated_text = "A cat was sitting on a mat. The weather was nice."

result = compute_vcs_score(
    reference_text=reference_text,
    generated_text=generated_text,
    segmenter_fn=simple_segmenter,
    embedding_fn_las=embedding_function,
    embedding_fn_gas=embedding_function,
    return_all_metrics=True,
    return_internals=True
)

print(f"VCS Score: {result['VCS']:.4f}")
print(f"GAS Score: {result['GAS']:.4f}")
print(f"LAS Score: {result['LAS']:.4f}")
print(f"NAS Score: {result['NAS']:.4f}")
```

## Advanced Usage

### With Sentence Transformers

```python
from sentence_transformers import SentenceTransformer
import torch
import nltk

# Download required NLTK data
nltk.download('punkt')

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

def sentence_segmenter(text):
    return nltk.sent_tokenize(text)

def sbert_embedding_function(texts):
    embeddings = model.encode(texts)
    return torch.tensor(embeddings)

# Compute VCS with better embeddings
result = compute_vcs_score(
    reference_text=reference_text,
    generated_text=generated_text,
    segmenter_fn=sentence_segmenter,
    embedding_fn_las=sbert_embedding_function,
    embedding_fn_gas=sbert_embedding_function,
    chunk_size=1,
    context_cutoff_value=0.6,
    context_window_control=4.0,
    lct=0,
    return_all_metrics=True,
    return_internals=True
)
```

### Generate Visualizations

```python
from vcs import (
    visualize_similarity_matrix,
    visualize_las,
    visualize_distance_nas,
    create_vcs_pdf_report
)

# Generate individual visualizations
if 'internals' in result:
    internals = result['internals']
    
    # Create similarity matrix plot
    sim_fig = visualize_similarity_matrix(internals)
    sim_fig.show()
    
    # Create LAS visualization
    las_fig = visualize_las(internals)
    las_fig.show()
    
    # Create distance-based NAS visualization
    nas_fig = visualize_distance_nas(internals)
    nas_fig.show()
    
    # Generate comprehensive PDF report
    create_vcs_pdf_report(
        internals=internals,
        output_file="vcs_analysis_report.pdf",
        metrics_to_include="all"  # or specify list like ["LAS", "NAS Distance"]
    )
```

## API Reference

### Main Function

#### `compute_vcs_score()`

Computes the Video Comprehension Score and related metrics.

**Parameters:**
- `reference_text` (str): The reference text to compare against
- `generated_text` (str): The generated text to evaluate  
- `segmenter_fn` (Callable): Function to segment text into units
- `embedding_fn_las` (Callable): Function to compute embeddings for LAS calculation
- `embedding_fn_gas` (Callable, optional): Function for GAS calculation (defaults to embedding_fn_las)
- `chunk_size` (int, default=1): Number of segments to group together
- `context_cutoff_value` (float, default=0.6): Threshold for context window application
- `context_window_control` (float, default=4.0): Controls context window size
- `lct` (int, default=0): Local Chronology Tolerance for narrative flow
- `return_all_metrics` (bool, default=False): Return detailed breakdown of all metrics
- `return_internals` (bool, default=False): Return internal computation details for visualization

**Returns:**
Dictionary containing VCS score and optionally other metrics and internals.

### Visualization Functions

- `visualize_config()`: Display configuration parameters
- `visualize_text_chunks()`: Show text segmentation
- `visualize_similarity_matrix()`: Display similarity heatmap
- `visualize_mapping_windows()`: Show alignment windows
- `visualize_best_match()`: Display matching details
- `visualize_las()`: Local Alignment Score visualization
- `visualize_distance_nas()`: Distance-based NAS metrics
- `visualize_line_nas()`: Line-based NAS metrics  
- `visualize_window_regularizer()`: Window regularization analysis
- `visualize_metrics_summary()`: Overview of all metrics
- `create_vcs_pdf_report()`: Generate comprehensive PDF report

## Configuration

The library provides several configuration constants that can be imported:

```python
from vcs import (
    DEFAULT_CONTEXT_CUTOFF_VALUE,    # 0.6
    DEFAULT_CONTEXT_WINDOW_CONTROL,  # 4.0
    DEFAULT_LCT,                     # 0
    DEFAULT_CHUNK_SIZE,              # 1
)
```

## Understanding the Metrics

### VCS (Video Comprehension Score)
The overall metric combining GAS, LAS, and NAS to provide a comprehensive similarity score.

### GAS (Global Alignment Score)  
Measures semantic similarity between the complete reference and generated texts using full-document embeddings.

### LAS (Local Alignment Score)
Evaluates similarity at the segment level by finding optimal alignments between reference and generated text segments.

### NAS (Narrative Alignment Score)
Assesses how well the narrative structure and flow is preserved, combining:
- **NAS-D (Distance-based)**: Penalizes segments that align far from expected positions
- **NAS-L (Line-based)**: Evaluates the smoothness of the alignment path

## Requirements

- Python 3.8+
- numpy >= 1.20.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0
- PyTorch >= 1.9.0 (install separately, see below)

### PyTorch Installation

PyTorch is not included as a direct dependency to avoid conflicts with existing installations. Install it separately:

```bash
# For CPU-only (most common)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# For CUDA (if you have compatible GPU)
pip install torch torchvision torchaudio
```

In Google Colab, PyTorch is pre-installed, so no additional installation is needed.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/yourusername/vcs-metrics.git
cd vcs-metrics
pip install -e ".[dev]"
pre-commit install
```

### Code Formatting

```bash
black src/
isort src/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this library in your research, please cite:

```bibtex
@software{vcs_metrics,
  title = {VCS Metrics: Video Comprehension Score for Text Similarity},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/yourusername/vcs-metrics}
}
```

## Support

- Documentation: [https://vcs-metrics.readthedocs.io](https://vcs-metrics.readthedocs.io)
- Issues: [GitHub Issues](https://github.com/yourusername/vcs-metrics/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/vcs-metrics/discussions)