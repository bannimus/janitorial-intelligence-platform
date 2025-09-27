import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Dil desteği - app.py ile aynı
LANGUAGES = {
    'tr': {
        'title': '📊 Analitik Dashboard',
        'subtitle': 'Temizlik Hizmetleri Veri Analizi',
        'no_data_warning': '⚠️ Henüz veri bulunmuyor. Önce kapsam oluşturun.',
        'total_scopes': 'Toplam Kapsam',
        'last_30_days': 'Son 30 Gün',
        'most_common_freq': 'En Yaygın Sıklık',
        'different_companies': 'Farklı Şirket',
        'service_freq_dist': '🏢 Hizmet Sıklığı Dağılımı',
        'monthly_creation': '📅 Aylık Kapsam Oluşturma',
        'activity_over_time': '⏰ Zaman İçindeki Aktivite',
        'popular_services': '🔥 En Popüler Temizlik Görevleri',
        'all_scope_data': '📋 Tüm Kapsam Verileri',
        'filter_by_freq': 'Sıklığa göre filtrele',
        'filter_by_company': 'Şirkete göre filtrele',
        'download_csv': '📥 CSV Olarak İndir',
        'csv_downloaded': '✅ CSV dosyası indirildi!',
        'start_using_dashboard': '📊 Dashboard\'ı kullanmaya başlamak için önce ana sayfadan kapsamlar oluşturun.',
        'sidebar_header': '🎛️ Dashboard Kontrolleri',
        'sidebar_content': 'Bu sayfada:',
        'data_metrics': 'Veri metrikleri',
        'visualizations': 'Görselleştirmeler',
        'popular_services_text': 'Popüler hizmetler',
        'data_filtering': 'Veri filtreleme',
        'main_page': '🏠 Ana Sayfa',
        'refresh': '🔄 Yenile',
        'dashboard_version': '📈 Analitik Dashboard v1.0',
        'na': 'N/A',
        'frequency': 'Sıklık',
        'count': 'Sayı',
        'month': 'Ay',
        'scope_count': 'Kapsam Sayısı',
        'date': 'Tarih',
        'daily_scope': 'Günlük Kapsam',
        'service': 'Hizmet',
        'demand_count': 'Talep Sayısı',
        'top_5_services': 'Top 5 Hizmet',
        'all': 'Tümü'
    },
    'en': {
        'title': '📊 Analytics Dashboard',
        'subtitle': 'Cleaning Services Data Analysis',
        'no_data_warning': '⚠️ No data found yet. Please create scopes first.',
        'total_scopes': 'Total Scopes',
        'last_30_days': 'Last 30 Days',
        'most_common_freq': 'Most Common Frequency',
        'different_companies': 'Different Companies',
        'service_freq_dist': '🏢 Service Frequency Distribution',
        'monthly_creation': '📅 Monthly Scope Creation',
        'activity_over_time': '⏰ Activity Over Time',
        'popular_services': '🔥 Most Popular Cleaning Tasks',
        'all_scope_data': '📋 All Scope Data',
        'filter_by_freq': 'Filter by frequency',
        'filter_by_company': 'Filter by company',
        'download_csv': '📥 Download as CSV',
        'csv_downloaded': '✅ CSV file downloaded!',
        'start_using_dashboard': '📊 To start using the Dashboard, first create scopes from the main page.',
        'sidebar_header': '🎛️ Dashboard Controls',
        'sidebar_content': 'On this page:',
        'data_metrics': 'Data metrics',
        'visualizations': 'Visualizations',
        'popular_services_text': 'Popular services',
        'data_filtering': 'Data filtering',
        'main_page': '🏠 Main Page',
        'refresh': '🔄 Refresh',
        'dashboard_version': '📈 Analytics Dashboard v1.0',
        'na': 'N/A',
        'frequency': 'Frequency',
        'count': 'Count',
        'month': 'Month',
        'scope_count': 'Scope Count',
        'date': 'Date',
        'daily_scope': 'Daily Scope',
        'service': 'Service',
        'demand_count': 'Demand Count',
        'top_5_services': 'Top 5 Services',
        'all': 'All'
    }
}

def get_text(key):
    lang = st.session_state.get('language', 'tr')
    return LANGUAGES[lang][key]

st.set_page_config(layout="wide", page_title=get_text('title'))

st.title(get_text('title'))
st.subheader(get_text('subtitle'))

def load_data():
    try:
        df = pd.read_csv("cleaning_scopes.csv")
        if 'Oluşturma Tarihi' in df.columns:
            df['Oluşturma Tarihi'] = pd.to_datetime(df['Oluşturma Tarihi'])
        return df
    except FileNotFoundError:
        st.warning(get_text('no_data_warning'))
        return None

# Ana metrikler
def show_metrics(df):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_scopes = len(df)
        st.metric(get_text('total_scopes'), total_scopes)

    with col2:
        if 'Oluşturma Tarihi' in df.columns:
            last_30_days = datetime.now() - timedelta(days=30)
            recent_scopes = len(df[df['Oluşturma Tarihi'] > last_30_days])
            st.metric(get_text('last_30_days'), recent_scopes)
        else:
            st.metric(get_text('last_30_days'), get_text('na'))

    with col3:
        if 'Hizmet Sıklığı' in df.columns:
            most_common_freq = df['Hizmet Sıklığı'].mode().iloc[0] if not df['Hizmet Sıklığı'].mode().empty else get_text('na')
            st.metric(get_text('most_common_freq'), most_common_freq)
        else:
            st.metric(get_text('most_common_freq'), get_text('na'))

    with col4:
        if 'Şirket Adı' in df.columns:
            unique_companies = df['Şirket Adı'].nunique()
            st.metric(get_text('different_companies'), unique_companies)
        else:
            st.metric(get_text('different_companies'), get_text('na'))

# Veri görselleştirmeleri
def show_visualizations(df):
    if df is None or len(df) == 0:
        return
        
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(get_text('service_freq_dist'))
        if 'Hizmet Sıklığı' in df.columns:
            freq_counts = df['Hizmet Sıklığı'].value_counts()
            fig = px.bar(x=freq_counts.index, y=freq_counts.values,
                        labels={'x': get_text('frequency'), 'y': get_text('count')})
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader(get_text('monthly_creation'))
        if 'Oluşturma Tarihi' in df.columns:
            monthly_data = df.groupby(df['Oluşturma Tarihi'].dt.to_period('M')).size()
            fig = px.line(x=monthly_data.index.astype(str), y=monthly_data.values,
                         labels={'x': get_text('month'), 'y': get_text('scope_count')})
            st.plotly_chart(fig, use_container_width=True)

    # Zaman serisi
    if 'Oluşturma Tarihi' in df.columns:
        st.subheader(get_text('activity_over_time'))
        daily_data = df.groupby(df['Oluşturma Tarihi'].dt.date).size().reset_index()
        daily_data.columns = [get_text('date'), get_text('count')]

        fig = px.scatter(daily_data, x=get_text('date'), y=get_text('count'),
                        trendline="rolling", trendline_options=dict(window=3),
                        labels={get_text('date'): get_text('date'), get_text('count'): get_text('daily_scope')})
        st.plotly_chart(fig, use_container_width=True)

# En popüler hizmetler
def show_popular_services(df):
    if df is None or len(df) == 0:
        return
        
    st.subheader(get_text('popular_services'))

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
                services_df = pd.DataFrame(sorted_services[:10], columns=[get_text('service'), get_text('demand_count')])
                st.dataframe(services_df, use_container_width=True)

            with col2:
                top_5 = dict(sorted_services[:5])
                fig = px.pie(values=list(top_5.values()), names=list(top_5.keys()),
                           title=get_text('top_5_services'))
                st.plotly_chart(fig, use_container_width=True)

# Veri tablosu
def show_data_table(df):
    if df is None or len(df) == 0:
        return
        
    st.subheader(get_text('all_scope_data'))

    # Filtreleme seçenekleri
    col1, col2 = st.columns(2)

    with col1:
        if 'Hizmet Sıklığı' in df.columns:
            freq_filter = st.selectbox(get_text('filter_by_freq'),
                                     [get_text('all')] + list(df['Hizmet Sıklığı'].unique()))
        else:
            freq_filter = get_text('all')

    with col2:
        if 'Şirket Adı' in df.columns:
            company_filter = st.selectbox(get_text('filter_by_company'),
                                        [get_text('all')] + list(df['Şirket Adı'].unique()))
        else:
            company_filter = get_text('all')
    
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
            label=get_text('download_csv'),
            data=filtered_df.to_csv(index=False),
            file_name=f"cleaning_scopes_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        ):
            st.success(get_text('csv_downloaded'))

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
    st.info(get_text('start_using_dashboard'))

    # Örnek metrikler
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(get_text('total_scopes'), "0")
    with col2:
        st.metric(get_text('last_30_days'), "0")
    with col3:
        st.metric(get_text('most_common_freq'), "-")
    with col4:
        st.metric(get_text('different_companies'), "0")

# Sidebar
st.sidebar.header(get_text('sidebar_header'))
st.sidebar.write(get_text('sidebar_content'))
st.sidebar.write(f"• {get_text('data_metrics')}")
st.sidebar.write(f"• {get_text('visualizations')}")
st.sidebar.write(f"• {get_text('popular_services_text')}")
st.sidebar.write(f"• {get_text('data_filtering')}")

col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button(get_text('main_page')):
        st.switch_page("app.py")
with col2:
    if st.button(get_text('refresh')):
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.write(get_text('dashboard_version'))