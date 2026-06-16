# Podcast Generation Pipeline

基于 Podcastfy 的设计理念，将课程内容转为对话式播客。

## 流水线

```
lesson HTML
  ↓ extract_lessons.py (去代码/图表/导航)
cleaned .txt
  ↓ Claude + podcast_prompt_zh.md (Prompt 参数化生成)
episode-XXXX.json (对话稿, {speaker, text}[])
  ↓ generate_podcast.py (edge-tts 合成 + 合并)
episode-XXXX.mp3
```

## 两步走

### 第 1 步：生成对话稿

让 Claude 根据 prompt template 和课程内容生成 JSON 对话稿。

Claude 会读取：
- `prompts/podcast_prompt_zh.md`（参数化 prompt 模板）
- `config.yaml`（角色、风格、长度配置）
- `{episode}-*.txt`（课程清洁文本）

然后生成 `episode-XXXX.json`。

### 第 2 步：合成音频

```bash
python generate_podcast.py episode-0001.json episode-0001.mp3
```

## 角色

| 角色 | 声音 | 定位 |
|------|------|------|
| 云扬 (host) | Yunyang (男, 专业) | 好奇的学习者, 提问, 类比 |
| 晓晓 (cohost) | Xiaoxiao (女, 温暖) | 技术专家, 解释, 对比 |

## 设计参考

基于 Podcastfy 的 4 维参数化：
1. 角色非对称（asymmetric roles）：主持人=学习者，嘉宾=专家
2. 风格控制：口语化、填充词、打断、自然
3. 长度控制：按 word_count 分块，chunk 间上下文衔接
4. 信息密度：定义→为什么→例子→权衡

## 配置

`config.yaml` 控制所有参数，可独立修改不需改代码。
