# Movie-Revenue-Prediction-
🎬 Predict movie box office revenue using ML | Streamlit app for live prediction
🧠 Problem Statement
🎥 The movie industry often struggles with predicting revenue before a film is released. Studio executives, investors, and production teams invest millions based on gut feeling or limited forecasting.

🔍 Goal: Build a machine learning solution that predicts how much revenue a movie will generate based on early-stage features such as budget, popularity, cast and crew information.
🎯 Business Use Case
💼 This model provides production houses, streaming platforms, and investors with:

📈 Accurate revenue forecasting
🎯 Informed decision-making about casting, budgeting, and marketing
💡 Risk mitigation by identifying potentially underperforming projects before large investments

🗂️ Dataset Description
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
We used two datasets:
movies.csv: Contains core details like budget, popularity, vote_average, runtime, etc.
credits.csv: Contains cast and crew information

🛠️ Technologies & Libraries

Tool	Purpose
Pandas	Data loading, cleaning
NumPy	Feature transformation
Sklearn	Model building & evaluation
Matplotlib/Seaborn	Data visualization
Streamlit	Web app deployment
Pickle	Model serialization

🧹 Data Preprocessing Highlights
✔️ Merged both datasets on movie_id
✔️ Selected useful columns for prediction
✔️ Converted genres, cast, and crew JSON-like strings into counts using ast.literal_eval
✔️ Final feature set:

budget, popularity,runtime,vote_average ,vote_count,genre_count ,cast_count,crew_count

🎯 Target Variable: revenue
🤖 ML Models Compared
We trained and compared multiple supervised regression models using the same dataset:

🔢 Model	                      🧮 MSE (↓)	                    📊 R² Score (↑)
Linear Regression            	1.06 × 10¹⁶	                          0.49
Decision Tree Regressor     	1.49 × 10¹⁵                         	0.92
Random Forest Regressor     	1.30 × 10¹⁵                       	0.94
Support Vector Regressor	       Poor result	                     -0.01

Best Model: Random Forest — It outperformed other models with high R² score and low Mean Squared Error.

📈 Visual Comparison
We used a bar chart to visually compare R² scores of all models. This makes performance differences easily understandable for stakeholders.

🌐 Web App with Streamlit
A Streamlit web application was developed where users can input:
budget, popularity,runtime,vote_average ,vote_count,genre_count ,cast_count,crew_count

🔮 And get an instant revenue prediction!

streamlit run pic.py

🔋 Future Improvements
🎭 Use actor popularity metrics (IMDb, )
🧾 Sentiment analysis of trailers or scripts
📅 Include release seasonality
🧠 Use deep learning or ensemble stacked models
📦 Deploy to cloud ( AWS)








