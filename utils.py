
import graphviz
from IPython.display import display

def visualize_langgraph(graph, title=None):
    """
    LangGraph 그래프를 Graphviz를 사용하여 시각화합니다.
    
    Args:
        graph: LangGraph의 StateGraph 또는 CompiledStateGraph 객체
        title: 그래프 제목 (선택사항)
    """
    if title:
        print(f"# {title}")
    
    # 그래프 객체로부터 노드와 엣지 정보 추출
    nodes = []
    edges = []
    
    # 그래프 정보 추출 시도
    try:
        if hasattr(graph, "nodes"):
            nodes = list(graph.nodes)
        
        if hasattr(graph, "edges"):
            for src, targets in graph.edges.items():
                for tgt in targets:
                    edges.append((src, tgt))
    except Exception as e:
        print(f"그래프 정보 추출 오류: {e}")
    
    # Graphviz 그래프 생성
    dot = graphviz.Digraph(comment=title or "LangGraph")
    
    # 스타일 설정
    dot.attr('node', shape='box', style='filled', color='lightblue')
    dot.attr('edge', color='gray')
    dot.attr(rankdir='LR')  # 왼쪽에서 오른쪽으로 흐름
    
    # 노드 추가
    for node in nodes:
        dot.node(node)
    
    # 엣지 추가
    for src, tgt in edges:
        dot.edge(src, tgt)
    
    # 그래프 표시
    display(dot)
    
    # 노드 및 엣지 정보 텍스트로도 출력
    print(f"\n노드 ({len(nodes)}개): {', '.join(nodes)}")
    
    if edges:
        print(f"\n엣지 ({len(edges)}개):")
        for src, tgt in edges:
            print(f"  {src} → {tgt}")