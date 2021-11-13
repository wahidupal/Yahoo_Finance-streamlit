import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import plotly.graph_objects as go


def load_data():
    """Function for loading data"""
    df = pd.read_csv("stock.csv", index_col="Date")

    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    stock_column = df['company_name']

    unique_stocks = stock_column.unique()

    return df, numeric_cols, text_cols, unique_stocks


df, numeric_cols, text_cols, unique_stocks = load_data()


# Title of dashboard
st.title("Stock Dashboard")


# add checknob to sidebar
check_box = st.sidebar.checkbox(label="Display dataset")

if check_box:
    # lets show the dataset
    st.write(df)

# give sidebar a title
st.sidebar.title("Fixture")
st.sidebar.subheader("Timeline Fixture")
feature_selection = st.sidebar.multiselect(label="Features to plot",
                                           options=numeric_cols)

stock_dropdown = st.sidebar.selectbox(label="Company",
                                      options=unique_stocks)

print(feature_selection)

df = df[df['company_name']==stock_dropdown]
df_features = df[feature_selection]

chart_select= st.sidebar.selectbox(
                    label='Select the chart type',
                    
                     options=['Scatterplots','Lineplot','Histogram','Boxplot','Barchart'])
#global ploty_figure

if chart_select =='Scatterplots':
    
    plotly_figure = px.scatter(data_frame=df_features,
                            x=df_features.index,y=feature_selection,
                            title=(str(stock_dropdown) + ' ' +'timeline')
                            )
    st.plotly_chart(plotly_figure)  

elif chart_select =='Lineplot':
    plotly_figure = px.line(data_frame=df_features,
                            x=df_features.index,y=feature_selection,
                            title=(str(stock_dropdown) + ' ' +'timeline')
                            )
    st.plotly_chart(plotly_figure)  

elif chart_select =='Histogram':
    plotly_figure = px.histogram(data_frame=df_features,
                            x=df_features.index,y=feature_selection,
                            title=(str(stock_dropdown) + ' ' +'timeline')
                            )
    st.plotly_chart(plotly_figure)

elif chart_select =='Boxplot':
    plotly_figure = px.box(data_frame=df_features,
                            x=df_features.index,y=feature_selection,
                            title=(str(stock_dropdown) + ' ' +'timeline')
                            )
    st.plotly_chart(plotly_figure)

elif chart_select =='Barchart':
    plotly_figure = px.bar(data_frame=df_features,
                            x=df_features.index,y=feature_selection,
                            title=(str(stock_dropdown) + ' ' +'timeline')
                            )
    st.plotly_chart(plotly_figure)