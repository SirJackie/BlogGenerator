import json
import os
import markdown

if __name__ == "__main__":
    with open("config.json", "rb") as f:
        config = json.loads(f.read().decode("UTF-8"))

    source_dir = config["source_dir"]
    destination_dir = config["destination_dir"]

    # Filter out the markdown files.
    markdown_filenames = []

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file[-3:] == ".md":
                markdown_filenames.append(os.path.join(root, file))

    print(markdown_filenames)

    # Generate a "from-to" list
    from_to_list = []

    for filename in markdown_filenames:
        from_to_list.append(
            {
                "from": filename,
                "to": filename.replace(source_dir, destination_dir).replace(".md", ".html")
            }
        )

    # Complete the conversions.
    for article in from_to_list:

        with open(article["from"], "rb") as f:
            markdown_text = f.read().decode("UTF-8")

        html_code = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])

        with open(article["to"], "wb") as f:
            f.write(html_code.encode("UTF-8"))

        print(f"Converted: from {article['from']} to {article['to']}")

    pass
