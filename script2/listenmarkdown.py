import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import re

class MarkdownHandler(FileSystemEventHandler):
    def __init__(self, markdown_file, output_file):
        self.markdown_file = markdown_file
        self.output_file = output_file

    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"{event.src_path} 文件已修改，正在提取代码块...")
            extract_code_blocks(self.markdown_file, self.output_file)

def extract_code_blocks(markdown_file, output_file):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    code_pattern = re.compile(r"```(\w*)\n(.*?)\n```", re.DOTALL)
    code_blocks = code_pattern.findall(markdown_content)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for language, code in code_blocks:
            out_file.write(f"### {language} code block\n")
            out_file.write(code.strip() + "\n\n")

    print(f"代码块已提取并保存到 {output_file}")

if __name__ == "__main__":
    markdown_file = "../script1/同时更新个人仓库和组织仓库同一项目.md"
    output_file = "../script1/extracted_code.py"

    event_handler = MarkdownHandler(markdown_file, output_file)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(markdown_file), recursive=False)
    observer.start()

    print(f"开始监听 {markdown_file} 文件的变化...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()