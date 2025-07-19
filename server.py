from graph import research_graph, AgentState


def handle(initial_state: dict):
    result = research_graph.invoke(initial_state)

    
    try:
        import graphviz
        dot = research_graph.get_graph().draw()
        dot.render("workflow", format="png", cleanup=True)
        result["workflow.png"] = "workflow.png"
    except Exception as e:
        print(" Could not render workflow graph:", e)

    return result
