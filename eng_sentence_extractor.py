from summa.summarizer import summarize
# 분석하고자 하는 텍스트 읽기
fileName = 'eng_input.txt'
texts = ''
with open(fileName, encoding='utf-8-sig') as file:
    for line in file:
        texts += line.split(',')[-1] # 텍스트 구조에 따라 달라집니다.

# 문장 출력부분
with open('eng_sentence_output.txt',mode='w',encoding='utf-8-sig') as file:
    file.write(summarize(texts, language='english', ratio=0.1)) # ratio -> 전체 문장중 요약으로 뽑을 비율
