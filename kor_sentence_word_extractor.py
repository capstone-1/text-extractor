from krwordrank.word import KRWordRank
from krwordrank.sentence import make_vocab_score
from krwordrank.sentence import MaxScoreTokenizer
from krwordrank.sentence import keysentence
# 분석하고자 하는 텍스트 읽기
fileName = 'kor_input.txt'
texts = []
with open(fileName, encoding='utf-8-sig') as file:
    for line in file:
        texts.append(line.split(',')[-1].rstrip())  # 텍스트 구조에 따라 달라집니다.

# 키워드 학습
wordrank_extractor = KRWordRank(
    min_count=5,  # 단어의 최소 출현 빈도수
    max_length=10,  # 단어의 최대길이
    verbose = True
)
beta = 0.85
max_iter = 10

keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter, num_keywords=100)

# 단어 출력부분
with open('kor_word_output.txt',mode='w',encoding='utf-8-sig') as file:
    for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:10]:
        file.write('%8s:\t%.4f\n' % (word, r))

stopwords = {}  # ?
vocab_score = make_vocab_score(keywords, stopwords, scaling=lambda x : 1)
tokenizer = MaxScoreTokenizer(vocab_score)  # 문장 내 단어 추출기

#  패널티 설정 및 핵심 문장 추출
penalty = lambda x: 0 if 25 <= len(x) <= 80 else 1
sentencses = keysentence(
    vocab_score, texts, tokenizer.tokenize,
    penalty=penalty,
    diversity=0.3,
    topk=10  # 추출 핵심 문장 갯수 설정
)

# 문장 출력부분
with open('kor_sentence_output.txt',mode='w',encoding='utf-8-sig') as file:
    for sentence in sentencses:
        file.write(sentence+'\n')