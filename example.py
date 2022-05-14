#%%
from summarizer import Summarizer
from summarizer.text_processors.sentence_handler import SentenceHandler
from transformers import AutoModel, AutoTokenizer, AutoConfig
from spacy.lang.zh import Chinese

#%%
modelName = "bert-base-chinese" # 選擇使用的 HugingFace Pretrained Model

print("wait a second...")
custom_config = AutoConfig.from_pretrained(modelName, output_hidden_states=True)    # 載入模型的config，並設定是否輸出每層得到的隱向量(必須)
custom_tokenizer = AutoTokenizer.from_pretrained(modelName)                         # 載入tokenizer
custom_model = AutoModel.from_pretrained(modelName, config=custom_config)           # 載入模型

model = Summarizer(
    custom_model=custom_model, 
    custom_tokenizer=custom_tokenizer,
    sentence_handler = SentenceHandler(language=Chinese)                            # 設定摘要模型語言(沒設效果有差)
)

#%%
body = "國民黨副總統候選人張善政昨日公開指行政院長蘇貞昌住院,並稱「老天有眼,很快就會讓他住回醫院去」等語,遭行政院駁斥假訊息。蘇貞昌長女、立委蘇巧慧今(28)日也表示,張善政發言已超過社會底線,就算他道歉,社會也已經撕裂、傷害已經造成。 蘇巧慧受訪時表示,每個人都有父母,做子女的看到爸爸在公開場合被別人詛咒式的發言、嘲諷,其他人哄堂大笑、拍手叫好,心情非常非常難過。 蘇巧慧說,台灣社會有一個底線,選舉可以有攻防,但是不會對對方的健康和生命,做這樣的惡質發言,這已經超過了底線,未來台灣要選擇怎樣的國家領導人,大家真的要睜大眼睛好好看看。 蘇巧慧說,父親就是過度勞累,面部神經短暫麻痺,對體能沒有影響,所以休息一天就回到行政院上班,上個禮拜院會影片也都公開給大家看,甚至今早已到政院主持院會了;她不懂為什麼這樣子公開資訊,張善政還可以造謠住院,非常非常不適當。 蘇巧慧也說,就算張善政有道歉,這個社會也已撕裂了,因為他的支持者為了維護候選人,也用更激烈的言論攻防,傷害已經造成。 媒體詢問是否會提告?蘇巧慧說,這不是提不提告的問題,傷害已經在這裡,就算提告也依然會存在,而且看出來的是,候選人本身人品的問題,他是不是適合坐在這樣的高位?大家真的應該好好想一想。 至於蘇貞昌本人心情,蘇巧慧表示可能比她好一些,父親從政這麼多年,面對這樣的攻擊習以為常,所以反而是父親叫她說不要太在意,他還是會盡全力衝衝衝。 除了蘇巧慧以外,昨天稱張善政是「政客墮落的血淋淋個案」的蔡英文競選文宣群副執行長林鶴明,今天上午也繼續指出,請張善政拿出道德勇氣道歉,知錯能改至少會獲得肯定,但如果只是出來辯解和說一些言不由衷的前提,那張善政就是讓年輕人對國民黨越來越失望的元兇之一。"
result = model(body, ratio=0.30, max_length=100)
full = ''.join(result)
print(full)
