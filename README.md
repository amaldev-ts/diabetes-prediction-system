# 🩺 Diabetes Prediction System


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A Machine Learning-based web application that predicts whether a person is likely to have diabetes based on medical parameters. Built with Python, Flask, and Scikit-Learn for accurate and instant predictions.

---


---

## 📖 Overview

This project uses **Machine Learning algorithms** to analyze patient health data and predict diabetes risk. The application provides a simple web interface where users can enter medical details and receive prediction results **instantly**.

The model is trained on the famous **Pima Indians Diabetes Dataset** and uses advanced preprocessing techniques to ensure accurate predictions.

---

## ✨ Features

### 🎯 Core Features
- 🩺 **Diabetes Risk Prediction** — Instant ML-based predictions
- 🎨 **User-Friendly Web Interface** — Clean and intuitive design
- 🧠 **Trained ML Model** — Optimized for accuracy
- 📊 **Data Preprocessing & Scaling** — Standardized inputs
- ⚡ **Fast Prediction Results** — Get results in milliseconds
- 🌐 **Flask-Based Deployment** — Production-ready web app

### 🚀 Technical Features
- 🔬 Advanced feature engineering
- 📈 Real-time predictions
- 💾 Persistent model storage (.pkl files)
- 🔄 Scalable architecture
- 📱 Responsive design

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web framework |
| **Scikit-Learn** | Machine Learning library |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computing |
| **HTML5** | Frontend structure |
| **CSS3** | Styling and design |

---

## 📊 Dataset

The model is trained using the **Pima Indians Diabetes Dataset**.

### 📥 Input Parameters

| Parameter | Description | Unit |
|---|---|---|
| 🤰 **Pregnancies** | Number of times pregnant | Count |
| 🩸 **Glucose Level** | Plasma glucose concentration | mg/dL |
| 💓 **Blood Pressure** | Diastolic blood pressure | mm Hg |
| 📏 **Skin Thickness** | Triceps skin fold thickness | mm |
| 💉 **Insulin** | 2-Hour serum insulin | mu U/ml |
| ⚖️ **BMI** | Body Mass Index | kg/m² |
| 👨‍👩‍👧 **Diabetes Pedigree Function** | Diabetes hereditary factor | Score |
| 🎂 **Age** | Age of the person | Years |

### 🎯 Output
- **0** → No Diabetes (Negative)
- **1** → Diabetes Detected (Positive)

---

## 📂 Project Structure

```
diabetes-prediction-system/
│
├── static/                  # CSS, JS, Images
│   └── style.css
├── templates/               # HTML templates
│   └── index.html
├── app.py                   # Flask application
├── main.py                  # Main entry point
├── predict.py               # Prediction logic
├── train_model.py           # Model training script
├── diabetes.csv             # Dataset
├── diabetes_model.pkl       # Trained ML model
├── scaler.pkl               # Feature scaler
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/amaldev-ts/diabetes-prediction-system.git
```

### Step 2: Navigate to Project Folder

```bash
cd diabetes-prediction-system
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open Browser

```
http://127.0.0.1:5000
```

🎉 **Your app is now running locally!**

---

## 🎯 How to Use

1. 🌐 Open the web application
2. 📝 Fill in all the medical parameters:
   - Pregnancies
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin Level
   - BMI
   - Diabetes Pedigree Function
   - Age
3. 🔍 Click the **Predict** button
4. ✅ Get instant prediction result

---

## 🧠 Machine Learning Workflow

```
1. 📥 Data Collection
   ↓
2. 🧹 Data Preprocessing
   ↓
3. 📊 Feature Scaling
   ↓
4. 🤖 Model Training
   ↓
5. ✅ Model Evaluation
   ↓
6. 🚀 Prediction Deployment
```

### Detailed Steps:

#### 1️⃣ Data Collection
- Loaded Pima Indians Diabetes Dataset
- 768 patient records
- 8 medical features + 1 outcome

#### 2️⃣ Data Preprocessing
- Handled missing values
- Removed outliers
- Cleaned the dataset

#### 3️⃣ Feature Scaling
- Applied StandardScaler
- Normalized all features
- Ensured equal weight to all parameters

#### 4️⃣ Model Training
- Split data: 80% training, 20% testing
- Trained multiple ML algorithms
- Selected best performing model

#### 5️⃣ Model Evaluation
- Accuracy testing
- Cross-validation
- Confusion matrix analysis

#### 6️⃣ Deployment
- Saved model as .pkl file
- Integrated with Flask backend
- Deployed to live server

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| 🎯 **Accuracy** | ~80% |
| 📊 **Precision** | ~78% |
| 🔍 **Recall** | ~75% |
| ⚖️ **F1-Score** | ~76% |

---

## 🌍 Browser Support

Works on all modern browsers:
- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Edge
- ✅ Safari
- ✅ Brave
- ✅ Opera

---

## 🚀 Future Improvements

- [ ] Deploy on Streamlit Cloud
- [ ] Improve prediction accuracy with deep learning
- [ ] Add user authentication system
- [ ] Store prediction history in database
- [ ] Add advanced analytics dashboard
- [ ] Integrate with health APIs
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] PDF report generation
- [ ] Email notification system
- [ ] Doctor consultation feature
- [ ] Diet recommendation system

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- ⭐ Star the repository

### Steps to Contribute:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

> 🩺 **Important:** This application is built for **educational and learning purposes only**. The predictions made by this model should **NOT** be considered as professional medical advice. Always consult a qualified healthcare provider for accurate diagnosis and treatment.

---

## 📝 License

This project is for **educational and learning purposes**. Free to use, modify, and distribute.

---

## 📊 Project Stats

- 📅 **Created:** 2025
- 🔢 **Lines of Code:** ~500+
- 📦 **Dataset Size:** 768 records
- 🧠 **Model Type:** Supervised Learning
- ⚡ **Prediction Time:** < 1 second
- 🎯 **Accuracy:** ~80%

---

## 🐛 Known Issues

None currently! If you find any bugs, please [open an issue](https://github.com/amaldev-ts/diabetes-prediction-system/issues).

---

## ⭐ Show Your Support

If you like this project, please:
- ⭐ Star the repository on GitHub
- 🔄 Share it with friends
- 💬 Provide feedback

---

## 🙏 Acknowledgments

- 📊 **Dataset:** Pima Indians Diabetes Database (UCI ML Repository)
- 🧠 **Inspiration:** Healthcare AI research
- 🎨 **UI Design:** Modern web design principles
- 💖 **Built with passion** for AI and healthcare

---

## 👨‍💻 Author & Contact

**Amal Dev**

Computer Science and Engineering Student

Connect with me on:

- 🐙 **GitHub:** [@amaldev-ts](https://github.com/amaldev-ts)
- 📧 **Email:** [amalts5885@gmail.com](mailto:amalts5885@gmail.com)

---

## 📞 Get in Touch

Have questions, suggestions, or want to collaborate? Feel free to reach out!

- 📧 **For Email Inquiries:** amalts5885@gmail.com
- 🐙 **For Bug Reports:** [GitHub Issues](https://github.com/amaldev-ts/diabetes-prediction-system/issues)
I'm always open to:
- 💼 Job opportunities
- 🤝 Collaboration projects
- 💬 Tech discussions
- 📚 Learning together
- 🔬 Research opportunities

---

### 🎉 Made with ❤️ by Amal Dev

**Stay Healthy! Stay Aware! 🩺✨**

---

⭐ **Don't forget to star this repository if you found it useful!** ⭐
