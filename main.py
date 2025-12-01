import streamlit as st
from st_social_media_links import SocialMediaIcons
from badges import badge_dict
import pandas as pd
import json
from spotify import show_spotify_playlist
import uuid

st.set_page_config(page_title="Juana Wong | Portfolio", layout="wide")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sintony&display=swap');
    .block-container {
        padding-top: 1rem;
    }
    html, body, [class*="css"] {
        font-family: 'Sintony', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

## -- summary
st.title("Juana Wong")

col1, col2, col3 = st.columns([0.9, 0.1, 4])

with col1:
    links = [
        "https://github.com/wong-ja",
        "https://linkedin.com/in/wongjuanaa",
        "https://twitter.com/wong8ja",
        # "wong-ja.github.io",
        "wong-ja.streamlit.app/",
        "https://huggingface.co/wong-ja",
    ]

    colors = ["#f63366", "#6f452eff", "#f63366", "#6f452eff", "#f63366"]
    social_media_icons = SocialMediaIcons(links, colors)
    social_media_icons.render()

    st.write("")

with col3:
    comfort_keys = ["Python", "SQL", "Pandas", "NumPy", "Streamlit", "Jupyter Notebooks", "Git", "Github"]
    badges_comfort = [badge_dict[k] for k in comfort_keys if k in badge_dict]
    comfort = " ".join(badges_comfort)
    st.markdown(comfort, unsafe_allow_html=True)

st.markdown("___")



## -- tabs
st.markdown("""
<style>
.stTabs [data-baseweb="tab-list"] {
    display: flex;
    justify-content: space-between;
}
.stTabs [data-baseweb="tab"] {
    flex: 1 1 0;
    text-align: center;
}
.stTabs [data-baseweb="tab-list"] button[data-baseweb="tab"] p {
    font-size: 18px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

tabs = st.tabs(["About Me", "Education", "Work Experience", "Projects", "Resume"])



with tabs[0]:
    col1, spc, col2 = st.columns([1, 0.1, 3])
    with col1:
        st.image("images/dream.webp", width='stretch')
    with col2:
        st.subheader("Hello, I'm Juana.")
        # st.markdown("CS @ CCNY | CTP Data Science Fellow | Aspiring Data Scientist")
        st.write("")
        st.markdown("My technical interests broadly span android development, web development, and **data analytics + data science**.")
        spc, col, spc = st.columns([1,2,1])
        with col:
            lines = ["I look and look", "Looking's a way of being: one becomes", "sometimes, a pair of eyes walking.", "Walking wherever looking takes one."]
            for line in lines:
                st.markdown(f'<p style="font-family: Georgia, serif;">{line}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-family: Georgia, serif; text-align: center;"> — Denise Levertov</p>', unsafe_allow_html=True)
        st.write("")
        st.markdown("**Things I enjoy**: stories, insights & jamming out to my own playlists. I also like visiting parks & museums.")
        # st.markdown("NYC-native, book-lover, orange-eater.")
        # st.markdown("ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧𐦯 _ _ ")
    
    st.divider()

    playlist_ids = {
        "2025" : "3tPSgqZWq4nw7jqE25sHer?si=ac2c7a7abdd74a25",
        "2024" : "53Nr8oc4a6NjSWIC4bHM10?si=Dk6ko3q_TY-djhjfPdJS3g",
    }

    cols = st.columns(len(playlist_ids))
    for col, (year, playlist_id) in zip(cols, playlist_ids.items()):
        with col:
            st.write(year)
            show_spotify_playlist(playlist_id)

    # st.divider()
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.markdown(f"PROMETHEAN - Vol. 52 - Spring 2025")
    #     promethean_2025 = "https://drive.google.com/file/d/1KbZCquCkE41d1zrkKXYiaaaANx0v154I/view"
    #     promethean_2025_img = "https://images.squarespace-cdn.com/content/v1/5bd619458d97407cf3c1a9cc/1747268121908-5VT9H71E3YNHQZN7H71Z/Promethean+2025+Cover+Image.png?format=1500w"
    #     st.markdown(
    #         f"""
    #         <a href="{promethean_2025}" target="_blank">
    #             <img src="{promethean_2025_img}" style="max-width:100%; height:auto;" />
    #         </a>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    st.markdown("---")



with tabs[1]:
    col1, spc, col2, spc, col3 = st.columns([1, 0.1, 1, 0.1, 1])
    with col1:
        st.subheader("Education")
        # - Degree 1, Institution, Graduation Year  
        # - Awards, Honors, Scholarships  
        st.write("")
        ccny_url = "https://www.ccny.cuny.edu"
        ccny_img = "https://www.ccny.cuny.edu/sites/default/files/inline-images/Grove%20G%20Logo%20%2B%20CCNY%20Nameplate%204-19.jpg"
        st.markdown(
            f"""
            <a href="{ccny_url}" target="_blank">
                <img src="{ccny_img}" style="max-width:300px height:auto;" />
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.divider()
        st.markdown("""
        **Computer Science, B.S.** \n\n Mathematics minor \n\n Expected December 2025
        """)

    with col2:
        st.subheader("Fellowships")
        st.write("")
        ctp_url = "https://cunytechprep.org/"
        ctp_img = "https://cunytechprep.org/_next/static/media/ctp-logo-square.6a1210b7.png"
        st.markdown(
            f"""
            <a href="{ctp_url}" target="_blank">
                <img src="{ctp_img}" style="max-width:300px; height:auto;" />
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.divider()
        st.markdown("""
        **Data Science Fellow** \n\n Cohort 11 \n\n July 2025 - Present
        """)

    with col3:
        # st.markdown("---")
        st.subheader("Certifications")
        # - Certification 1, Issuing Organization, Date  
        st.write("")
        st.write("")
        codepath_url = "https://www.codepath.org/"
        codepath_img = "https://www.codepath.org/hs-fs/hubfs/logoblack.png?width=1406&height=131&name=logoblack.png"
        st.markdown(
            f"""
            <a href="{codepath_url}" target="_blank">
                <img src="{codepath_img}" style="max-width:300px; height:auto;" />
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.divider()
        st.markdown("""
        [Intro to Android Development](https://drive.google.com/file/d/1UdeHKtmsAjHqIjGjB6Iolis5TndpUGar/view?usp=sharing) \n\n Summer 2025
        """)



with tabs[2]:
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




with tabs[3]:
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
            # proj title, hyperlink, timeframe
            st.markdown(f"#### [{row['title']}]({row['url']})")
            st.caption(f"{row['timeframe']}")
            # image
            st.image(f"images/{row['image']}", width='stretch')
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




with tabs[4]:
    st.subheader("Resume")
    st.markdown(">Last updated: October 2025")

    with open("resume.pdf", "rb") as f:
        pdf_bytes = f.read()
        st.pdf(pdf_bytes, height=650)
    spc, col, spc = st.columns([1,1,1])
    with col:
        btn = st.download_button(
            label="Download Resume PDF",
            data=pdf_bytes,
            file_name="resume.pdf",
            mime="application/pdf",
            key=f"download_{uuid.uuid4()}",
            width='stretch'
        )