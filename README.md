 ## <div align="center">VEHICLE MOVEMENT ANALYSIS AND INSIGHT GENERATION USING EDGE AI - TEAM INNOVATE5 🚀</div>

### <div align="center">Intel Unnati Industrial Training Program 2024 </div>


### <div align="center">Deparment of CSE-AIML, Sreenidhi Insitute of Science and Technology, Hyderabad </div>

### A powerful edge AI based tool for vehicle entry and exit checking, parking lot occupancy evaluation and insight generation and vehicle matching. 

## <div align="center">RUN STREAMLIT APP 📄</div>

**CHECK OUT** [dashboard_here](https://dashboardvmsapp.streamlit.app/)

<details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/doli-hemanth-sai/INTEL_UTP_PS_13/blob/main/requirements.txt) 

```bash
git clone https://github.com/doli-hemanth-sai/INTEL_UTP_PS_13  # clone
cd INTEL_UTP_PS_13
pip install -r requirements.txt  # install
```
</details>

  
<details open>
<summary>Running the application</summary>
To test out the entire project after installation, run the following:
 
```
cd src
```
then go to streamlit
```
cd streamlit
```
In streamlit we have three different files run base don your requirement..
```
cd dashboard
```
Running the Streamlit app
```
python -m streamlit run dashboard_app.py
```

Code for insights generation is present in the "streamlit" folder
Please refer to the README files in each of the folders for more information.

</details>

### Details 🔎

The project contains the following:
1. **data** - Links to the datasets used for training, validation and testing purposes
2. **models** - The trained models for parking space detection, license plate detection, and license plates OCR. Also contains the model formats optimized for Edge AI 
3. **notebooks** - Contains the notebooks used for model training and export.
4. **scripts** - scripts for data preprocessing, data generation, test data sampling for export, etc.
5. **src** - The CLI based code for model inference of the parking space,streamlit  and license plate models.
Part of the main source code of the project. 
6. **test_data** - Test images for testing the license plate and parking detection models
7. **requirements.txt** - The requirements file, containing all dependencies for the project.

### Features 🧠:
Certainly! Here's a summarized version of the features implemented in your intelligent vehicle management system project:

### Project Features 

1. **System Infrastructure:**
   - Deployment of high-resolution cameras and edge AI devices for real-time data processing.

2. **Data Acquisition and Storage:**
   - Establishment of a robust database for storing image data, timestamps, and vehicle information.

3. **Model Development and Optimization:**
   - Implementation of algorithms for analyzing vehicle movement patterns and peak traffic times.
   - Integration of object detection (YOLOv8) for real-time parking occupancy and OCR (easyocr) for license plate recognition.

4. **Real-Time Processing and Monitoring:**
   - Utilization of edge AI devices and video streaming for immediate data analysis.
   - Development of real-time dashboards to monitor vehicle movements and parking occupancy.

5. **Analysis and Predictive Insights:**
   - Application of machine learning models to analyze movement patterns and forecast parking occupancy trends.

6. **Integration for Security and Management:**
   - Unified system integration for comprehensive campus security.
   - Implementation of an alert system for unauthorized vehicle detection and policy development based on data insights.

7. **Testing, Deployment, and Maintenance:**
   - Controlled testing to validate system accuracy and performance.
   - Campus-wide deployment and continuous monitoring to ensure operational efficiency.


### Objectives achieved ✅: 

1. **Enhanced Campus Security:** By detecting unauthorized vehicles and monitoring movements in real-time.
2. **Improved Management:** Through insights into parking occupancy and traffic patterns.
3. **Efficiency in Operations:** Reduced latency and bandwidth usage with edge AI devices.
4. **Proactive Decision Making:** Enabled by predictive analytics and real-time dashboards.
5. **Scalability and Sustainability:** Ensured by continuous maintenance and updates.

### For complete details about implementation, methodology and results, along with visualizations, please refer the project report [here](https://github.com/doli-hemanth-sai/INTEL_UTP_PS_13/blob/main/reports/project_report_intel_Innovate5.pdf)


Example of License plate evaluation

<div align="center">
  <p>
      <img width="100%" src="https://github.com/user-attachments/assets/92c331ba-827a-49f6-a3fb-338523cea8f4"></a></p>   
</div>

Example of insight generation

<div align="center">
  <p>
      <img width="100%" src="https://github.com/user-attachments/assets/92c331ba-827a-49f6-a3fb-338523cea8f4"></a></p>   
</div>

Example of parking lot occupancy monitoring:

<div align="center">
  <p>
      <img width="100%" src="https://github.com/user-attachments/assets/92c331ba-827a-49f6-a3fb-338523cea8f4"></a></p>   
</div>

### The Team ✨

1. Doli Hemanth Sai - [21311A6635@sreenidhi.edu.in](mailto:21311A6635@sreenidhi.edu.in), CSE-AI&ML

2. Amidhepuram Umasravani - [21311A6622@sreenidhi.edu.in](mailto:21311A6622@sreenidhi.edu.in), CSE-AI&ML

3. Medisetti Sai kiran varma - [21311A6621@sreenidhi.edu.in](mailto:21311A6621@sreenidhi.edu.in), CSE-AI&ML

4. Sattaram Sai Praneeth Reddy - [21311A6649@sreenidhi.edu.in](mailto:21311A6649@sreenidhi.edu.in), CSE-AI&ML

5. Pulluri Sreni - [21311A6645@sreenidhi.edu.in](mailto:21311A6645@sreenidhi.edu.in), CSE-AI&ML

### Credits 🎓
Huge thanks to our internal mentor, **Dr. T.V. Rajinkanth**, Professor & Head, Department of CSE-AI&ML, SNIST, for his invaluable support throughout this project.

Special gratitude goes to our external mentor, **Archana Vaidheeswaran**, for her guidance and expertise which were instrumental in the successful execution of this project.

We are also grateful to the Intel Unnati team for providing us with the opportunity to develop a solution for such a fascinating and unique problem statement.
