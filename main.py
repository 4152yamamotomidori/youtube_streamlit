import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'start!!'
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1) # 0.1秒時間をとめる

'Done!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


expander=st.expander('問い合わせ1')
expander.write('問い合わせの回答1')
# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'あなたの趣味：',text
# 'コンディション：',condition

# if st.checkbox('Show Image'):
#     img=Image.open('IMG_0008.JPG')
#     st.image(img, caption='KANON', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)
# # st.line_chart(df)
# # st.bar_chart(df)





# st.table(df.style.highlight_max(axis=0))


#以下マジックコマンド
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """