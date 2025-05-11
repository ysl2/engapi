# EngAPI

## Introduction

从欧路词典的某个词本导出,再导入到墨墨背单词的某个词本

## Usage

```bash
cp config.example.py config.py
python main.py
```

- `FRDIC_LIBNAME`: 欧路词典要导出的词本
- `MAIMEMO_LIBNAME`:  墨墨背单词要导入的词本
- `FRDIC_API_KEY`: https://my.eudic.net/OpenAPI/Authorization
- `MAIMEMO_API_KEY`: app内,"更多设置" -> "实验功能" -> "开放API"
