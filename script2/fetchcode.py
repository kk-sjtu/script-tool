import re

def extract_code_blocks(markdown_file, output_file):
    """
    从 Markdown 文件中提取代码块，并保存到指定的输出文件中。

    参数:
        markdown_file (str): Markdown 文件路径
        output_file (str): 输出代码文件路径
    """
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # 匹配代码块的正则表达式（支持多种语言）
    code_pattern = re.compile(r"```(\w*)\n(.*?)\n```", re.DOTALL)
    code_blocks = code_pattern.findall(markdown_content)

    # 将提取的代码块写入到输出文件
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for language, code in code_blocks:
            out_file.write(f"### {language} code block\n")
            out_file.write(code.strip() + "\n\n")

    print(f"代码块已提取并保存到 {output_file}")

# 示例用法
if __name__ == "__main__":
    markdown_file = "../script1/同时更新个人仓库和组织仓库同一项目.md"  # Markdown 文件路径
    output_file = "../script1/extracted_code.py"  # 输出代码文件路径
    extract_code_blocks(markdown_file, output_file)