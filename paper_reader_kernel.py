import fitz
import subprocess
import os
from fpdf import FPDF
import textwrap
import re

def extract_text_from_pdf(pdf_path, max_pages=50):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(min(len(doc), max_pages)):
        page = doc[page_num]
        text += page.get_text()
    return text

def extract_post_think_text(full_text):
    parts = full_text.split("</think>")
    return parts[1].strip() if len(parts) > 1 else full_text

def query_deepseek(prompt_text, context_text):
    
    import random
    rand_int = random.randint(1, 999999999)  # 1 到 10，包括 1 和 10
    print(rand_int)

    output_path = f"output{rand_int}.txt"
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

def query_deepseek(prompt_text, context_text):
    full_prompt = f"{prompt_text}\n\nHere is the content:\n{context_text}"

    process = subprocess.run(
        ["ollama", "run", "deepseek-r1:70b"],
        input=full_prompt,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if process.returncode != 0:
        raise RuntimeError(f"DeepSeek execution failed:\n{process.stderr}")

    return process.stdout.strip()


import subprocess
import shlex

def run_shell_command(command, *args):
    """
    Safely runs a shell command with arguments that may contain spaces or special characters.
    
    Parameters:
    - command: the base command (e.g., 'md2pdf' or 'rm')
    - *args: file paths or other arguments
    
    Example usage:
        run_shell_command('md2pdf', input_path, output_path)
        run_shell_command('rm', file_path)
    """
    # Use shlex.quote to safely escape each argument
    safe_args = [shlex.quote(arg) for arg in args]
    cmd_str = f"{command} {' '.join(safe_args)}"
    try:
        subprocess.run(cmd_str, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")


from prompt_text import *
import time

def paper_reader(pdf_path, markdown_filename_pdf, iteration_num=5):

    start_time = time.time()
    markdown_filename = markdown_filename_pdf.replace('.pdf','.md')
    if not os.path.exists(markdown_filename):

        extracted_text = extract_text_from_pdf(pdf_path)
        context_text = textwrap.shorten(extracted_text, width=30000, placeholder='...')

        print("🤖 Querying DeepSeek model...")

        # paper reading
        # print(paper_reading_prompt_text)


        # ############################## A
        # answer = query_deepseek(paper_reading_prompt_text, context_text)
        # main_text = extract_post_think_text(answer)
        # final_text = f'**Reading Notes: {pdf_path}** \n\n' + main_text
        # ############################## A


        ############################# B
        all_text = ''
        for ver_idx in range(iteration_num):
            answer = query_deepseek(paper_reading_prompt_text, context_text)
            main_text = extract_post_think_text(answer)
            all_text = all_text + f'results {ver_idx}:' + main_text

        answer = query_deepseek('Merge all result to one!', all_text)
        main_text = extract_post_think_text(answer)
        final_text = f'**Reading Notes: {pdf_path}** \n\n' + main_text
        ############################# B

        with open(markdown_filename, "w", encoding="utf-8") as f:
            f.write(final_text)
        print(f"✅ Summary saved as Markdown: {markdown_filename}")


    # os.system(f'md2pdf {markdown_filename} {markdown_filename_pdf}')
    # os.system(f'rm {markdown_filename}')

    run_shell_command("md2pdf", markdown_filename, markdown_filename_pdf)
    run_shell_command("rm", markdown_filename)

    print(time.time() - start_time)


# # pdf_path = "/ifs/loni/faculty/shi/spectrum/yxia/github_2025/LLM/CLIP/2301.02228v3.pdf"
# # markdown_filename_pdf = "/ifs/loni/faculty/shi/spectrum/yxia/github_2025/LLM/CLIP/2301.02228v3_summary.pdf"
# # paper_reader(pdf_path, markdown_filename_pdf, iteration_num=8)

# from glob import glob
# pdf_paths = glob("/ifs/loni/faculty/shi/spectrum/yxia/tmp/Readings/**/*.pdf", recursive=True)
# print(len(pdf_paths)*800/3600)

# for pdf_path in sorted(pdf_paths):
#     summary_pdf = pdf_path.replace('.pdf', '_summary.pdf')

#     print(30*'*')
#     print(pdf_path)
#     print(summary_pdf)
#     paper_reader(pdf_path, summary_pdf, iteration_num=5)

