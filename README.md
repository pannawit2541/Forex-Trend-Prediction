# FOREIGN EXCHANGE MARKET PREDICTION SYSTEM

> สวัสดีรับ ระบบทำนายตลาดฟอเร็กซ์ จัดทำโดย นายปัณณวิชญ์ พันธ์วงศ์
> โดยมีวัตถุประสงค์คือ
> - เพื่อช่วยในการตัดสินใจลงทุนในตลาดฟอเร็กซ์
> - ลดโอกาสผิดพลาด
> - ลดเวลาในการวิเคราะห์

## OVERVIEW SYSTEM
> - `Machine Learning` โดยใช้ `Support Vector Regression` ในการทำนาย
> - `Flask API` เป็น `API` ที่เชื่อมระบบทั้งหมด
> - `Website` ใช้ `Vue.js` ในการพัฒนา

## SOFTWARE REQUIRED
> - Python 3.7
> - Vue.js

## INSTALLATION
สำหรับ Machine Learning จะใช้ Library ในการสร้าง Features และ Train model โดยจะต้องติดตั้งดังต่อไปนี้
Library พื้นฐานที่ใช้พัฒนา
```python
pip install pandas
pip install numpy
```
เมื่อติดตั้ง libray พื้นฐานที่กล่าวมาข้างต้นแล้ว ต่อไปจะเป็นการติดตั้ง Library ในการสร้าง Features โดยสามารถศึกษาวิธีการตามลิงค์ที่แนบให้
- TA-Lib : https://github.com/mrjbq7/ta-lib
- Technical Analysis Library in Python (ta) : https://github.com/bukosabino/ta?fbclid=IwAR2TN1sWhVr4HESxBbDpSyaM6SkdQvs7MakEVbY02MrMSmR87jMGqIxcAvs
