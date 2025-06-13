# Azure Monitoring Demo with Flask

This is a simple Flask web application integrated with **Azure Application Insights** for real-time logging and monitoring.

## 🔧 Technologies Used

- Python 3.11  
- Flask  
- Azure Application Insights  
- opencensus-ext-azure  
- Kusto Query Language (KQL)  
- Visual Studio Code  

## 🚀 What It Does

- Logs page visits to Azure Application Insights  
- Allows querying logs in Azure using KQL  
- Demonstrates practical integration between Python apps and Azure monitoring  

## 💡 How to Run It

1. Clone this repo  
2. Set up a virtual environment:  

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:  

   ```bash
   pip install -r requirements.txt
   ```

4. Replace the `connection_string` in `app.py` with your Application Insights string  

5. Run the app:  

   ```bash
   python app.py
   ```

6. Open your browser and go to:  
   [http://localhost:5000](http://localhost:5000)

---

## 📷 Screenshots

### 🖼️ Local Flask App  
![Flask App Screenshot](images/flask_app.png)

### 📊 Azure Logs in Application Insights  
![Azure Logs Screenshot](images/azure_logs.png)

---

## 📈 Kusto Query Used

```kusto
traces
| order by timestamp desc
```

Use this query in Azure Log Analytics to view the logs.

---

## 📝 Notes

> 🚫 **Do not upload your InstrumentationKey or connection string to GitHub**  
Keep it local and private for security reasons.

---

## 📌 Author

**Youssef Tayachi**  
[GitHub Profile](https://github.com/YoussefTayachi)
