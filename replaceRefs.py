import os

def modify_latex_file(latex_file):
    # 读取 LaTeX 文件
    with open(latex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换 \bibliography{custom} 为 \bibliography{main}
    content = content.replace(r'\bibliography{custom}', r'\bibliography{main}')

    # 写回修改后的内容到 LaTeX 文件
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {latex_file}.")

def rename_bib_and_bbl(directory):
    # 定义 custom.bib 和 custom.bbl 文件路径
    custom_bib = os.path.join(directory, 'custom.bib')
    custom_bbl = os.path.join(directory, 'output.bbl')

    # 定义 main.bib 和 main.bbl 文件路径
    main_bib = os.path.join(directory, 'main.bib')
    main_bbl = os.path.join(directory, 'main.bbl')

    # 重命名 custom.bib 和 custom.bbl 为 main.bib 和 main.bbl，如果文件存在
    if os.path.exists(custom_bib):
        os.rename(custom_bib, main_bib)
        print(f"Renamed {custom_bib} to {main_bib}.")

    if os.path.exists(custom_bbl):
        os.rename(custom_bbl, main_bbl)
        print(f"Renamed {custom_bbl} to {main_bbl}.")

def main():
    # 设置 LaTeX 文件路径和目录
    latex_file = '/mnt/chenjh/project/arxiv_tool/coling_latex.tex'  # 请替换成实际的 LaTeX 文件路径
    directory = os.path.dirname(latex_file)  # 获取文件所在的目录

    # 修改 LaTeX 文件
    modify_latex_file(latex_file)

    # 重命名相关的 .bib 和 .bbl 文件
    rename_bib_and_bbl(directory)

if __name__ == "__main__":
    main()
