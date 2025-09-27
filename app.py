import streamlit as st
import pandas as pd
from datetime import datetime

# Dil desteği
LANGUAGES = {
    'tr': {
        'title': '🏢 Janitorial Service Intelligence Platform',
        'subtitle': 'Temizlik Hizmeti Kapsamı Oluşturma Formu',
        'customer_info': '👤 Müşteri Bilgileri',
        'cleaning_areas': '🧹 Temizlik Alanları ve Görevler',
        'special_req': '📝 Ek Bilgiler',
        'create_button': '🎯 Kapsamı Oluştur ve Kaydet',
        'pdf_button': '📋 Detaylı PDF Raporu Hazırla',
        'download_pdf': '📥 PDF Raporunu İndir',
        'success_message': '✅ Kapsam başarıyla mevcut verilere eklendi!',
        'new_file_message': '✅ Yeni kapsam dosyası oluşturuldu ve kaydedildi!',
        'error_message': '❌ Lütfen müşteri adı ve şirket adını doldurun!',
        'no_tasks': '⚠️ Hiç temizlik görevi seçilmedi!',
        'special_req_title': 'Özel Gereksinimler',
        'dashboard_button': '📊 Dashboard\'a Git',
        'navigation': '🧭 Navigasyon',
        'main_page': 'Ana Sayfa: Kapsam oluşturma formu',
        'dashboard_page': 'Dashboard: Veri analizi ve raporlar',
        'sidebar_title': '🧭 Navigasyon',
        'reception': '🏢 Resepsiyon Alanı',
        'office': '💼 Ofis Alanları',
        'kitchen': '🍽️ Mutfak (Staff Kitchen)',
        'toilet': '🚻 Tuvaletler',
        'floor_cleaning': 'Zemin temizliği',
        'dust_cleaning': 'Toz alma',
        'vacuum_cleaning': 'Süpürme/elektrik süpürgesi',
        'glass_cleaning': 'Cam temizliği',
        'desk_cleaning': 'Masa temizliği',
        'trash_cleaning': 'Çöp toplama',
        'disinfect_cleaning': 'Dezenfeksiyon',
        'supplies_cleaning': 'Sarf malzeme ikmali',
        'sanitary_cleaning': 'Hijyenik temizlik',
        'mirror_cleaning': 'Ayna temizliği',
        'fixtures_cleaning': 'Armatür temizliği',
        'tiles_cleaning': 'Fayans temizliği',
        'surfaces_cleaning': 'Tezgah temizliği',
        'appliances_cleaning': 'Cihaz temizliği',
        'fridge_cleaning': 'Buzdolabı temizliği',
        'microwave_cleaning': 'Mikrodalga temizliği',
        'dishwasher_cleaning': 'Bulaşık makinesi',
        'not_included': 'Dahil Değil',
        'daily': 'Günlük',
        'weekly': 'Haftalık',
        'monthly': 'Aylık',
        'biweekly': '2 Haftalık',
        'customer_name': 'Müşteri Adı',
        'company_name': 'Şirket Adı',
        'email': 'E-posta',
        'phone': 'Telefon',
        'address': 'Adres',
        'start_date': 'Hizmet Başlangıç Tarihi',
        'frequency': 'Hizmet Sıklığı',
        'requirements': 'Özel Gereksinimler',
        'name_placeholder': 'Müşteri adını girin',
        'company_placeholder': 'Şirket adını girin',
        'email_placeholder': 'ornek@email.com',
        'phone_placeholder': '0555 555 55 55',
        'address_placeholder': 'Tam adres bilgisini girin',
        'requirements_placeholder': 'Special cleaning requirements, points to consider...',
        'data_analysis': '📊 Veri Analizi',
        'show_dataset': 'Veri Setini Göster',
        'open_new_tab_dashboard': '💡 Dashboard için tarayıcıda yeni sekme açın:'
    },
    'en': {
        'data_analysis': '📊 Data Analysis',
        'show_dataset': 'Show Dataset',
        'open_new_tab_dashboard': '💡 Open new tab in browser for Dashboard:'
    }
    'en': {
        'title': '🏢 Janitorial Service Intelligence Platform',
        'subtitle': 'Cleaning Service Scope Creation Form',
        'customer_info': '👤 Customer Information',
        'cleaning_areas': '🧹 Cleaning Areas and Tasks',
        'special_req': '📝 Additional Information',
        'create_button': '🎯 Create and Save Scope',
        'pdf_button': '📋 Prepare Detailed PDF Report',
        'download_pdf': '📥 Download PDF Report',
        'success_message': '✅ Scope successfully added to existing data!',
        'new_file_message': '✅ New scope file created and saved!',
        'error_message': '❌ Please fill in customer name and company name!',
        'no_tasks': '⚠️ No cleaning tasks selected!',
        'special_req_title': 'Special Requirements',
        'dashboard_button': '📊 Go to Dashboard',
        'navigation': '🧭 Navigation',
        'main_page': 'Main Page: Scope creation form',
        'dashboard_page': 'Dashboard: Data analysis and reports',
        'sidebar_title': '🧭 Navigation',
        'reception': '🏢 Reception Area',
        'office': '💼 Office Areas',
        'kitchen': '🍽️ Kitchen (Staff Kitchen)',
        'toilet': '🚻 Toilets',
        'floor_cleaning': 'Floor cleaning',
        'dust_cleaning': 'Dusting',
        'vacuum_cleaning': 'Vacuuming',
        'glass_cleaning': 'Glass cleaning',
        'desk_cleaning': 'Desk cleaning',
        'trash_cleaning': 'Trash collection',
        'disinfect_cleaning': 'Disinfection',
        'supplies_cleaning': 'Supplies restocking',
        'sanitary_cleaning': 'Sanitary cleaning',
        'mirror_cleaning': 'Mirror cleaning',
        'fixtures_cleaning': 'Fixtures cleaning',
        'tiles_cleaning': 'Tiles cleaning',
        'surfaces_cleaning': 'Surfaces cleaning',
        'appliances_cleaning': 'Appliances cleaning',
        'fridge_cleaning': 'Fridge cleaning',
        'microwave_cleaning': 'Microwave cleaning',
        'dishwasher_cleaning': 'Dishwasher',
        'not_included': 'Not Included',
        'daily': 'Daily',
        'weekly': 'Weekly',
        'monthly': 'Monthly',
        'biweekly': 'Bi-weekly',
        'customer_name': 'Customer Name',
        'company_name': 'Company Name',
        'email': 'Email',
        'phone': 'Phone',
        'address': 'Address',
        'start_date': 'Service Start Date',
        'frequency': 'Service Frequency',
        'requirements': 'Special Requirements',
        'name_placeholder': 'Enter customer name',
        'company_placeholder': 'Enter company name',
        'email_placeholder': 'example@email.com',
        'phone_placeholder': '555 555 55 55',
        'address_placeholder': 'Enter full address',
        'requirements_placeholder': 'Special cleaning requirements, points to consider...'
    }
}

def get_text(key):
    lang = st.session_state.get('language', 'tr')
    return LANGUAGES[lang][key]

# Varsayılan dili session state'e ayarla
if 'language' not in st.session_state:
    st.session_state.language = 'tr'

st.set_page_config(layout="wide", page_title="Ana Sayfa - Temizlik Kapsamı Oluşturucu")

# Dil seçici
col1, col2 = st.columns([3, 1])
with col2:
    language = st.selectbox(
        "🌐 Dil / Language",
        options=['tr', 'en'],
        format_func=lambda x: '🇹🇷 Türkçe' if x == 'tr' else '🇺🇸 English',
        key='language_selector',
        label_visibility="collapsed"
    )
    st.session_state.language = language

st.title(get_text('title'))
st.subheader(get_text('subtitle'))

# Sidebar navigasyon
st.sidebar.title(get_text('navigation'))
st.sidebar.write(f"**{get_text('main_page')}")
st.sidebar.write(f"**{get_text('dashboard_page')}")

# Sidebar navigasyon - Dashboard butonu için bilgi
st.sidebar.write(get_text('open_new_tab_dashboard'))
st.sidebar.write("http://localhost:8502/dashboard")

# Müşteri bilgileri bölümü
st.header(get_text('customer_info'))
with st.form("cleaning_scope_form"):
    col1, col2 = st.columns(2)

    with col1:
        customer_name = st.text_input(get_text('customer_name'), placeholder=get_text('name_placeholder'))
        company_name = st.text_input(get_text('company_name'), placeholder=get_text('company_placeholder'))
        contact_email = st.text_input(get_text('email'), placeholder=get_text('email_placeholder'))

    with col2:
        contact_phone = st.text_input(get_text('phone'), placeholder=get_text('phone_placeholder'))
        service_start_date = st.date_input(get_text('start_date'))
        service_frequency = st.selectbox(get_text('frequency'),
                                       [get_text('daily'), f"{get_text('weekly')} (5 gün)", f"{get_text('weekly')} (3 gün)", get_text('weekly'), get_text('biweekly'), get_text('monthly')])
    
    address = st.text_area("Adres", placeholder="Tam adres bilgisini girin")

    # Temizlik alanları
    st.header(get_text('cleaning_areas'))

    # Sıklık seçenekleri
    frequency_options = [get_text('not_included'), get_text('daily'), get_text('weekly'), get_text('monthly')]

    # Resepsiyon
    with st.expander(get_text('reception')):
        col1, col2, col3 = st.columns(3)

        with col1:
            reception_floor = st.selectbox(get_text('floor_cleaning'), frequency_options, key="reception_floor")
            reception_dust = st.selectbox(get_text('dust_cleaning'), frequency_options, key="reception_dust")
            reception_vacuum = st.selectbox(get_text('vacuum_cleaning'), frequency_options, key="reception_vacuum")

        with col2:
            reception_glass = st.selectbox(get_text('glass_cleaning'), frequency_options, key="reception_glass")
            reception_desk = st.selectbox(get_text('desk_cleaning'), frequency_options, key="reception_desk")
            reception_trash = st.selectbox(get_text('trash_cleaning'), frequency_options, key="reception_trash")

        with col3:
            reception_disinfect = st.selectbox(get_text('disinfect_cleaning'), frequency_options, key="reception_disinfect")
            reception_supplies = st.selectbox(get_text('supplies_cleaning'), frequency_options, key="reception_supplies")

    # Ofis Alanları
    with st.expander(get_text('office')):
        col1, col2, col3 = st.columns(3)

        with col1:
            office_floor = st.selectbox(get_text('floor_cleaning'), frequency_options, key="office_floor")
            office_dust = st.selectbox(get_text('dust_cleaning'), frequency_options, key="office_dust")
            office_vacuum = st.selectbox(get_text('vacuum_cleaning'), frequency_options, key="office_vacuum")

        with col2:
            office_glass = st.selectbox(get_text('glass_cleaning'), frequency_options, key="office_glass")
            office_desk = st.selectbox(get_text('desk_cleaning'), frequency_options, key="office_desk")
            office_trash = st.selectbox(get_text('trash_cleaning'), frequency_options, key="office_trash")

        with col3:
            office_disinfect = st.selectbox(get_text('disinfect_cleaning'), frequency_options, key="office_disinfect")
            office_supplies = st.selectbox(get_text('supplies_cleaning'), frequency_options, key="office_supplies")

    # Mutfak
    with st.expander(get_text('kitchen')):
        col1, col2, col3 = st.columns(3)

        with col1:
            kitchen_floor = st.selectbox(get_text('floor_cleaning'), frequency_options, key="kitchen_floor")
            kitchen_surfaces = st.selectbox(get_text('surfaces_cleaning'), frequency_options, key="kitchen_surfaces")
            kitchen_appliances = st.selectbox(get_text('appliances_cleaning'), frequency_options, key="kitchen_appliances")

        with col2:
            kitchen_fridge = st.selectbox(get_text('fridge_cleaning'), frequency_options, key="kitchen_fridge")
            kitchen_microwave = st.selectbox(get_text('microwave_cleaning'), frequency_options, key="kitchen_microwave")
            kitchen_trash = st.selectbox(get_text('trash_cleaning'), frequency_options, key="kitchen_trash")

        with col3:
            kitchen_dishwasher = st.selectbox(get_text('dishwasher_cleaning'), frequency_options, key="kitchen_dishwasher")
            kitchen_disinfect = st.selectbox(get_text('disinfect_cleaning'), frequency_options, key="kitchen_disinfect")
            kitchen_supplies = st.selectbox(get_text('supplies_cleaning'), frequency_options, key="kitchen_supplies")

    # Tuvaletler
    with st.expander(get_text('toilet')):
        col1, col2, col3 = st.columns(3)

        with col1:
            toilet_floor = st.selectbox(get_text('floor_cleaning'), frequency_options, key="toilet_floor")
            toilet_sanitary = st.selectbox(get_text('sanitary_cleaning'), frequency_options, key="toilet_sanitary")
            toilet_mirrors = st.selectbox(get_text('mirror_cleaning'), frequency_options, key="toilet_mirrors")

        with col2:
            toilet_supplies = st.selectbox(get_text('supplies_cleaning'), frequency_options, key="toilet_supplies")
            toilet_disinfect = st.selectbox(get_text('disinfect_cleaning'), frequency_options, key="toilet_disinfect")
            toilet_trash = st.selectbox(get_text('trash_cleaning'), frequency_options, key="toilet_trash")

        with col3:
            toilet_fixtures = st.selectbox(get_text('fixtures_cleaning'), frequency_options, key="toilet_fixtures")
            toilet_tiles = st.selectbox(get_text('tiles_cleaning'), frequency_options, key="toilet_tiles")

    # Ek bilgiler
    st.header(get_text('special_req'))
    special_requirements = st.text_area(get_text('requirements'),
                                       placeholder=get_text('requirements_placeholder'))

    submitted = st.form_submit_button(get_text('create_button'), type="primary")

# Form gönderildiğinde
if submitted:
    if not customer_name or not company_name:
        st.error(get_text('error_message'))
    else:
        # Verileri topla
        data = {
            "Müşteri Adı": customer_name,
            "Şirket Adı": company_name,
            "E-posta": contact_email,
            "Telefon": contact_phone,
            "Adres": address,
            "Başlangıç Tarihi": service_start_date.strftime("%Y-%m-%d"),
            "Hizmet Sıklığı": service_frequency,
            "Resepsiyon - Zemin": reception_floor,
            "Resepsiyon - Toz Alma": reception_dust,
            "Resepsiyon - Süpürme": reception_vacuum,
            "Resepsiyon - Cam": reception_glass,
            "Resepsiyon - Masa": reception_desk,
            "Resepsiyon - Çöp": reception_trash,
            "Resepsiyon - Dezenfeksiyon": reception_disinfect,
            "Resepsiyon - Sarf Malzeme": reception_supplies,
            "Ofis - Zemin": office_floor,
            "Ofis - Toz Alma": office_dust,
            "Ofis - Süpürme": office_vacuum,
            "Ofis - Cam": office_glass,
            "Ofis - Masa": office_desk,
            "Ofis - Çöp": office_trash,
            "Ofis - Dezenfeksiyon": office_disinfect,
            "Ofis - Sarf Malzeme": office_supplies,
            "Mutfak - Zemin": kitchen_floor,
            "Mutfak - Tezgah": kitchen_surfaces,
            "Mutfak - Cihaz": kitchen_appliances,
            "Mutfak - Buzdolabı": kitchen_fridge,
            "Mutfak - Mikrodalga": kitchen_microwave,
            "Mutfak - Çöp": kitchen_trash,
            "Mutfak - Bulaşık Makinesi": kitchen_dishwasher,
            "Mutfak - Dezenfeksiyon": kitchen_disinfect,
            "Mutfak - Sarf Malzeme": kitchen_supplies,
            "Tuvalet - Zemin": toilet_floor,
            "Tuvalet - Hijyenik": toilet_sanitary,
            "Tuvalet - Ayna": toilet_mirrors,
            "Tuvalet - Sarf Malzeme": toilet_supplies,
            "Tuvalet - Dezenfeksiyon": toilet_disinfect,
            "Tuvalet - Çöp": toilet_trash,
            "Tuvalet - Armatür": toilet_fixtures,
            "Tuvalet - Fayans": toilet_tiles,
            "Özel Gereksinimler": special_requirements,
            "Oluşturma Tarihi": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # DataFrame oluştur
        df = pd.DataFrame([data])
        
        # CSV'ye kaydet
        try:
            existing_df = pd.read_csv("cleaning_scopes.csv")
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            combined_df.to_csv("cleaning_scopes.csv", index=False)
            st.success(get_text('success_message'))
        except FileNotFoundError:
            df.to_csv("cleaning_scopes.csv", index=False)
            st.success(get_text('new_file_message'))
        
        # Sonucu göster
        st.header("📋 Oluşturulan Kapsam")
        
        # Müşteri bilgileri
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Müşteri Bilgileri")
            st.write(f"**Ad:** {customer_name}")
            st.write(f"**Şirket:** {company_name}")
            st.write(f"**E-posta:** {contact_email}")
            st.write(f"**Telefon:** {contact_phone}")
            st.write(f"**Adres:** {address}")
        
        with col2:
            st.subheader("Hizmet Bilgileri")
            st.write(f"**Başlangıç Tarihi:** {service_start_date.strftime('%d.%m.%Y')}")
            st.write(f"**Sıklık:** {service_frequency}")
            st.write(f"**Oluşturma:** {datetime.now().strftime('%d.%m.%Y %H:%M')}")
        
        # Temizlik görevleri özeti
        st.subheader("Seçilen Temizlik Görevleri")
        
        # Sadece dahil edilen görevleri göster
        included_tasks = []
        for key, value in data.items():
            if key not in ["Müşteri Adı", "Şirket Adı", "E-posta", "Telefon", "Adres",
                          "Başlangıç Tarihi", "Hizmet Sıklığı", "Özel Gereksinimler", "Oluşturma Tarihi"]:
                if value != "Dahil Değil":
                    included_tasks.append(f"{key}: {value}")
        
        if included_tasks:
            for task in included_tasks:
                st.write(f"✅ {task}")
        else:
            st.warning(get_text('no_tasks'))

        if special_requirements:
            st.subheader(get_text('special_req_title'))
            st.write(special_requirements)
        
        # PDF Rapor oluşturma
        st.subheader("📄 PDF Rapor Oluştur")

        if st.button(get_text('pdf_button'), type="secondary"):
            try:
                from reportlab.lib.pagesizes import letter, A4
                from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
                from reportlab.lib.units import inch
                from reportlab.lib import colors
                import io
                
                # PDF buffer
                buffer = io.BytesIO()
                
                # Document oluştur
                doc = SimpleDocTemplate(buffer, pagesize=A4)
                styles = getSampleStyleSheet()
                
                # Custom styles
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Title'],
                    fontSize=24,
                    spaceAfter=30,
                    textColor=colors.darkblue
                )
                
                heading_style = ParagraphStyle(
                    'CustomHeading',
                    parent=styles['Heading1'],
                    fontSize=16,
                    spaceAfter=12,
                    textColor=colors.darkgreen
                )
                
                # İçerik
                content = []
                
                # Başlık
                content.append(Paragraph("Temizlik Hizmeti Kapsamı Raporu", title_style))
                content.append(Paragraph(f"Oluşturma Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')}", styles['Normal']))
                content.append(Spacer(1, 20))
                
                # Müşteri bilgileri
                content.append(Paragraph("MÜŞTERİ BİLGİLERİ", heading_style))
                
                customer_data = [
                    ["Müşteri Adı:", customer_name],
                    ["Şirket Adı:", company_name],
                    ["E-posta:", contact_email if contact_email else "Belirtilmemiş"],
                    ["Telefon:", contact_phone if contact_phone else "Belirtilmemiş"],
                    ["Adres:", address if address else "Belirtilmemiş"],
                    ["Başlangıç Tarihi:", service_start_date.strftime('%d.%m.%Y')],
                    ["Hizmet Sıklığı:", service_frequency]
                ]
                
                customer_table = Table(customer_data, colWidths=[2*inch, 4*inch])
                customer_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                
                content.append(customer_table)
                content.append(Spacer(1, 20))
                
                # Temizlik görevleri
                content.append(Paragraph("TEMİZLİK GÖREVLERİ", heading_style))
                
                # Sadece dahil edilen görevleri listele
                included_tasks = []
                task_categories = {
                    "Resepsiyon": [col for col in data.keys() if "Resepsiyon" in col and data[col] != "Dahil Değil"],
                    "Ofis": [col for col in data.keys() if "Ofis" in col and data[col] != "Dahil Değil"],
                    "Mutfak": [col for col in data.keys() if "Mutfak" in col and data[col] != "Dahil Değil"],
                    "Tuvalet": [col for col in data.keys() if "Tuvalet" in col and data[col] != "Dahil Değil"]
                }
                
                for category, tasks in task_categories.items():
                    if tasks:
                        content.append(Paragraph(f"{category}:", styles['Heading2']))
                        for task in tasks:
                            content.append(Paragraph(f"• {task}: {data[task]}", styles['Normal']))
                        content.append(Spacer(1, 10))
                
                # Özel gereksinimler
                if special_requirements:
                    content.append(Paragraph("ÖZEL GEREKSİNİMLER", heading_style))
                    content.append(Paragraph(special_requirements, styles['Normal']))
                
                # Footer
                content.append(Spacer(1, 30))
                content.append(Paragraph("Bu rapor Janitorial Service Intelligence Platform tarafından otomatik olarak oluşturulmuştur.",
                                       ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.gray)))
                
                # PDF oluştur
                doc.build(content)
                buffer.seek(0)
                
                # İndirme butonu
                st.download_button(
                    label=get_text('download_pdf'),
                    data=buffer,
                    file_name=f"temizlik_kapsami_{customer_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf",
                    mime="application/pdf",
                    key="pdf_download"
                )
                
                st.success("✅ PDF raporu hazır! İndirme butonuna tıklayarak kaydedebilirsiniz.")
                
            except Exception as e:
                st.error(f"❌ PDF oluşturulurken hata: {str(e)}")

# Sidebar - Veri analizi
st.sidebar.header(get_text('data_analysis'))
if st.sidebar.button(get_text('show_dataset')):
    try:
        df = pd.read_csv("cleaning_scopes.csv")
        st.sidebar.write(f"Toplam Kayıt: {len(df)}")
        
        # Sıklık dağılımı
        if 'Hizmet Sıklığı' in df.columns:
            freq_counts = df['Hizmet Sıklığı'].value_counts()
            st.sidebar.subheader("Hizmet Sıklığı Dağılımı")
            st.sidebar.bar_chart(freq_counts)
            
    except FileNotFoundError:
        st.sidebar.warning("Henüz veri bulunmuyor.")

st.sidebar.markdown("---")
st.sidebar.write("Janitorial Service Intelligence Platform v1.0")