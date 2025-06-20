import streamlit as st
import graphviz

# 페이지 설정
st.set_page_config(
    page_title="후기 작성 프로세스",
    page_icon="📝",
    layout="wide"
)

# 인증 시스템
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# 인증 확인
if not st.session_state.authenticated:
    st.title("🔐 시스템 로그인")
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 접근 권한이 필요합니다")
        password = st.text_input("비밀번호를 입력하세요:", type="password", placeholder="비밀번호 입력")
        
        if st.button("로그인", use_container_width=True):
            if password == "onlinetour1!":
                st.session_state.authenticated = True
                st.success("로그인 성공!")
                st.rerun()
            else:
                st.error("❌ 잘못된 비밀번호입니다.")
        
        st.info("💡 관리자에게 비밀번호를 문의하세요.")
    st.stop()

# 로그아웃 버튼 (상단 우측)
col1, col2 = st.columns([10, 1])
with col2:
    if st.button("🚪 로그아웃"):
        st.session_state.authenticated = False
        st.rerun()

# 사이드바 네비게이션
st.sidebar.title("🔄 프로세스 메뉴")
st.sidebar.markdown("---")

# 세션 상태 초기화
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = "사용자별 후기 작성 프로세스"

# 버튼 형식으로 메뉴 생성 (신규 메뉴 추가)
menu1_clicked = st.sidebar.button("📝 사용자별 후기 작성 프로세스", use_container_width=True)
menu2_clicked = st.sidebar.button("👤 회원 후기 작성 프로세스", use_container_width=True)
menu3_clicked = st.sidebar.button("👥 비회원 후기 작성 프로세스", use_container_width=True)
menu4_clicked = st.sidebar.button("🎯 여행 후기 시스템 개선 로드맵", use_container_width=True)
menu5_clicked = st.sidebar.button("🚀 TO-BE 개선 항목 리스트", use_container_width=True)

if menu1_clicked:
    st.session_state.selected_menu = "사용자별 후기 작성 프로세스"
if menu2_clicked:
    st.session_state.selected_menu = "회원 후기 작성 프로세스"
if menu3_clicked:
    st.session_state.selected_menu = "비회원 후기 작성 프로세스"
if menu4_clicked:
    st.session_state.selected_menu = "여행 후기 시스템 개선 로드맵"
if menu5_clicked:
    st.session_state.selected_menu = "TO-BE 개선 항목 리스트"

# 메인 콘텐츠 영역
def create_user_review_flowchart():
    """사용자별 후기 작성 프로세스 플로우차트 생성"""
    
    # Graphviz를 사용한 플로우차트 생성
    dot = graphviz.Digraph(comment='사용자별 후기 작성 프로세스')
    dot.attr(rankdir='LR', size='16,10')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')
    dot.attr('edge', fontname='Arial', fontsize='9')
    
    # 노드 정의 (색상별로 구분)
    # 시작/공통 프로세스 (연한 파란색)
    dot.node('A', '예약', fillcolor='lightblue')
    dot.node('B', '출발', fillcolor='lightblue')
    dot.node('C', '도착 +7일', fillcolor='lightblue')
    dot.node('D', '사용자 구분', fillcolor='yellow', shape='diamond')
    
    # 회원 프로세스 (연한 초록색)
    dot.node('E1', '회원', fillcolor='lightgreen')
    dot.node('F1', '알림톡 수신', fillcolor='lightgreen')
    dot.node('G1', '후기 작성 페이지\n접속', fillcolor='lightgreen')
    dot.node('H1', '후기 작성', fillcolor='lightgreen')
    dot.node('I1', '상품 자동 매핑', fillcolor='lightgreen')
    dot.node('J1', '후기 노출 완료', fillcolor='lightcoral')
    
    # 비회원 프로세스 (연한 주황색)
    dot.node('E2', '비회원', fillcolor='lightyellow')
    dot.node('F2', '담당자 문의', fillcolor='lightyellow')
    dot.node('G2', '비회원 후기 작성', fillcolor='lightyellow')
    dot.node('H2', '본인확인\n1. 출발일자\n2. 지역\n3. 상품 조회', fillcolor='lightyellow')
    dot.node('I2', '담당자 수동\n상품 매핑', fillcolor='lightyellow')
    dot.node('K2', '담당자 노출\n여부 결정', fillcolor='lightyellow')
    dot.node('J2', '후기 노출 완료', fillcolor='lightcoral')
    
    # 엣지 정의
    # 공통 프로세스
    dot.edge('A', 'B', '예약 완료')
    dot.edge('B', 'C', '여행 진행')
    dot.edge('C', 'D', '7일 경과')
    
    # 회원 프로세스
    dot.edge('D', 'E1', '회원')
    dot.edge('E1', 'F1')
    dot.edge('F1', 'G1')
    dot.edge('G1', 'H1')
    dot.edge('H1', 'I1')
    dot.edge('I1', 'J1')
    
    # 비회원 프로세스
    dot.edge('D', 'E2', '비회원')
    dot.edge('E2', 'F2')
    dot.edge('F2', 'G2')
    dot.edge('G2', 'H2')
    dot.edge('H2', 'I2')
    dot.edge('I2', 'K2')
    dot.edge('K2', 'J2')
    
    return dot

def create_member_review_swimlane():
    """회원 후기 작성 프로세스 Swimlane 다이어그램 생성"""
    
    dot = graphviz.Digraph(comment='회원 후기 작성 프로세스 Swimlane')
    dot.attr(rankdir='LR', size='20,12')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='9')
    dot.attr('edge', fontname='Arial', fontsize='8')
    dot.attr(compound='true')
    
    # OT 회원 Swimlane (상단)
    with dot.subgraph(name='cluster_0') as c:
        c.attr(style='filled,rounded', color='lightblue', fillcolor='#E6F3FF', 
               label='🙋‍♂️ OT 회원', fontsize='12', fontcolor='blue')
        c.attr('node', fillcolor='lightblue', height='1')
        c.node('M1', '여행\n종료')
        c.node('M2', '마이페이지\n나의 여행 후기\n메뉴로 이동')
        c.node('M3', '작성하기')
        c.node('M4', '후기 작성 팝업 오픈\n\n• 상품정보\n• 이용정보(예약번호, 여행기간)\n• 만족도평가 (max 5)\n• 제목\n• 후기 내용\n• 사진 첨부(Max 3, ≤10MB)')
        c.node('M5', '등록\n완료')
    
    # SERVER Swimlane (중간)
    with dot.subgraph(name='cluster_1') as c:
        c.attr(style='filled,rounded', color='orange', fillcolor='#FFF2E6',
               label='🖥️ SERVER', fontsize='12', fontcolor='darkorange')
        c.attr('node', fillcolor='lightyellow', height='1')
        c.node('S1', '후기 상태값 변경\n작성하기 → 작성 완료')
        c.node('S2', '전체 AVG평점 계산\n*서버/프론트 계산 확인 필요')
    
    # FRONT Swimlane (하단)
    with dot.subgraph(name='cluster_2') as c:
        c.attr(style='filled,rounded', color='green', fillcolor='#E6FFE6',
               label='🌐 FRONT', fontsize='12', fontcolor='darkgreen')
        c.attr('node', fillcolor='lightgreen', height='1')
        c.node('F1', '후기 노출')
    
    # 회원 영역 내부 연결 (가로 방향)
    dot.edge('M1', 'M2')
    dot.edge('M2', 'M3') 
    dot.edge('M3', 'M4')
    dot.edge('M4', 'M5')
    
    # 서버 영역 내부 연결
    dot.edge('S1', 'S2')
    
    # 레인 간 연결 (수직)
    dot.edge('M5', 'S1', label='등록 요청', style='dashed', color='red')
    dot.edge('S2', 'F1', label='노출 처리', style='dashed', color='red')
    
    return dot

def create_nonmember_review_swimlane():
    """비회원 후기 작성 프로세스 Swimlane 다이어그램 생성"""
    
    dot = graphviz.Digraph(comment='비회원 후기 작성 프로세스 Swimlane')
    dot.attr(rankdir='LR', size='26,14')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='8')
    dot.attr('edge', fontname='Arial', fontsize='7')
    dot.attr(compound='true')
    
    # 비회원 사용자 Swimlane (상단)
    with dot.subgraph(name='cluster_0') as c:
        c.attr(style='filled,rounded', color='lightblue', fillcolor='#E6F3FF', 
               label='👤 비회원 사용자', fontsize='12', fontcolor='blue')
        c.attr('node', fillcolor='lightblue', height='0.8')
        c.node('U1', '여행 종료\n후기 작성 문의')
        c.node('U2', '홈페이지 접속\n[예약확인/결제]\n비회원 예약 조회 탭 클릭')
        c.node('U3', '비회원 여행후기\n작성 [버튼 클릭]')
        c.node('U4', '비회원 여행 후기\nFORM 오픈')
        c.node('U5', '휴대폰\n본인 인증')
        c.node('U6', '🚩추가 수집 정보 입력\n여행 후기 남기기', fillcolor='gold')
        c.node('U7', '비회원 여행 후기\n작성 버튼')
        c.node('U8', '등록 완료 페이지\n<작성한 글 수정하기 옵션>')
    
    # OBMS 담당자 Swimlane (하단)
    with dot.subgraph(name='cluster_1') as c:
        c.attr(style='filled,rounded', color='orange', fillcolor='#FFF2E6',
               label='🏢 OBMS 담당자', fontsize='12', fontcolor='darkorange')
        c.attr('node', fillcolor='lightyellow', height='0.8')
        c.node('O1', '유틸리티 > 홈페이지게시판\n> 비회원 상품평\n> 해당 사용자 조회\n또는 일자별 후기 조회')
        c.node('O2', '🚩관련상품 매칭\n상품번호 조회 후 매핑\n(회원 조회/예약번호 -> 상품번호)', fillcolor='gold')
        c.node('O3', '🚩등록 상태 값 및\n노출 여부 결정', fillcolor='gold')
        c.node('O4', '후기 노출')
    
    # 비회원 사용자 영역 내부 연결
    dot.edge('U1', 'U2')
    dot.edge('U2', 'U3')
    dot.edge('U3', 'U4')
    dot.edge('U4', 'U5')
    dot.edge('U5', 'U6')
    dot.edge('U6', 'U7')
    dot.edge('U7', 'U8')
    
    # OBMS 담당자 영역 내부 연결
    dot.edge('O1', 'O2')
    dot.edge('O2', 'O3')
    dot.edge('O3', 'O4')
    
    # 레인 간 상호작용 - 등록 완료 후 담당자가 처리 시작
    dot.edge('U8', 'O1', label='등록 알림', style='dashed', color='red')
    
    return dot

# 메인 화면 렌더링
current_menu = st.session_state.selected_menu

if current_menu == "TO-BE 개선 항목 리스트":
    # TO-BE 개선 항목 페이지
    st.title("🚀 TO-BE 항목별 개선 ITEM LIST")
    st.markdown("---")
    
    # 각 개선 항목을 섹션별로 구성
    improvement_items = [
        {
            "title": "🎯 원스톱 후기 작성",
            "description": "여행 종료 후 쿠팡 사례와 같이 '가이드 평가 + 여행 후기'를 한 번에 작성할 수 있는 통합 프로세스를 제공합니다.",
            "category": "프로세스 개선"
        },
        {
            "title": "👥 가이드별 관리 시스템",
            "description": "상품별 가이드 관리 및 평가 기능을 추가하여 효율적인 가이드 운영을 지원합니다 (현재 미구현 기능).",
            "category": "관리 기능"
        },
        {
            "title": "🎥 동영상 후기 활성화",
            "description": "최대 1분 이내의 짧은 동영상 후기 기능을 제공하여 생생한 경험 공유를 유도합니다. (향후 숏폼 콘텐츠 확장 및 회원 기능 강화: 프로필 이미지, 여행 후기 랭킹 시스템 연계)",
            "category": "콘텐츠 확장"
        },
        {
            "title": "⭐ 리뷰 유용성 기능",
            "description": "노랑풍선 타사 사례와 같이 리뷰 필터, 정렬, 신고, 차단 등의 기능을 제공하여 사용자에게 유용한 리뷰를 선별하고 관리할 수 있도록 합니다.",
            "category": "사용자 경험"
        },
        {
            "title": "📊 구조화된 리뷰 도입",
            "description": "쿠팡 사례와 같이 여행 유형, 가이드 전문성 등 구체적인 항목을 기반으로 하는 구조화된 리뷰 시스템을 구축합니다. 쿠팡의 경우 제품의 성격/특성에 따라 평가 항목이 변경됩니다.",
            "category": "리뷰 시스템"
        },
        {
            "title": "🤖 AI 감성 분석 (추후 과제)",
            "description": "NLP 기술을 활용하여 리뷰 텍스트의 감성을 분석하고 긍정/부정 키워드를 자동으로 분류하는 시스템을 도입합니다.",
            "category": "AI 기술"
        },
        {
            "title": "👫 동행자 리뷰 기능",
            "description": "현재 미구현된 동행자도 리뷰를 등록할 수 있는 기능을 추가하여 다양한 관점의 후기를 확보합니다.",
            "category": "사용자 확장"
        },
        {
            "title": "🏆 업셀링 기회 창출",
            "description": "에어비앤비 사례를 참고하여 우수 상품/가이드 뱃지 시스템을 도입하여 업셀링 기회를 증대합니다.",
            "category": "마케팅",
            "sub_items": [
                "**LUXE 뱃지**: 높은 객단가와 차별화된 경험을 제공하는 최상위 프리미엄 상품에 부여 (사용자 후기 기반이 아닌, 상품 자체 속성 및 내부 기준 기반 선별).",
                "**여행자 선호 뱃지**: 후기, 평점, 리뷰 수 등 성과 데이터 기반으로 시스템이 주기적으로 자동 부여 및 회수됩니다."
            ]
        },
        {
            "title": "📢 고객 피드백 실시간 확인",
            "description": "여행 후기 작성 시 WEBHOOK을 통해 Slack 또는 G-Space로 알림을 발송하여 고객 피드백을 실시간으로 확인하고, 이를 통한 고객 중심 문화 구축을 목표로 합니다.",
            "category": "운영 효율화"
        },
        {
            "title": "🔗 API 연동",
            "description": "여기어때 및 온라인투어 상품 후기 API를 제공하여 기술 연동을 통해 다양한 채널에서 후기 정보를 활용할 수 있도록 합니다 (채널별 연동 상태 설명 포함).",
            "category": "기술 확장"
        }
    ]
    
    # 카테고리별로 그룹화
    categories = {}
    for item in improvement_items:
        category = item["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(item)
    
    # 카테고리별로 표시
    for category, items in categories.items():
        st.subheader(f"📋 {category}")
        
        for item in items:
            with st.expander(f"**{item['title']}**", expanded=False):
                st.write(item["description"])
                
                # 서브 아이템이 있는 경우 표시
                if "sub_items" in item:
                    st.markdown("**세부 항목:**")
                    for sub_item in item["sub_items"]:
                        st.markdown(f"• {sub_item}")
        
        st.markdown("---")
    
    # 요약 통계
    st.subheader("📊 개선 항목 요약")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("총 개선 항목", f"{len(improvement_items)}개")
    
    with col2:
        st.metric("카테고리 수", f"{len(categories)}개")
    
    with col3:
        st.metric("우선순위", "★★★")
    


elif current_menu == "여행 후기 시스템 개선 로드맵":
    # 로드맵 페이지 내용
    st.title("🎯 여행 후기 시스템 개선 로드맵")
    st.markdown("---")

    # PHASE 1
    st.header("🏗️ PHASE 1: 가이드 및 후기 시스템 기반 강화")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("👥 OBMS 가이드 관리 기능 도입")

    with col2:
        st.subheader("📊 가이드 및 여행 후기 평가 항목 구조화")

    with col3:
        st.subheader("🎥 동영상 후기 추가")

    st.markdown("---")

    # PHASE 2
    st.header("🚀 PHASE 2: 후기 작성 프로세스 및 참여 확대")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎯 원스탑 후기 작성 프로세스")

    with col2:
        st.subheader("🔓 비회원 및 OBMS 후기 작성 개선")

    with col3:
        st.subheader("👬 동행자 후기 등록 기능 추가")

    st.markdown("---")

    # PHASE 3
    st.header("✨ PHASE 3: 후기 UI/UX 개선 및 콘텐츠 확장")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("✨ 후기 UI/UX 개선")

    with col2:
        st.subheader("🏆 우수 상품/가이드 뱃지 시스템 도입")

    with col3:
        st.subheader("🔗 여기어때 & 온라인투어 상품 후기 API 제공")

    st.markdown("---")

    # PHASE 4
    st.header("🤖 PHASE 4: AI 기반 후기 분석 및 활용")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.subheader("🤖 구조화된 리뷰 및 AI 활용")

    st.markdown("---")

    # 간단한 요약
    st.header("📊 프로젝트 요약")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("총 작업 항목", "10개")

    with col2:
        st.metric("단계 수", "4개")

    st.success("🚀 여행 후기 시스템 혁신을 통한 사용자 경험 개선")

else:
    # # 기존 프로세스 플로우차트 페이지들
    # st.title("📝 후기 작성 프로세스 플로우차트")
    # st.markdown("---")

    if current_menu == "사용자별 후기 작성 프로세스":
        st.header("🔄 사용자별 후기 작성 프로세스")
        st.markdown("""
        이 플로우차트는 여행 상품 이용 후 후기 작성 과정을 회원과 비회원으로 구분하여 보여줍니다. *상세 플로우는 회원 후기 작성 프로세스 및 비회원 후기 작성 프로세스 확인인
        """)
        
        # 플로우차트 생성 및 표시
        try:
            flowchart = create_user_review_flowchart()
            st.graphviz_chart(flowchart.source)
            
            # 프로세스 설명
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("👤 회원 프로세스")
                st.markdown("""
                1. **알림톡 수신**: 자동으로 후기 작성 알림
                2. **후기 작성**: 간편한 온라인 작성
                3. **자동 매핑**: 상품 정보 자동 연결
                4. **즉시 노출**: 작성 완료 시 바로 게시
                """)
            
            with col2:
                st.subheader("👥 비회원(오프라인 포함) 프로세스")
                st.markdown("""
                1. **담당자 문의**: 고객센터 연락 필요
                2. **본인확인**: 휴대폰 본인 인증
                3. **수동 매핑**: 담당자가 직접 상품 연결
                4. **검토 후 노출**: 담당자 승인 후 게시
                """)
                
        except Exception as e:
            st.error("플로우차트를 생성하는 중 오류가 발생했습니다.")
            st.error(f"오류 내용: {str(e)}")
            
            # 대체 텍스트 기반 플로우차트
            st.markdown("""
            ### 📋 프로세스 흐름 (텍스트 버전)
            
            **공통 단계:**
            ```
            예약 → 출발 → 도착 +7일
            ```
            
            **회원 경로:**
            ```
            회원 → 알림톡 → 후기 작성 페이지 → 작성 → 상품 자동 매핑 → 후기 노출 완료
            ```
            
            **비회원 경로:**
            ```
            비회원 → 담당자 문의 → 비회원 후기 작성 → 본인확인 → 담당자 수동 상품 매핑 → 담당자 노출 여부 결정 → 후기 노출 완료
            ```
            """)

    elif current_menu == "회원 후기 작성 프로세스":
        st.header("👤 회원 후기 작성 프로세스")
        st.markdown("""
        이 다이어그램은 OT 회원, 서버, 프론트엔드 간의 상호작용을 보여줍니다.
        """)
        
        # 회원 후기 작성 Swimlane 다이어그램 생성
        try:
            member_flowchart = create_member_review_swimlane()
            st.graphviz_chart(member_flowchart.source)
            
            # 프로세스 상세 설명
            st.subheader("📋 프로세스 상세")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**🙋‍♂️ OT 회원 영역**")
                st.markdown("""
                - 여행 종료 후 마이페이지 접근
                - 나의 여행 후기 메뉴 이동
                - 후기 작성 팝업에서 정보 입력
                - 등록 완료 처리
                """)
            
            with col2:
                st.markdown("**🖥️ SERVER 영역**")
                st.markdown("""
                - 후기 상태값 변경 처리
                - 작성하기 → 작성 완료 상태 전환
                - 전체 평균 평점 계산
                """)
            
            with col3:
                st.markdown("**🌐 FRONT 영역**")
                st.markdown("""
                - 최종 후기 노출 처리
                - 사용자 인터페이스 업데이트
                """)
                
            # 입력 정보 상세
            st.subheader("📝 후기 작성 팝업 입력 정보")
            st.markdown("""
            - **상품정보**: 예약한 여행 상품 정보
            - **이용정보**: 예약번호, 여행기간 (시작일/종료일)
            - **만족도평가**: 1~5점 척도
            - **제목**: 후기 제목
            - **후기 내용**: 상세 후기 내용
            - **사진 첨부**: 최대 3장, 각 파일 10MB 이하
            """)
            
        except Exception as e:
            st.error("Swimlane 다이어그램을 생성하는 중 오류가 발생했습니다.")
            st.error(f"오류 내용: {str(e)}")
            
            # 대체 텍스트 기반 Swimlane
            st.markdown("""
            ### 📋 회원 후기 작성 프로세스 (텍스트 버전)
            
            **OT 회원**
            ```
            여행 종료 → 마이페이지 접근 → 나의 여행 후기 메뉴 → 작성하기 → 후기 작성 팝업 → 등록 완료
            ```
            
            **SERVER**
            ```
            후기 상태값 변경 (작성하기 → 작성 완료) + 전체 AVG평점 계산
            ```
            
            **FRONT**
            ```
            후기 노출
            ```
            """)

    elif current_menu == "비회원 후기 작성 프로세스":
        st.header("👥 비회원 후기 작성 프로세스")
        st.markdown("""
        이 다이어그램은 비회원 사용자와 OBMS 담당자 간의 상호작용을 보여줍니다.
        🚩 표시는 중요한 처리 단계를 나타냅니다.
        """)
        
        # 비회원 후기 작성 Swimlane 다이어그램 생성
        try:
            nonmember_flowchart = create_nonmember_review_swimlane()
            st.graphviz_chart(nonmember_flowchart.source)
            
            # 프로세스 상세 설명
            st.subheader("📋 프로세스 상세")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**👤 비회원 사용자 영역**")
                st.markdown("""
                - 여행 종료 후 후기 작성 문의
                - 홈페이지 접속하여 비회원 예약 조회
                - 비회원 여행후기 작성 FORM 작성
                - 휴대폰 본인 인증 진행
                - 🚩 추가 수집 정보 입력 및 후기 작성
                - 등록 완료 (수정 옵션 제공)
                """)
            
            with col2:
                st.markdown("**🏢 OBMS 담당자 영역**")
                st.markdown("""
                - 후기 작성 가이드 안내
                - 유틸리티를 통한 비회원 상품평 조회
                - 🚩 관련 상품 매칭 (상품번호 조회 후 매핑)
                - 🚩 등록 상태값 및 노출 여부 결정
                - 최종 후기 노출 처리
                """)
                
            # 중요 프로세스 강조
            st.subheader("🚩 중요 처리 단계")
            st.markdown("""
            1. **추가 수집 정보 입력**: 비회원 신원 확인을 위한 추가 정보 수집
            2. **관련 상품 매칭**: 담당자가 수동으로 예약번호를 통해 상품번호 조회 및 매핑
            3. **등록 상태값 및 노출 여부 결정**: 담당자 검토를 통한 최종 승인 단계
            """)

            # 중요 프로세스 강조
            st.subheader("🚩 비회원 후기 수집 정보")
            st.markdown("""
            1. **이름**
            2. **휴대폰번호(인증 필수)**
            3. **비밀번호 등록**
            4. **비밀번호 확인**
            """)

            # 중요 프로세스 강조
            st.subheader("🚩본인 인증 완료 후 추가 수집 정보")
            st.markdown("""
            1. 출발하신 일자가 언제였나요?
            2. 다녀오신 여행지가 어디였나요?
            3. 여행하신 상품이 다음이 맞나요? 
            """)

            # 중요 프로세스 강조
            st.subheader("🎯 추가 문제점 진단")
            st.markdown("""
            1. 후기 경험의 파편화 : 마이페이지, 고객의 소리 비회원 사용자 후기, 베스트 가이드 페이지 등 다양한 경로에 후기 기능이 분산되어 있어 사용자 경험의 일관성 부족
            2. 동행자 : 대표 예약자와 상품의 1:1 구조로 매핑되어 동행자 후기 작성 불가능 
            """)
            
        except Exception as e:
            st.error("비회원 후기 작성 Swimlane 다이어그램을 생성하는 중 오류가 발생했습니다.")
            st.error(f"오류 내용: {str(e)}")
            
            # 대체 텍스트 기반 Swimlane
            st.markdown("""
            ### 📋 비회원 후기 작성 프로세스 (텍스트 버전)
            
            **비회원 사용자**
            ```
            여행 종료 → 후기 작성 문의 → 홈페이지 접속 → 비회원 예약 조회 → 후기 FORM 작성 → 본인 인증 → 🚩추가 정보 입력 → 등록 완료
            ```
            
            **OBMS 담당자**
            ```
            가이드 안내 → 비회원 상품평 조회 → 🚩상품 매칭 → 🚩노출 여부 결정 → 후기 노출
            ```
            """)