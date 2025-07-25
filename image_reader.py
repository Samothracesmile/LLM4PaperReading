import subprocess
from output_control import extract_post_think_text
import os

def analyze_tau_pathology(image_path):
    """
    Use Ollama's gemma3:27b model to analyze a cortical surface image
    and describe the pattern of tau pathology.

    Args:
        image_path (str): Path to the cortical surface image (.png)

    Returns:
        str: Model's textual analysis output
    """
    prompt = (
        "Describe the pattern and regional distribution of tau pathology on this cortical surface. "
        "Identify any visible asymmetries, regions with elevated tau accumulation, and possible clinical implications."
    )

    try:
        result = subprocess.run(
            ["ollama", "run", "gemma3:27b", prompt, image_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def query_deepseek(prompt_text, context_text):
    output_path = "output1.txt"
    # full_prompt = f"{prompt_text}\n\nHere is the paper content:\n{context_text}"
    full_prompt = f"{prompt_text}\n\n Here is the content:\n{context_text}"

    with open(output_path, "w", encoding="utf-8") as output_file:
        subprocess.run([
            "ollama", "run", "deepseek-r1:70b"],
            input=full_prompt,
            stdout=output_file,
            text=True
        )

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read().strip()

    os.system(f'rm {output_path}')

    return result 



from glob import glob

for tau_img_file in sorted(glob("/ifs/loni/faculty/shi/spectrum/yxia/tau_6_view_plots/*.png")):
    # print(tau_img_file)

    result = analyze_tau_pathology(tau_img_file)
    # print(result)

    answer = query_deepseek('Refine the results: ', result)
    final_text = extract_post_think_text(answer)
    # print(final_text)

    markdown_filename_pdf = tau_img_file.replace('.png', '_summary.pdf')
    markdown_filename = markdown_filename_pdf.replace('.pdf','.md')
    with open(markdown_filename, "w", encoding="utf-8") as f:
        f.write(final_text)
    print(f"✅ Summary saved as Markdown: {markdown_filename}")

    os.system(f'md2pdf {markdown_filename} {markdown_filename_pdf}')