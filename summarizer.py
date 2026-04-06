def summarize(text):
    sentences = text.split("。")
    summary = sentences[:2]
    return "。".join(summary)

if __name__ == "__main__":
    article = input("请输入文章内容：")
    result = summarize(article)

    print("\n总结结果：")
    print(result)
