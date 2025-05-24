# 🚀 **Machine Learning Model Public API Deployment on Google Colab**

## 📌 **Project Overview**

This project demonstrates how to deploy a pre-trained machine learning model as a **publicly accessible API**. The model predicts whether a person is diabetic based on specific medical features. Deployment is done using **FastAPI** for API creation and **Ngrok** to expose the server publicly, all within **Google Colaboratory**.

✅ **Goal:** Enable real-time, public access to a diabetes prediction ML model through an HTTP API hosted from Google Colab.

---

## ✨ **Features**

- Deploy a **machine learning model** as a web API.  
- Provide a **public URL** using **Ngrok**.  
- Accept input data in **JSON format**.  
- Use the **POST method** for predictions.  
- Predict whether a person is **diabetic or not**.  
- Integrated **CORS middleware** to support UI connections.  
- Fully operational within **Google Colaboratory**.  

---

## ⚙️ **Setup and Installation**

Follow these steps to deploy and test the API using Google Colab:

### 1. **Obtain the Trained Model**
- Get the `diabetes_model.sav` file (generated in prior processing of `diabetes.csv`).  
- Upload the `.sav` file to your **Google Colab** runtime environment.

### 2. **Open the Colab Notebook**
- Use the notebook provided with the project or follow the transcript steps to build your own.  
- Ensure **internet connection** and run all setup cells sequentially.

### 3. **Install Required Libraries**
The notebook includes installation cells for the following packages:

- `fastapi`, `uvicorn`, `nest-asyncio`, `pyngrok`  
- `pydantic`, `pickle`, `scikit-learn`, `requests`, `json`

### 4. **Import & Initialize**
- Import libraries.  
- Initialize **FastAPI app**.  
- Add **CORS middleware**.  
- Define data schema using **Pydantic**.  
- Load the trained ML model using **Pickle**.

---

## 🚀 **Deployment Instructions**

### **Create the API Endpoint:**
- Define the **POST** endpoint: `/diabetes_prediction`.

### **Run the API with Uvicorn and Ngrok:**
- The notebook cell uses `pyngrok` to create a public URL pointing to the local **FastAPI** server.  
- **Ngrok** will generate a **temporary public URL**.

### **Public API Usage:**
- The API receives data in **JSON format**.  
- Example parameters include:  
  - `pregnancies`, `glucose`, `blood_pressure`, `skin_thickness`, `insulin`, `bmi`, `diabetes_pedigree_function`, `age`

- Send requests to:
```
https://<NGROK_URL>/diabetes_prediction
```

### **Interacting with the API:**
- Send **POST requests** with the expected parameters.  
- Receive prediction response:  
  - **"The person is diabetic"**  
  - **"The person is not diabetic"**

---

## 📤 **Output**

The API returns a response based on the model's prediction:

- Label `0` → **"The person is not diabetic"**  
- Label `1` → **"The person is diabetic"**

An HTTP status code of **200 OK** confirms successful request processing.

---

## ⚠️ **Limitations**

- **Temporary Access:** Ngrok URL resets each time the server restarts.  
- **Session Bound:** Public access ends once the Colab session is closed or disconnected.  
- **Not for Production:** This setup is ideal for testing or demos, but not suitable for stable, always-on services.  
- **Feature Warning (Non-breaking):** Minor **scikit-learn** warnings may appear regarding unnamed features during prediction.

---
