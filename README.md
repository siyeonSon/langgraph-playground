# 환경 세팅
- python 3.11 이상
- uv 설치: `curl -LsSf https://astral.sh/uv/install.sh | sh`

```shell
uv init langagraph-playground
cd langagraph-playground

uv add langgraph-cli --extra names
uv add langchain-openai ipykernel
```

## 참고할 사이트
- [langgraph](https://langchain-ai.github.io/langgraph/) - Agentic Workflow Framework
- [langsmith](https://smith.langchain.com/) - Monitoring
- [langgraph studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/#getting-started) - Developing & Debugging
- [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui) - Chat UI
- [MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) - mcp servers to tools

---

### 시나리오 1 - hello world
1. agent1.py
```python
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
```
    
2. langgraph.json(studio를 위한 설정)
```json
{
    "dependencies": ["."],
    "graphs": {
        "agent1": "./agent1.py:graph"
    },
    "env": ".env"
}
```
    
3. studio를 띄우고 graph를 실행시켜보자
```
uv run langgraph dev
```

4. shell에서 실행해서 state에 값이 어떻게 들어가 있는지 확인해보자
```
uv run python agent1.py
```
