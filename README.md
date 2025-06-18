# Your First LangGraph Project: Building a Joke Bot (AAIDC-Week5-Lesson-2b)

This project is part of the AAIDC course assignment: [Your First LangGraph Project: Building a Joke Bot](https://app.readytensor.ai/publications/T8WbWCjwJ4Mm)

## Overview

This project implements a simple joke-telling bot using LangGraph. Without using LLMs (Large Language Models), it aims to teach the basic mechanisms of graph-based workflows.

The joke bot has the following features:

- Fetches jokes from different categories (neutral, chuck, all)
- Responds to user choices through an interactive menu
- Tracks joke history through state management
- Controls flow using a graph-based workflow

## Technical Features

Through this project, you can learn the following basic concepts of LangGraph:

1. State definition and management
2. Creating node functions
3. Routing with conditional edges
4. Building and running a graph

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the joke bot, run the following command:

```bash
python joke_bot.py
```

After launching, follow the on-screen instructions:

- `n`: Display the next joke
- `c`: Change the joke category
- `q`: Exit the bot

### Example Execution

Here's an example of what running the joke bot looks like:

```
🎉==========================================================🎉
    WELCOME TO THE LANGGRAPH JOKE BOT!
    This example demonstrates agentic state flow without LLMs
============================================================


🚀==========================================================🚀
    STARTING JOKE BOT SESSION...
============================================================
🎭 Menu | Category: NEUTRAL | Jokes: 0
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: n

😂 Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25.

🎭 Menu | Category: NEUTRAL | Jokes: 1
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: c

📂 Available categories:
[0] neutral
[1] chuck
[2] all
Select category [0-2]: 1

✅ Category updated to: CHUCK

🎭 Menu | Category: CHUCK | Jokes: 1
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: n

😂 Chuck Norris doesn't read books. He stares them down until he gets the information he wants.

🎭 Menu | Category: CHUCK | Jokes: 2
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: q

🚪==========================================================🚪
    GOODBYE!
============================================================

🎊==========================================================🎊
    SESSION COMPLETE!
============================================================
    📈 You enjoyed 2 jokes during this session!
    📂 Final category: CHUCK
    🙏 Thanks for using the LangGraph Joke Bot!
============================================================
```

## Project Structure

```
AAIDC-Week5-Lesson-2b/
├── README.md          # Project description
├── requirements.txt   # Required libraries
├── joke_bot.py        # Main Python script
└── joke_bot_diagram.md # Workflow diagram
```

## Learning Points

Through this project, you can learn:

- Basic usage of LangGraph
- State management methods
- Building graph-based workflows
- Implementing conditional routing

While LangGraph is typically used in combination with agents and language models, this project is implemented without them to focus on the core functionality.

---

# LangGraph ジョークボット (AAIDC-Week5-Lesson-2b)

このプロジェクトはAAIDCコースの課題の一部です：[Your First LangGraph Project: Building a Joke Bot](https://app.readytensor.ai/publications/T8WbWCjwJ4Mm)

## 概要

このプロジェクトは、LangGraphを使用した簡単なジョークボットの実装です。LLM（大規模言語モデル）を使用せず、グラフベースのワークフローの基本的な仕組みを学ぶことを目的としています。

このジョークボットは以下の機能を持っています：

- 異なるカテゴリ（neutral、chuck、all）からジョークを取得
- インタラクティブなメニューでユーザーの選択に応じた動作
- 状態管理によるジョーク履歴の追跡
- グラフベースのワークフローによる制御フロー

## 技術的な特徴

このプロジェクトでは、以下のLangGraphの基本的な概念を学ぶことができます：

1. 状態の定義と管理
2. ノード関数の作成
3. 条件付きエッジによるルーティング
4. グラフの構築と実行

## インストール方法

必要なライブラリをインストールするには、以下のコマンドを実行してください：

```bash
pip install -r requirements.txt
```

## 使用方法

ジョークボットを起動するには、以下のコマンドを実行してください：

```bash
python joke_bot.py
```

起動後は、画面の指示に従って操作してください：

- `n`: 次のジョークを表示
- `c`: ジョークのカテゴリを変更
- `q`: ボットを終了

### 実行例

以下は、ジョークボットを実行した例です：

```
🎉==========================================================🎉
    WELCOME TO THE LANGGRAPH JOKE BOT!
    This example demonstrates agentic state flow without LLMs
============================================================


🚀==========================================================🚀
    STARTING JOKE BOT SESSION...
============================================================
🎭 Menu | Category: NEUTRAL | Jokes: 0
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: n

😂 プログラマーがハロウィンとクリスマスを混同するのはなぜですか？Oct 31 は Dec 25 に等しいからです。

🎭 Menu | Category: NEUTRAL | Jokes: 1
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: c

📂 Available categories:
[0] neutral
[1] chuck
[2] all
Select category [0-2]: 1

✅ Category updated to: CHUCK

🎭 Menu | Category: CHUCK | Jokes: 1
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: n

😂 チャック・ノリスは本を読みません。欲しい情報を得るまで本をにらみつけます。

🎭 Menu | Category: CHUCK | Jokes: 2
--------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit
User Input: q

🚪==========================================================🚪
    GOODBYE!
============================================================

🎊==========================================================🎊
    SESSION COMPLETE!
============================================================
    📈 You enjoyed 2 jokes during this session!
    📂 Final category: CHUCK
    🙏 Thanks for using the LangGraph Joke Bot!
============================================================
```

## プロジェクト構造

```
AAIDC-Week5-Lesson-2b/
├── README.md          # プロジェクトの説明
├── requirements.txt   # 必要なライブラリ
├── joke_bot.py        # メインのPythonスクリプト
└── joke_bot_diagram.md # ワークフローダイアグラム
```

## 学習ポイント

このプロジェクトを通じて以下の点を学ぶことができます：

- LangGraphの基本的な使い方
- 状態管理の方法
- グラフベースのワークフローの構築
- 条件付きルーティングの実装

LangGraphは通常、エージェントや言語モデルと組み合わせて使用されますが、このプロジェクトではコア機能に焦点を当てるために、それらを使用せずに実装しています。