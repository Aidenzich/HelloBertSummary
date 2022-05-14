# Install
```
pip install requirements.txt
```

## bert-extractive-summarizer
- [github](https://github.com/dmmiller612/bert-extractive-summarizer)

## Example
```python
python example.py
```

## 設定 sentence_handler 成中文
- 未設定 SentenceHandler
    ```
    蘇巧慧受訪時表示,每個人都有父母,做子女的看到爸爸在公開場合被別人詛咒式的發言、嘲諷,其他人哄堂大笑、拍手叫好,心情非常非常難過。 蘇巧慧說,台灣社會有一個底線,選舉可以有攻防,但是不會對對方的健康和生命,做這樣的惡質發言,這已經超過了底線,未來台灣要選擇怎樣的國家領導人,大家真的要睜大眼睛好好看看。
    ```
- 設定 SentenceHandler(language=Chinese)
    ```
    國民黨副總統候選人張善政昨日公開指行政院長蘇貞昌住院,並稱「老天有眼,很快就會讓他住回醫院去」等語,遭行政院駁斥假訊息。 蘇巧慧也說,就算張善政有道歉,這個社會也已撕裂了,因為他的支持者為了維護候選人,也用更激烈的言論攻防,傷害已經造成。
    ```

## Summarizer usecase
```python
body = "<摘要對象文章內容>"
result = model(body, ratio=0.30, max_length=100) # 摘要長度設定
full = ''.join(result)
print(full)  # 摘要結果
```

### Parameters
- body: str # The string body that you want to summarize
- ratio: float # The ratio of sentences that you want for the final summary
- min_length: int # Parameter to specify to remove sentences that are less than 40 characters
- max_length: int # Parameter to specify to remove sentences greater than the max length,
- num_sentences: Number of sentences to use. Overrides ratio if supplied.