# LangGraph-Agent-Study

🎯 주요목표: LangChain과 LangGraph의 내부 동작 원리를 깊이 이해하고, 단순 API 호출을 넘어 프레임워크의 핵심 메커니즘을 파악하여 실제 프로덕션 환경에서 안정적으로 활용할 수 있는 수준의 전문성 확보

> **주요사항**: 2025/02/27 Release된 LangGraph 0.3 버전 이상을 사용합니다.

## 설치 및 실행

```shell
poetry install --with dev
```
- 모든 실습은 Jupyter 또는 vscode에서 수행됩니다.
- 모든 실습은 ChatOpenAI를 활용하여 진행됩니다.


[LangChain]
- LangChain의 Runnable / Chain / LCEL에 대한 개념이해
- ChatModel 및 멀티모달에 대한 실습 위주의 이해
- Messages, tool_calling 개념에 대한 기본적인 이해 

그 외, Memory 및 ToolCall

[LangGraph]
1. LangGraph 기초 개념 이해 (Node, Edge, State, StageGraph)
2. LangGraph 아키텍처 분석 (create_react_agent메서드를 예시로)
3. LangGraph 핵심 컴포넌트 분석
- Node의 내부구현과 동작원리
- Edge타입과 조건부 전환 메커니즘
- Graph의 상태관리 및 메모리 구조
- State 흐름 제어 방식 분석
4. 에이전트 구현 실습
- 도구(Tool) 연결 및 통합 메커니즘
- create_supervisor_agent실습
5. supervisor기반의 MultiAgent구축
- 

[참고문서]
- https://python.langchain.com/docs/concepts/
- https://langchain-ai.github.io/langgraph