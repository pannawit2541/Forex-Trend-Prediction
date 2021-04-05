# FOREIGN EXCHANGE MARKET PREDICTION SYSTEM

สวัสดีรับ ระบบทำนายตลาดฟอเร็กซ์ จัดทำโดย นายปัณณวิชญ์ พันธ์วงศ์ โดยมีวัตถุประสงค์คือ
> - เพื่อช่วยในการตัดสินใจลงทุนในตลาดฟอเร็กซ์
> - ลดโอกาสผิดพลาด
> - ลดเวลาในการวิเคราะห์

## OVERVIEW SYSTEM
โปรเจคนี้จะมีระบบโดยจะแบ่งออกเป็น 3 ส่วน ได้แก่
> - `Machine Learning` โดยใช้ `Support Vector Regression` ในการทำนาย
> - `Flask API` เป็น `API` ที่เชื่อมระบบทั้งหมด
> - `Website` ใช้ `Vue.js` ในการพัฒนา

## SOFTWARE REQUIRED
สำหรับภาษาที่ใช้พัฒนาจะมีดังนี้
> - Python 3.7
> - Vue.js

## Project Info
ไฟล์ Data จะประกอบไปด้วย 2 ไฟล์หลักๆ คือ 
> - ไฟล์ raw data คือไฟล์ <ชื่อสกุลเงิน>_H1.csv
> - ไฟล์ preprocess คือ <ชื่อสกุลเงิน>_features.csv เป็นไฟล์ที่ preprocessing จาก raw data 

## INSTALLATION

### MACHINE LEANING LIBRARY REQUIRED
สำหรับ Machine Learning จะใช้ Library ในการสร้าง Features และ Train model โดยจะต้องติดตั้งดังต่อไปนี้
Library พื้นฐานที่ใช้พัฒนา
```python
pip install pandas
pip install numpy
```
เมื่อติดตั้ง libray พื้นฐานที่กล่าวมาข้างต้นแล้ว ต่อไปจะเป็นการติดตั้ง Library ในการสร้าง Features โดยสามารถศึกษาวิธีการตามลิงค์ที่แนบให้
> - [TA-Lib](https://github.com/mrjbq7/ta-lib)
> - [Technical Analysis Library in Python (ta)](https://github.com/bukosabino/ta?fbclid=IwAR2TN1sWhVr4HESxBbDpSyaM6SkdQvs7MakEVbY02MrMSmR87jMGqIxcAvs)

เมื่อเราทำการสร้าง Features ได้ ต่อมาจะเป็นการติดตั้ง Library สำหรับไว้เทรนโมเดล โดยใช้ [Scikit-learn](https://scikit-learn.org/stable/install.html)
```python
pip install -U scikit-learn
pip install joblib
```

### FLASK API LIBRARY REQUIRED
ในส่วนของ API จะมีการ ใช้ apscheduler ในการ fetch ข้อมูลทุกๆ ชั่วโมง และ flask ที่เป็น api
> - [Flask installation](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)
```python
pip install apscheduler 
```

### Vue.js LIBRARY REQUIRED
ในส่วนเว็บไซต์จะใช้ [Vue.js](https://vuejs.org/v2/guide/installation.html) ในการพัฒนาโดยจะมี Library ที่ต้องสร้าง กราฟต่างๆดังนี้
> - [Vue-ApexChart](https://apexcharts.com/docs/vue-charts/)
> - [Vue-chartjs](https://vue-chartjs.org/)
> - [Trading-vue-js](https://github.com/tvjsx/trading-vue-js)

ในส่วนของ API เชื่อมกับ Flask จะใช้ axios ในการเชื่อม
> - [Axios](https://www.npmjs.com/package/axios)

สำหรับ CSS และ Icon ใช้ Buefy
> - [Buefy](https://buefy.org/)
> - [Font Awesome](https://fontawesome.com/icons)



