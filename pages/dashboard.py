import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide", page_title="Analitik Dashboard")

st.title("📊 Analitik Dashboard")
st.subheader("Temizlik Hizmetleri Veri Analizi")

def load_data():
    try:
        df = pd.read_csv("cleaning_scopes.csv")
        if 'Oluşturma Tarihi' in df.columns:
            df['Oluşturma Tarihi'] = pd.to_datetime(df['Oluşturma Tarihi'])
        return df
    except FileNotFoundError:
        st.warning("⚠️ Henüz veri bulunmuyor. Önce kapsam oluşturun.")
        return None

# Ana metrikler
def show_metrics(df):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_scopes = len(df)
        st.metric("Toplam Kapsam", total_scopes)
    
    with col2:
        if 'Oluşturma Tarihi' in df.columns:
            last_30_days = datetime.now() - timedelta(days=30)
            recent_scopes = len(df[df['Oluşturma Tarihi'] > last_30_days])
            st.metric("Son 30 Gün", recent_scopes)
        else:
            st.metric("Son 30 Gün", "N/A")
    
    with col3:
        if 'Hizmet Sıklığı' in df.columns:
            most_common_freq = df['Hizmet Sıklığı'].mode().iloc[0] if not df['Hizmet Sıklığı'].mode().empty else "N/A"
            st.metric("En Yaygın Sıklık", most_common_freq)
        else:
            st.metric("En Yaygın Sıklık", "N/A")
    
    with col4:
        if 'Şirket Adı' in df.columns:
            unique_companies = df['Şirket Adı'].nunique()
            st.metric("Farklı Şirket", unique_companies)
        else:
            st.metric("Farklı Şirket", "N/A")

# Veri görselleştirmeleri
def show_visualizations(df):
    if df is None or len(df) == 0:
        return
        
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 Hizmet Sıklığı Dağılımı")
        if 'Hizmet Sıklığı' in df.columns:
            freq_counts = df['Hizmet Sıklığı'].value_counts()
            fig = px.bar(x=freq_counts.index, y=freq_counts.values,
                        labels={'x': 'Sıklık', 'y': 'Sayı'})
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📅 Aylık Kapsam Oluşturma")
        if 'Oluşturma Tarihi' in df.columns:
            monthly_data = df.groupby(df['Oluşturma Tarihi'].dt.to_period('M')).size()
            fig = px.line(x=monthly_data.index.astype(str), y=monthly_data.values,
                         labels={'x': 'Ay', 'y': 'Kapsam Sayısı'})
            st.plotly_chart(fig, use_container_width=True)
    
    # Zaman serisi
    if 'Oluşturma Tarihi' in df.columns:
        st.subheader("⏰ Zaman İçindeki Aktivite")
        daily_data = df.groupby(df['Oluşturma Tarihi'].dt.date).size().reset_index()
        daily_data.columns = ['Tarih', 'Sayı']
        
        fig = px.scatter(daily_data, x='Tarih', y='Sayı',
                        trendline="rolling", trendline_options=dict(window=3),
                        labels={'Tarih': 'Tarih', 'Sayı': 'Günlük Kapsam'})
        st.plotly_chart(fig, use_container_width=True)

# En popüler hizmetler
def show_popular_services(df):
    if df is None or len(df) == 0:
        return
        
    st.subheader("🔥 En Popüler Temizlik Görevleri")
    
    service_columns = [col for col in df.columns if any(area in col for area in 
                                                       ['Resepsiyon', 'Ofis', 'Mutfak', 'Tuvalet'])]
    
    if service_columns:
        service_counts = {}
        for col in service_columns:
            if col in df.columns:
                counts = df[col][df[col] != 'Dahil Değil'].value_counts()
                for service, count in counts.items():
                    key = f"{col}: {service}"
                    service_counts[key] = service_counts.get(key, 0) + count
        
        if service_counts:
            sorted_services = sorted(service_counts.items(), key=lambda x: x[1], reverse=True)
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                services_df = pd.DataFrame(sorted_services[:10], columns=['Hizmet', 'Talep Sayısı'])
                st.dataframe(services_df, use_container_width=True)
            
            with col2:
                top_5 = dict(sorted_services[:5])
                fig = px.pie(values=list(top_5.values()), names=list(top_5.keys()),
                           title="Top 5 Hizmet")
                st.plotly_chart(fig, use_container_width=True)

# Veri tablosu
def show_data_table(df):
    if df is None or len(df) == 0:
        return
        
    st.subheader("📋 Tüm Kapsam Verileri")
    
    # Filtreleme seçenekleri
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Hizmet Sıklığı' in df.columns:
            freq_filter = st.selectbox("Sıklığa göre filtrele", 
                                     ["Tümü"] + list(df['Hizmet Sıklığı'].unique()))
        else:
            freq_filter = "Tümü"
    
    with col2:
        if 'Şirket Adı' in df.columns:
            company_filter = st.selectbox("Şirkete göre filtrele",
                                        ["Tümü"] + list(df['Şirket Adı'].unique()))
        else:
            company_filter = "Tümü"
    
    # Filtrelenmiş veri
    filtered_df = df.copy()
    
    if freq_filter != "Tümü":
        filtered_df = filtered_df[filtered_df['Hizmet Sıklığı'] == freq_filter]
    
    if company_filter != "Tümü":
        filtered_df = filtered_df[filtered_df['Şirket Adı'] == company_filter]
    
    # Sadece önemli sütunları göster
    display_columns = ['Müşteri Adı', 'Şirket Adı', 'Hizmet Sıklığı', 'Başlangıç Tarihi', 'Oluşturma Tarihi']
    available_columns = [col for col in display_columns if col in filtered_df.columns]
    
    if available_columns:
        st.dataframe(filtered_df[available_columns], use_container_width=True)
    
    # CSV indirme
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.download_button(
            label="📥 CSV Olarak İndir",
            data=filtered_df.to_csv(index=False),
            file_name=f"temizlik_kapsamlari_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        ):
            st.success("✅ CSV dosyası indirildi!")

# Ana sayfa içeriği
df = load_data()

if df is not None and len(df) > 0:
    show_metrics(df)
    st.markdown("---")
    show_visualizations(df)
    st.markdown("---")
    show_popular_services(df)
    st.markdown("---")
    show_data_table(df)
else:
    st.info("📊 Dashboard'ı kullanmaya başlamak için önce ana sayfadan kapsamlar oluşturun.")
    
    # Örnek metrikler
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Toplam Kapsam", "0")
    with col2:
        st.metric("Son 30 Gün", "0")
    with col3:
        st.metric("En Yaygın Sıklık", "-")
    with col4:
        st.metric("Farklı Şirket", "0")

# Sidebar
st.sidebar.header("🎛️ Dashboard Kontrolleri")
st.sidebar.write("Bu sayfada:")
st.sidebar.write("• Veri metrikleri")
st.sidebar.write("• Görselleştirmeler")
st.sidebar.write("• Popüler hizmetler")
st.sidebar.write("• Veri filtreleme")

col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("🏠 Ana Sayfa"):
        st.switch_page("app.py")
with col2:
    if st.button("🔄 Yenile"):
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.write("📈 Analitik Dashboard v1.0")