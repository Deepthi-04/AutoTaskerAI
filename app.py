import streamlit as st
from planner import create_plan
from executor import execute_plan

st.set_page_config(page_title="AutoTasker AI", page_icon="🤖")

st.title("🤖 AutoTasker AI")
st.subheader("A simple Agentic AI project")

goal = st.text_input("Enter your goal:")
text = st.text_area("Paste your content here:", height=250)

if st.button("Run Agent"):
    if goal.strip() == "" or text.strip() == "":
        st.warning("Please enter both goal and content.")
    else:
        plan = create_plan(goal)
        memory = execute_plan(goal, plan, text)

        st.success("Agent execution completed.")

        st.markdown("## User Goal")
        st.write(memory["goal"])

        st.markdown("## Generated Plan")
        for i, task in enumerate(memory["plan"], start=1):
            st.write(f"{i}. {task}")

        st.markdown("## Results")
        results = memory["results"]

        if "summarize_text" in results:
            st.markdown("### Summary")
            st.write(results["summarize_text"])

        if "extract_insights" in results:
            st.markdown("### Insights")
            st.write(results["extract_insights"])

        if "generate_quiz" in results:
            st.markdown("### Quiz")
            st.write(results["generate_quiz"])