# 🛒 Superstore 電商營運分析 Dashboard

> 電商營運分析 Dashboard | Python · SQL · Plotly · Streamlit · Power BI

## 🔗 Live Demo
👉 [點此查看 Streamlit Dashboard](https://superstore-eda-dashboard-5zahahqvkuzw7nhcs72tqo.streamlit.app/)

## 專案簡介
透過 Sample Superstore 資料集進行完整的電商營運 EDA 分析，
分別用 **Python + Streamlit** 和 **Power BI** 建立互動式 Dashboard，
找出銷售與利潤的關鍵驅動因子。

## 📊 Power BI Dashboard
![Power BI Dashboard](screenshots/dashboard_overview.png)

**功能：**
- KPI 卡片：總銷售額、總利潤、利潤率、訂單數
- 月度銷售趨勢折線圖
- 品類銷售長條圖
- Region 互動篩選器（點選即時更新所有圖表）

## 🐍 Python + Streamlit Dashboard
👉 [Live Demo](https://superstore-eda-dashboard-5zahahqvkuzw7nhcs72tqo.streamlit.app/)

**功能：**
- 側邊欄多維度篩選（年份、品類、地區）
- 月度銷售 & 利潤趨勢
- 折扣率 vs 利潤率散佈圖
- 品類利潤率分析
- 動態商業洞察

## 主要發現
- 📌 **折扣陷阱**：折扣超過 40% 的訂單平均利潤率為負
- 📌 **品類差異**：Technology 銷售額最高，但部分子品類持續虧損
- 📌 **季節性**：Q4（11-12月）銷售明顯拉升，建議提前布局庫存

## 技能展示
| 技能 | 應用 |
|------|------|
| Python / pandas | 資料清理、前處理、衍生欄位計算 |
| SQL (SQLite) | 聚合查詢、GROUP BY、CASE WHEN |
| Plotly | 互動式圖表（趨勢、散佈、長條）|
| Streamlit | Dashboard 建構與雲端部署 |
| Power BI | KPI 卡片、互動篩選、DAX 量值 |
| 商業分析 | 折扣策略、利潤率分析、地區表現 |

## 專案結構
```
superstore-eda-dashboard/
├── data/
│   └── superstore.csv
├── notebooks/
│   └── 01_eda.ipynb
├── scripts/
│   └── dashboard.py
├── screenshots/
│   └── dashboard_overview.png
├── superstore_dashboard.pbix
└── requirements.txt
```

## 資料來源
[Kaggle - Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
