"""
CSIT 349 - Applied AI | Autobiography and Portfolio (Streamlit)

Run with:  streamlit run app.py

HOW TO MAKE THIS YOURS
Everything personal lives in the "YOUR CONTENT" block just below.
Look for the  EDIT  comments. The grading rubric says the writing and the
projects must be your own words, so rewrite the bio, milestones, and project
descriptions in your own voice before you submit.
"""

from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Joshua Dave G. Abella | Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

FULL_NAME = "Joshua Dave G. Abella"
SECTION = "CSIT 349 - G01"
PROGRAM = "BS Information Technology"
YEAR_LEVEL = "3rd Year"
SCHOOL = "Cebu Institute of Technology - University"
LOCATION = "Cebu City, Philippines"
TAGLINE = "Full-stack and Android developer in the making"

GITHUB_URL = "github.com/joshuadaveabella"
EMAIL = "joshuadave.abella@cit.edu"
LINKEDIN_URL = ""

HERE = Path(__file__).parent
PHOTO = HERE / "assets" / "profile.jpg"
PLACEHOLDER = HERE / "assets" / "img20240207_19053676(edited).jpg"

BIO = """
I'm a third-year BS Information Technology student in Cebu City, Philippines.
I like building things people can actually use, from a canteen pre-ordering
system for my campus to an Android attendance app that uses biometrics.

Outside the classroom I work as a scholar in my university's Safety and
Security Department, and I completed my on-the-job training at an IT retailer.
Those two experiences taught me how to deal with real users and real deadlines.
"""

MILESTONES = [
    ("Junior High School", "Graduated with high honors. This is where I learned that "
                           "steady effort beats last-minute cramming."),
    ("Senior High School", "Completed senior high school in Cebu and chose the "
                           "path that led me to IT."),
    ("College (BSIT)", "Now in third year, working across web, Android, and "
                       "capstone projects."),
    ("Working Scholar", "Supporting my university's Safety and Security Department "
                        "while studying."),
    ("On-the-Job Training", "Completed my OJT at an IT retailer."),
]

INTERESTS = {
    "Full-stack web": "React on the front, Spring Boot and MySQL on the back. "
                      "I enjoy wiring forms to real endpoints.",
    "Android": "Kotlin and the MVP pattern. BioAttend taught me to keep UI "
               "and logic separate.",
    "Entrepreneurship": "Pitching app ideas like CoinControl in Technopreneurship "
                        "made me think about users first.",
    "Applied AI": "Currently exploring data analysis and machine learning in CSIT 349.",
    "Fitness": "I follow structured Push/Pull/Legs training. Consistency again.",
}

SKILLS = [
    ("Java", "Backend", 7),
    ("Spring Boot", "Backend", 7),
    ("MySQL", "Backend", 6),
    ("React", "Frontend", 7),
    ("JavaScript", "Frontend", 7),
    ("Kotlin", "Mobile", 6),
    ("PHP", "Backend", 5),
    ("Python", "Data / AI", 5),
    ("Git and GitHub", "Tools", 6),
    ("Streamlit", "Data / AI", 4),
]

PROJECTS = [
    {
        "title": "Palit Daan - Canteen Pre-ordering System",
        "role": "Full-stack developer (capstone team)",
        "tools": ["React", "Spring Boot", "MySQL", "Git and GitHub"],
        "outcome": "Capstone project for my campus: students pre-order from the "
                   "canteen. I built the Sign Up, Login, and Profile pages and "
                   "connected them to the backend auth and user endpoints.",
        "status": "Presented",
        "link": "https://github.com/mhalnicole/csit321-appdev-wanmilyon.git",
    },
    {
        "title": "BioAttend - Biometric Attendance",
        "role": "Android developer",
        "tools": ["Kotlin", "Android", "MVP architecture"],
        "outcome": "An Android attendance app that uses biometrics. I applied the "
                   "MVP architecture and prepared the presentation and demo.",
        "status": "Presented",
        "link": "",
    },
    {
        "title": "Session-based Login System",
        "role": "Full-stack developer",
        "tools": ["React", "Spring Boot", "MySQL", "Git and GitHub"],
        "outcome": "A working sign-up and login flow with session-based "
                   "authentication. I fixed database driver and connection issues "
                   "along the way and published the code on GitHub.",
        "status": "Completed",
        "link": "",
    },
    {
        "title": "CoinControl - Budget Tracker Pitch",
        "role": "Pitch team member (Technopreneurship)",
        "tools": ["Mobile app concept", "Pitch deck"],
        "outcome": "A mobile budget-tracker concept pitched for my "
                   "Technopreneurship course with my group.",
        "status": "Presented",
        "link": "",
    },
    {
        "title": "PathFinder - Campus Navigation",
        "role": "Developer / presenter",
        "tools": ["PHP", "Web"],
        "outcome": "A campus navigation system demo that helps people find "
                   "their way around.",
        "status": "Demoed",
        "link": "",
    },
]

FUN_FACTS = [
    "I work as a scholar while studying full time.",
    "I follow a Push/Pull/Legs workout split.",
    "My favorite debugging companion is the browser console.",
]


if "messages" not in st.session_state:
    st.session_state.messages = []
if "kudos" not in st.session_state:
    st.session_state.kudos = 0


@st.cache_data
def load_skills() -> pd.DataFrame:
    """Turn the SKILLS list into a table. Cached so it only builds once."""
    return pd.DataFrame(SKILLS, columns=["Skill", "Category", "Level"])


def tool_counts() -> pd.DataFrame:
    """Count how many projects use each tool."""
    counts = {}
    for project in PROJECTS:
        for tool in project["tools"]:
            counts[tool] = counts.get(tool, 0) + 1
    table = pd.DataFrame(list(counts.items()), columns=["Tool", "Projects"])
    return table.sort_values("Projects", ascending=False).set_index("Tool")


def bio_text() -> str:
    """Plain-text version of the autobiography for the download button."""
    lines = [FULL_NAME, f"{PROGRAM}, {YEAR_LEVEL} - {SCHOOL}", SECTION, "", BIO.strip(), ""]
    lines.append("MILESTONES")
    for title, text in MILESTONES:
        lines.append(f"- {title}: {text}")
    lines.append("")
    lines.append("PROJECTS")
    for p in PROJECTS:
        lines.append(f"- {p['title']} ({p['role']}): {p['outcome']}")
    return "\n".join(lines)


skills_df = load_skills()


with st.sidebar:
    st.image(str(PHOTO if PHOTO.exists() else PLACEHOLDER), width="stretch")
    if not PHOTO.exists():
        st.caption("")
    st.markdown(f"### {FULL_NAME}")
    st.caption(f"{PROGRAM} - {YEAR_LEVEL}")
    st.caption(SECTION)

    st.divider()
    st.subheader("Make it yours")
    greeting_lang = st.selectbox(
        "Greeting language", ["English", "Cebuano", "Filipino"]
    )
    accent = st.color_picker("Accent color", "#0F766E")
    show_facts = st.checkbox("Show fun facts", value=True)

    st.divider()
    if st.button("Give kudos 👏", width="stretch"):
        st.session_state.kudos += 1
        st.toast("Thanks for the kudos!", icon="🎉")
    st.caption(f"Kudos this session: {st.session_state.kudos}")

    if GITHUB_URL:
        st.link_button("GitHub", GITHUB_URL, width="stretch")
    if LINKEDIN_URL:
        st.link_button("LinkedIn", LINKEDIN_URL, width="stretch")


GREETINGS = {"English": "Hello, I'm", "Cebuano": "Maayong adlaw, ako si", "Filipino": "Magandang araw, ako si"}

st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {accent}, #10231F);
                padding: 2.2rem 2rem; border-radius: 18px; color: white;">
        <div style="font-size: 1.05rem; opacity: .85;">{GREETINGS[greeting_lang]}</div>
        <div style="font-size: 3rem; font-weight: 800; line-height: 1.1;">{FULL_NAME}</div>
        <div style="font-size: 1.15rem; margin-top: .4rem;">{TAGLINE}</div>
        <div style="font-size: .95rem; margin-top: .8rem; opacity: .85;">
            {PROGRAM} · {YEAR_LEVEL} · {SCHOOL} · {SECTION}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Year level", YEAR_LEVEL)
m2.metric("Projects showcased", len(PROJECTS))
m3.metric("Skills tracked", len(skills_df))
m4.metric("Kudos", st.session_state.kudos)

st.write("")

tab_about, tab_skills, tab_projects, tab_contact = st.tabs(
    ["👤 Autobiography", "🛠️ Skills", "🚀 Projects", "✉️ Contact"]
)


with tab_about:
    left, right = st.columns([3, 2], gap="large")

    with left:
        st.header("About me")
        st.write(BIO)

        st.subheader("My journey")
        for title, text in MILESTONES:
            with st.expander(title):
                st.write(text)

    with right:
        st.subheader("Interests")
        chosen = st.selectbox("Pick an interest to learn more", list(INTERESTS))
        st.info(INTERESTS[chosen])

        st.subheader("Quick facts")
        st.markdown(
            f"- **Program:** {PROGRAM}\n"
            f"- **Year:** {YEAR_LEVEL}\n"
            f"- **School:** {SCHOOL}\n"
            f"- **Based in:** {LOCATION}"
        )

        if show_facts:
            st.subheader("Fun facts")
            for fact in FUN_FACTS:
                st.markdown(f"- {fact}")

with tab_skills:
    st.header("Skills")
    st.caption("Self-rated from 1 to 10. Use the filters to explore.")

    f1, f2 = st.columns(2)
    categories = f1.multiselect(
        "Category",
        sorted(skills_df["Category"].unique()),
        default=sorted(skills_df["Category"].unique()),
    )
    min_level = f2.slider("Minimum level", 1, 10, 1)

    filtered = skills_df[
        skills_df["Category"].isin(categories) & (skills_df["Level"] >= min_level)
    ].sort_values("Level", ascending=False)

    if filtered.empty:
        st.warning("No skills match those filters. Try lowering the minimum level.")
    else:
        t_col, c_col = st.columns([1, 1], gap="large")
        with t_col:
            st.dataframe(
                filtered,
                hide_index=True,
                width="stretch",
                column_config={
                    "Level": st.column_config.ProgressColumn(
                        "Level", min_value=0, max_value=10, format="%d / 10"
                    )
                },
            )
        with c_col:
            st.bar_chart(filtered.set_index("Skill")["Level"], color=accent)

        top = filtered.iloc[0]
        st.success(f"Strongest in this view: **{top['Skill']}** ({top['Level']}/10)")

    st.subheader("Currently learning")
    st.progress(40, text="Applied AI and Streamlit (CSIT 349)")

with tab_projects:
    st.header("Projects")

    all_tools = sorted({tool for p in PROJECTS for tool in p["tools"]})
    p1, p2, p3 = st.columns([3, 2, 1])
    picked_tools = p1.multiselect("Filter by tool", all_tools)
    layout = p2.radio("Layout", ["Cards", "Table"], horizontal=True)
    show_outcomes = p3.checkbox("Show outcomes", value=True)

    shown = [
        p for p in PROJECTS
        if not picked_tools or any(tool in p["tools"] for tool in picked_tools)
    ]
    st.caption(f"Showing {len(shown)} of {len(PROJECTS)} projects")

    if layout == "Cards":
        for project in shown:
            with st.container(border=True):
                head, status = st.columns([4, 1])
                head.subheader(project["title"])
                status.markdown(f":green-badge[{project['status']}]")
                st.markdown(f"**Role:** {project['role']}")
                st.markdown(" ".join(f":blue-badge[{t}]" for t in project["tools"]))
                if show_outcomes:
                    st.write(project["outcome"])
                if project["link"]:
                    st.link_button("View project", project["link"])
    else:
        table = pd.DataFrame(
            [
                {
                    "Project": p["title"],
                    "Role": p["role"],
                    "Tools": ", ".join(p["tools"]),
                    "Status": p["status"],
                    **({"Outcome": p["outcome"]} if show_outcomes else {}),
                }
                for p in shown
            ]
        )
        st.dataframe(table, hide_index=True, width="stretch")

    st.subheader("Tools across my projects")
    st.bar_chart(tool_counts(), color=accent, horizontal=True)

with tab_contact:
    st.header("Say hello")
    c_left, c_right = st.columns([3, 2], gap="large")

    with c_left:
        with st.form("contact_form", clear_on_submit=True):
            n1, n2 = st.columns(2)
            visitor_name = n1.text_input("Your name")
            visitor_email = n2.text_input("Your email")
            topic = st.selectbox(
                "Topic", ["Feedback on this site", "Project collaboration", "Just saying hi"]
            )
            found_via = st.radio(
                "How did you find this page?",
                ["Class", "Friend", "Search", "Other"],
                horizontal=True,
            )
            message = st.text_area("Message", height=140, max_chars=500)
            rating = st.slider("Rate this site", 1, 5, 4)
            ok_to_reply = st.checkbox("It's okay to reply to my email")
            sent = st.form_submit_button("Send message", type="primary")

        if sent:
            if not visitor_name.strip() or not message.strip():
                st.error("Please enter your name and a message.")
            elif visitor_email and "@" not in visitor_email:
                st.error("That email doesn't look right. Please check it.")
            else:
                st.session_state.messages.append(
                    {
                        "Name": visitor_name.strip(),
                        "Topic": topic,
                        "Found via": found_via,
                        "Rating": rating,
                        "Message": message.strip(),
                    }
                )
                st.success(f"Thanks, {visitor_name.strip()}! Your message was received.")
                st.toast("Message sent", icon="✅")
                st.balloons()
        st.caption("Messages stay in this browser session. Nothing is emailed or stored elsewhere.")

    with c_right:
        st.subheader("Other ways to reach me")
        st.markdown(f"📍 {LOCATION}")
        if EMAIL:
            st.markdown(f"📧 {EMAIL}")
        if GITHUB_URL:
            st.markdown(f"💻 [GitHub]({GITHUB_URL})")
        if not (EMAIL or GITHUB_URL):
            st.caption("Use the form to get in touch.")

        st.subheader("Download")
        st.download_button(
            "Download my bio (.txt)",
            data=bio_text(),
            file_name="joshuadaveabella_bio.txt",
            mime="text/plain",
            width="stretch",
        )

    if st.session_state.messages:
        st.subheader("Messages this session")
        inbox = pd.DataFrame(st.session_state.messages)
        st.dataframe(inbox, hide_index=True, width="stretch")
        st.download_button(
            "Download messages (.csv)",
            data=inbox.to_csv(index=False),
            file_name="messages.csv",
            mime="text/csv",
        )

st.divider()
st.caption(f"{FULL_NAME} · {SECTION} · CSIT 349 Applied AI · Built with Streamlit")