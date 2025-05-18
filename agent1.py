import time

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class State(TypedDict):
    name: str
    greeting: str


def greet(state: State) -> State:
    time.sleep(3)
    return {"greeting": f"Hello, {state['name']}!"}


def init_graph() -> StateGraph:
    graph = StateGraph(State)
    graph.add_node("greet", greet)

    graph.add_edge(START, "greet")
    graph.add_edge("greet", END)

    return graph.compile()


graph = init_graph()


if __name__ == "__main__":
    state = graph.invoke({"name": "John"})
    print(state)