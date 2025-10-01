# 🤖 LLM専門家相談アプリ

LangChainとOpenAI APIを使用したStreamlitベースのWebアプリケーションです。様々な分野の専門家AIと対話できます。

## 🎯 機能

- **4種類の専門家AI**
  - 💻 IT・プログラミング専門家
  - 💰 ビジネス・経営コンサルタント
  - 🎨 デザイン・クリエイティブ専門家
  - 📚 教育・学習アドバイザー

- **使いやすいインターフェース**
  - ラジオボタンによる専門家選択
  - テキストエリアでの質問入力
  - リアルタイムでのAI回答表示

## 🛠️ 技術仕様

- **フレームワーク**: Streamlit 1.41.1
- **AI技術**: OpenAI GPT-3.5-turbo
- **言語**: Python 3.12
- **主要ライブラリ**: 
  - LangChain 0.3.27
  - LangChain-OpenAI 0.3.33
  - python-dotenv 1.0.1

## 🚀 デプロイ

このアプリはStreamlit Community Cloudでホスティングされています。

### 環境変数設定

デプロイ時は以下の環境変数が必要です：

- `OPENAI_API_KEY`: OpenAI APIキー

## 📝 ローカル開発

1. リポジトリをクローン
```bash
git clone https://github.com/hashuhasuminewanguriching0132-oss/streamlit-llm-app.git
cd streamlit-llm-app
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

3. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
`.env`ファイルを作成し、OpenAI APIキーを設定：
```
OPENAI_API_KEY=your_openai_api_key_here
```

5. アプリの起動
```bash
streamlit run app.py
```

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。