# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv('dATA.csv')

print("==================================================")
print("       BÖLÜM A — VERİ SETİNİ TANIMA")
print("==================================================")
print(f"1. Satır Sayısı: {df.shape[0]}, Sütun Sayısı: {df.shape[1]}")
print(f"2. Değişken İsimleri: {df.columns.tolist()}")

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

print(f"\n5. Eksik Değer Sayısı: {df.isnull().sum().sum()}")
print(f"6. Tekrar Eden Kayıt Sayısı: {df.duplicated().sum()}")

df_model = df.copy()
le = LabelEncoder()
for col in categorical_cols:
    if col != 'Heart patient':
        df_model[col] = le.fit_transform(df_model[col])

X = df_model.drop(columns=['Heart patient'])
y = df['Heart patient'].map({'Yes': 1, 'No': 0})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

print(f"\nLojistik Regresyon Doğruluk (Accuracy): {accuracy_score(y_test, y_pred_lr):.4f}")

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(14, 18))
sns.countplot(data=df, x='Heart patient', ax=axes[0,0], palette='Set2')
sns.countplot(data=df, x='Age', hue='Heart patient', ax=axes[0,1], order=['< 35', '35–50', '> 50'], palette='Set1')
sns.countplot(data=df, x='Gender', hue='Heart patient', ax=axes[1,0], palette='Set1')
sns.boxplot(data=df, x='Heart patient', y='BMI', ax=axes[1,1], palette='Set3')
sns.countplot(data=df, x='Blood Pressure', hue='Heart patient', ax=axes[2,0], order=['Hypotension', 'Normal', 'Pre-hypertension', 'Hypertension'], palette='Set1')
sns.countplot(data=df, x='Physical activity', hue='Heart patient', ax=axes[2,1], order=['Rarely / Never', 'Less than 2 days per week', '2–4 days per week', '5 or more days per week'], palette='Set1')

for ax in axes.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=15)

plt.tight_layout()
fig.savefig('heart_disease_plots.png', dpi=300)
print("\n[BİLGİ] 'heart_disease_plots.png' başarıyla kaydedildi.")
