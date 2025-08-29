#!/usr/bin/env python3
"""
Aqwel-Aion v0.1.7 - Comprehensive Example Showcase
==================================================

This example demonstrates the full power of the Aqwel-Aion AI research library
with real-world use cases for AI researchers and developers.

Author: Aksel Aghajanyan
Email: aqwelaiofficial@gmail.com
"""

import aion

def print_section(title):
    """Helper function to print formatted section headers."""
    print(f"\n{'='*60}")
    print(f"🚀 {title}")
    print('='*60)

def print_subsection(title):
    """Helper function to print formatted subsection headers."""
    print(f"\n🔹 {title}")
    print('-'*40)

# ============================================================================
# �� MATHEMATICS & STATISTICS SHOWCASE
# ============================================================================

print_section("ADVANCED MATHEMATICS & STATISTICS")

print_subsection("Basic Mathematical Operations")
# Flexible input handling - numbers, lists, strings
result1 = aion.maths.addition([1, 2, 3], [4, 5, 6])
result2 = aion.maths.multiplication("2,3,4", 5)  # String input
result3 = aion.maths.division([10, 20, 30], 2)

print(f"Vector addition [1,2,3] + [4,5,6] = {result1}")
print(f"String multiplication '2,3,4' * 5 = {result2}")
print(f"Vector division [10,20,30] / 2 = {result3}")

print_subsection("Advanced Mathematical Functions")
# Trigonometry and logarithms
angles = [0, 3.14159/4, 3.14159/2]
sin_values = [aion.maths.sin(angle) for angle in angles]
matrix_det = aion.maths.determinant([[1, 2], [3, 4]])

print(f"sin(0°, 45°, 90°) = {[round(x, 3) for x in sin_values]}")
print(f"Determinant of [[1,2],[3,4]] = {matrix_det}")

print_subsection("Statistical Analysis")
# Real research data simulation
research_data = [23.1, 25.4, 22.8, 26.7, 24.3, 23.9, 25.1, 24.8, 23.5, 25.9]
control_data = [20.3, 21.1, 19.8, 21.4, 20.7, 20.9, 21.2, 20.5, 21.0, 20.8]

mean_research = aion.maths.mean(research_data)
mean_control = aion.maths.mean(control_data)
std_research = aion.maths.std_dev(research_data, ddof=1)
correlation_coeff = aion.maths.correlation(research_data, control_data)

print(f"Research group mean: {mean_research:.2f} ± {std_research:.2f}")
print(f"Control group mean: {mean_control:.2f}")
print(f"Correlation coefficient: {correlation_coeff:.3f}")

# ============================================================================
# 🤖 MACHINE LEARNING & AI SHOWCASE
# ============================================================================

print_section("MACHINE LEARNING & AI TOOLS")

print_subsection("Neural Network Activation Functions")
# Test data for neural network
test_inputs = [-2, -1, 0, 1, 2]
sigmoid_outputs = aion.maths.sigmoid(test_inputs)
relu_outputs = aion.maths.relu(test_inputs)

print(f"Inputs: {test_inputs}")
print(f"Sigmoid: {[round(x, 3) for x in sigmoid_outputs]}")
print(f"ReLU: {relu_outputs}")

# Softmax for classification
logits = [2.0, 1.0, 0.1]
probabilities = aion.maths.softmax(logits)
print(f"Softmax({logits}) = {[round(x, 3) for x in probabilities]}")

print_subsection("Model Evaluation Metrics")
# Simulated model predictions
y_true_class = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat', 'bird', 'dog']
y_pred_class = ['cat', 'dog', 'bird', 'bird', 'dog', 'cat', 'bird', 'cat']

y_true_reg = [2.5, 3.1, 4.2, 1.8, 3.7]
y_pred_reg = [2.3, 3.0, 4.5, 1.9, 3.5]

# Classification metrics
class_metrics = aion.evaluate.calculate_classification_metrics(y_pred_class, y_true_class)
print(f"Classification Accuracy: {class_metrics['accuracy']:.3f}")

# Regression metrics  
reg_metrics = aion.evaluate.calculate_regression_metrics(y_pred_reg, y_true_reg)
print(f"Regression MSE: {reg_metrics['mse']:.3f}")
print(f"Regression R²: {reg_metrics['r2']:.3f}")

print_subsection("Distance Metrics & Similarity")
# Vector similarity for embeddings
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [1.1, 2.1, 2.9, 4.1]

euclidean_dist = aion.maths.euclidean_distance(vector1, vector2)
cosine_sim = aion.maths.cosine_similarity(vector1, vector2)

print(f"Euclidean distance (similar vectors): {euclidean_dist:.3f}")
print(f"Cosine similarity (similar vectors): {cosine_sim:.3f}")

# ============================================================================
# 🔗 TEXT EMBEDDINGS & NLP SHOWCASE
# ============================================================================

print_section("TEXT EMBEDDINGS & NLP")

print_subsection("Text Embedding Generation")
try:
    # Generate embeddings
    embedding1 = aion.embed.embed_text("Machine learning algorithms for optimization")
    print(f"Embedding dimensions: {embedding1.shape}")
    print("✅ Text embedding generated successfully")
    
except Exception as e:
    print(f"⚠️  Embeddings: {e}")
    print("💡 Install with: pip install aqwel-aion[ai]")

print_subsection("Text Processing & Analysis")
research_text = """
Artificial intelligence and machine learning have revolutionized data science.
Neural networks show remarkable performance in various tasks.
"""

word_count = aion.text.count_words(research_text)
char_count = aion.text.count_characters(research_text)
emails = aion.text.extract_emails("Contact: researcher@university.edu")

print(f"Text analysis: {word_count} words, {char_count} characters")
print(f"Extracted email: {emails}")

# ============================================================================
# 🧠 CODE ANALYSIS SHOWCASE
# ============================================================================

print_section("CODE ANALYSIS & QUALITY ASSESSMENT")

research_code = '''
def train_model(X, y, epochs=100):
    """Train a neural network."""
    for epoch in range(epochs):
        predictions = model.forward(X)
        loss = calculate_loss(predictions, y)
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")
    return model
'''

explanation = aion.code.explain_code(research_code)
complexity = aion.code.analyze_complexity(research_code)
functions = aion.code.extract_functions(research_code)

print(f"Code explanation: {explanation[:60]}...")
print(f"Functions found: {functions}")
print(f"Cyclomatic complexity: {complexity['cyclomatic_complexity']}")

# ============================================================================
# 📝 AI PROMPT ENGINEERING SHOWCASE
# ============================================================================

print_section("AI PROMPT ENGINEERING")

templates = aion.prompt.get_prompt_templates()
print(f"Available prompt templates: {len(templates)}")

custom_prompt = aion.prompt.create_custom_prompt(
    "Analyze {data_type} using {method}",
    data_type="neural network",
    method="gradient descent"
)
print(f"Custom prompt: {custom_prompt}")

# ============================================================================
# 📁 FILE MANAGEMENT SHOWCASE
# ============================================================================

print_section("FILE MANAGEMENT & DOCUMENTATION")

# Create and manage files
test_file = "demo_research.txt"
aion.files.create_empty_file(test_file)
aion.files.write_file(test_file, "# Research Data\nExperiment results here...")

if aion.files.file_exists(test_file):
    info = aion.files.get_file_info(test_file)
    print(f"Created file: {test_file} ({info['size']} bytes)")

# Generate documentation
try:
    report_file = aion.pdf.create_pdf_report(
        "AI Research Demo", 
        ["Experiment completed", "Results: Successful", "Next steps: Analysis"],
        "demo_report.txt"
    )
    print(f"✅ Report created: {report_file}")
except Exception as e:
    print(f"📄 Report generation: {e}")

# ============================================================================
# 🎯 RESEARCH WORKFLOW DEMONSTRATION
# ============================================================================

print_section("COMPLETE AI RESEARCH WORKFLOW")

print("🔬 Demonstrating AI research pipeline...")

# 1. Data preprocessing
raw_data = [85, 92, 78, 95, 88, 91, 84, 89, 93, 87]
normalized_data = aion.maths.min_max_scale(raw_data)
print(f"1️⃣ Data normalized: range [{min(normalized_data):.3f}, {max(normalized_data):.3f}]")

# 2. Statistical analysis
data_mean = aion.maths.mean(raw_data)
data_std = aion.maths.std_dev(raw_data)
print(f"2️⃣ Statistics: μ={data_mean:.2f}, σ={data_std:.2f}")

# 3. Model evaluation
predicted = [0.85, 0.92, 0.78, 0.95, 0.88]
actual = [0.87, 0.90, 0.80, 0.93, 0.86]
mse = aion.maths.mse_loss(actual, predicted)
print(f"3️⃣ Model MSE: {mse:.4f}")

# 4. Documentation
summary = f"""
RESEARCH SUMMARY - Generated by Aqwel-Aion v{aion.__version__}
Data: {len(raw_data)} samples, Mean: {data_mean:.2f}
Model MSE: {mse:.4f}
Status: {'Excellent' if mse < 0.01 else 'Good'}
"""

aion.files.write_file("research_summary.txt", summary)
print("4️⃣ ✅ Research summary saved")

# ============================================================================
# 🎉 DEMONSTRATION COMPLETE
# ============================================================================

print_section("DEMONSTRATION COMPLETE")

print("🎉 AQWEL-AION v0.1.7 COMPREHENSIVE SHOWCASE FINISHED!")
print(f"""
📊 DEMONSTRATED CAPABILITIES:
   🧮 Mathematics: 71+ functions (linear algebra, statistics, ML)
   �� AI Tools: Embeddings, evaluation, prompt engineering
   🧠 Code Analysis: Quality assessment and complexity metrics
   📁 File Management: Professional operations and documentation
   📄 Research Pipeline: Complete workflow automation

🚀 Total functions shown: 25+ out of 175+ available!

💡 This is just a sample of Aqwel-Aion's capabilities.
📧 Contact: aqwelaiofficial@gmail.com
🌐 Website: https://aqwelai.com/#aqwel-aion
""")

# Cleanup
cleanup_files = [test_file, "demo_report.txt", "research_summary.txt"]
for filename in cleanup_files:
    if aion.files.file_exists(filename):
        aion.files.delete_file(filename)

print("✅ Cleanup complete. Ready for your AI research!")

if __name__ == "__main__":
    print("\n🚀 Run this file to see Aqwel-Aion in action!")
    print("   python example.py")
