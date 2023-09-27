import streamlit as st
import base64
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

set_bg_hack('Trueskill_PlayerMatching/pexels-roman-odintsov-12718982.jpg')

st.markdown(f'<h1 style="color:#F65454;font-size:40px;margin-left:100px">{"PLAYER MATCHING APP"}</h1>',
                unsafe_allow_html=True)
# st.title('PLAYER MATCHING APP')
st.sidebar.markdown('Select a set of indicators from the list below and click on the Predict button to make predictions.')
st.markdown(f'<h1 style="color:#FFFFFF;font-size:17px;">{"Select a set of indicators from the list below and click on the Predict button to make predictions."}</h1>',
                unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')

username,password = st.columns(2)
userid = username.text_input('Username', help='Enter the charge paid by customer per month')
password = password.text_input('Password', help='Enter the charge paid by customer per month')



