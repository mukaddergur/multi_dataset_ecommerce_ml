import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Ticaret Zekası", layout="wide")

@st.cache_data
def get_clean_data():
    df = pd.read_csv("data/customer_shopping_data.csv")
    df.columns = df.columns.str.strip().str.lower()
    df['total_amount'] = df['price'] * df['quantity']
    bins = [0, 18, 25, 35, 45, 60, 100]
    labels = ["0-18", "19-25", "26-35", "36-45", "46-60", "60+"]
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
    return df
df = get_clean_data()

st.title(" E-Ticaret Müşteri Analiz Paneli")
st.markdown("---")

m1, m2, m3 = st.columns(3)
m1.metric("Toplam Satış Hacmi", f"{df['total_amount'].sum():,.0f} TL")
m2.metric("Ortalama Sepet", f"{df['total_amount'].mean():.2f} TL")
m3.metric("En Çok Tercih Edilen", df['category'].mode()[0])
st.markdown("---")
st.subheader(" Hangi Yaş Grubu Ne Alıyor?")
age_cat_summary = df.groupby(['age_group', 'category'], observed=True).size().reset_index(name='islem_sayisi')
fig = px.bar(age_cat_summary, 
             x="age_group", 
             y="islem_sayisi", 
             color="category",
             title="Kategori Bazlı İşlem Dağılımı",
             barmode="group", 
             height=500,
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_layout(xaxis_title="Yaş Grubu", yaxis_title="İşlem Sayısı")
st.plotly_chart(fig, use_container_width=True)
with st.expander(" Yaş Gruplarının Favori Şampiyonlarını Gör"):
    top_cats = age_cat_summary.loc[age_cat_summary.groupby('age_group')['islem_sayisi'].idxmax()]
    st.table(top_cats.sort_values(by='age_group'))