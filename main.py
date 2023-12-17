import streamlit as st
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.1)

'Done!!'

option = st.selectbox(
    'あなたが好きな数字を指定していください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション：', condition