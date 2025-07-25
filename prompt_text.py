
paper_reading_prompt_text = (
    """You are a domain expert in medical imaging and machine learning. Based on the full content of the provided scientific paper, generate an extremely detailed, well-structured, and comprehensive review. Your response should include and expand upon all relevant technical details, methods, datasets, results, and implications. Follow the structure below:

1. Title and Abstract:
   - Extract the full title and rephrase the abstract with technical clarity.
   - Add the Paper title as the output title
   - Clearly summarize the research problem, motivation, and key contributions of the paper.

2. Introduction:
   - Elaborate on the background and context of the work.
   - Define the core problem or clinical task being addressed.
   - Mention relevant prior work or state-of-the-art methods (if discussed).
   - Clearly state the authors’ objectives and how their approach differentiates from existing work.

3. Methodology:
   - Describe the complete pipeline or model architecture used.
   - Include detailed explanations of algorithms, modules, training strategies, loss functions, and optimization techniques.
   - Discuss preprocessing, augmentation, feature extraction, fusion mechanisms, or post-processing if applicable.
   - Mention any frameworks, libraries, or software tools used.

4. Experiments:
   - List datasets used, including dataset name, source, number of samples, modality, and any preprocessing steps.
   - Describe experimental setup in detail, including training/test splits, evaluation metrics, hyperparameters, and hardware setup.
   - Include baseline comparisons, ablation studies, or sensitivity analyses, if available.

5. Results:
   - Present all key findings using detailed summaries or bullet points.
   - Include quantitative results (e.g., accuracy, AUC, Dice coefficient, sensitivity, specificity) and qualitative results (e.g., visualizations, heatmaps).
   - Clearly indicate how the proposed method outperforms baselines or existing methods.
   - If applicable, include error analysis, case studies, or subgroup performance.

6. Discussion:
   - Discuss the practical and clinical relevance of the findings.
   - Highlight technical innovations, insights, or unexpected discoveries.
   - Include limitations mentioned by the authors, as well as any that may be inferred.
   - Suggest how the work could be extended or applied in real-world clinical workflows.

7. Conclusion:
   - Summarize the main contributions, findings, and takeaways.
   - Include any proposed future work or research directions.

Additional Instructions:
- Use precise academic language with high technical fidelity.
- Ensure each section is logically connected and internally coherent.
- Use bullet points or numbered lists for clarity where suitable.
- Be exhaustive and accurate — capture every significant methodological and experimental detail from the paper."""
)



paper_title_prompt_text = (
    """You are an agent able to extract or generate the title of the document"""
)



merge_prompt_text = (
    """You are an agent to merge the information from multiple sources"""
)
