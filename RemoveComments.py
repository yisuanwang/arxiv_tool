def remove_full_comment_lines(input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.readlines()


    content_no_comments = [line for line in content if not line.strip().startswith('%')]


    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(content_no_comments)


input_file = '/mnt/chenjh/project/Idea23D/coling_latex.tex'  # 这里填入你的原 LaTeX 文件路径
output_file = '/mnt/chenjh/project/Idea23D/coling_latex_no_full_comments.tex'  # 这里填入你想要保存的文件路径

remove_full_comment_lines(input_file, output_file)
