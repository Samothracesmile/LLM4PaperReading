# import os
# from concurrent.futures import ProcessPoolExecutor
# from glob import glob
# from paper_reader_kernel import paper_reader

# max_workers = 4

# pdf_paths = glob("/ifs/loni/faculty/shi/spectrum/yxia/tmp/Reading*/**/*.pdf", recursive=True)
# pdf_paths = [path for path in pdf_paths if not path.endswith("_summary.pdf")]


# # Prepare tasks
# tasks = []
# for pdf_path in sorted(pdf_paths):
#     summary_pdf = pdf_path.replace('.pdf', '_summary.pdf')
#     if not os.path.exists(summary_pdf):
#         tasks.append((pdf_path, summary_pdf))
#         # print((pdf_path, summary_pdf))

# # print(len(tasks) * 800 / (3600*max_workers))

# # Parallel execution
# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=max_workers) as executor:
#         executor.map(lambda args: paper_reader(*args, iteration_num=5), tasks)


import os
from concurrent.futures import ThreadPoolExecutor  # ← changed to thread-based
from glob import glob
from paper_reader_kernel import paper_reader

# print("CUDA_VISIBLE_DEVICES:", os.environ.get("CUDA_VISIBLE_DEVICES"))

pdf_paths = glob("/ifs/loni/faculty/shi/spectrum/yxia/github_2025/LLM/LLM4PaperReading/paper2read/*.pdf", recursive=True)
pdf_paths = [path for path in pdf_paths if not path.endswith("_summary.pdf")]

tasks = []
for pdf_path in sorted(pdf_paths):
    summary_pdf = pdf_path.replace('.pdf', '_summary.pdf')
    if not os.path.exists(summary_pdf):
        tasks.append((pdf_path, summary_pdf))
        paper_reader(pdf_path, summary_pdf, iteration_num=5)

# #         print((pdf_path, summary_pdf))
# print(len(tasks))

# max_workers = 4  # Adjust based on GPU capacity
# # Parallel is not working for now
# # if __name__ == "__main__":
# #     with ThreadPoolExecutor(max_workers=max_workers) as executor:
# #         executor.map(lambda args: paper_reader(*args, iteration_num=5), tasks)
