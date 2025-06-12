
import sys 
import os
import markdown
import time
# 현재 시간을 밀리초 단위로 가져오기 (JavaScript의 Date.now()처럼)
code_id = f"code_{int(time.time() * 1000)}"

def convert_files_to_html(readme_path, sql_path, output_path=f"output.html"):
    # README.md 읽기 및 마크다운 -> HTML 변환
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        # 원하는 줄만 선택 (인덱스는 0부터 시작하므로 주의)
        selected_lines = []
        if len(lines) >= 1:
            selected_lines.append(lines[0])  # 1번째 줄
        if len(lines) >= 3:
            selected_lines.append(lines[2])  # 3번째 줄
        if len(lines) >= 21:
            selected_lines.extend(lines[20:])  # 21번째 줄부터 마지막 줄까지

        # 선택된 줄들을 하나의 문자열로 합치고 마크다운 파싱
        readme_content = ''.join(selected_lines)
        readme_html = markdown.markdown(readme_content)


    # SQL 파일 읽기 및 HTML 코드블럭 처리
    with open(sql_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()
        sql_html = f"<h2>SQL Code</h2>\n<pre id=\"{code_id}\" class=\"sql\" data-ke-language=\"sql\" data-ke-type=\"codeblock\"><code>{sql_content}</code></pre>"

    # 전체 HTML 구성
    full_html = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>README and SQL Viewer</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        code {{
            font-family: Consolas, monospace;
        }}
    </style>
    </head>
    <body>
    <div class='markdown-body'>
    
    {readme_html}
    <hr>
    <br>
    <br>
    {sql_html}
    </div>
    </body>
    </html>
    """

    # HTML 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"✅ HTML 파일이 생성되었습니다: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("❌ 사용법: python blogpost.py <README.md 경로> <정답코드 경로> <output.html 경로>")
    else:
        convert_files_to_html(sys.argv[1], sys.argv[2], sys.argv[3])

