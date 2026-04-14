import json
import os

# 1. 建立存放網頁檔案的 docs 資料夾
if not os.path.exists("docs"):
    os.makedirs("docs")

# 2. 讀取影片資料
with open("videos.json", "r", encoding="utf-8") as f:
    videos = json.load(f)

# 3. 設定網站核心結構檔
yaml_content = """site_name: 孫葛數學線上題庫
theme:
  name: material
  features:
    - navigation.tabs
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true
extra_javascript:
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
nav:
  - 首頁: index.md
  - 解題影片庫:
"""

# 4. 生成網站首頁
with open("docs/index.md", "w", encoding="utf-8") as f:
    f.write("# 歡迎來到孫葛數學線上題庫\n\n請從左側選單選擇你想觀看的題目解析。\n")

# 5. 自動生成網頁與清理檔名符號
nav_list = []
for video in videos:
    title = video['title']
    video_id = video['id']
    
    # 【修改重點 1】檔名終極清理：把中括號、全形括號通通換成底線 _
    safe_filename = title.replace("/", "_").replace("\\", "_").replace(" ", "_").replace(":", "_").replace("?", "_").replace("\"", "").replace("'", "").replace("[", "_").replace("]", "_").replace("【", "_").replace("】", "_")
    filename = f"{safe_filename}.md"
    
    # 目錄清理
    safe_nav_title = title.replace("'", "").replace('"', "").replace("[", "【").replace("]", "】").replace(":", "：")
    
    md_content = f"# {title}\n\n"
    md_content += f'<iframe width="640" height="360" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>\n\n'
    md_content += "---\n\n## 文字詳解與觀念補充\n\n*(未來可以在這裡輸入 LaTeX 公式，例如：$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$)*\n"
    
    with open(f"docs/{filename}", "w", encoding="utf-8") as f:
        f.write(md_content)
        
    # 【修改重點 2】用單引號把檔名包起來，徹底避免 YAML 崩潰
    nav_list.append(f"    - '{safe_nav_title}': '{filename}'\n")

# 將所有題目加入目錄
for nav_item in nav_list:
    yaml_content += nav_item

with open("mkdocs.yml", "w", encoding="utf-8") as f:
    f.write(yaml_content)

print(f"✅ 網頁與目錄自動生成完畢！這次連檔名都徹底消毒了。")