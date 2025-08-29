#!/usr/bin/env python3
"""
LinkAI-Aion Evaluation Metrics Module
====================================

Advanced evaluation metrics and model assessment utilities for AI/ML projects.
"""

import json
import csv
from typing import List, Dict, Any, Union, Tuple, Optional
import numpy as np


def evaluate_predictions(preds_file: str, answers_file: str) -> Dict[str, float]:
    """
    Evaluate predictions against ground truth answers.
    
    Args:
        preds_file: Path to predictions file (JSON or CSV)
        answers_file: Path to answers file (JSON or CSV)
        
    Returns:
        Dictionary of evaluation metrics
    """
    print(f"📊 Evaluating predictions in: {preds_file}")
    print(f"✅ Against answers in: {answers_file}")
    
    try:
        # Load predictions and answers
        predictions = _load_data(preds_file)
        answers = _load_data(answers_file)
        
        # Calculate metrics based on data type
        if isinstance(predictions[0], (int, float)) and isinstance(answers[0], (int, float)):
            # Regression metrics
            return calculate_regression_metrics(predictions, answers)
        else:
            # Classification metrics
            return calculate_classification_metrics(predictions, answers)
            
    except Exception as e:
        print(f"❌ Error evaluating predictions: {e}")
        return {}


def _load_data(filepath: str) -> List[Any]:
    """Load data from JSON or CSV file."""
    if filepath.endswith('.json'):
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data if isinstance(data, list) else [data]
    elif filepath.endswith('.csv'):
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]  # Assume single column
    else:
        # Try to read as text file with one value per line
        with open(filepath, 'r') as f:
            return [line.strip() for line in f.readlines()]


def calculate_classification_metrics(y_pred: List[Any], y_true: List[Any]) -> Dict[str, float]:
    """
    Calculate classification metrics.
    
    Args:
        y_pred: Predicted labels
        y_true: True labels
        
    Returns:
        Dictionary with accuracy, precision, recall, f1_score
    """
    if len(y_pred) != len(y_true):
        raise ValueError("Predictions and answers must have the same length")
    
    # Convert to numpy arrays for easier computation
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    
    # Basic accuracy
    accuracy = np.mean(y_pred == y_true)
    
    # For binary classification, calculate precision, recall, F1
    unique_labels = np.unique(np.concatenate([y_pred, y_true]))
    
    if len(unique_labels) == 2:
        # Binary classification
        tp = np.sum((y_pred == unique_labels[1]) & (y_true == unique_labels[1]))
        fp = np.sum((y_pred == unique_labels[1]) & (y_true == unique_labels[0]))
        fn = np.sum((y_pred == unique_labels[0]) & (y_true == unique_labels[1]))
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        return {
            'accuracy': float(accuracy),
            'precision': float(precision),
            'recall': float(recall),
            'f1_score': float(f1_score)
        }
    else:
        # Multi-class classification
        return {
            'accuracy': float(accuracy),
            'num_classes': len(unique_labels)
        }


def calculate_regression_metrics(y_pred: List[float], y_true: List[float]) -> Dict[str, float]:
    """
    Calculate regression metrics.
    
    Args:
        y_pred: Predicted values
        y_true: True values
        
    Returns:
        Dictionary with MSE, RMSE, MAE, R²
    """
    if len(y_pred) != len(y_true):
        raise ValueError("Predictions and answers must have the same length")
    
    y_pred = np.array(y_pred, dtype=float)
    y_true = np.array(y_true, dtype=float)
    
    # Mean Squared Error
    mse = np.mean((y_pred - y_true) ** 2)
    
    # Root Mean Squared Error
    rmse = np.sqrt(mse)
    
    # Mean Absolute Error
    mae = np.mean(np.abs(y_pred - y_true))
    
    # R-squared
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0.0
    
    return {
        'mse': float(mse),
        'rmse': float(rmse),
        'mae': float(mae),
        'r2': float(r2)
    }


def confusion_matrix(y_pred: List[Any], y_true: List[Any]) -> np.ndarray:
    """
    Calculate confusion matrix.
    
    Args:
        y_pred: Predicted labels
        y_true: True labels
        
    Returns:
        Confusion matrix as numpy array
    """
    unique_labels = sorted(list(set(y_pred + y_true)))
    n_labels = len(unique_labels)
    
    # Create label to index mapping
    label_to_idx = {label: i for i, label in enumerate(unique_labels)}
    
    # Initialize confusion matrix
    cm = np.zeros((n_labels, n_labels), dtype=int)
    
    # Fill confusion matrix
    for pred, true in zip(y_pred, y_true):
        cm[label_to_idx[true], label_to_idx[pred]] += 1
    
    return cm


def calculate_auc_roc(y_scores: List[float], y_true: List[int]) -> float:
    """
    Calculate AUC-ROC for binary classification.
    
    Args:
        y_scores: Prediction scores/probabilities
        y_true: True binary labels (0 or 1)
        
    Returns:
        AUC-ROC score
    """
    # Simple implementation of AUC calculation
    # Sort by scores
    sorted_indices = np.argsort(y_scores)[::-1]  # Descending order
    y_scores_sorted = np.array(y_scores)[sorted_indices]
    y_true_sorted = np.array(y_true)[sorted_indices]
    
    # Calculate TPR and FPR at different thresholds
    n_pos = np.sum(y_true)
    n_neg = len(y_true) - n_pos
    
    if n_pos == 0 or n_neg == 0:
        return 0.5  # Random performance when all samples are one class
    
    tpr_values = []
    fpr_values = []
    
    tp = 0
    fp = 0
    
    for i in range(len(y_true_sorted)):
        if y_true_sorted[i] == 1:
            tp += 1
        else:
            fp += 1
        
        tpr = tp / n_pos
        fpr = fp / n_neg
        
        tpr_values.append(tpr)
        fpr_values.append(fpr)
    
    # Calculate AUC using trapezoidal rule
    auc = 0.0
    for i in range(1, len(fpr_values)):
        auc += (fpr_values[i] - fpr_values[i-1]) * (tpr_values[i] + tpr_values[i-1]) / 2
    
    return auc


def evaluate_text_similarity(pred_texts: List[str], true_texts: List[str]) -> Dict[str, float]:
    """
    Evaluate text similarity using various metrics.
    
    Args:
        pred_texts: Predicted text strings
        true_texts: True text strings
        
    Returns:
        Dictionary with similarity metrics
    """
    if len(pred_texts) != len(true_texts):
        raise ValueError("Predictions and ground truth must have the same length")
    
    exact_matches = sum(1 for p, t in zip(pred_texts, true_texts) if p.strip() == t.strip())
    exact_match_ratio = exact_matches / len(pred_texts)
    
    # Simple word overlap metric
    word_overlaps = []
    for pred, true in zip(pred_texts, true_texts):
        pred_words = set(pred.lower().split())
        true_words = set(true.lower().split())
        
        if len(true_words) == 0:
            overlap = 1.0 if len(pred_words) == 0 else 0.0
        else:
            overlap = len(pred_words.intersection(true_words)) / len(true_words)
        word_overlaps.append(overlap)
    
    avg_word_overlap = np.mean(word_overlaps)
    
    return {
        'exact_match_ratio': float(exact_match_ratio),
        'avg_word_overlap': float(avg_word_overlap)
    }