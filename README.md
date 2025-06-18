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