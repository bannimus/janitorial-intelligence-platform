# 🏢 Janitorial Service Intelligence Platform

Profesyonel temizlik şirketleri için kapsam (scope) oluşturma ve veri analizi platformu.

## 🚀 Özellikler

### ✨ Ana Özellikler
- **Kapsam Oluşturma**: Detaylı temizlik kapsamları oluşturun
- **Veri Kaydetme**: Tüm kapsamları CSV formatında saklayın
- **Analitik Dashboard**: Verilerinizi görsel olarak analiz edin
- **PDF Rapor**: Profesyonel PDF raporlar oluşturun
- **Çoklu Sayfa**: Ana sayfa ve dashboard arasında geçiş

### 📋 Temizlik Alanları
- 🏢 **Resepsiyon**: Zemin, toz alma, cam, masa temizliği
- 💼 **Ofis Alanları**: Çalışma alanları ve mobilyalar
- 🍽️ **Mutfak**: Tezgah, cihazlar, buzdolabı temizliği
- 🚻 **Tuvaletler**: Hijyenik temizlik ve dezenfeksiyon

### 📊 Dashboard Özellikleri
- Veri metrikleri ve KPI'lar
- İnteraktif grafikler (Plotly)
- Zaman serisi analizi
- Popüler hizmetler analizi
- Veri filtreleme ve dışa aktarma

## 🛠️ Kurulum

### Gereksinimler
- Python 3.8+
- pip

### Adım Adım Kurulum

1. **Sanal ortam oluşturun:**
```bash
python -m venv venv
```

2. **Sanal ortamı aktifleştirin:**
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Gerekli paketleri yükleyin:**
```bash
pip install streamlit pandas plotly reportlab python-docx
```

4. **Uygulamayı çalıştırın:**
```bash
streamlit run app.py
```

## 🎯 Kullanım

### Kapsam Oluşturma
1. Ana sayfada müşteri bilgilerini doldurun
2. Temizlik alanlarını ve sıklıklarını seçin
3. "Kapsamı Oluştur ve Kaydet" butonuna tıklayın
4. PDF rapor oluşturmak için ilgili butona tıklayın

### Dashboard Analizi
1. Sidebar'dan "Dashboard" sayfasına geçin
2. Veri metriklerini inceleyin
3. Grafikleri ve analizleri görüntüleyin
4. Verileri filtreleyin ve CSV olarak dışa aktarın

## 📁 Proje Yapısı

```
janitorial-service-intelligence/
│
├── app.py                 # Ana sayfa - Kapsam oluşturma
├── pages/
│   └── dashboard.py       # Analitik dashboard
├── cleaning_scopes.csv    # Kapsam verileri (otomatik oluşturulur)
├── README.md             # Bu dosya
└── docs/                 # Proje dokümantasyonları
    ├── proje_baslangic_bilgisi.txt
    ├── yol_haritasi.md
    └── Scope Builder.docx
```

## 🔧 Yapılandırma

### Veri Saklama
- Kapsam verileri `cleaning_scopes.csv` dosyasında saklanır
- Her yeni kapsam mevcut verilere eklenir
- Dashboard bu dosyadan verileri okur

### PDF Raporlar
- Detaylı müşteri ve hizmet bilgileri
- Seçilen temizlik görevleri
- Özel gereksinimler
- Profesyonel format

## 🎨 Özelleştirme

### Yeni Temizlik Alanları Eklemek
`app.py` dosyasında ilgili bölümlere yeni alanlar ekleyebilirsiniz:

```python
# Yeni alan örneği
with st.expander("🏢 Yeni Alan"):
    yeni_gorev = st.selectbox("Görev", ["Dahil Değil", "Günlük", "Haftalık"], key="yeni_gorev")
```

### Dashboard Metrikleri
`pages/dashboard.py` dosyasında yeni metrikler ekleyebilirsiniz.

## 🚀 Geliştirme

### Katkıda Bulunma
1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Lisans

Bu proje öğrenme ve geliştirme amaçlı oluşturulmuştur.

## 🤝 Destek

Herhangi bir sorun yaşarsanız:
- GitHub Issues sayfasını kullanın
- E-posta gönderin

## 📊 Sürüm Geçmişi

### v1.0.0
- İlk sürüm
- Temel kapsam oluşturma
- Dashboard analizi
- PDF raporlama

---

**Janitorial Service Intelligence Platform** - Profesyonel temizlik yönetimi için akıllı çözüm 🏢✨