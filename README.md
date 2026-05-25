# 🛒 Superstore 電商營運分析 Dashboard

> 電商營運分析 Dashboard | Python · SQL · Plotly · Streamlit

## 🔗 Live Demo
👉 [點此查看 Dashboard](https://superstore-eda-dashboard-5zahahqvkuzw7nhcs72tqo.streamlit.app/)

## 專案簡介
透過 Sample Superstore 資料集進行完整的電商營運 EDA 分析，
並建立互動式 Dashboard，找出銷售與利潤的關鍵驅動因子。

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
└── requirements.txt
```

## 資料來源
[Kaggle - Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
