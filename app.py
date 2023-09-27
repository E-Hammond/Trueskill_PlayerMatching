import streamlit as st
import base64
from skills import random_match,skill_match,update_player_ratings
import pandas as pd


def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack('pexels-ketut-subiyanto-4132411.jpg')

st.markdown(f'<h1 style="color:#FFFFFF;font-size:40px;margin-left:100px">{"PLAYER MATCHING APP"}</h1>',
                unsafe_allow_html=True)
# st.title('PLAYER MATCHING APP')
st.sidebar.write('Select a set of indicators from the list below and click on the Predict button to make predictions.')
st.write('Select a set of indicators from the list below and click on the Predict button to make predictions.')
st.write('')
st.write('')


username,password = st.columns(2)
userid = username.text_input('Username', help='Enter username')
password = password.text_input('Password', help='Enter password')
login = st.button('Login')


st.write('Select a set of indicators from the list below and click on the Predict button to make predictions.')


# st.markdown(f'<h1 style="color:#FFFFFF;font-size:17px;">{"Select a set of indicators from the list below and click on the Predict button to make predictions."}</h1>',
#                 unsafe_allow_html=True)

df = pd.read_csv('data.csv')

l,r= st.columns(2)

if l.button('Random Match'):
    st.write(random_match(userid,df))

if r.button('Skill Match'):
    st.write(skill_match(userid,df))

st.write('')
st.write('')

results, result_button,rr = st.columns([6,1.5,1.2])
result_button.selectbox('',('win','lose','draw'))
results.write('Select a set of indicators from the list below and click on the Predict button to make predictions.')
rr.button('Submit')




