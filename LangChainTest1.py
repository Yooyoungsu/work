# -*- coding: euc-kr -*-
import os
#@markdown https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "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" 

#@markdown https://huggingface.co/settings/tokens
#@markdown HuggingFace���� �� �ٿ�ε峪 Ŭ���� �� ����ϱ� ���ؼ� �ʿ� (����)
HUGGINGFACEHUB_API_TOKEN = "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" #@param {type:"string"}

#@markdown https://serpapi.com/manage-api-key
#@markdown ���� �˻��ϱ� ���ؼ� �ʿ� (�� 100ȸ ����)
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
sys = SystemMessage(content="����� �Ĵ� ��õ�� ���ִ� ���� AI�Դϴ�.")
msg = HumanMessage(content='���￡�� ���ִ� �߱��Ĵ� 5�� ��õ����.')

aimsg = chat([sys, msg])
print(aimsg.content)