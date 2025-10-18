# 📊 Instagram Non-Follower Analyzer

A lightweight Python tool that checks your Instagram JSON data export and finds **people you follow who don’t follow you back** — exporting them into a clean Excel file.

---

## 🧠 What It Does
This tool helps you analyze your Instagram connections by comparing your **following** and **followers** lists.  
It produces a simple Excel file with only the users you follow but who don't follow you back.

---

## 🚀 Features
✅ Reads Instagram’s official JSON data export  
✅ Finds users who don’t follow you back  
✅ Outputs a neatly formatted Excel file with serial numbers  
✅ Zero external setup — just JSON + Python  

---

## 🧩 How to Get Your Instagram Data
1. Open Instagram → **Settings → Privacy and Security → Download Your Information**
2. Choose **JSON format** (not HTML)
3. Once downloaded, extract the ZIP
4. Inside the `connections/` folder, find:
   - `following.json`
   - `followers_1.json`
5. Copy both files into the same folder as this script

---

## 🐍 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/instagram-non-follower-analyzer.git
   cd instagram-non-follower-analyzer
