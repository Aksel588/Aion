#!/usr/bin/env python3
"""
LinkAI-Aion Embedding Utilities Module
======================================

Advanced embedding generation and vector operations for AI projects.
"""

import os
import hashlib
from typing import List, Dict, Any, Optional, Union, Tuple
import numpy as np

# Optional imports for advanced features
try:
    from sentence_transformers import SentenceTransformer
    _HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    _HAS_SENTENCE_TRANSFORMERS = False


def embed_file(filepath: str, model_name: str = "all-MiniLM-L6-v2") -> Optional[np.ndarray]:
    """
    Generate embeddings for a file's contents.
    
    Args:
        filepath: Path to the file to embed
        model_name: Name of the embedding model to use
        
    Returns:
        Embedding vector for the file contents, or None if file cannot be read
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if _HAS_SENTENCE_TRANSFORMERS:
            model = SentenceTransformer(model_name)
            embedding = model.encode(content)
            print(f"🔗 Successfully embedded file: {filepath}")
            return embedding
        else:
            print(f"🔗 Embedding file: {filepath} (sentence-transformers not available)")
            # Return a simple hash-based embedding as fallback
            hash_val = int(hashlib.md5(content.encode()).hexdigest(), 16)
            return np.array([hash_val % 1000] * 384, dtype=float)  # 384-dim vector
        
    except Exception as e:
        print(f"🔗 Error embedding file {filepath}: {e}")
        return None


def embed_text(text: str, model_name: str = "all-MiniLM-L6-v2") -> np.ndarray:
    """
    Generate embeddings for text.
    
    Args:
        text: Text to embed
        model_name: Name of the embedding model to use
        
    Returns:
        Embedding vector
    """
    if _HAS_SENTENCE_TRANSFORMERS:
        model = SentenceTransformer(model_name)
        return model.encode(text)
    else:
        # Fallback to simple hash-based embedding
        hash_val = int(hashlib.md5(text.encode()).hexdigest(), 16)
        return np.array([hash_val % 1000] * 384, dtype=float)


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vec1: First vector
        vec2: Second vector
        
    Returns:
        Cosine similarity score (-1 to 1)
    """
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return dot_product / (norm1 * norm2)