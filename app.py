import pickle
import pandas as pd
import streamlit as st

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------
# Custom styling
# ----------------------------
st.markdown("""
<style>
    /* Overall app background */
    .stApp {
        background: linear-gradient(180deg, #fff5f5 0%, #ffffff 22%);
    }

    /* Hero header */
    .hero {
        background: linear-gradient(135deg, #b91c1c 0%, #e11d48 55%, #f97316 100%);
        padding: 2.2rem 2rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 1.6rem;
        box-shadow: 0 10px 30px rgba(185, 28, 28, 0.25);
    }
    .hero h1 {
        color: white;
        font-size: 2.1rem;
        margin-bottom: 0.3rem;
    }
    .hero p {
        color: #ffe4e6;
        font-size: 1rem;
        margin: 0;
    }

    /* Section cards */
    .section-card {
        background: white;
        border-radius: 14px;
        padding: 1.4rem 1.5rem 0.6rem 1.5rem;
        margin-bottom: 1.2rem;
        border: 1px solid #f1e3e3;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .section-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #b91c1c;
        margin-bottom: 0.6rem;
    }

    /* Predict button */
    div.stButton > button, button[kind="formSubmit"] {
        background: linear-gradient(135deg, #b91c1c, #e11d48);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 1rem;
        font-weight: 600;
        font-size: 1.05rem;
        transition: transform 0.15s ease;
    }
    div.stButton > button:hover, button[kind="formSubmit"]:hover {
        transform: scale(1.01);
        color: white;
        border: none;
    }

    /* Result cards */
    .result-card {
        border-radius: 16px;
        padding: 1.6rem;
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .result-high {
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        border: 1px solid #f87171;
    }
    .result-low {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        border: 1px solid #4ade80;
    }
    .result-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .result-high .result-title { color: #991b1b; }
    .result-low .result-title { color: #166534; }
    .result-sub {
        font-size: 0.95rem;
        color: #444;
    }

    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load model
# ----------------------------
@st.cache_resource
def load_model():
    with open("HeartHealthPredictor.pickle", "rb") as f:
        return pickle.load(f)

model = load_model()

FEATURE_ORDER = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal",
]

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.header("ℹ️ About this app")
    st.write(
        "This tool estimates heart disease risk using a **Gaussian Naive Bayes** "
        "classifier trained on the UCI Heart Disease dataset (303 patient records, "
        "13 clinical features)."
    )
    st.markdown("**Model performance on test data:**")
    st.metric("Accuracy", "86.9%")
    st.metric("F1 Score", "87.1%")
    st.divider()
    st.caption(
        "⚠️ Educational demo only — not a substitute for professional "
        "medical diagnosis or advice."
    )

# ----------------------------
# Hero header
# ----------------------------
st.markdown("""
<div class="hero">
    <h1>❤️ Heart Disease Risk Predictor</h1>
    <p>Enter patient clinical details to estimate heart disease risk in real time.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Input form
# ----------------------------
with st.form("patient_form"):

    st.markdown('<div class="section-card"><div class="section-title">🧍 Patient Information</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age (years)", 18, 100, 54)
    with col2:
        sex = st.radio("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female", horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card"><div class="section-title">🩺 Vitals & Blood Work</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        trestbps = st.slider("Resting blood pressure (mm Hg)", 80, 220, 130)
        fbs = st.radio(
            "Fasting blood sugar > 120 mg/dL?",
            options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True,
        )
    with col4:
        chol = st.slider("Serum cholesterol (mg/dL)", 100, 600, 246)
        thalach = st.slider("Max heart rate achieved", 60, 220, 150)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card"><div class="section-title">💓 ECG & Exercise Results</div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        cp = st.selectbox(
            "Chest pain type",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "Typical angina", 1: "Atypical angina",
                2: "Non-anginal pain", 3: "Asymptomatic",
            }[x],
        )
        exang = st.radio(
            "Exercise-induced angina?",
            options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No", horizontal=True,
        )
        slope = st.selectbox(
            "Slope of peak exercise ST segment",
            options=[0, 1, 2],
            format_func=lambda x: {0: "Upsloping", 1: "Flat", 2: "Downsloping"}[x],
        )
    with col6:
        restecg = st.selectbox(
            "Resting ECG results",
            options=[0, 1, 2],
            format_func=lambda x: {
                0: "Normal", 1: "ST-T wave abnormality",
                2: "Left ventricular hypertrophy",
            }[x],
        )
        oldpeak = st.slider("ST depression (oldpeak)", 0.0, 7.0, 1.0, step=0.1)
        ca = st.selectbox("Major vessels colored by fluoroscopy (0-4)", options=[0, 1, 2, 3, 4])

    thal = st.selectbox(
        "Thalassemia test result",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Normal", 1: "Fixed defect",
            2: "Reversible defect", 3: "Unknown/Other",
        }[x],
    )
    st.markdown('</div>', unsafe_allow_html=True)

    submitted = st.form_submit_button("🔍 Predict Risk", use_container_width=True)

# ----------------------------
# Prediction
# ----------------------------
if submitted:
    input_dict = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal,
    }
    input_df = pd.DataFrame([input_dict])[FEATURE_ORDER]

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    if prediction == 1:
        st.markdown(f"""
        <div class="result-card result-high">
            <div class="result-title">⚠️ Higher Risk of Heart Disease</div>
            <div class="result-sub">Model confidence: {proba[1]*100:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-card result-low">
            <div class="result-title">✅ Lower Risk of Heart Disease</div>
            <div class="result-sub">Model confidence: {proba[0]*100:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.progress(float(proba[1]), text=f"Estimated probability of heart disease: {proba[1]*100:.1f}%")

    with st.expander("📋 See the values used for this prediction"):
        st.dataframe(input_df, use_container_width=True)

st.divider()
st.caption("Model: Gaussian Naive Bayes · Dataset: UCI Heart Disease · Built with Streamlit")
