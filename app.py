# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:42:54 2022

@author: mike
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# df = pd.read_csv(")
# df_block_1 = df[['model_label_1', 'score_1']]
# df_block_1.columns = ['label', 'score']
# df_block_2 = df[['model_label_2', 'score_2']]
# df_block_2.columns = ['label', 'score']
# df_unfold = pd.concat([df_block_1,df_block_2])

# threshhold = 0.5

# df_filt = df_unfold[df_unfold['score'] >= threshhold]

# ##### vis ######

# df_filt_count = df_filt.groupby('label').count().reset_index()

# # create dataset
# height = list(df_filt_count['score'])
# bars = tuple(df_filt_count['label'])
# x_pos = np.arange(len(bars))

# # Create bars and choose color
# plt.bar(x_pos, height, color = (0.5,0.1,0.5,0.6))
 
# # Add title and axis names
# plt.title('Count of Labels in Dataset')
# plt.xlabel('categories')
# plt.xticks(rotation=90)
# plt.ylabel('Count')
 
# # Create names on the x axis
# plt.xticks(x_pos, bars)
 
# # Show graph
# plt.show()

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    
    ##############
    #PHASE 1 Login
    ##############
    
    st.sidebar.image('data:image/png;base64,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')
    uploaded_file = None
    st.title("McCrindle Visualisation of Qual Outputs")
    
    #processing 
    uploaded_file = st.file_uploader("Upload label output from Qual App", type = ['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df_block_1 = df[['model_label_1', 'score_1']]
        df_block_1.columns = ['label', 'score']
        df_block_2 = df[['model_label_2', 'score_2']]
        df_block_2.columns = ['label', 'score']
        df_unfold = pd.concat([df_block_1,df_block_2])
    
        threshhold =  st.slider('Set threshhold level', 0.0, 1.0, 0.3)
        df_filt = df_unfold[df_unfold['score'] >= threshhold]
    
        ##### vis ######
        
        df_filt_count = df_filt.groupby('label').count().reset_index()
        # create dataset
        height = list(df_filt_count['score'])
        bars = tuple(df_filt_count['label'])
        
        fig, _ = plt.subplots(figsize =(12, 8))
        x_pos = np.arange(len(bars))
    
        # Create bars and choose color
        plt.bar(x_pos, height, color = (0.5,0.1,0.5,0.6))
         
        # Add title and axis names
        plt.title('Count of Labels in Dataset')
        plt.xlabel('categories')
        plt.xticks(rotation=90)
        plt.ylabel('Count')
         
        # Create names on the x axis
        plt.xticks(x_pos, bars)
    
        # Show graph
        st.pyplot(fig)
    
    
    
    
