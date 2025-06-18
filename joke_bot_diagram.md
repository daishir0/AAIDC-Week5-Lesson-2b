# ジョークボット ワークフローダイアグラム

以下のMermaidコードは、ジョークボットのワークフローを視覚的に表現しています。このコードをMermaid対応のツールやウェブサイト（例：[Mermaid Live Editor](https://mermaid.live/)）に貼り付けることで、ダイアグラムを生成できます。

```mermaid
graph TD
    A[show_menu] -->|n| B[fetch_joke]
    A -->|c| C[update_category]
    A -->|q| D[exit_bot]
    
    B --> A
    C --> A
    D --> E[__end__]
    
    style A fill:#9370DB,stroke:#333,stroke-width:2px
    style B fill:#90EE90,stroke:#333,stroke-width:2px
    style C fill:#6495ED,stroke:#333,stroke-width:2px
    style D fill:#FF6347,stroke:#333,stroke-width:2px
    style E fill:#D3D3D3,stroke:#333,stroke-width:2px
```

## ダイアグラムの説明

このワークフローは以下の4つのノードで構成されています：

1. **show_menu** (紫色)：
   - メインのコントロールノード
   - ユーザーに3つの選択肢を提示：
     - 次のジョークを聞く (n)
     - ジョークのカテゴリを変更する (c)
     - アプリを終了する (q)
   - ユーザーの入力に基づいて、次のノードにルーティングします

2. **fetch_joke** (緑色)：
   - 選択されたカテゴリからジョークを取得して表示
   - ジョークを表示した後、show_menuに戻ります

3. **update_category** (青色)：
   - ユーザーが新しいジョークカテゴリを選択できるようにします
   - カテゴリ更新後、show_menuに戻ります

4. **exit_bot** (赤色)：
   - ユーザーが終了を選択した場合、さようならを言ってグラフを終了
   - 特別な__end__ノードにルーティングします

このシステムは、ユーザーが明示的に終了を選択するまでループします。