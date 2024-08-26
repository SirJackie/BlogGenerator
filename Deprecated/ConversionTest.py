import markdown

# Markdown 文本
markdown_text = """
# 这是一个标题

这是一些 *斜体* 和 **粗体** 的文本。

- 列表项 1
- 列表项 2
"""

# 转换为 HTML
html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])

# 输出 HTML
print(html)

with open("output.html", "wb") as f:
    f.write(html.encode("UTF-8"))
