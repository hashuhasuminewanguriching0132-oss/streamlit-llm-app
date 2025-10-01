import streamlit as st
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

# アプリのタイトル
st.title("🤖 LLM専門家相談アプリ")

# アプリの説明
st.markdown("""
## 📋 アプリ概要
このアプリでは、様々な分野の専門家AIと対話できます。
相談したい分野を選択し、質問を入力してください。

## 🔧 操作方法
1. 下のラジオボタンから相談したい専門家を選択
2. テキストボックスに質問を入力
3. 「相談する」ボタンをクリック
4. AI専門家からの回答が表示されます
""")

# 専門家の選択
expert_type = st.radio(
    "相談したい専門家を選択してください:",
    [
        "💻 IT・プログラミング専門家",
        "💰 ビジネス・経営コンサルタント", 
        "🎨 デザイン・クリエイティブ専門家",
        "📚 教育・学習アドバイザー"
    ]
)

# 質問の入力
user_question = st.text_area(
    "質問を入力してください:",
    height=100,
    placeholder="例: Pythonでウェブアプリを作りたいのですが、どの技術を使えばいいですか？"
)

def get_expert_response(expert_type, question):
    """
    専門家タイプと質問を受け取り、LLMからの回答を返す関数
    
    Args:
        expert_type (str): 選択された専門家タイプ
        question (str): ユーザーの質問
    
    Returns:
        str: LLMからの回答
    """
    
    # 専門家タイプに応じてシステムメッセージを設定
    if "IT・プログラミング" in expert_type:
        system_message = """あなたは経験豊富なIT・プログラミング専門家です。
        プログラミング言語、フレームワーク、システム設計、技術選定などについて、
        初心者にもわかりやすく、実践的なアドバイスを提供してください。
        具体的なコード例や学習リソースも含めて回答してください。"""
        
    elif "ビジネス・経営" in expert_type:
        system_message = """あなたは経験豊富なビジネス・経営コンサルタントです。
        経営戦略、マーケティング、組織運営、財務管理などについて、
        実践的で具体的なアドバイスを提供してください。
        業界動向や成功事例も含めて回答してください。"""
        
    elif "デザイン・クリエイティブ" in expert_type:
        system_message = """あなたは経験豊富なデザイン・クリエイティブ専門家です。
        UI/UXデザイン、グラフィックデザイン、ブランディング、クリエイティブ戦略などについて、
        美的センスと実用性を両立した具体的なアドバイスを提供してください。
        デザインツールや制作プロセスも含めて回答してください。"""
        
    elif "教育・学習" in expert_type:
        system_message = """あなたは経験豊富な教育・学習アドバイザーです。
        効果的な学習方法、スキル習得、キャリア開発、教育技術などについて、
        科学的根拠に基づいた実践的なアドバイスを提供してください。
        具体的な学習計画や教材推奨も含めて回答してください。"""
    
    try:
        # LangChainを使用してOpenAI APIを呼び出し
        from langchain_openai import ChatOpenAI
        from langchain.schema import HumanMessage, SystemMessage
        
        # ChatOpenAIインスタンスを作成
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7
        )
        
        # メッセージを作成
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=question)
        ]
        
        # LLMに送信して回答を取得
        response = llm.invoke(messages)
        return response.content
        
    except Exception as e:
        return f"エラーが発生しました: {str(e)}\n\nOpenAI APIキーが正しく設定されているか確認してください。"

# 相談ボタン
if st.button("🤖 相談する", type="primary"):
    if user_question.strip():
        # レスポンス用のコンテナを作成
        response_container = st.container()
        
        with st.spinner("専門家が回答を考えています..."):
            response = get_expert_response(expert_type, user_question)
        
        # コンテナ内に結果を表示
        with response_container:
            st.markdown("## 💡 専門家からの回答")
            st.markdown(f"**選択した専門家:** {expert_type}")
            st.markdown("---")
            st.markdown(response)
        
    else:
        st.warning("質問を入力してください。")

# サイドバーに追加情報
st.sidebar.markdown("## ℹ️ 使用上の注意")
st.sidebar.markdown("""
- このアプリはOpenAI APIを使用しています
- 質問内容によっては回答に時間がかかる場合があります
- 専門的な内容については、必要に応じて実際の専門家にも相談することをお勧めします
""")

st.sidebar.markdown("## 🔧 技術仕様")
st.sidebar.markdown("""
- **フレームワーク:** Streamlit
- **AI技術:** OpenAI GPT-3.5-turbo
- **言語:** Python 3.12
- **ライブラリ:** LangChain, python-dotenv
""")