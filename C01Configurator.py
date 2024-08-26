import json

if __name__ == "__main__":
    source_dir = input("请输入Markdown存放目录：")
    destination_dir = input("请输入HTML生成目录：")

    config = {
        "source_dir": source_dir,
        "destination_dir": destination_dir
    }

    with open("config.json", "wb") as f:
        f.write(json.dumps(config, indent=4).encode("UTF-8"))
