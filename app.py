import streamlit as st


# =========================================================
# FUNAAB ADMISSION CALCULATOR
# Created by: Arisekola Abdulrahman Ayomide
# Nickname: Atomic
# =========================================================


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="FUNAAB Admission Calculator",
    page_icon="🎓",
    layout="centered"
)


# =========================================================
# GRADE POINTS
# =========================================================

GRADE_POINTS = {
    "A1": 6,
    "B2": 5,
    "B3": 4,
    "C4": 3,
    "C5": 2,
    "C6": 1,
    "D7": 0,
    "E8": 0,
    "F9": 0
}


# =========================================================
# OFFICIAL 2026 FUNAAB PROGRAMMES
# =========================================================

COURSES = {

    "Agriculture": {
        "Agricultural Administration": 160,
        "Agricultural Economics and Farm Management": 160,
        "Agricultural Extension and Rural Development": 160,
        "Animal Breeding and Genetics": 160,
        "Animal Nutrition": 160,
        "Animal Physiology": 160,
        "Animal Production and Health": 160,
        "Aquaculture and Fisheries Management": 160,
        "Climate Science and Agricultural Meteorology": 160,
        "Crop Protection": 160,
        "Environmental Management and Toxicology": 160,
        "Forest Resource Management": 160,
        "Geology": 160,
        "Horticulture": 160,
        "Hydrology And Water Resources Management": 160,
        "Pasture and Range Management": 160,
        "Plant Breeding and Seed Technology": 160,
        "Plant Physiology and Crop Production": 160,
        "Soil Science and Land Management": 160,
        "Water Resources Management and Agro-meteorology": 160,
        "Wildlife and Eco-tourism Management": 160,
        "Water Sanitation and Hygiene": 160
    },

    "Biological Science": {
        "Biochemistry": 200,
        "Biotechnology": 190,
        "Microbiology": 200,
        "Public Health": 190,
        "Pure and Applied Botany": 180,
        "Pure and Applied Zoology": 180,
        "Science Lab Technology": 190
    },

    "Computing Science": {
        "Computer Science": 200,
        "Cyber Security": 200,
        "Data Science": 200,
        "Information Communication Technology": 200,
        "Information Systems": 200,
        "Information Technology": 200,
        "Software Engineering": 200
    },

    "Food Science and Human Ecology": {
        "Clothing & Textile Design": 180,
        "Food Science and Technology": 200,
        "Home Science and Management": 180,
        "Hospitality and Tourism": 180,
        "Nutrition and Dietetics": 200
    },

    "Physical Science": {
        "Chemistry": 180,
        "Geophysics": 180,
        "Industrial Chemistry": 180,
        "Mathematics": 200,
        "Physics": 200,
        "Statistics": 200
    },

    "Engineering": {
        "Agricultural Engineering": 200,
        "Civil Engineering": 200,
        "Electrical and Electronics Engineering": 200,
        "Mechanical Engineering": 200,
        "Mechatronic Engineering": 200
    },

    "Veterinary Medicine": {
        "Veterinary Medicine": 200
    },

    "Entrepreneurial and Development Studies": {
        "Accounting": 200,
        "Banking and Finance": 200,
        "Business Administration": 200,
        "Cooperative Studies": 160,
        "Development Studies": 160,
        "Economics": 200,
        "Entrepreneurial Studies": 180,
        "Library and Information Science": 180
    }
}


# =========================================================
# SUBJECT LISTS
# =========================================================

ALL_SUBJECTS = [
    "Accounting",
    "Agricultural Science",
    "Biology",
    "Chemistry",
    "Commerce",
    "Computer Studies",
    "Economics",
    "English Language",
    "Further Mathematics",
    "Geography",
    "Government",
    "History",
    "Literature in English",
    "Mathematics",
    "Physics",
    "Social Studies",
    "Technical Drawing"
]


SOCIAL_SCIENCE_SUBJECTS = [
    "Accounting",
    "Commerce",
    "Economics",
    "Geography",
    "Government",
    "History",
    "Social Studies"
]


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_all_courses():

    all_courses = []

    for category in COURSES:

        for course in COURSES[category]:

            all_courses.append(course)

    return sorted(all_courses)


def get_category(course):

    for category in COURSES:

        if course in COURSES[category]:

            return category

    return None


def get_cutoff(course):

    for category in COURSES:

        if course in COURSES[category]:

            return COURSES[category][course]

    return None


def valid_name(name):

    return (
        name.strip() != ""
        and all(
            character.isalpha() or character.isspace()
            for character in name
        )
    )


def calculate_jamb(score):

    return (score / 400) * 60


def calculate_olevel(grades):

    total = 0

    for grade in grades:

        total += GRADE_POINTS[grade]

    return total


def calculate_sitting(sittings):

    if sittings == 1:

        return 10

    return 6


# =========================================================
# SUBJECT COMBINATION CHECKER
# =========================================================

def check_subject_combination(
    category,
    selected_subjects
):

    # -----------------------------------------
    # ENGLISH AND MATHEMATICS
    # -----------------------------------------

    if "English Language" not in selected_subjects:

        return False, (
            "English Language is compulsory."
        )

    if "Mathematics" not in selected_subjects:

        return False, (
            "Mathematics is compulsory."
        )


    # -----------------------------------------
    # MANAGEMENT SCIENCES
    # -----------------------------------------

    if category == "Entrepreneurial and Development Studies":

        if "Economics" not in selected_subjects:

            return False, (
                "Economics is required for Management "
                "and related programmes."
            )

        other_subjects = []

        for subject in selected_subjects:

            if subject not in [
                "English Language",
                "Mathematics",
                "Economics"
            ]:

                if subject in ALL_SUBJECTS:

                    other_subjects.append(subject)

        valid_other_subjects = []

        for subject in other_subjects:

            if (
                subject in SOCIAL_SCIENCE_SUBJECTS
                or subject in [
                    "Biology",
                    "Chemistry",
                    "Physics"
                ]
            ):

                valid_other_subjects.append(subject)

        if len(valid_other_subjects) < 2:

            return False, (
                "You need Economics plus two other "
                "Social Science or Science subjects."
            )

        return True, "Valid Management Science combination."


    # -----------------------------------------
    # AGRICULTURE
    # -----------------------------------------

    if category == "Agriculture":

        if (
            "Biology" not in selected_subjects
            and "Agricultural Science" not in selected_subjects
        ):

            return False, (
                "Biology is required for Agriculture "
                "programmes. Agricultural Science may "
                "be accepted in place of Biology for "
                "Agricultural programmes."
            )

        if "Chemistry" not in selected_subjects:

            return False, "Chemistry is required."

        if "Physics" not in selected_subjects:

            return False, "Physics is required."

        return True, (
            "Valid Agricultural programme combination."
        )


    # -----------------------------------------
    # GENERAL SCIENCE / ENGINEERING /
    # COMPUTING / VETERINARY / FOOD
    # -----------------------------------------

    required_subjects = [
        "English Language",
        "Mathematics",
        "Chemistry",
        "Physics",
        "Biology"
    ]

    missing = []

    for subject in required_subjects:

        if subject not in selected_subjects:

            missing.append(subject)

    if missing:

        return False, (
            "Missing required subject(s): "
            + ", ".join(missing)
        )

    return True, "Valid subject combination."


# =========================================================
# HEADER
# =========================================================

st.title("🎓 FUNAAB Admission Calculator")

st.write(
    "An educational tool for estimating admission "
    "screening components and checking basic "
    "O'Level subject combinations."
)

st.info(
    "This is a student programming project. "
    "It is NOT an official FUNAAB admission decision."
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📋 Main Menu")

menu = st.sidebar.radio(
    "Select an option:",
    [
        "Full Screening Calculator",
        "JAMB Aggregate /60",
        "O'Level Aggregate /30",
        "Check Course Requirements",
        "Available Courses",
        "About"
    ]
)


# =========================================================
# JAMB CALCULATOR
# =========================================================

if menu == "JAMB Aggregate /60":

    st.header("📊 JAMB Aggregate Calculator")

    jamb_score = st.number_input(
        "Enter your JAMB score",
        min_value=0,
        max_value=400,
        value=0,
        step=1
    )

    if st.button(
        "Calculate JAMB Aggregate"
    ):

        aggregate = calculate_jamb(
            jamb_score
        )

        st.success(
            f"JAMB Aggregate: "
            f"{aggregate:.2f} / 60"
        )


# =========================================================
# O'LEVEL CALCULATOR
# =========================================================

elif menu == "O'Level Aggregate /30":

    st.header("📚 O'Level Aggregate Calculator")

    st.write(
        "Select five different O'Level subjects "
        "and enter their grades."
    )

    selected_subjects = []

    selected_grades = []


    for number in range(5):

        col1, col2 = st.columns([2, 1])

        with col1:

            subject = st.selectbox(
                f"Subject {number + 1}",
                ALL_SUBJECTS,
                key=f"olevel_subject_{number}"
            )

        with col2:

            grade = st.selectbox(
                f"Grade {number + 1}",
                list(GRADE_POINTS.keys()),
                key=f"olevel_grade_{number}"
            )

        selected_subjects.append(subject)

        selected_grades.append(grade)


    if st.button(
        "Calculate O'Level Aggregate"
    ):

        if len(set(selected_subjects)) != 5:

            st.error(
                "You cannot select the same subject twice."
            )

        else:

            total = calculate_olevel(
                selected_grades
            )

            st.success(
                f"O'Level Aggregate: "
                f"{total:.2f} / 30"
            )


# =========================================================
# COURSE REQUIREMENTS
# =========================================================

elif menu == "Check Course Requirements":

    st.header("📖 Course Requirements")

    course = st.selectbox(
        "Select a FUNAAB programme",
        get_all_courses()
    )


    category = get_category(course)

    cutoff = get_cutoff(course)


    st.write(
        f"**Programme Category:** {category}"
    )

    st.write(
        f"**2026 UTME minimum shown by FUNAAB:** "
        f"{cutoff}"
    )


    st.divider()


    if category == "Entrepreneurial and Development Studies":

        st.subheader(
            "O'Level Requirement"
        )

        st.write(
            "English Language"
        )

        st.write(
            "Mathematics"
        )

        st.write(
            "Economics"
        )

        st.write(
            "Any two other Social Science or Science subjects"
        )


    elif category == "Agriculture":

        st.subheader(
            "O'Level Requirement"
        )

        st.write(
            "English Language"
        )

        st.write(
            "Mathematics"
        )

        st.write(
            "Chemistry"
        )

        st.write(
            "Physics"
        )

        st.write(
            "Biology"
        )

        st.info(
            "For Agricultural programmes, "
            "a pass in Biology with a credit in "
            "Agricultural Science is acceptable."
        )


    else:

        st.subheader(
            "O'Level Requirement"
        )

        st.write(
            "English Language"
        )

        st.write(
            "Mathematics"
        )

        st.write(
            "Chemistry"
        )

        st.write(
            "Physics"
        )

        st.write(
            "Biology"
        )


# =========================================================
# AVAILABLE COURSES
# =========================================================

elif menu == "Available Courses":

    st.header(
        "🎓 FUNAAB 2026/2027 Programmes"
    )

    st.write(
        f"Total programmes listed: "
        f"**{len(get_all_courses())}**"
    )


    for category in COURSES:

        with st.expander(
            category
        ):

            for course, cutoff in sorted(
                COURSES[category].items()
            ):

                st.write(
                    f"**{course}** — "
                    f"Minimum UTME: {cutoff}"
                )


# =========================================================
# ABOUT
# =========================================================

elif menu == "About":

    st.header(
        "ℹ️ About the Calculator"
    )

    st.markdown(
        """
### Created by

**Arisekola Abdulrahman Ayomide**

**Nickname:** Atomic

### Goal

Aspiring Mechatronic Engineering student.

### Background

Secondary school graduate.

### Interests

Programming • Technology • Engineering

### About the Project

This is a Python programming project designed to
help students estimate JAMB and O'Level screening
components and check basic O'Level subject
requirements.

The project demonstrates Python programming,
input validation, functions, lists, dictionaries,
conditional statements, calculations and web
application development.

**Disclaimer:** This calculator is an educational
project and does not make official admission
decisions.
"""
    )


# =========================================================
# FULL SCREENING CALCULATOR
# =========================================================

elif menu == "Full Screening Calculator":

    st.header(
        "📝 Full Screening Calculator"
    )


    # -----------------------------------------
    # NAME
    # -----------------------------------------

    name = st.text_input(
        "Student Full Name"
    )


    # -----------------------------------------
    # COURSE
    # -----------------------------------------

    course = st.selectbox(
        "Choose your FUNAAB programme",
        ["Select a programme"] + get_all_courses()
    )


    # -----------------------------------------
    # JAMB
    # -----------------------------------------

    jamb_score = st.number_input(
        "JAMB Score",
        min_value=0,
        max_value=400,
        value=0,
        step=1
    )


    # -----------------------------------------
    # SITTINGS
    # -----------------------------------------

    sittings = st.selectbox(
        "O'Level Sittings",
        [1, 2]
    )


    st.subheader(
        "📚 O'Level Results"
    )


    st.write(
        "Select five different subjects and "
        "their grades."
    )


    selected_subjects = []

    selected_grades = []


    for number in range(5):

        col1, col2 = st.columns([2, 1])


        with col1:

            subject = st.selectbox(
                f"Subject {number + 1}",
                ALL_SUBJECTS,
                key=f"full_subject_{number}"
            )


        with col2:

            grade = st.selectbox(
                f"Grade {number + 1}",
                list(GRADE_POINTS.keys()),
                key=f"full_grade_{number}"
            )


        selected_subjects.append(subject)

        selected_grades.append(grade)


    st.divider()


    # -----------------------------------------
    # CALCULATE
    # -----------------------------------------

    if st.button(
        "🚀 Calculate Screening",
        type="primary"
    ):


        # NAME VALIDATION

        if not valid_name(name):

            st.error(
                "Invalid name. Please use letters "
                "and spaces only."
            )

            st.stop()


        # COURSE VALIDATION

        if course == "Select a programme":

            st.error(
                "Please select a FUNAAB programme."
            )

            st.stop()


        # -------------------------------------
        # JAMB MINIMUM CHECK
        # -------------------------------------

        minimum_jamb = get_cutoff(course)


        if jamb_score < minimum_jamb:

            st.error(
                f"Your JAMB score of {jamb_score} "
                f"is below the listed minimum UTME "
                f"score of {minimum_jamb} for "
                f"{course}."
            )

            st.stop()


        # -------------------------------------
        # DUPLICATE SUBJECT CHECK
        # -------------------------------------

        if len(set(selected_subjects)) != 5:

            st.error(
                "You cannot enter the same subject twice."
            )

            st.stop()


        # -------------------------------------
        # SUBJECT COMBINATION
        # -------------------------------------

        category = get_category(course)


        valid, message = check_subject_combination(
            category,
            selected_subjects
        )


        if not valid:

            st.error(
                f"❌ Invalid Subject Combination\n\n"
                f"{message}"
            )

            st.stop()


        # -------------------------------------
        # CALCULATIONS
        # -------------------------------------

        jamb_component = calculate_jamb(
            jamb_score
        )


        olevel_component = calculate_olevel(
            selected_grades
        )


        sitting_component = calculate_sitting(
            sittings
        )


        final_aggregate = (
            jamb_component
            + olevel_component
            + sitting_component
        )


        # -------------------------------------
        # ESTIMATE
        # -------------------------------------

        if final_aggregate >= 72:

            status = "🌟 HIGH ESTIMATE"

        elif final_aggregate >= 62:

            status = "⚖️ MEDIUM ESTIMATE"

        elif final_aggregate >= 50:

            status = "🟡 LOW-MEDIUM ESTIMATE"

        else:

            status = "⚠️ LOW ESTIMATE"


        # -------------------------------------
        # REPORT
        # -------------------------------------

        st.success(
            "Screening calculation completed!"
        )


        st.subheader(
            "📄 Screening Report"
        )


        st.write(
            f"**Student:** {name.title()}"
        )


        st.write(
            f"**Programme:** {course}"
        )


        st.write(
            f"**Category:** {category}"
        )


        st.write(
            f"**JAMB Score:** {jamb_score}/400"
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "JAMB Component",
                f"{jamb_component:.2f}/60"
            )


        with col2:

            st.metric(
                "O'Level Component",
                f"{olevel_component:.2f}/30"
            )


        with col3:

            st.metric(
                "Sitting Component",
                f"{sitting_component:.2f}/10"
            )


        st.divider()


        st.metric(
            "FINAL AGGREGATE",
            f"{final_aggregate:.2f}/100"
        )


        st.info(
            f"Admission Estimate: **{status}**"
        )


        st.caption(
            "This aggregate is based on the scoring "
            "model used in this student project. "
            "It is not an official FUNAAB admission "
            "calculation or guarantee."
        )