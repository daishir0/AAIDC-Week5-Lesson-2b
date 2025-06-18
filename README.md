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
├── joke_bot.py        # Basic joke bot implementation
├── joke_bot1.py       # Version with language switching
├── joke_bot2.py       # Version with history reset
├── joke_bot3.py       # Version using OpenAI for jokes
├── config.yaml        # Configuration for OpenAI API
└── joke_bot_diagram.md # Workflow diagram
```

## Extended Versions

This project includes three extended versions of the joke bot, each adding new functionality:

### 1. Language Switching (joke_bot1.py)

This version adds the ability to switch between different languages:

```bash
python joke_bot1.py
```

Features:
- Support for multiple languages (English, German, Spanish, Italian, French)
- New menu option: `[l]` to change language
- Updated state management to track language preference

### 2. History Reset (joke_bot2.py)

This version adds the ability to reset joke history:

```bash
python joke_bot2.py
```

Features:
- New menu option: `[r]` to reset joke history
- Clears all previously told jokes from memory
- Allows starting fresh without restarting the bot

### 3. LLM-Powered Jokes (joke_bot3.py)

This version replaces pyjokes with OpenAI API for generating jokes:

```bash
python joke_bot3.py
```

Features:
- Uses OpenAI API to generate jokes on demand
- Different joke categories: programmer, chuck, dad
- Loads API key from config.yaml
- More varied and potentially funnier jokes

Before running joke_bot3.py, make sure to:
1. Update your OpenAI API key in config.yaml
2. Install additional dependencies with `pip install -r requirements.txt`

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
├── joke_bot.py        # 基本的なジョークボットの実装
├── joke_bot1.py       # 言語切り替え機能を追加したバージョン
├── joke_bot2.py       # 履歴リセット機能を追加したバージョン
├── joke_bot3.py       # OpenAIを使用したジョーク生成バージョン
├── config.yaml        # OpenAI APIの設定ファイル
└── joke_bot_diagram.md # ワークフローダイアグラム
```

## 拡張バージョン

このプロジェクトには、新しい機能を追加した3つの拡張バージョンのジョークボットが含まれています：

### 1. 言語切り替え機能 (joke_bot1.py)

このバージョンでは、異なる言語を切り替える機能が追加されています：

```bash
python joke_bot1.py
```

特徴：
- 複数の言語をサポート（英語、ドイツ語、スペイン語、イタリア語、フランス語）
- 新しいメニューオプション：`[l]`で言語を変更
- 言語設定を追跡するための状態管理の更新

### 2. 履歴リセット機能 (joke_bot2.py)

このバージョンでは、ジョーク履歴をリセットする機能が追加されています：

```bash
python joke_bot2.py
```

特徴：
- 新しいメニューオプション：`[r]`でジョーク履歴をリセット
- 以前に表示したすべてのジョークをメモリからクリア
- ボットを再起動せずに新しく始めることが可能

### 3. LLMを使用したジョーク生成 (joke_bot3.py)

このバージョンでは、pyjokesの代わりにOpenAI APIを使用してジョークを生成します：

```bash
python joke_bot3.py
```

特徴：
- OpenAI APIを使用してジョークをオンデマンドで生成
- 異なるジョークカテゴリ：programmer、chuck、dad
- config.yamlからAPIキーを読み込み
- より多様で潜在的に面白いジョーク

joke_bot3.pyを実行する前に、以下の準備が必要です：
1. config.yamlにOpenAI APIキーを設定
2. `pip install -r requirements.txt`で追加の依存関係をインストール

## 学習ポイント

このプロジェクトを通じて以下の点を学ぶことができます：

- LangGraphの基本的な使い方
- 状態管理の方法
- グラフベースのワークフローの構築
- 条件付きルーティングの実装

LangGraphは通常、エージェントや言語モデルと組み合わせて使用されますが、このプロジェクトではコア機能に焦点を当てるために、それらを使用せずに実装しています。