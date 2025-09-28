#import the neccessary libraries
import streamlit as st

def run_storytelling():
    st.title("📖 Collaborative Storytelling")

    #initialize a dictionary in session state to store all chapter info
    #each chapter is stored with keys: title, writer, story, illustrator, and art
    if "chapters" not in st.session_state:
        st.session_state.chapters = {}  # {chapter_number: {"title": str, "writer": str, "story": str, "illustrator": str, "art": file}}
    #create four tabs: Write, Illustrate, Story, Contributors
    tabs = st.tabs(["✍️ Write", "🎨 Illustrate", "📚 Story", "👥 Contributors"])

    # WRITE TAB
    with tabs[0]:
        st.subheader("Write a Chapter")
        #ask for the writers name
        name = st.text_input("Your name (or alias)")
        #ask which chapter number (1–10) they want to write
        chapter_number = st.selectbox("Select a Chapter Number", [f"Chapter {i}" for i in range(1, 11)])
        #writer chooses a title for the chapter
        chapter_title = st.text_input("Select a Chapter Title")
        #writer inputs their short story directly (or via upload)
        story = st.text_area("Your short story (max 500 words)", max_chars=3000)
        #allow file upload as alternative story submission (.txt or .md)
        file = st.file_uploader("Or upload a .txt/.md file", type=["txt", "md"])
        #handle the submit
        if st.button("Submit Story ✍️"):
            if not name.strip():
                st.error("Please enter your name or alias before submitting.")
            elif not chapter_title.strip():
                st.error("Please enter a chapter title before submitting.")
            elif not story.strip() and not file:
                st.error("Please write a story or upload a file before submitting.")
            else:
                # Handle optional file text
                if file:
                    story = file.read().decode("utf-8")

                st.session_state.chapters[chapter_number] = {
                    "title": chapter_title.strip(),
                    "writer": name.strip(),
                    "story": story.strip(),
                    "illustrator": None,
                    "art": None
                }
                st.success(f"✅ Chapter saved: [{chapter_number}] - {chapter_title} by {name}")

    # ILLUSTRATE TAB
    with tabs[1]:
        st.subheader("Illustrate a Chapter")

        #build dropdown options: show only chapters that already have a story
        available_chapters = {
            f"[{num}] - {info['title']}": num
            for num, info in st.session_state.chapters.items()
            if info.get("story")
        }

        if available_chapters:
            #select which chapter to illustrate
            choice = st.selectbox("Choose a Chapter to Illustrate", list(available_chapters.keys()))
            selected_number = available_chapters[choice]
            chapter_info = st.session_state.chapters[selected_number]

            #display the story text so illustrators know the content
            st.write(f"### {selected_number}: {chapter_info['title']}")
            st.write(chapter_info["story"])

            #mandatory illustrator name
            illustrator_name = st.text_input("Your name (or alias) as illustrator")
            #allow artwork upload (optional)
            art = st.file_uploader("Upload Your Artwork", type=["png", "jpg", "jpeg"])

            if st.button("Submit Artwork 🎨"):
                if not illustrator_name.strip():
                    st.error("Please enter your name or alias before submitting.")
                else:
                    chapter_info["illustrator"] = illustrator_name.strip()
                    if art:  #only save if the art is uploaded
                        chapter_info["art"] = art
                        st.success(f"✅ Artwork submitted for {choice} by {illustrator_name} (with artwork)")
                    else:
                        st.success(f"✅ Artwork submitted for {choice} by {illustrator_name} (no artwork uploaded)")


        else:
            st.info("No chapters available yet. Writers need to submit first.")


    
    # STORY TAB
    with tabs[2]:
        st.subheader("Our Shared Story")
        #filter only completed chapters (story + illustrator required)
        completed = [
            (num, info) for num, info in st.session_state.chapters.items()
            if info.get("story") and info.get("illustrator")
        ]
        if completed:
            for num, info in completed:
                #show chapter number, title, and story
                st.write(f"## {num}: {info['title']}")
                st.write(info["story"])
                #show artwork if uploaded, otherwise only note illustrator’s name
                if info.get("art"):
                    st.image(info["art"], caption=f"Illustration by {info['illustrator']}")
                else:
                    st.info(f"(No artwork uploaded yet — illustrated by {info['illustrator']})")
                st.markdown("---")
        else:
            st.info("No completed chapters yet. Stories and illustrators need to be submitted first.")


    # CONTRIBUTORS TAB 
    with tabs[3]:
        st.subheader("Contributors")
        #separate contributors into writers and illustrators lists
        writers = []
        illustrators = []
        for num, info in st.session_state.chapters.items():
            if info.get("writer"):
                writers.append(f"✍️ {info['writer']} – {num}: {info['title']}")
            if info.get("illustrator"):
                illustrators.append(f"🎨 {info['illustrator']} – {num}: {info['title']}")
        #display writers section if any
        if writers:
            st.write("### Writers")
            for w in writers:
                st.write(w)
        #display illustrators section if any
        if illustrators:
            st.write("### Illustrators")
            for i in illustrators:
                st.write(i)
        #show placeholder message if no contributors exist
        if not writers and not illustrators:
            st.info("No contributors yet.")
