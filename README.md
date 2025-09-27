# 🏢 Janitorial Service Intelligence Platform

**Intelligent Scope Creation and Data Analytics Platform for Professional Cleaning Companies**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)]()

---

## ⚠️ **PROPRIETARY SOFTWARE NOTICE**

**This software is protected by copyright.**
- © 2024 BanniMus. All rights reserved.
- License required for commercial use.
- Copying, modifying, or distributing source code is prohibited.
- Unauthorized use may result in legal action.

---

## 🚀 **Features**

### ✨ **Core Features**
- **🔐 Secure Scope Creation**: Multi-language support for detailed cleaning scopes
- **📊 Intelligent Data Analytics**: Real-time dashboard and reporting
- **📄 Professional PDF Reports**: Automated reports for client presentations
- **🌐 Multi-Language Support**: Turkish and English interface
- **☁️ Cloud Compatible**: Instant deployment with Streamlit Cloud

### 🏢 **Cleaning Areas**
| Area | Number of Tasks | Supported Frequencies |
|------|----------------|---------------------|
| **Reception** | 8 tasks | Daily/Weekly/Monthly |
| **Office Areas** | 8 tasks | Daily/Weekly/Monthly |
| **Kitchen** | 9 tasks | Daily/Weekly/Monthly |
| **Toilets** | 8 tasks | Daily/Weekly/Monthly |

### 📊 **Dashboard Features**
- **KPI Metrics**: Total scopes, growth rates
- **Interactive Charts**: Dynamic visualizations with Plotly
- **Time Series**: Activity trend analysis
- **Service Analysis**: Most popular cleaning types
- **Data Export**: CSV and PDF export

## 💰 **Licensing**

### **Pricing Plans**
| Package | Monthly | Annual | Features |
|---------|---------|--------|----------|
| **Starter** | $29 | $290 | Basic scope creation, 100 customers |
| **Professional** | $79 | $790 | Advanced analytics, unlimited customers, PDF reports |
| **Enterprise** | $199 | $1,990 | Multi-user, API access, custom domain |

### **Feature Comparison**
- ✅ **Starter**: Scope creation, basic dashboard
- ✅ **Professional**: Advanced analytics, PDF reports, priority support
- ✅ **Enterprise**: Multi-user, custom developments, SLA guarantee

## 🛠️ **Technical Requirements**

### **Minimum System Requirements**
- **Python**: 3.8 or higher
- **RAM**: 2 GB
- **Disk**: 500 MB free space
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+

### **Supported Platforms**
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu 20.04+)
- ✅ Cloud (AWS, Google Cloud, Azure)

## 📋 **Quick Start**

### **Live Demo**
🌐 **[View Live Demo](https://bannimus-janitorial-intelligence-platform.streamlit.app)**

### **Local Installation**
```bash
# 1. Clone the repository
git clone https://github.com/bannimus/janitorial-intelligence-platform.git
cd janitorial-intelligence-platform

# 2. Create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app.py
```

## 🎯 **User Guide**

### **1. Creating Scopes**
1. **Enter customer information** (name, company, contact)
2. **Select service date** and **frequency**
3. **Expand cleaning areas** and select tasks
4. **Click "Create Scope"** button
5. **Download PDF report**

### **2. Dashboard Analysis**
1. **Navigate to Dashboard** from sidebar
2. **Review metrics**
3. **Analyze charts**
4. **Filter and export data**

## 📁 **Proje Yapısı**

```
janitorial-intelligence-platform/
│
├── 📄 app.py                  # Ana uygulama (kapsam oluşturma)
├── 📁 pages/
│   └── 📄 dashboard.py        # Analitik dashboard
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📄 Procfile               # Heroku deployment
├── 📄 .gitignore            # Gizli dosyalar
└── 📄 README.md             # Bu dokümantasyon
```

## 🔧 **API Referansı**

### **Veri Formatları**
```json
{
  "customer_name": "string",
  "company_name": "string",
  "service_frequency": "Daily|Weekly|Monthly",
  "cleaning_areas": {
    "reception": ["floor_cleaning", "dust_cleaning"],
    "office": ["vacuum_cleaning", "desk_cleaning"]
  }
}
```

## 🤝 **Support & Contact**

### **Support Channels**
- 📧 **Email**: support@bannimus.com
- 💬 **Live Chat**: Available 24/7 on our website
- 📞 **Phone**: [Contact number]
- 📋 **Ticket**: Through our support portal

### **SLA Guarantees**
| Package | Response Time | Resolution Time |
|---------|---------------|-----------------|
| **Starter** | 24 hours | 72 hours |
| **Professional** | 4 hours | 24 hours |
| **Enterprise** | 1 hour | 8 hours |

## 📊 **Version History**

| Version | Date | Key Changes |
|---------|------|-------------|
| **v1.0.0** | 2024 | First commercial release |
| **v1.1.0** | Planned | Advanced analytics features |
| **v1.2.0** | Planned | Mobile application |

## ⚖️ **Legal Disclaimers**

### **Terms of Use**
1. This software may only be used by licensed users
2. Examining, copying, or modifying source code is prohibited
3. Cannot be transferred to third parties
4. Data privacy and security standards must be followed

### **Disclaimer**
- Software is provided "as is"
- No liability for indirect damages
- User data security is user's responsibility

### **Violation Policy**
- 🚫 **Warning**: Written warning for first violation
- 🚫 **License Termination**: For repeated violations
- ⚖️ **Legal Action**: In case of commercial loss

---

## 🏆 **About BanniMus**

**BanniMus** is a professional software development company founded in 2024. We provide digital solutions specialized for the cleaning industry.

**🏢 Address**: [Company address]
**🌐 Website**: [www.bannimus.com]
**📧 Email**: info@bannimus.com
**📞 Phone**: [Contact number]

---

**🔒 © 2024 BanniMus. All rights reserved.**
**⚖️ This software is protected by copyright and trade secrets.**