import wikipedia
from nltk import sent_tokenize
import json


def clean_paragraph(para):
    para = para.replace("\\'", "'")
    para = re.sub(r'\[[^]]*\]|\([^)]*\)', '', para)

    return para


def get_random_title():
    return wikipedia.random()


def get_page_summary(title):
    print(title)
    try:
        summ = wikipedia.summary(title)
        if "\\u" in summ:
            return ""
        return summ
    except:
        print("Disambiguation error in {}".format(title))
        return ""


def main():
    pages = []
    for i in range(5000):
        summary = get_page_summary(get_random_title())
        sentences = sent_tokenize(summary)
        pages.append(sentences)

    out = json.dumps(pages)
    with open("sentence_dump.txt", "a") as f:
        f.write(out)


# with open("sentence_dump.txt", "r") as f:
#     pages = json.loads(f.read())

main()
