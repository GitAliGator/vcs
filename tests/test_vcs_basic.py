"""
Basic tests for VCS metrics library.
"""

import pytest
import torch
import numpy as np
from vcs import compute_vcs_score, __version__


def simple_segmenter(text):
    """Simple segmenter for testing."""
    return [s.strip() for s in text.split('.') if s.strip()]


def dummy_embedding_function(texts):
    """Dummy embedding function for testing."""
    # Return random embeddings with consistent shape
    np.random.seed(42)  # For reproducible tests
    embeddings = np.random.randn(len(texts), 384)
    return torch.tensor(embeddings, dtype=torch.float32)


class TestVCSBasic:
    """Basic tests for VCS functionality."""
    
    def test_version(self):
        """Test that version is defined."""
        assert __version__ is not None
        assert isinstance(__version__, str)
    
    def test_basic_vcs_computation(self):
        """Test basic VCS score computation."""
        reference_text = "The cat sat on the mat. It was a sunny day."
        generated_text = "A cat was sitting on a mat. The weather was nice."
        
        result = compute_vcs_score(
            reference_text=reference_text,
            generated_text=generated_text,
            segmenter_fn=simple_segmenter,
            embedding_fn_las=dummy_embedding_function
        )
        
        # Check that VCS score is returned
        assert 'VCS' in result
        assert isinstance(result['VCS'], (int, float))
        assert 0 <= result['VCS'] <= 1
    
    def test_all_metrics_returned(self):
        """Test that all metrics are returned when requested."""
        reference_text = "The cat sat on the mat."
        generated_text = "A cat sits on a mat."
        
        result = compute_vcs_score(
            reference_text=reference_text,
            generated_text=generated_text,
            segmenter_fn=simple_segmenter,
            embedding_fn_las=dummy_embedding_function,
            return_all_metrics=True
        )
        
        # Check for expected metrics
        expected_metrics = ['VCS', 'GAS', 'LAS', 'NAS']
        for metric in expected_metrics:
            assert metric in result
            assert isinstance(result[metric], (int, float))
            assert 0 <= result[metric] <= 1
    
    def test_internals_returned(self):
        """Test that internals are returned when requested."""
        reference_text = "Hello world."
        generated_text = "Hello there."
        
        result = compute_vcs_score(
            reference_text=reference_text,
            generated_text=generated_text,
            segmenter_fn=simple_segmenter,
            embedding_fn_las=dummy_embedding_function,
            return_internals=True
        )
        
        # Check that internals are present
        assert 'internals' in result
        internals = result['internals']
        
        # Check for expected internal structure
        assert 'texts' in internals
        assert 'similarity' in internals
        assert 'mapping_windows' in internals
        assert 'alignment' in internals
        assert 'metrics' in internals
        assert 'config' in internals
    
    def test_empty_text_handling(self):
        """Test handling of empty texts."""
        with pytest.raises((ValueError, IndexError, RuntimeError)):
            compute_vcs_score(
                reference_text="",
                generated_text="Some text here.",
                segmenter_fn=simple_segmenter,
                embedding_fn_las=dummy_embedding_function
            )
    
    def test_custom_parameters(self):
        """Test VCS computation with custom parameters."""
        reference_text = "First sentence. Second sentence. Third sentence."
        generated_text = "One sentence. Two sentences. Three sentences."
        
        result = compute_vcs_score(
            reference_text=reference_text,
            generated_text=generated_text,
            segmenter_fn=simple_segmenter,
            embedding_fn_las=dummy_embedding_function,
            chunk_size=2,
            context_cutoff_value=0.5,
            context_window_control=3.0,
            lct=1,
            return_all_metrics=True
        )
        
        # Should still return valid VCS score
        assert 'VCS' in result
        assert 0 <= result['VCS'] <= 1
    
    def test_identical_texts(self):
        """Test VCS score for identical texts."""
        text = "The quick brown fox jumps over the lazy dog."
        
        result = compute_vcs_score(
            reference_text=text,
            generated_text=text,
            segmenter_fn=simple_segmenter,
            embedding_fn_las=dummy_embedding_function,
            return_all_metrics=True
        )
        
        # With identical texts, scores should be high (though not necessarily 1.0 due to randomness in dummy embeddings)
        assert result['VCS'] >= 0.5  # Should be reasonably high for identical texts


class TestInputValidation:
    """Test input validation."""
    
    def test_missing_embedding_function(self):
        """Test that missing embedding function raises error."""
        with pytest.raises(ValueError):
            compute_vcs_score(
                reference_text="Test text.",
                generated_text="Another text.",
                segmenter_fn=simple_segmenter,
                embedding_fn_las=None
            )
    
    def test_invalid_segmenter(self):
        """Test that invalid segmenter raises error."""
        with pytest.raises((TypeError, ValueError)):
            compute_vcs_score(
                reference_text="Test text.",
                generated_text="Another text.",
                segmenter_fn=None,
                embedding_fn_las=dummy_embedding_function
            )


if __name__ == "__main__":
    pytest.main([__file__])