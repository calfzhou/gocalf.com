---
title: Azure OpenAI and Microsoft Foundry
notebook: notes
tags:
  - it/ai
date: 2026-01-13 23:22:31
updated: 2026-01-13 23:22:31
---
## Background

想把 Azure OpenAI（即 AOAI）用作日常 AI Chat 使用。

目前 Azure OpenAI 和其他 AI 服务都在 Microsoft Foundry 下。

## 创建 Foundry Resource

在 [Microsoft Azure portal](https://portal.azure.com/#home) 中进入 [Microsoft Foundry](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/AIFoundryPhaseTwo_overview)，菜单 "Use with Foundry" 下有 "Foundry" 和 "Azure OpenAI"。后者现在不太好用。

在 "Foundry" 中创建 resource，选一个 region（如 East US）（不行就换一个 region 重新创建）；"Default project name" 随意；"Pricing tier" 是 "S0"。

创建好后进入该 resource。完整的 Resource ID 是：

```text
/subscriptions/{SubscriptionID}/resourceGroups/{ResourceGroup}/providers/Microsoft.CognitiveServices/accounts/{ResourceName}
```

"Resource Management" » "Keys and Endpoint"，有两个 API key（比如在重新生成某个 key 的时候，可以先用另一个避免服务中断）。Endpoint 主要是有 Foundry 和 OpenAI 两种，分别是：

```yaml
Foundry: https://{ResourceName}.services.ai.azure.com/
OpenAI: https://{ResourceName}.openai.azure.com/
```

这时候还不能用，需要先 deploy models。

## Deploy Base Models

在 resource 的 "Overview" 页面，点击 "Go to Foundry portal" 打开 [Microsoft Foundry portal](https://ai.azure.com/)。

> Azure 里只是创建和管理 resource 的常规信息，具体的要在 Foundry 里操作。

如果启用了 "New Foundry" 模式，打开后直接进入创建 resource 时设定的 default project 的首页。首页显示 Foundry endpoint 和 API key 1。点 "Start building" » "Browse models" 或 "Build" » "Models" » "Deploy a base model"。选一个 model（如 `gpt-5.2-chat`），在 model 详情页点 "Deploy"。

列的 models 很多，实际能用的没几个，不同 region 可用的差别也很大。

> [!caution]
> 由于可用 region 的限制，deploy base model 的时候，可能只能选一个跟当前 resource / project 不同的 region，这会再创建一个对应 region 的 resource，新的 resource 会有自己的 API key 和 endpoint。

Deploy 的 models 在 "Build" » "Models" 里展示，点击会进入 playground，可以直接尝试 chat。

## 调用 Base Model

### Python

```bash
pip install openai

pip show openai
# Version: 2.15.0
```

使用 OpenAI endpoint 和 `OpenAI` class：

```python try_openai.py
from openai import OpenAI

endpoint = "https://RESOURCE-NAME.openai.azure.com/openai/v1/"
deployment_name = "gpt-5.2-chat" # DEPLOYED-MODEL-NAME
api_key = "API-KEY"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)
```

使用 Foundry endpoint 和 `AzureOpenAI` class：

```python try_azure_openai.py
from openai import AzureOpenAI

endpoint = "https://RESOURCE-NAME.services.ai.azure.com/"
deployment_name = "gpt-5.2-chat" # DEPLOYED-MODEL-NAME
api_key = "API-KEY"
api_version = "2024-10-21"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)
completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)
```

### curl

使用 v1 API (Next Generation) (starting in August 2025):

```bash
curl --request POST \
  --url 'https://RESOURCE-NAME.openai.azure.com/openai/v1/chat/completions' \
  --header 'api-key: API-KEY' \
  --header 'content-type: application/json' \
  --data '{
    "model": "DEPLOYED-MODEL-NAME",
    "messages": [{
      "role": "user",
      "content": "What is the capital of France?"
    }]
  }'
```

以前的方式（需要指定 `api-version`）：

```bash
curl --request POST \
  --url 'https://RESOURCE-NAME.openai.azure.com/openai/deployments/DEPLOYED-MODEL-NAME/chat/completions?api-version=2024-10-21' \
  --header 'api-key: API-KEY' \
  --header 'content-type: application/json' \
  --data '{
    "messages": [{
      "role": "user",
      "content": "What is the capital of France?"
    }]
  }'
```

## 客户端 - Chatbox AI

[Chatbox AI: Your AI Copilot, Best AI Client on any device, Free Download](https://chatboxai.app/en/)

> Chatbox AI is an AI client application and smart assistant. Compatible with many cutting-edge AI models and APIs. Available on Windows, MacOS, Android, iOS, Web, and Linux.

{% badge_github chatboxai chatbox %}

v1.18,2

### 配置 Azure OpenAI

Settings » Model Provider » Azure OpenAI:

- API Key: 在 Azure 里看到的那两个 API key 之一。Foundry 里也有。
- Azure Endpoint: 直接填 Foundry 的 resource name。
- Azure API Version: 可缺省。2025 年 8 月 v1 API (Next Generation) 出来之前的 GA 版本应该是 `2024-10-21`。详见 [API lifecycle guide](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic#api-evolution)。

> [!caution]
> "Fetch" 功能不好使，无法拉到 deploy 过的 models。需要手动添加，填入 deployed model name，如果正确，点 "Text Model" 会成功。

### 配置自定义 Provider

可能会遇到不同的 model 被 deploy 到不同的 region，则会对应不同的 resource name 和 API key。

Chatbox AI 里，在 Azure OpenAI 那里可以配置一个 resource 的信息，其他的用自定义 provider。

- API Mode: "OpenAI API Compatible"
- API Key: 在 Azure 里看到的 API key。
- API Host: `{RESOURCE-NAME}.openai.azure.com/openai`
- API Path: 缺省。
