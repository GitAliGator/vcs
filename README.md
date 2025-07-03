<div align="center">
  <h1 align="center">Video Comprehension Score (VCS)</h1>
  <a href="https://github.com/hdubey-debug/vcs">
    <img src=".github/assets/vcs-process-flow.png" alt="VCS Process Flow" width="700"/>
  </a>
  <p align="center">
    <em>A Comprehensive Python Library for Narrative Similarity Evaluation between two very long descriptions </em>
    <br />
  </p>
</div>

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/vcs-metrics?color=teal&style=for-the-badge)](https://badge.fury.io/py/vcs-metrics)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-teal?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-github.io-teal?style=for-the-badge&logo=gitbook&logoColor=white)](https://hdubey-debug.github.io/vcs/)

</div>

<p align="center">
  <a href="https://github.com/hdubey-debug/vcs/issues">🐛 Report Bug</a>
  ·
  <a href="https://github.com/hdubey-debug/vcs/discussions">💬 Community Q&A</a>
</p>

---
## 🌟 Key Features

Click on a feature to learn more.

<table width="100%" align="center" style="border: none; border-collapse: collapse;">
  <tr style="background-color: transparent;">
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">🌍 Global Alignment (GAS)</summary>
        <p style="padding-top: 10px;">Measures semantic similarity at the full-text level using advanced embeddings. It provides a holistic view of how well the generated text captures the overall meaning of the reference text.</p>
      </details>
    </td>
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">🎯 Local Alignment (LAS)</summary>
        <p style="padding-top: 10px;">Evaluates segment-by-segment semantic similarity with optimal matching. This is crucial for understanding if specific details and events are correctly represented in the generated text.</p>
      </details>
    </td>
  </tr>
  <tr style="background-color: transparent;">
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">📖 Narrative Flow (NAS)</summary>
        <p style="padding-top: 10px;">Assesses how well the narrative structure and chronology are preserved. It ensures that the order and flow of events in the generated text match the reference.</p>
      </details>
    </td>
    <td style="padding: 10px; border: none; vertical-align: top;">
      <details style="border: 1px solid #14b8a6; border-radius: 12px; padding: 20px; background: linear-gradient(145deg, #1f2937, #111827); color: #e5e7eb; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <summary style="cursor: pointer; font-weight: bold; font-size: 1.2em; color: #6ee7b7;">📊 Rich Visualizations</summary>
        <p style="padding-top: 10px;">Generate detailed plots, similarity heatmaps, and comprehensive PDF reports to visually inspect and understand the quality of narrative alignment.</p>
      </details>
    </td>
  </tr>
</table>

---

## ⚡ Getting Started

Welcome to VCS Metrics! This guide will walk you through everything you need to start analyzing narrative similarity between texts. We'll cover installation, setup, and your first VCS analysis step by step.


---

### 📦 Step 1: Installation

Choose the installation method that fits your needs:

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🎯 **For Most Users** 
*Recommended if you just want to use VCS*

<details>
<summary><b>🖱️ Click to expand installation steps</b></summary>

<br>

**Terminal Installation:**
```bash
pip install vcs-metrics
```

**Jupyter/Colab Installation:**
```bash
!pip install vcs-metrics
```

<div align="center">

✅ **Ready in 30 seconds**  
🔥 **Zero configuration needed**  
⚡ **Instant access to all features**

</div>

</details>

</td>
<td width="50%" align="center">

### 🛠️ **For Developers**
*If you want to contribute or modify VCS*

<details>
<summary><b>🖱️ Click to expand development setup</b></summary>

<br>

**Terminal Setup:**
```bash
git clone https://github.com/hdubey-debug/vcs.git
cd vcs
pip install -e ".[dev]"
pre-commit install
```

**Jupyter/Colab Setup:**
```bash
!git clone https://github.com/hdubey-debug/vcs.git
%cd vcs
!pip install -e ".[dev]"
!pre-commit install
```

<div align="center">

🔧 **Latest features first**  
🧪 **Testing capabilities**  
🤝 **Contribution ready**

</div>

</details>

</td>
</tr>
</table>

---

<div align="center">

### ⚠️ **PyTorch Requirement**

</div>

<div align="center">
<table style="border: 2px solid #f59e0b; border-radius: 12px; background: linear-gradient(145deg, #fef3c7, #fde68a); padding: 20px;">
<tr>
<td align="center">

**🔥 PyTorch >= 1.9.0 Required**

VCS Metrics needs PyTorch but doesn't install it automatically to avoid conflicts.

<div align="center">

[![PyTorch](https://img.shields.io/badge/Get_PyTorch-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)

</div>

**💡 Pro Tip:** In Google Colab, PyTorch is pre-installed!

</td>
</tr>
</table>
</div>

---

### 🛠️ System Requirements

Before installing VCS, make sure your system meets these requirements:

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🐍 **Python**

<div style="background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 20px; border-radius: 12px; border: 2px solid #3b82f6;">

<img src="https://img.shields.io/badge/Python-3.10+-306998?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>

**Required: Python 3.10 or higher**

VCS Metrics uses modern Python features and requires Python 3.10+. We recommend Python 3.11+ for optimal performance.

</div>

</td>
<td width="50%" align="center">

### 🔥 **PyTorch**

<div style="background: linear-gradient(145deg, #fed7d7, #fca5a5); padding: 20px; border-radius: 12px; border: 2px solid #dc2626;">

<img src="https://img.shields.io/badge/PyTorch-1.9+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>

**Required: PyTorch 1.9.0+**

PyTorch handles tensor operations. Install it separately to avoid conflicts with your existing setup.

</div>

</td>
</tr>
</table>

<div align="center">
<table style="border: 2px solid #10b981; border-radius: 12px; background: linear-gradient(145deg, #d1fae5, #a7f3d0); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**💡 Note:** VCS automatically installs other dependencies (numpy, matplotlib, seaborn) - you don't need to worry about them!

</td>
</tr>
</table>
</div>

---

### 🔧 Step 2: Understanding VCS Functions

Before you can use VCS, you need to understand the two key functions it requires:


<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🔪 **Segmenter Function**
*Intelligent Text Splitting*

<div style="background: linear-gradient(145deg, #fef3c7, #fde68a); padding: 20px; border-radius: 12px; border: 2px solid #f59e0b;">

**Purpose:** Transform raw text into meaningful segments

**Input:** `str` (raw text)  
**Output:** `List[str]` (text segments)

<details>
<summary><b>📋 View Function Signature</b></summary>

```python
def segmenter_function(text: str) -> List[str]:
    """
    Split text into segments for analysis.
    
    Args:
        text: Input text to segment
        
    Returns:
        List of text segments
    """
    pass
```

</details>

</div>

</td>
<td width="50%" align="center">

### 🧠 **Embedding Function**
*Text to Vector Transformation*

<div style="background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 20px; border-radius: 12px; border: 2px solid #7c3aed;">

**Purpose:** Convert text segments to numerical vectors

**Input:** `List[str]` (text segments)  
**Output:** `torch.Tensor` (embeddings)

<details>
<summary><b>📋 View Function Signature</b></summary>

```python
def embedding_function(texts: List[str]) -> torch.Tensor:
    """
    Convert text segments to embeddings.
    
    Args:
        texts: List of text segments to embed
        
    Returns:
        PyTorch tensor of shape (len(texts), embedding_dim)
    """
    pass
```

</details>

</div>

</td>
</tr>
</table>

---

<div align="center">

## 🌟 **SOTA Recommendations 2025**
*Cutting-edge models for optimal performance*

</div>

<div align="center">
<table style="border: 2px solid #dc2626; border-radius: 12px; background: linear-gradient(145deg, #fecaca, #fca5a5); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

⚠️ **Technology Evolution Alert** ⚠️  
*These recommendations are current as of 2025. As better models emerge, always research the latest SOTA options.*

</td>
</tr>
</table>
</div>

<table align="center" width="100%">
<tr>
<td width="50%" align="center">

### 🔪 **Segmentation Champion**

<div align="center">
<img src="https://img.shields.io/badge/Segment_Any_Text-SAT-ff6b6b?style=for-the-badge&logo=artificial-intelligence&logoColor=white" alt="SAT"/>
</div>

<div style="background: linear-gradient(145deg, #fff5f5, #fed7d7); padding: 20px; border-radius: 12px; border: 2px solid #e53e3e;">

**🏆 Winner: Segment Any Text (SAT)**

✨ **Why SAT dominates:**
- 🎯 State-of-the-art accuracy  
- ⚡ Intelligent boundary detection  
- 🧠 Context-aware segmentation  
- 🔬 Research-grade performance  

<details>
<summary><b>🚀 View SAT Implementation</b></summary>

```python
import re, string, contractions
# from wtpsplit import SaT
# sat_adapted = SaT("sat-12l-sm")

punctuations = set(string.punctuation) - {"'"}

def sat_segmenter(text: str) -> list[str]:
    # Expand contractions & clean text
    text = contractions.fix(text)
    text = remove_punctuation(text)
    text = fix_punctuation_spacing(text)
    
    # SAT magic ✨
    sentences = sat_adapted.split(text)
    return [s.strip() for s in sentences if s.strip()]
```

</details>

</div>

</td>
<td width="50%" align="center">

### 🧠 **Embedding Powerhouse**

<div align="center">
<img src="https://img.shields.io/badge/NVIDIA-NV--Embed--v2-76b900?style=for-the-badge&logo=nvidia&logoColor=white" alt="NV-Embed"/>
</div>

<div style="background: linear-gradient(145deg, #f0fff4, #c6f6d5); padding: 20px; border-radius: 12px; border: 2px solid #38a169;">

**🥇 Champion: nv-embed-v2**

🌟 **Why nv-embed-v2 excels:**
- 📊 [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) leader  
- 🚀 Superior semantic understanding  
- 💪 Robust multilingual support  
- ⚡ Optimized for VCS metrics  

<details>
<summary><b>🔥 View nv-embed-v2 Implementation</b></summary>

```python
import torch, torch.nn.functional as F
# model_nv = SentenceTransformer('nvidia/NV-Embed-v2', 
#                                trust_remote_code=True)

def nv_embed_embedding_fn(texts: list[str], 
                         model=None, batch_size=8):
    # Process in batches for memory efficiency
    all_embs = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        emb_np = model.encode(batch, max_length=32768)
        emb = torch.tensor(emb_np, dtype=torch.float)
        emb = F.normalize(emb, p=2, dim=1)  # Normalize
        all_embs.append(emb)
    
    return torch.cat(all_embs, dim=0)
```

</details>

</div>

</td>
</tr>
</table>

<div align="center">
<table style="border: 2px solid #3182ce; border-radius: 12px; background: linear-gradient(145deg, #bee3f8, #90cdf4); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**🔬 Research Alternatives**  
*Traditional: NLTK, spaCy | Lightweight: sentence-transformers | Custom: Build your own!*

</td>
</tr>
</table>
</div>

---

### 💻 Step 3: Run Your First VCS Analysis

Now let's see VCS in action with a complete working example:

<div align="center">
<table style="border: 2px solid #059669; border-radius: 12px; background: linear-gradient(145deg, #d1fae5, #a7f3d0); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**⚡ Performance Notes**  
*SOTA models require GPU. For CPU testing, this example uses lightweight alternatives.*

</td>
</tr>
</table>
</div>

<details>
<summary><h3>🚀 <b>Interactive Code Example</b> - Click to expand complete tutorial</h3></summary>

<div style="background: linear-gradient(145deg, #1f2937, #111827); padding: 25px; border-radius: 15px; border: 2px solid #6366f1;">

### 🎯 **Complete Working Example**
*Copy, paste, and run this code to see VCS in action*

```python
# Fix import path issue if running from vcs/ root directory
import sys
import os
if os.path.basename(os.getcwd()) == 'vcs' and os.path.exists('src/vcs'):
    sys.path.insert(0, 'src')
    print("🔧 Fixed import path for development directory")

# Test the installation
try:
    import vcs
    print("✅ VCS package imported successfully!")
    
    # Test main function availability
    if hasattr(vcs, 'compute_vcs_score'):
        print("✅ Main function 'compute_vcs_score' is available!")
    else:
        print("⚠️ Main function not found - there might be an installation issue")
        
    # Try to get version
    try:
        print(f"📦 Version: {vcs.__version__}")
    except AttributeError:
        print("📦 Version: Unable to determine (this is normal for development installs)")
        
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("💡 Make sure you:")
    print("   1. Installed VCS correctly: pip install -e .[dev]")
    print("   2. Restarted your notebook kernel") 
    print("   3. You're NOT in the root vcs/ directory (this causes import conflicts)")

# Import required libraries
import torch
from typing import List

# Define lightweight segmenter function
def simple_segmenter(text: str) -> List[str]:
    """
    Simple sentence segmenter using period splitting.
    
    Args:
        text: Input text to segment
        
    Returns:
        List of text segments
    """
    # Split by periods and clean up
    segments = [s.strip() for s in text.split('.') if s.strip()]
    return segments

# Define lightweight embedding function using sentence-transformers
def lightweight_embedding_function(texts: List[str]) -> torch.Tensor:
    """
    Lightweight embedding function using sentence-transformers.
    
    Args:
        texts: List of text segments to embed
        
    Returns:
        PyTorch tensor of shape (len(texts), embedding_dim)
    """
    try:
        from sentence_transformers import SentenceTransformer
        
        # Use a lightweight model (only downloads ~80MB)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Generate embeddings
        embeddings = model.encode(texts)
        return torch.tensor(embeddings, dtype=torch.float32)
        
    except ImportError:
        print("⚠️ sentence-transformers not found. Installing...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sentence-transformers"])
        
        # Try again after installation
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(texts)
        return torch.tensor(embeddings, dtype=torch.float32)

# Example texts
reference_text = """
The quick brown fox jumps over the lazy dog.
It was a beautiful sunny day in the forest.
The fox was looking for food for its family.
"""

generated_text = """
A brown fox jumped over a sleeping dog.
The weather was nice and sunny in the woods.
The fox needed to find food for its cubs.
"""

# Compute VCS score
print("🧠 Computing VCS score...")
try:
    result = vcs.compute_vcs_score(
        reference_text=reference_text,
        generated_text=generated_text,
        segmenter_fn=simple_segmenter,
        embedding_fn_las=lightweight_embedding_function,
        embedding_fn_gas=lightweight_embedding_function,
        return_all_metrics=True,
        return_internals=True
    )
    
    print("🎯 VCS Results:")
    print(f"VCS Score: {result['VCS']:.4f}")
    print(f"GAS Score: {result['GAS']:.4f}")
    print(f"LAS Score: {result['LAS']:.4f}")
    print(f"NAS Score: {result['NAS']:.4f}")
    print("✅ VCS is working correctly!")
    
    # Generate visualization (optional)
    if 'internals' in result:
        try:
            fig = vcs.visualize_metrics_summary(result['internals'])
            print("📊 Visualization generated successfully!")
            # fig.show()  # Uncomment to display
        except Exception as viz_error:
            print(f"⚠️ Visualization failed (this is normal in some environments): {viz_error}")
    
except Exception as e:
    print(f"❌ Error running VCS: {e}")
    print("💡 Make sure PyTorch is installed and try restarting your kernel")
```

<div align="center">
<table style="border: 2px solid #3b82f6; border-radius: 12px; background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**📝 Scale Note:** This example uses small text for illustration - VCS excels with long-form content!  
**⚠️ Import Tip:** Running from `vcs/` root? The example includes an automatic path fix.

</td>
</tr>
</table>
</div>

</div>

</details>

---

### ⚙️ Step 4: Configure VCS Parameters (Optional)

Once you're comfortable with the basics, you can fine-tune VCS behavior for your specific use case:


<table align="center" width="100%">
<tr>
<td width="50%">

### 🎯 **Core Parameters**

<div style="background: linear-gradient(145deg, #ede9fe, #ddd6fe); padding: 20px; border-radius: 12px; border: 2px solid #7c3aed;">

**🎛️ Essential Controls:**

| Parameter | Default | Purpose |
|:----------|:-------:|:--------|
| `chunk_size` | 1 | Segment grouping |
| `context_cutoff_value` | 0.6 | Similarity threshold |
| `context_window_control` | 4.0 | Context window size |
| `lct` | 0 | Narrative reordering tolerance |

</div>

</td>
<td width="50%">

### 🚀 **Example Configuration**

<div style="background: linear-gradient(145deg, #ecfdf5, #d1fae5); padding: 20px; border-radius: 12px; border: 2px solid #059669;">

```python
from vcs import (
    DEFAULT_CONTEXT_CUTOFF_VALUE,    # 0.6
    DEFAULT_CONTEXT_WINDOW_CONTROL,  # 4.0
    DEFAULT_LCT,                     # 0
    DEFAULT_CHUNK_SIZE,              # 1
)

# 🎯 For strict matching
result = compute_vcs_score(
    reference_text=ref_text,
    generated_text=gen_text,
    segmenter_fn=segmenter,
    embedding_fn_las=embedder,
    chunk_size=2,                    # Group segments
    context_cutoff_value=0.7,        # Higher threshold
    context_window_control=3.0,      # Tighter windows
    lct=1,                          # Some reordering OK
)
```

</div>

</td>
</tr>
</table>


---

## 📈 Performance & Benchmarks


## 🛠️ Requirements

<div align="center">

| **Component** | **Version** | **Purpose** |
|:---|:---:|:---|
| **Python** | 3.8+ | Core runtime |
| **PyTorch** | ≥1.9.0 | Tensor operations |
| **NumPy** | ≥1.20.0 | Numerical computing |
| **Matplotlib** | ≥3.5.0 | Plotting and visualization |
| **Seaborn** | ≥0.11.0 | Statistical visualizations |

</div>

> **📝 Note**: PyTorch is not included as a direct dependency to avoid conflicts. Install it separately from the [official PyTorch website](https://pytorch.org/get-started/locally/).

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>🤔 How does VCS differ from BLEU/ROUGE?</strong></summary>
<p>Unlike BLEU/ROUGE which focus on n-gram overlap, VCS evaluates semantic similarity and narrative structure preservation, making it ideal for long-form text evaluation where meaning and flow matter more than exact word matches.</p>
</details>

<details>
<summary><strong>⚡ What's the minimum text length for VCS?</strong></summary>
<p>VCS works with any text length, but it's optimized for longer texts (100+ words) where narrative structure is important. For very short texts, simpler metrics might be more appropriate.</p>
</details>

<details>
<summary><strong>🧠 Which embedding models work best?</strong></summary>
<p>We recommend checking the <a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB leaderboard</a> for the latest SOTA models. As of 2024, nv-embed-v2 and similar transformer-based models provide excellent results.</p>
</details>

<details>
<summary><strong>🚀 Can I use VCS in production?</strong></summary>
<p>Yes! VCS is production-ready with comprehensive error handling, memory optimization, and batch processing capabilities. See our performance benchmarks above.</p>
</details>

<details>
<summary><strong>🔧 How do I customize VCS parameters?</strong></summary>
<p>VCS provides several tunable parameters like <code>context_cutoff_value</code>, <code>chunk_size</code>, and <code>lct</code>. Check our documentation for detailed parameter explanations and tuning guides.</p>
</details>

---

## 🏗️ Project Structure

```
vcs-metrics/
├── 📁 src/vcs/                 # Main package code
│   ├── 📄 __init__.py
│   ├── 📁 _metrics/           # Core metrics implementations
│   ├── 📁 _visualize_vcs/     # Visualization components
│   └── 📄 scorer.py           # Main API
├── 📁 docs/                   # Documentation and website
│   ├── 📄 index.html          # Main website
│   ├── 📄 playground.html     # Interactive playground
│   └── 📄 api.html            # API documentation
├── 📁 .github/workflows/      # CI/CD pipelines
├── 📄 pyproject.toml         # Package configuration
└── 📄 README.md              # This file
```

---

## 🚀 Development & Contributing

### 🔧 Development Setup

```bash
# Clone the repository
git clone https://github.com/hdubey-debug/vcs.git
cd vcs

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## 📚 Citation

If you use VCS Metrics in your research, please cite:

```bibtex
@software{vcs_metrics_2024,
  title = {VCS Metrics: Video Comprehension Score for Text Similarity Evaluation},
  author = {Harsh Dubey, Mukhtiar Ali, Sugam Mishra, and Chulwoo Pack},
  year = {2024},
  institution = {South Dakota State University},
  url = {https://github.com/hdubey-debug/vcs},
  note = {Python package for narrative similarity evaluation}
}
```

---

## 🏆 Meet Our Contributors

<div align="center">

### 🌟 **The VCS Team - Building the Future of Text Similarity**

</div>

<table>
<tr>
<td align="center">

<a href="https://github.com/hdubey-debug">
  <img src="https://github.com/hdubey-debug.png" width="100" height="100" style="border-radius: 50%;"/>
</a>

**Harsh Dubey**  
*Lead Developer & Research Scientist*  
*South Dakota State University*

| Commits | Lines | Files |
|:---:|:---:|:---:|
| **126** | **30K** | **95** |

**📋 Key Work:**
• VCS Algorithm Architecture  
• Visualization Engine  
• LAS, GAS, and NAS Metrics  

[![GitHub](https://img.shields.io/badge/-GitHub-14b8a6?style=flat&logo=github)](https://github.com/hdubey-debug)

</td>
</tr>
</table>

<div align="center">

### 🤖 **Automated Contributors**

| **Contributor** | **Role** | **Contributions** | **Badge** |
|:---:|:---:|:---:|:---:|
| 🤖 **GitHub Actions** | CI/CD Automation | 3 commits | [![Bot](https://img.shields.io/badge/Bot-Automated_Testing-6c5ce7?style=flat&logo=github-actions&logoColor=white)](#) |

### 📊 **Contribution Analytics**

[![Contributors](https://img.shields.io/github/contributors/hdubey-debug/vcs?style=for-the-badge&color=14b8a6&labelColor=0f172a)](https://github.com/hdubey-debug/vcs/graphs/contributors)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/hdubey-debug/vcs?style=for-the-badge&color=ff6b6b&labelColor=0f172a)](https://github.com/hdubey-debug/vcs/pulse)
[![Last Commit](https://img.shields.io/github/last-commit/hdubey-debug/vcs?style=for-the-badge&color=4ecdc4&labelColor=0f172a)](https://github.com/hdubey-debug/vcs/commits)
[![Code Frequency](https://img.shields.io/github/languages/count/hdubey-debug/vcs?style=for-the-badge&color=f9ca24&labelColor=0f172a)](https://github.com/hdubey-debug/vcs)

### 🎯 **Want to Contribute?**

We're always looking for passionate developers and researchers to join our mission!

[![Contribute](https://img.shields.io/badge/👨‍💻_Join_the_Team-Contribute_Now-14b8a6?style=for-the-badge&logo=github)](https://github.com/hdubey-debug/vcs/blob/main/CONTRIBUTING.md)
[![Issues](https://img.shields.io/badge/🐛_Find_Bugs-Good_First_Issues-ff6b6b?style=for-the-badge&logo=github)](https://github.com/hdubey-debug/vcs/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
[![Features](https://img.shields.io/badge/💡_Suggest_Ideas-Feature_Requests-4ecdc4?style=for-the-badge&logo=lightbulb)](https://github.com/hdubey-debug/vcs/issues/new?assignees=&labels=enhancement&template=feature_request.md)

**Areas where we need help:**
- 🧪 Testing on diverse datasets
- 🌐 Multi-language support 
- ⚡ Performance optimizations
- 📚 Documentation improvements
- 🎨 UI/UX enhancements

</div>

---

## 🌍 Community & Stats

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/hdubey-debug/vcs?style=social)](https://github.com/hdubey-debug/vcs/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/hdubey-debug/vcs?style=social)](https://github.com/hdubey-debug/vcs/network/members)
[![GitHub issues](https://img.shields.io/github/issues/hdubey-debug/vcs?color=red)](https://github.com/hdubey-debug/vcs/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/hdubey-debug/vcs?color=blue)](https://github.com/hdubey-debug/vcs/pulls)

![Downloads](https://img.shields.io/pypi/dm/vcs-metrics?color=teal&label=PyPI%20Downloads)
![Contributors](https://img.shields.io/github/contributors/hdubey-debug/vcs?color=orange)
![Last Commit](https://img.shields.io/github/last-commit/hdubey-debug/vcs?color=green)

### 💫 Join Our Growing Community!

| Platform | Purpose | Link |
|:---:|:---|:---|
| 🐙 **GitHub** | Source code, issues, PRs | [hdubey-debug/vcs](https://github.com/hdubey-debug/vcs) |
| 💬 **Discussions** | Q&A, ideas, showcase | [GitHub Discussions](https://github.com/hdubey-debug/vcs/discussions) |
| 📦 **PyPI** | Package releases | [vcs-metrics](https://pypi.org/project/vcs-metrics/) |
| 📖 **Docs** | Complete documentation | [hdubey-debug.github.io/vcs](https://hdubey-debug.github.io/vcs/) |

</div>

---

## 🤝 Contributing

Contributions are welcome! Please see the [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**MIT License** - see the [LICENSE](LICENSE) file for details

---

### 🌟 **Made with ❤️ by the VCS Team**

**Authors**: Harsh Dubey, Mukhtiar Ali, Sugam Mishra, and Chulwoo Pack  
**Institution**: South Dakota State University  
**Year**: 2024

[⭐ Star this repo](https://github.com/hdubey-debug/vcs) • [🐛 Report Bug](https://github.com/hdubey-debug/vcs/issues) • [💡 Request Feature](https://github.com/hdubey-debug/vcs/issues) • [💬 Join Discussion](https://github.com/hdubey-debug/vcs/discussions)

</div>
