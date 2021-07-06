import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd



html_header="""
<head>
<title>PControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="project control, dashboard, management, EVA">
<meta name="description" content="project control dashboard">
<meta name="author" content="Larry Prato">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#008080; font-family:Georgia"> PROJECT CONTROL <br>
 <h2 style="color:#008080; font-family:Georgia"> DASHBOARD</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""
st.set_page_config(page_title="Project Control Dashboard", page_icon="", layout="wide")
st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
data=pd.read_excel('curva.xlsx')

html_card_header1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Global Actual Progress</h3>
  </div>
</div>
"""
html_card_footer1="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Baseline 46%</p>
  </div>
</div>
"""
html_card_header2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Global Spend Hours</h3>
  </div>
</div>
"""
html_card_footer2="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Baseline 92.700</p>
  </div>
</div>
"""
html_card_header3="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">TCPI</h3>
  </div>
</div>
"""
html_card_footer3="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">To Complete Performance Index ≤ 1.00</p>
  </div>
</div>
"""
### Block 1#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,15,1,15,1,15,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header1, unsafe_allow_html=True)
        fig_c1 = go.Figure(go.Indicator(
            mode="number+delta",
            value=35,
            number={'suffix': "%", "font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
            delta={'position': "bottom", 'reference': 46, 'relative': False},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c1.update_layout(autosize=False,
                             width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#fbfff0", font={'size': 20})
        st.plotly_chart(fig_c1)
        st.markdown(html_card_footer1, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header2, unsafe_allow_html=True)
        fig_c2 = go.Figure(go.Indicator(
            mode="number+delta",
            value=73500,
            number={'suffix': " HH", "font": {"size": 40, 'color': "#008080", 'family': "Arial"}, 'valueformat': ',f'},
            delta={'position': "bottom", 'reference': 92700},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c2.update_layout(autosize=False,
                             width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#fbfff0", font={'size': 20})
        fig_c2.update_traces(delta_decreasing_color="#3D9970",
                             delta_increasing_color="#FF4136",
                             delta_valueformat='f',
                             selector=dict(type='indicator'))
        st.plotly_chart(fig_c2)
        st.markdown(html_card_footer2, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        st.markdown(html_card_header3, unsafe_allow_html=True)
        fig_c3 = go.Figure(go.Indicator(
            mode="number+delta",
            value=1.085,
            number={"font": {"size": 40, 'color': "#008080", 'family': "Arial"}},
            delta={'position': "bottom", 'reference': 1, 'relative': False},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c3.update_layout(autosize=False,
                             width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#fbfff0", font={'size': 20})
        fig_c3.update_traces(delta_decreasing_color="#3D9970",
                             delta_increasing_color="#FF4136",
                             delta_valueformat='.3f',
                             selector=dict(type='indicator'))
        st.plotly_chart(fig_c3)
        st.markdown(html_card_footer3, unsafe_allow_html=True)
    with col7:
        st.write("")
html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)


html_card_header4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 250px;
   height: 50px;">
    <h4 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 10px 0;">Global Actual Progress</h4>
  </div>
</div>
"""
html_card_footer4="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value (%)</p>
  </div>
</div>
"""
html_card_header5="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 250px;
   height: 50px;">
    <h4 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 10px 0;">Global Spend Hours</h4>
  </div>
</div>
"""
html_card_footer5="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Relative Change (%)</p>
  </div>
</div>
"""


### Block 2#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,10,1,10,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header4, unsafe_allow_html=True)
        x = ['Actual', 'Previous', 'Average', 'Planned']
        y = [5.5, 4.2, 6.3, 8.5]
        fig_m_prog = go.Figure([go.Bar(x=x, y=y, text=y, textposition='auto')])
        fig_m_prog.update_layout(paper_bgcolor="#fbfff0", plot_bgcolor="#fbfff0",
                                 font={'color': "#008080", 'family': "Arial"}, height=100, width=250,
                                 margin=dict(l=15, r=1, b=4, t=4))
        fig_m_prog.update_yaxes(title='y', visible=False, showticklabels=False)
        fig_m_prog.update_traces(marker_color='#17A2B8', selector=dict(type='bar'))
        st.plotly_chart(fig_m_prog)
        st.markdown(html_card_footer4, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header5, unsafe_allow_html=True)
        x = ['Δ vs Prev', 'Δ vs Aver', 'Δ vs Plan']
        y = [10, 12, 8]
        fig_m_hh = go.Figure([go.Bar(x=x, y=y, text=y, textposition='auto')])
        fig_m_hh.update_layout(paper_bgcolor="#fbfff0", plot_bgcolor="#fbfff0",
                               font={'color': "#008080", 'family': "Arial"}, height=100, width=250,
                               margin=dict(l=15, r=1, b=1, t=1))
        fig_m_hh.update_yaxes(title='y', visible=False, showticklabels=False)
        fig_m_hh.update_traces(marker_color='#17A2B8', selector=dict(type='bar'))
        st.plotly_chart(fig_m_hh)
        st.markdown(html_card_footer5, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        y = data.loc[data.Activity_name == 'Total']
        # Create traces
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=y['Date'], y=y['Progress'],
                                  mode='lines',
                                  name='Progress',
                                  marker_color='#FF4136'))
        fig3.add_trace(go.Scatter(x=y['Date'], y=y['Baseline'],
                                  mode='lines',
                                  name='Baseline',
                                  marker_color='#17A2B8'))
        fig3.update_layout(title={'text': "Actual Progress vs Planned", 'x': 0.5}, paper_bgcolor="#fbfff0",
                           plot_bgcolor="#fbfff0", font={'color': "#008080", 'size': 12, 'family': "Georgia"}, height=220,
                           width=540,
                           legend=dict(orientation="h",
                                       yanchor="top",
                                       y=0.99,
                                       xanchor="left",
                                       x=0.01),
                           margin=dict(l=1, r=1, b=1, t=30))
        fig3.update_xaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=6, rangemode="tozero",
                          showgrid=False, gridwidth=0.5, gridcolor='#F7F7F7')
        fig3.update_yaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=10, rangemode="tozero",
                          showgrid=True, gridwidth=0.5, gridcolor='#F7F7F7')
        fig3.layout.yaxis.tickformat = ',.0%'
        st.plotly_chart(fig3)
    with col7:
        st.write("")

html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_card_header6="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 250px;
   height: 50px;">
    <h4 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 10px 0;">Cost Variance</h4>
  </div>
</div>
"""
html_card_footer6="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value </p>
  </div>
</div>
"""
html_card_header7="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 250px;
   height: 50px;">
    <h4 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 10px 0;">Schedule Variance</h4>
  </div>
</div>
"""
html_card_footer7="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value</p>
  </div>
</div>
"""

### Block 3#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,10,1,10,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header6, unsafe_allow_html=True)
        fig_cv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=1.05,
            number={"font": {"size": 22, 'color': "#008080", 'family': "Arial"}, "valueformat": "#,##0"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "#06282d"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 1], 'color': '#FF4136'},
                    {'range': [1, 1.5], 'color': '#3D9970'}]}))

        fig_cv.update_layout(paper_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Arial"}, height=135, width=250,
                             margin=dict(l=10, r=10, b=15, t=20))
        st.plotly_chart(fig_cv)
        st.markdown(html_card_footer6, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header7, unsafe_allow_html=True)
        fig_sv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=0.95,
            number={"font": {"size": 22, 'color': "#008080", 'family': "Arial"}, "valueformat": "#,##0"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "#06282d"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 1], 'color': '#FF4136'},
                    {'range': [1, 1.5], 'color': '#3D9970'}]}))
        fig_sv.update_layout(paper_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Arial"}, height=135, width=250,
                             margin=dict(l=10, r=10, b=15, t=20))
        st.plotly_chart(fig_sv)
        st.markdown(html_card_footer7, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        y = data.loc[data.Activity_name == 'Total']
        y = data.loc[data.Activity_name == 'Total']
        fig_hh = go.Figure()
        fig_hh.add_trace(go.Bar(
            x=y['Date'],
            y=y['Spend_Hours'],
            name='Spend Hours',
            marker_color='#FF4136'
        ))
        fig_hh.add_trace(go.Bar(
            x=y['Date'],
            y=y['Planned_Hours'],
            name='Planned Hours',
            marker_color='#17A2B8'
        ))
        fig_hh.update_layout(barmode='group', title={'text': 'Spend Hours vs Planned', 'x': 0.5}, paper_bgcolor="#fbfff0",
                             plot_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Georgia"}, height=250, width=540,
                             legend=dict(orientation="h",
                                         yanchor="top",
                                         y=0.99,
                                         xanchor="left",
                                         x=0.01),
                             margin=dict(l=5, r=1, b=1, t=25))
        fig_hh.update_xaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=6, rangemode="tozero",
                            showgrid=False, gridwidth=0.5, gridcolor='#F7F7F7')
        fig_hh.update_yaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=10, rangemode="tozero",
                            showgrid=False, gridwidth=0.5, gridcolor='#F7F7F7')
        st.plotly_chart(fig_hh)
    with col7:
        st.write("")

html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_subtitle="""
<h2 style="color:#008080; font-family:Georgia;"> Details by Discipline: </h2>
"""
st.markdown(html_subtitle, unsafe_allow_html=True)

html_table=""" 
<table>
  <tr style="background-color:#eef9ea; color:#008080; font-family:Georgia; font-size: 15px">
    <th style="width:130px">Discipline</th>
    <th style="width:90px">Baseline</th>
    <th style="width:90px">Progress</th>
    <th style="width:90px">Manpower</th>
    <th style="width:90px">Cost Variance</th>
    <th style="width:90px">Schedule Variance</th>
  </tr>
  <tr style="height: 40px; color:#008080; font-size: 14px">
    <th>Civil</th>
    <th>70,00%</th>
    <th>68,50%</th>
    <th>70.000</th>
    <th>0,99</th>
    <th>1,09</th>
  </tr>
  <tr style="background-color:#eef9ea; height: 40px; color:#008080; font-size: 14px">
    <th>Mechanical</th>
    <th>50,00%</th>
    <th>45,50%</th>
    <th>10.000</th>
    <th>0,95</th>
    <th>0,98</th>
  </tr>
  <tr style="height: 40px; color:#008080; font-size: 14px">
    <th>Piping</th>
    <th>30,00%</th>
    <th>30,00%</th>
    <th>60.000</th>
    <th>0,99</th>
    <th>1,01</th>
  </tr>
  <tr style="background-color:#eef9ea; height: 40px; color:#008080; font-size: 14px">
    <th>Electricity</th>
    <th>20,00%</th>
    <th>15,00%</th>
    <th>40.000</th>
    <th>0,90</th>
    <th>0,98</th>
  </tr>
  <tr style="height: 40px; color:#008080; font-size: 14px">
    <th>Intrumentation</th>
    <th>5,00%</th>
    <th>0,00%</th>
    <th>30.000</th>
    <th>-</th>
    <th>-</th>
  </tr>
  <tr style="background-color:#eef9ea; height: 40px; color:#008080; font-size: 14px">
    <th>Commissioning</th>
    <th>0,00%</th>
    <th>0,00%</th>
    <th>15.000</th>
    <th>-</th>
    <th>-</th>
  </tr>
  <tr style="height: 40px; color:#008080; font-size: 15px">
    <th>Total</th>
    <th>35,00%</th>
    <th>46,00%</th>
    <th>225.000</th>
    <th>0,97</th>
    <th>0,91</th>
  </tr>
</table>
"""
### Block 4#########################################################################################
with st.beta_container():
    col1, col2, col3 = st.beta_columns([12,1,12])
    with col1:
        st.markdown(html_table, unsafe_allow_html=True)
    with col2:
        st.write("")
    with col3:
        # *******Gantt Chart
        df = pd.DataFrame([
            dict(Disc="Civ", Start='2021-01-04', Finish='2021-08-10'),
            dict(Disc="Mec", Start='2021-03-05', Finish='2021-09-15'),
            dict(Disc="Pip", Start='2021-04-20', Finish='2021-11-30'),
            dict(Disc="Ele", Start='2021-05-20', Finish='2021-12-05'),
            dict(Disc="Ins", Start='2021-06-20', Finish='2021-12-20'),
            dict(Disc="Com", Start='2021-07-20', Finish='2021-12-30')
        ])
        fig2 = px.timeline(df, x_start="Start", x_end="Finish", y='Disc')
        fig2.update_yaxes(autorange="reversed")
        fig2.update_layout(title={'text': "Main dates", 'x': 0.5}, plot_bgcolor="#eef9ea", paper_bgcolor="#eef9ea",
                           font={'color': "#008080", 'family': "Georgia"}, height=340, width=550, margin=dict(
                l=51, r=5, b=10, t=50))
        fig2.update_traces(marker_color='#17A2B8', selector=dict(type='bar'))
        st.plotly_chart(fig2)

disciplinas= ['Civil', 'Mechanical', 'Piping', 'Electricity', 'Instrumentation', 'Commissioning']

selected_disc = st.selectbox(' Select discipline', disciplinas)
html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_card_header4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 10px; width: 250px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 5px 0;">Progress For Selected Discipline</h5>
  </div>
</div>
"""
html_card_footer4="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value (%)</p>
  </div>
</div>
"""
html_card_header5="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 10px; width: 250px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 5px 0;">Spend Hours For Selected Discipline</h5>
  </div>
</div>
"""
html_card_footer5="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Relative Change (%)</p>
  </div>
</div>
"""


### Block 5#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,10,1,10,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header4, unsafe_allow_html=True)
        x = ['Actual', 'Previous', 'Average', 'Planned']
        y = [5.5, 4.2, 6.3, 8.5]
        fig_m_prog = go.Figure([go.Bar(x=x, y=y, text=y, textposition='auto')])
        fig_m_prog.update_layout(paper_bgcolor="#fbfff0", plot_bgcolor="#fbfff0",
                                 font={'color': "#008080", 'family': "Arial"}, height=100, width=250,
                                 margin=dict(l=15, r=1, b=4, t=4))
        fig_m_prog.update_yaxes(title='y', visible=False, showticklabels=False)
        fig_m_prog.update_traces(marker_color='#17A2B8', selector=dict(type='bar'))
        st.plotly_chart(fig_m_prog)
        st.markdown(html_card_footer4, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header5, unsafe_allow_html=True)
        x = ['Δ vs Prev', 'Δ vs Aver', 'Δ vs Plan']
        y = [10, 12, 8]
        fig_m_hh = go.Figure([go.Bar(x=x, y=y, text=y, textposition='auto')])
        fig_m_hh.update_layout(paper_bgcolor="#fbfff0", plot_bgcolor="#fbfff0",
                               font={'color': "#008080", 'family': "Arial"}, height=100, width=250,
                               margin=dict(l=15, r=1, b=1, t=1))
        fig_m_hh.update_yaxes(title='y', visible=False, showticklabels=False)
        fig_m_hh.update_traces(marker_color='#17A2B8', selector=dict(type='bar'))
        st.plotly_chart(fig_m_hh)
        st.markdown(html_card_footer5, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        y = data.loc[data.Activity_name == 'Total']
        # Create traces
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=y['Date'], y=y['Progress'],
                                  mode='lines',
                                  name='Progress',
                                  marker_color='#FF4136'))
        fig3.add_trace(go.Scatter(x=y['Date'], y=y['Baseline'],
                                  mode='lines',
                                  name='Baseline',
                                  marker_color='#17A2B8'))
        fig3.update_layout(title={'text': "Actual Progress vs Planned", 'x': 0.5}, paper_bgcolor="#fbfff0",
                           plot_bgcolor="#fbfff0", font={'color': "#008080", 'size': 12, 'family': "Georgia"}, height=220,
                           width=540,
                           legend=dict(orientation="h",
                                       yanchor="top",
                                       y=0.99,
                                       xanchor="left",
                                       x=0.01),
                           margin=dict(l=1, r=1, b=1, t=30))
        fig3.update_xaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=6, rangemode="tozero",
                          showgrid=False, gridwidth=0.5, gridcolor='#F7F7F7')
        fig3.update_yaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=10, rangemode="tozero",
                          showgrid=True, gridwidth=0.5, gridcolor='#F7F7F7')
        fig3.layout.yaxis.tickformat = ',.0%'
        st.plotly_chart(fig3)
    with col7:
        st.write("")

html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_card_header6="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 10px; width: 250px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 5px 0;">Cost Variance For Selected Discipline</h5>
  </div>
</div>
"""
html_card_footer6="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value </p>
  </div>
</div>
"""
html_card_header7="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 250px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 8px 0;">Schedule Variance For Selected Discipline</h5>
  </div>
</div>
"""
html_card_footer7="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value</p>
  </div>
</div>
"""
html_card_header8="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 550px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 10px 0;">Main Issues By Discipline</h5>
  </div>
</div>
"""

html_list="""
<ul style="color:#008080; font-family:Georgia; font-size: 15px">
  <li>Nulla volutpat aliquam velit</li>
  <li>Maecenas sed diam eget risus varius blandit</li>
  <li>Etiam porta sem malesuada magna mollis euismod</li>
  <li>Fusce dapibus, tellus ac cursus commodo</li>
  <li>Maecenas sed diam eget risus varius blandit</li>
</ul> 
"""

### Block 6#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,10,1,10,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header6, unsafe_allow_html=True)
        fig_cv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=1.05,
            number={"font": {"size": 22, 'color': "#008080", 'family': "Arial"}, "valueformat": "#,##0"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "#06282d"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 1], 'color': '#FF4136'},
                    {'range': [1, 1.5], 'color': '#3D9970'}]}))

        fig_cv.update_layout(paper_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Arial"}, height=135, width=250,
                             margin=dict(l=10, r=10, b=15, t=20))
        st.plotly_chart(fig_cv)
        st.markdown(html_card_footer6, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header7, unsafe_allow_html=True)
        fig_sv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=0.95,
            number={"font": {"size": 22, 'color': "#008080", 'family': "Arial"}, "valueformat": "#,##0"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "#06282d"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 1], 'color': '#FF4136'},
                    {'range': [1, 1.5], 'color': '#3D9970'}]}))
        fig_sv.update_layout(paper_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Arial"}, height=135, width=250,
                             margin=dict(l=10, r=10, b=15, t=20))
        st.plotly_chart(fig_sv)
        st.markdown(html_card_footer7, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        st.markdown(html_card_header8, unsafe_allow_html=True)
        st.markdown(html_list, unsafe_allow_html=True)
    with col7:
        st.write("")

html_line="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<p style="color:Gainsboro; text-align: right;">By: larryprato@gmail.com</p>
"""
st.markdown(html_line, unsafe_allow_html=True)
