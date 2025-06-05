VCS Metrics Documentation
=========================

.. raw:: html

   <div style="background: linear-gradient(135deg, #0d9488, #0f766e); color: white; padding: 2rem; text-align: center; border-radius: 0.75rem; margin-bottom: 2rem; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
       <h1 style="color: white; border: none; margin: 0; font-size: 2.5rem; font-weight: 700;">VCS Metrics</h1>
       <p style="color: #ccfbf1; font-size: 1.2rem; margin: 0.5rem 0 0 0;">Video Comprehension Score - A comprehensive metric for evaluating narrative similarity</p>
   </div>

VCS Metrics is a Python library that provides a comprehensive approach to measuring narrative similarity between reference and generated text. It combines multiple alignment scores to evaluate how well generated content preserves the semantic meaning, local structure, and narrative flow of the original text.

.. image:: https://img.shields.io/pypi/v/vcs-metrics.svg
   :target: https://pypi.org/project/vcs-metrics/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.8+

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

Key Features
------------

🎯 **Comprehensive Scoring**: Combines Global Alignment Score (GAS), Local Alignment Score (LAS), and Narrative Alignment Score (NAS)

📊 **Rich Visualizations**: Generate detailed plots, heatmaps, and PDF reports for analysis

🔧 **Flexible Configuration**: Customizable parameters for different use cases and text types

📈 **Detailed Analytics**: Access to internal calculations for deep analysis and debugging

🎨 **Publication Ready**: Professional visualizations and reports suitable for research and presentations

Quick Example
-------------

.. code-block:: python

   import torch
   from vcs import compute_vcs_score

   # Simple example with basic functions
   def simple_segmenter(text):
       return text.split('.')

   def simple_embedder(texts):
       # Replace with actual embeddings (e.g., sentence transformers)
       return torch.randn(len(texts), 384)

   # Compute VCS score
   result = compute_vcs_score(
       reference_text="The cat sat on the mat. It was sunny.",
       generated_text="A cat was on a mat in the sunshine.",
       segmenter_fn=simple_segmenter,
       embedding_fn_las=simple_embedder
   )

   print(f"VCS Score: {result['VCS']:.4f}")

Core Metrics
------------

**VCS (Video Comprehension Score)**: The overall similarity metric combining all components

**GAS (Global Alignment Score)**: Measures semantic similarity at the full-text level using document embeddings

**LAS (Local Alignment Score)**: Evaluates segment-by-segment semantic similarity with optimal alignment

**NAS (Narrative Alignment Score)**: Assesses narrative flow preservation through distance-based and line-based analysis

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   usage
   api

.. toctree::
   :maxdepth: 1
   :caption: Additional Resources:

   GitHub Repository <https://github.com/yourusername/vcs-metrics>
   PyPI Package <https://pypi.org/project/vcs-metrics/>

Citation
--------

If you use VCS Metrics in your research, please cite:

.. code-block:: bibtex

   @software{vcs_metrics,
     title = {VCS Metrics: Video Comprehension Score for Text Similarity},
     author = {Harsh Dubey and Chulwoo Pack},
     year = {2024},
     url = {https://github.com/yourusername/vcs-metrics}
   }

Support
-------

- **Documentation**: You're reading it! 📖
- **Issues**: `GitHub Issues <https://github.com/yourusername/vcs-metrics/issues>`_
- **Discussions**: `GitHub Discussions <https://github.com/yourusername/vcs-metrics/discussions>`_

License
-------

This project is licensed under the MIT License - see the `LICENSE <https://github.com/yourusername/vcs-metrics/blob/main/LICENSE>`_ file for details.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`