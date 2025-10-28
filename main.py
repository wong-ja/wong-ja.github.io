import streamlit as st
from st_social_media_links import SocialMediaIcons
from st_tabs import TabBar
from badges import badge_dict
import pandas as pd
import json
from spotify import show_spotify_playlist

st.set_page_config(page_title="My Portfolio", layout="wide")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sintony&display=swap');

    html, body, [class*="css"] {
        font-family: 'Sintony', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


badges_comfort = """
<img src="https://img.shields.io/badge/Python-hsl%28216%2C60%25%2C70%25%29?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/SQL-hsl%28210%2C10%25%2C70%25%29?style=for-the-badge&logo=sqlite&logoColor=black" alt="SQL" />

<img src="https://img.shields.io/badge/Pandas-hsl%280%2C0%25%2C85%25%29?style=for-the-badge&logo=pandas&logoColor=black" alt="Pandas" />
<img src="https://img.shields.io/badge/NumPy-hsl%28210%2C50%25%2C70%25%29?style=for-the-badge&logo=numpy&logoColor=black" alt="NumPy" />
<img src="https://img.shields.io/badge/Seaborn-hsl%28150%2C40%25%2C70%25%29?style=for-the-badge&logo=seaborn&logoColor=black" alt="Seaborn" />
<img src="https://img.shields.io/badge/Jupyter_Notebooks-hsl%2830%2C80%25%2C70%25%29?style=for-the-badge&logo=jupyter&logoColor=black" alt="Jupyter Notebooks" />

<img src="https://img.shields.io/badge/Git-FFE5B4?style=for-the-badge&logo=git&logoColor=F05032" alt="Git" />
<img src="https://img.shields.io/badge/GitHub-hsl%280%2C0%25%2C85%25%29?style=for-the-badge&logo=github&logoColor=black" alt="GitHub" />

"""


## -- summary
st.title("Juana Wong")

col1, col2, col3 = st.columns([0.9, 0.1, 4])

with col1:
    links = [
        "https://github.com/wong-ja",
        "https://linkedin.com/in/wongjuanaa",
        "https://twitter.com/wong8ja",
        # "wong-ja.github.io",
        "wong-ja.streamlit.app/"
    ]

    colors = ["#f63366", "#6f452eff", "#f63366", "#6f452eff"]
    social_media_icons = SocialMediaIcons(links, colors)
    social_media_icons.render()

    st.write("")
    st.markdown("NYC-native, book-lover, orange-eater.")

with col3:
    st.markdown("""
    CS @ CCNY | CTP Data Science Fellow | Aspiring Data Scientist & Machine Learning Engineer
    """)
    st.markdown(badges_comfort, unsafe_allow_html=True)

st.markdown("___")



## -- tabs
tab = TabBar(
    tabs=["Education", "Work Experience", "Projects", "Resume", "Socials", "Miscellaneous", "About Me"],
    default=0,
    fontSize="18px",
    fontWeight="600",
    color="#6f452eff",
    activeColor="#f63366",
)


if tab == 0:
    st.subheader("Education")
    # - Degree 1, Institution, Graduation Year  
    # - Awards, Honors, Scholarships  
    st.markdown("""
    - **Computer Science, B.S.** | Mathematics minor | [The City College of New York (CCNY)](https://www.ccny.cuny.edu) | Expected December 2025
    """)

    # st.markdown("---")
    st.subheader("Fellowships")
    st.markdown("""
    - **Data Science Fellow** | Cohort 11 | [CUNY Tech Prep (CTP)](https://cunytechprep.org/) | July 2025 - Present
    """)

    # st.markdown("---")
    st.subheader("Certifications")
    # - Certification 1, Issuing Organization, Date  
    st.markdown("""
    - [Intro to Android Development](https://bit.ly/w8jacpand101) | [Codepath](https://www.codepath.org/) | Summer 2025
    """)



if tab == 1:
    st.subheader("Work Experience")
    df = pd.read_csv("data/work_experience.csv")
    st.markdown("")

    for _, row in df.iterrows():
        # job title, company, timeframe
        expander_label = f"{row['JobTitle']} @ **{row['Company']}** __🕰️__ {row['StartDate']} - {row['EndDate']}"

        with st.expander(expander_label, expanded=True):

            col1, col2, col3 = st.columns([3, 4.5, 1.5])

            with col1:
                st.markdown(f"###### {row['JobTitle']}")
            with col2:
                st.markdown(f"*{row['Company']}*")
            with col3:
                st.markdown(f"_{row['StartDate']} - {row['EndDate']}_")

            # XYZ bullet points
            if pd.notna(row['Accomplishments']):
                accomplishments = row['Accomplishments'].split(';')
                for item in accomplishments:
                    st.markdown(f"- {item.strip()}")

            # tech stack / skills
            if pd.notna(row['Skills']):
                skills_list = [skill.strip() for skill in row['Skills'].split(',')]
                badges_html = " ".join(badge_dict.get(skill, "") for skill in skills_list)
                st.markdown(badges_html, unsafe_allow_html=True)




if tab == 2:
    st.subheader("Projects")
    df = pd.read_csv("data/projects.csv", sep=";")
    
    techs = st.multiselect(
        "Search technologies:",
        options=list(badge_dict.keys()),
        default=[]
    )
    st.write("")

    if techs:
        df = df[df['technologies'].apply(lambda x: any(t.lower() in x.lower() for t in techs))]

    col1, spacer1, col2, spacer2, col3 = st.columns([1, 0.05, 1, 0.05, 1])
    columns = [col1, col2, col3]

    for idx, row in df.iterrows():
        col_idx = idx % 3
        with columns[col_idx]:
            # proj title, hyperlink
            st.markdown(f"#### [{row['title']}]({row['url']})")
            # image
            st.image(f"images/{row['image']}", use_container_width=True)
            # description
            st.write(row["description"])
            # other/supplemental links
            if pd.notna(row.get('supplemental_links', None)):
                try:
                    supp_links = json.loads(row['supplemental_links'])
                    for name, link in supp_links.items():
                        st.markdown(f"[{name}]({link})  ")
                except json.JSONDecodeError:
                    st.write("Invalid supplemental links data.")
            # tech stack
            if pd.notna(row['technologies']):
                skills_list = [skill.strip() for skill in row['technologies'].split(',')]
                badges_html = " ".join(badge_dict.get(skill, "") for skill in skills_list)
                st.markdown(badges_html, unsafe_allow_html=True)

            st.write("")




if tab == 3:
    st.subheader("Resume")
    st.markdown(">Last updated: October 2025")
    with open("resume.pdf", "rb") as f:
        pdf_bytes = f.read()
        st.pdf(pdf_bytes)
    btn = st.download_button(
        label="Download Resume PDF",
        data=pdf_bytes,
        file_name="resume.pdf",
        mime="application/pdf"
    )



if tab == 4:
    st.subheader("Socials")
    # links = [
    #     "https://github.com/wong-ja",
    #     "https://linkedin.com/in/wongjuanaa",
    #     "https://twitter.com/wong8ja",
    #     "wong-ja.github.io",
    #     "wong-ja.streamlit.app/"
    # ]
    st.markdown("\n".join([f"- [{link}]({link})" for link in links]), unsafe_allow_html=True)
    st.write("")

    st.markdown("---")



if tab == 5:
    st.subheader("Miscellaneous")
    st.markdown("---")

    # st.markdown(badge_dict, unsafe_allow_html=True)
    st.write("")

    playlist_ids = {
        "2025" : "3tPSgqZWq4nw7jqE25sHer?si=ac2c7a7abdd74a25",
        "2024" : "53Nr8oc4a6NjSWIC4bHM10?si=Dk6ko3q_TY-djhjfPdJS3g",
    }

    cols = st.columns(len(playlist_ids))
    for col, (year, playlist_id) in zip(cols, playlist_ids.items()):
        with col:
            st.write(year)
            show_spotify_playlist(playlist_id)

    st.markdown("---")


if tab == 6:
    col1, col2 = st.columns([1,3])
    with col1:
        st.image("images/dream.webp")
    with col2:
        st.subheader("Hello, I'm Juana.")
        st.write("")
        st.markdown("My technical interests broadly span android development, web development, and **data analytics + data science**.")
        st.markdown(">“Reading is a conversation. All books talk. But a good book listens as well.” — Mark Haddon")
        st.write("")
        st.markdown("**Things I enjoy**: stories, insights & jamming out to my own playlists. I also like visiting parks & museums.")
        # st.markdown("I mostly use **YouTube**, so I'm not really on social media.")
        st.markdown("ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧𐦯 _ _ ")

