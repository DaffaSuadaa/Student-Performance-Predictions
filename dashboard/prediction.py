import streamlit as st
import joblib
import numpy as np
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "random_forest_model.joblib")
model = joblib.load(model_path)

# Judul
st.title("🎓 Student Performance Prediction")

st.markdown("""
Selamat datang di Student Performance Prediction!!
            
Student Performance Prediction ini dikembangkan menggunakan metode **Machine Learning** untuk memprediksi status akademik mahasiswa, apakah mereka akan **Dropout**, **Masih Terdaftar (Enrolled)**, atau **Lulus (Graduate)**, berdasarkan data yang Anda masukkan.
""")

st.markdown("""

### Cara penggunaan : 
1. Masukkan data secara lengkap dan benar pada form di bawah ini.  
**Note:**
    -   🔍 *Perhatikan setiap keterangan yang telah disediakan di setiap bagian input.*  
    -    ⚠️ Jika muncul error, pastikan kembali bahwa semua input sudah sesuai format yang diminta.

2. Setelah semua data terisi, tekan tombol `Predict` untuk melakukan proses prediksi.

3. Hasil prediksi akan muncul pada keterrangan di bawah berdasarkan hasil pengisian yang telah di input. 

""")


marital_status_options = {
    1: "Single",
    2: "Married",
    3: "Widower",
    4: "Divorced",
    5: "Facto Union",
    6: "Legally Separated"
}

application_method_options = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
}

course_options = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}

attendance_options = {
    1: "Daytime",
    0: "Evening"
}

previous_qualification_options = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
}

nationality_options = {
    1: "Portuguese",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian"
}

mother_qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}

father_qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    13: "2nd year complementary high school course",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    20: "Complementary High School Course",
    22: "Technical-professional course",
    25: "Complementary High School Course - not concluded",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}

mother_occupation_options = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    122: "Health professionals",
    123: "teachers",
    125: "Specialists in information and communication technologies (ICT)",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff",
    151: "personal service workers",
    152: "sellers",
    153: "Personal care workers and the like",
    171: "Skilled construction workers and the like, except electricians",
    173: "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    191: "cleaning workers",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants"
}

father_occupation_options = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    101: "Armed Forces Officers",
    102: "Armed Forces Sergeants",
    103: "Other Armed Forces personnel",
    112: "Directors of administrative and commercial services",
    114: "Hotel, catering, trade and other services directors",
    121: "Specialists in the physical sciences, mathematics, engineering and related techniques",
    122: "Health professionals",
    123: "teachers",
    124: "Specialists in finance, accounting, administrative organization, public and commercial relations",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    135: "Information and communication technology technicians",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff",
    151: "personal service workers",
    152: "sellers",
    153: "Personal care workers and the like",
    154: "Protection and security services personnel",
    161: "Market-oriented farmers and skilled agricultural and animal production workers",
    163: "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    171: "Skilled construction workers and the like, except electricians",
    172: "Skilled workers in metallurgy, metalworking and similar",
    174: "Skilled workers in electricity and electronics",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    181: "Fixed plant and machine operators",
    182: "assembly workers",
    183: "Vehicle drivers and mobile equipment operators",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants",
    195: "Street vendors (except food) and street service providers"
}

displaced_options = {
    "No": 0,
    "Yes": 1
}

special_needs_options = {
    "No": 0,
    "Yes": 1
}

debtor_options = {
    "No": 0,
    "Yes": 1
}

tuition_up_to_date_options = {
    "No": 0,
    "Yes": 1
}

gender_options = {
    "Female": 0,
    "Male": 1
}

scholarship_holder_options = {
    "No": 0,
    "Yes": 1
}

international_options = {
    "No": 0,
    "Yes": 1
}




# Form input
with st.form("student_form"):
    marital_status_label = st.selectbox("Marital Status", list(marital_status_options.values()))
    application_method_label = st.selectbox("Application Method", list(application_method_options.values()))

    application_order = st.text_input(
        "Application Order (0 = First Choice, 9 = Last Choice)",
        help="Masukkan urutan pilihan antara 0 hingga 9, di mana 0 adalah pilihan utama."
    )

    selected_course_label = st.selectbox("Select the student's course",options=list(course_options.values()))
    selected_attendance_label = st.selectbox("Select attendance time",options=list(attendance_options.values()))
    previous_qualification_label = st.selectbox("Previous Qualification",options=list(previous_qualification_options.values()))
    previous_qualification_grade = st.number_input("Grade of Previous Qualification (0 - 200)",min_value=0,max_value=200,step=1)
    nationality_label = st.selectbox("Select Nationality",options=list(nationality_options.values()))

    mother_qualification_label = st.selectbox("Mother's Qualification",options=list(mother_qualification_options.values()))
    father_qualification_label = st.selectbox("Father's Qualification",options=list(father_qualification_options.values()))
    mother_occupation_label = st.selectbox("Mother's Occupation",options=list(mother_occupation_options.values()))
    father_occupation_label = st.selectbox("Father's Occupation",options=list(father_occupation_options.values()))
    admission_grade = st.number_input("Admission Grade (0.0 - 200.0)", min_value=0.0, max_value=200.0, step=0.1)


    displaced_label = st.selectbox("Is the student displaced?", options=list(displaced_options.keys()))
    special_needs_label = st.selectbox("Educational Special Needs?", options=list(special_needs_options.keys()))
    debtor_label = st.selectbox("Is the student a debtor?", options=list(debtor_options.keys()))
    tuition_up_to_date_label = st.selectbox("Tuition fees up to date?", options=list(tuition_up_to_date_options.keys()))
    gender_label = st.selectbox("Gender", options=list(gender_options.keys()))
    scholarship_holder_label = st.selectbox("Is the student a scholarship holder?", options=list(scholarship_holder_options.keys()))
    age_at_enrollment = st.number_input("Age at Enrollment", min_value=15, max_value=100, step=1)
    international_label = st.selectbox("Is the student international?", options=list(international_options.keys()))

    units_credited = st.number_input("Curricular Units 1st Sem (Credited)", min_value=0, step=1)
    units_enrolled = st.number_input("Curricular Units 1st Sem (Enrolled)", min_value=0, step=1)
    units_evaluated = st.number_input("Curricular Units 1st Sem (Evaluated)", min_value=0, step=1)
    units_approved = st.number_input("Curricular Units 1st Sem (Approved)", min_value=0, step=1)

    units_1st_sem_grade = st.number_input("Curricular Units 1st Sem (Grade)", min_value=0.0, max_value=200.0, step=0.1)
    units_1st_sem_wo_eval = st.number_input("Curricular Units 1st Sem (Without Evaluations)", min_value=0, step=1)

    units_2nd_sem_credited = st.number_input("Curricular Units 2nd Sem (Credited)", min_value=0, step=1)
    units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem (Enrolled)", min_value=0, step=1)
    units_2nd_sem_evaluated = st.number_input("Curricular Units 2nd Sem (Evaluated)", min_value=0, step=1)
    units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem (Approved)", min_value=0, step=1)
    units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem (Grade)", min_value=0.0, max_value=200.0, step=0.1)
    units_2nd_sem_wo_eval = st.number_input("Curricular Units 2nd Sem (Without Evaluations)", min_value=0, step=1)

    unemployment_rate = st.number_input("Unemployment Rate", min_value=0.0, step=0.1)
    inflation_rate = st.number_input("Inflation Rate", min_value=0.0, step=0.1)
    gdp = st.number_input("GDP", min_value=0.0, step=0.1)

    
    

    submit = st.form_submit_button("Predict")


def encode_input(form_data):
    encoded_data = []

    def reverse_lookup(value, dictionary):
        return {v: k for k, v in dictionary.items()}[value]

    # Encode categorical features
    encoded_data.append(reverse_lookup(form_data['marital_status'], marital_status_options))
    encoded_data.append(reverse_lookup(form_data['application_method'], application_method_options))
    encoded_data.append(int(form_data['application_order']))
    encoded_data.append(reverse_lookup(form_data['selected_course'], course_options))
    encoded_data.append(reverse_lookup(form_data['selected_attendance'], attendance_options))
    encoded_data.append(reverse_lookup(form_data['previous_qualification'], previous_qualification_options))
    encoded_data.append(form_data['previous_qualification_grade'])
    encoded_data.append(reverse_lookup(form_data['nationality'], nationality_options))
    encoded_data.append(reverse_lookup(form_data['mother_qualification'], mother_qualification_options))
    encoded_data.append(reverse_lookup(form_data['father_qualification'], father_qualification_options))
    encoded_data.append(reverse_lookup(form_data['mother_occupation'], mother_occupation_options))
    encoded_data.append(reverse_lookup(form_data['father_occupation'], father_occupation_options))
    encoded_data.append(form_data['admission_grade'])

    encoded_data.append(displaced_options[form_data['displaced']])
    encoded_data.append(special_needs_options[form_data['special_needs']])
    encoded_data.append(debtor_options[form_data['debtor']])
    encoded_data.append(tuition_up_to_date_options[form_data['tuition_up_to_date']])
    encoded_data.append(gender_options[form_data['gender']])
    encoded_data.append(scholarship_holder_options[form_data['scholarship']])
    encoded_data.append(form_data['age_at_enrollment'])
    encoded_data.append(international_options[form_data['international']])

    # Numerical input for semester data
    encoded_data.append(form_data['units_credited'])
    encoded_data.append(form_data['units_enrolled'])
    encoded_data.append(form_data['units_evaluated'])
    encoded_data.append(form_data['units_approved'])
    # Semester 1
    encoded_data.append(form_data['units_1st_sem_grade'])
    encoded_data.append(form_data['units_1st_sem_wo_eval'])

    # Semester 2
    encoded_data.append(form_data['units_2nd_sem_credited'])
    encoded_data.append(form_data['units_2nd_sem_enrolled'])
    encoded_data.append(form_data['units_2nd_sem_evaluated'])
    encoded_data.append(form_data['units_2nd_sem_approved'])
    encoded_data.append(form_data['units_2nd_sem_grade'])
    encoded_data.append(form_data['units_2nd_sem_wo_eval'])

    # Macro-economic
    encoded_data.append(form_data['unemployment_rate'])
    encoded_data.append(form_data['inflation_rate'])
    encoded_data.append(form_data['gdp'])


    return np.array([encoded_data])


if submit:
    form_data = {
        'marital_status': marital_status_label,
        'application_method': application_method_label,
        'application_order': application_order,
        'selected_course': selected_course_label,
        'selected_attendance': selected_attendance_label,
        'previous_qualification': previous_qualification_label,
        'previous_qualification_grade': previous_qualification_grade,
        'nationality': nationality_label,
        'mother_qualification': mother_qualification_label,
        'father_qualification': father_qualification_label,
        'mother_occupation': mother_occupation_label,
        'father_occupation': father_occupation_label,
        'admission_grade': admission_grade,
        'displaced': displaced_label,
        'special_needs': special_needs_label,
        'debtor': debtor_label,
        'tuition_up_to_date': tuition_up_to_date_label,
        'gender': gender_label,
        'scholarship': scholarship_holder_label,
        'age_at_enrollment': age_at_enrollment,
        'international': international_label,
        'units_credited': units_credited,
        'units_enrolled': units_enrolled,
        'units_evaluated': units_evaluated,
        'units_approved': units_approved,
        'units_1st_sem_grade': units_1st_sem_grade,
        'units_1st_sem_wo_eval': units_1st_sem_wo_eval,
        'units_2nd_sem_credited': units_2nd_sem_credited,
        'units_2nd_sem_enrolled': units_2nd_sem_enrolled,
        'units_2nd_sem_evaluated': units_2nd_sem_evaluated,
        'units_2nd_sem_approved': units_2nd_sem_approved,
        'units_2nd_sem_grade': units_2nd_sem_grade,
        'units_2nd_sem_wo_eval': units_2nd_sem_wo_eval,
        'unemployment_rate': unemployment_rate,
        'inflation_rate': inflation_rate,
        'gdp': gdp
    }

    input_data = encode_input(form_data)

    prediction = model.predict(input_data)[0]

    st.success(f"🎯 Predicted Student Status: **{prediction}**")
