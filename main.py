import streamlit as st
import pandas as pd
import numpy as np
# cSpell:disable

st.title("Streamlit Projects")

df=pd.DataFrame({
    'name':['Alice','Bob','Charlie'],
    'age':[25,30,35],
    'city':['New York','Los Angeles','Chicago']
})

# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0))

# st.table(df)

st.write('DataFrame with Streamlit')

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# ```

# ```python
# import pandas as pd
# ```

# ```python
# import numpy as np
# ```
# """

# df=pd.DataFrame(
#   np.random.rand(10,5),
#   columns=['a','b','c','d','e']
#   )
# df

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.scatter_chart(df)



df=pd.DataFrame(
  np.random.rand(10,2)/[10,10] + [33.5577,130.1958],
  columns=['lat','lon']
  )

if st.checkbox('Show Map'):
  st.map(df)

option = st.selectbox('Select a city', ['New York', 'Los Angeles', 'Chicago'])
'You selected:' ,option

# text = st.text_input('Enter your name')
# 'You entered:' ,text

# ... existing code ...

# コンテナを作成
text_container = st.empty()

# セッション状態を初期化
if 'input_text' not in st.session_state:
    st.session_state.input_text = ''

# ... existing code ...

# セッション状態を初期化
# if 'form_submitted' not in st.session_state:
#     st.session_state.form_submitted = False

# with st.form("text_form", clear_on_submit=True):
#     text = st.text_input('Enter your name', key="text_input")
#     submitted = st.form_submit_button("↩️で決定")
    
#     if submitted and text:
#         st.write('You entered:', text)
#         st.session_state.form_submitted = True

# condition=st.slider('Select a value', 0, 100, 50)
# 'You selected:', condition

# activate = st.sidebar.toggle('Activate')
# st.sidebar.write('You selected:', activate)
# st.write('You selected:', activate)

left_column, middle_column, right_column = st.columns(3)
button = left_column.button('Click me')
if button:
    right_column.write('Right')
    middle_column.write('Middle')

expander = st.expander('Expander')
expander.write('This is a expander')


# チャット履歴を初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャット入力
prompt = st.chat_input("指示を出して下さい")
if prompt:
    # ユーザーのメッセージを追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # アシスタントの応答を追加
    response = f"指示は'{prompt}'ですね"
    st.session_state.messages.append({"role": "assistant", "content": response})

# チャット履歴を表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



