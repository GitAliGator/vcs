Getting Started
===============

This guide will help you install VCS Metrics and understand the basic requirements for using the library.

Installation
------------

Basic Installation
~~~~~~~~~~~~~~~~~~

Install VCS Metrics from PyPI:

.. code-block:: bash

   pip install vcs-metrics

Development Installation
~~~~~~~~~~~~~~~~~~~~~~~~

For development or to get the latest features:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/yourusername/vcs-metrics.git
   cd vcs-metrics

   # Install in development mode
   pip install -e ".[dev]"

   # Install pre-commit hooks
   pre-commit install

PyTorch Installation
~~~~~~~~~~~~~~~~~~~

VCS Metrics requires PyTorch but doesn't install it automatically to avoid conflicts. Install PyTorch separately:

.. code-block:: bash

   # For CPU-only (most common)
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

   # For CUDA (if you have compatible GPU)
   pip install torch torchvision torchaudio

.. note::
   In Google Colab, PyTorch is pre-installed, so no additional installation is needed.

Requirements
------------

- Python 3.8+
- numpy >= 1.20.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0
- PyTorch >= 1.9.0 (install separately)

Core Function Requirements
--------------------------

VCS Metrics requires two types of functions that you need to provide:

1. **Segmenter Function**: Splits text into meaningful units
2. **Embedding Function**: Converts text segments into numerical vectors

Segmenter Function
~~~~~~~~~~~~~~~~~

The segmenter function takes a string and returns a list of strings (segments).

**Function Signature:**

.. code-block:: python

   def segmenter_function(text: str) -> List[str]:
       """
       Split text into segments for analysis.
       
       Args:
           text: Input text to segment
           
       Returns:
           List of text segments
       """
       pass

**Examples:**

.. code-block:: python

   # Simple sentence splitting
   def simple_segmenter(text):
       return [s.strip() for s in text.split('.') if s.strip()]

   # Using NLTK for sentence tokenization
   import nltk
   nltk.download('punkt')
   
   def nltk_segmenter(text):
       return nltk.sent_tokenize(text)

   # Using spaCy for sentence segmentation
   import spacy
   nlp = spacy.load("en_core_web_sm")
   
   def spacy_segmenter(text):
       doc = nlp(text)
       return [sent.text.strip() for sent in doc.sents]

   # Custom segmentation for dialog
   def dialog_segmenter(text):
       lines = text.split('\n')
       return [line.strip() for line in lines if line.strip()]

   # Paragraph-based segmentation
   def paragraph_segmenter(text):
       paragraphs = text.split('\n\n')
       return [p.strip() for p in paragraphs if p.strip()]

Embedding Function
~~~~~~~~~~~~~~~~~

The embedding function takes a list of strings and returns a PyTorch tensor with embeddings.

**Function Signature:**

.. code-block:: python

   def embedding_function(texts: List[str]) -> torch.Tensor:
       """
       Convert text segments to embeddings.
       
       Args:
           texts: List of text segments to embed
           
       Returns:
           PyTorch tensor of shape (len(texts), embedding_dim)
       """
       pass

**Examples:**

.. code-block:: python

   import torch
   from sentence_transformers import SentenceTransformer

   # Using Sentence Transformers (recommended)
   model = SentenceTransformer('all-MiniLM-L6-v2')
   
   def sbert_embeddings(texts):
       embeddings = model.encode(texts)
       return torch.tensor(embeddings)

   # Using different models for different purposes
   def fast_embeddings(texts):
       model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast, good quality
       return torch.tensor(model.encode(texts))
   
   def high_quality_embeddings(texts):
       model = SentenceTransformer('all-mpnet-base-v2')  # Slower, higher quality
       return torch.tensor(model.encode(texts))

   # Using Hugging Face transformers
   from transformers import AutoTokenizer, AutoModel
   import torch.nn.functional as F
   
   tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
   model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
   
   def huggingface_embeddings(texts):
       encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
       with torch.no_grad():
           model_output = model(**encoded_input)
           # Mean pooling
           embeddings = F.normalize(model_output.last_hidden_state.mean(dim=1), p=2, dim=1)
       return embeddings

   # Simple random embeddings (for testing only)
   def random_embeddings(texts):
       return torch.randn(len(texts), 384)

Quick Start Example
------------------

Here's a complete working example:

.. code-block:: python

   import torch
   from sentence_transformers import SentenceTransformer
   import nltk
   from vcs import compute_vcs_score

   # Download NLTK data (run once)
   nltk.download('punkt')

   # Set up the model
   model = SentenceTransformer('all-MiniLM-L6-v2')

   # Define functions
   def segment_sentences(text):
       return nltk.sent_tokenize(text)

   def get_embeddings(texts):
       embeddings = model.encode(texts)
       return torch.tensor(embeddings)

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
   result = compute_vcs_score(
       reference_text=reference_text,
       generated_text=generated_text,
       segmenter_fn=segment_sentences,
       embedding_fn_las=get_embeddings,
       return_all_metrics=True
   )

   # Print results
   print(f"VCS Score: {result['VCS']:.4f}")
   print(f"GAS Score: {result['GAS']:.4f}")
   print(f"LAS Score: {result['LAS']:.4f}")
   print(f"NAS Score: {result['NAS']:.4f}")

Configuration Parameters
------------------------

VCS Metrics provides several configuration parameters:

.. code-block:: python

   from vcs import (
       DEFAULT_CONTEXT_CUTOFF_VALUE,    # 0.6
       DEFAULT_CONTEXT_WINDOW_CONTROL,  # 4.0
       DEFAULT_LCT,                     # 0
       DEFAULT_CHUNK_SIZE,              # 1
   )

   result = compute_vcs_score(
       reference_text=ref_text,
       generated_text=gen_text,
       segmenter_fn=segmenter,
       embedding_fn_las=embedder,
       chunk_size=2,                    # Group segments in pairs
       context_cutoff_value=0.7,        # More restrictive matching
       context_window_control=3.0,      # Larger context windows
       lct=1,                          # Allow some narrative reordering
   )

Next Steps
----------

- Read the :doc:`usage` guide for detailed examples
- Explore the :doc:`api` reference for all available functions
- Check out the visualization capabilities for analysis and reporting

Troubleshooting
---------------

**ImportError: No module named 'torch'**
   Install PyTorch separately: ``pip install torch``

**NLTK data not found**
   Download required data: ``import nltk; nltk.download('punkt')``

**Memory issues with large texts**
   Try increasing ``chunk_size`` or segmenting texts into smaller pieces

**Poor VCS scores**
   Experiment with different segmentation strategies and embedding models