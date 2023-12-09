# -*- coding: euc-kr -*-
import os
#@markdown https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "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" 

#@markdown https://huggingface.co/settings/tokens
#@markdown HuggingFace에서 모델 다운로드나 클라우드 모델 사용하기 위해서 필요 (무료)
HUGGINGFACEHUB_API_TOKEN = "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" #@param {type:"string"}

#@markdown https://serpapi.com/manage-api-key
#@markdown 구글 검색하기 위해서 필요 (월 100회 무료)
SERPAPI_API_KEY = "d96dc34a129b8aef7a3f46104438655d7feb2667ccbb276a7db6accc164920a7" #@param {type:"string"}

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)
sys = SystemMessage(content="당신은 식당 추천을 해주는 전문 AI입니다.")
msg = HumanMessage(content='서울에서 맛있는 중국식당 5곳 추천해줘.')

aimsg = chat([sys, msg])
print(aimsg.content)