import crawler
from topic_processor import Corpus

if __name__ == '__main__':
    # 1. 시각화 할 말뭉치를 list에 담기
    cc = crawler.crawler()
    acl = cc.acl2023_crawler()

    # 2. n-gram을 통해 말뭉치 처리 및 시각화
    cp = Corpus(n_gram=3)
    cp.make_wordcloud_with(acl)
    