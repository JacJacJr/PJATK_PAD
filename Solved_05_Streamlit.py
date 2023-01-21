import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

st.set_page_config(layout = "wide")

page=st.sidebar.selectbox('Select page',['Poll', 'Stats'])

if page == 'Poll':
    st.title('Whats your name?')
    f_name=st.text_input('Enter your name')
    l_name=st.text_input('Enter your surname')
    if st.button('submit'):
        st.success(f'Welcome {f_name}!')

elif page == 'Stats':
    st.title("Let's explore some data")
    dataset = st.file_uploader("Upload your dataset [CSV only]", type=['csv'])
    if dataset is not None:
        st.text('Part of your data set:')
        df = pd.read_csv(dataset)
        st.dataframe(df.head(4))
        plot_choice=st.selectbox('Choose the plot type', ['bar', 'line'])
        col_df= df.columns.to_list()
        selected_col_df = st.multiselect("Select columns to plot", col_df)
        plot_data = df[selected_col_df]
        df=None
        if st.button('Confirm'):
            with st.spinner('Processing...'):
                if plot_choice=='bar':
                    st.bar_chart(plot_data)
                elif plot_choice=='line':
                    st.line_chart(plot_data)
                time.sleep(1)

    
