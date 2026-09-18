# resume.py
# 张佳琳 · 创新型可点击个人简历（Streamlit 单文件版）
# 运行：streamlit run resume.py

import streamlit as st
import pandas as pd
from pathlib import Path

import streamlit as st

st.markdown("""
<style>

    /* 全局背景保持不变 */
    .stApp {
        background-color: #f0f6ff;
        background-image:
            radial-gradient(circle at 10% 15%, rgba(255, 182, 193, 0.35) 0 80px, transparent 81px),
            radial-gradient(circle at 85% 20%, rgba(180, 210, 255, 0.45) 0 110px, transparent 111px),
            radial-gradient(circle at 75% 85%, rgba(255, 222, 190, 0.35) 0 90px, transparent 91px),
            radial-gradient(circle at 20% 80%, rgba(200, 230, 255, 0.5) 0 100px, transparent 101px),
            linear-gradient(180deg, #f7fbff 0%, #eaf4ff 100%);
        background-attachment: fixed;
    }

    /* 可爱装饰保持不变 */
    .stApp::before {
        
        position: fixed;
        top: 20px;
        right: 25px;
        font-size: 28px;
        letter-spacing: 18px;
        opacity: 0.55;
        pointer-events: none;
        z-index: 0;
    }

    .stApp::after {
        
        position: fixed;
        bottom: 30px;
        left: 20px;
        font-size: 24px;
        letter-spacing: 14px;
        opacity: 0.45;
        pointer-events: none;
        z-index: 0;
    }

    /* 正文加深 */
    p,
    .stMarkdown,
    .stText,
    .stWrite {
        color: #111111 !important;
        line-height: 1.7;
    }

    /* 主标题加深 */
    h1 {
        color: #0b1e3f !important;
        font-weight: 800;
        letter-spacing: 0.5px;
    }

    /* 二级标题加深 */
    h2 {
        color: #0b1e3f !important;
        font-weight: 700;
        border-left: 5px solid #6fa8dc;
        padding-left: 12px;
        background: rgba(255, 255, 255, 0.85);
        padding-top: 8px;
        padding-bottom: 8px;
        padding-right: 12px;
        border-radius: 10px;
    }

    /* 三级标题加深：基本信息、板块导航 */
    h3 {
        color: #0b1e3f !important;
        font-weight: 700;
    }

    /* 卡片保持不变 */
    div[data-testid="stContainer"] {
        background: rgba(255, 255, 255, 0.88);
        border-radius: 22px;
        padding: 24px;
        box-shadow:
            0 4px 14px rgba(111, 168, 220, 0.25),
            0 1px 3px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
        border: 1px solid rgba(180, 210, 255, 0.5);
        position: relative;
        z-index: 1;
    }

    div[data-testid="stContainer"]::before {
        content: "🎀";
        position: absolute;
        top: 10px;
        right: 14px;
        font-size: 20px;
        opacity: 0.5;
    }

    /* 大数字加深 */
    [data-testid="stMetricValue"] {
        color: #0b1e3f !important;
        font-weight: 800;
    }

    [data-testid="stMetricLabel"] {
        color: #1a2b48 !important;
        font-weight: 600;
    }

    /* 表格加深 */
    table {
        color: #111111;
    }

    th {
        color: #0b1e3f;
        background: rgba(180, 210, 255, 0.4);
        font-weight: 700;
    }

    td {
        color: #111111;
    }

    /* 左侧栏加深 */
    [data-testid="stSidebar"] {
        background-color: #d7e8ff !important;
    }

    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: #111111 !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #0b1e3f !important;
        font-weight: 700;
    }

    /* 粉色按钮保留，但文字加深 */
    .stButton > button {
        border-radius: 24px;
        background-color: #ff9ec7;
        color: #3b1228 !important;
        font-weight: 700;
        border: none;
        padding: 8px 22px;
        box-shadow: 0 3px 8px rgba(255, 158, 199, 0.4);
    }

    .stButton > button:hover {
        background-color: #ff7ab0;
    }

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="张佳琳 · 个人简历",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "resume_records.csv"
DATA_DIR.mkdir(parents=True, exist_ok=True)

COLUMNS = ["id", "title", "category", "notes", "created_at"]

PROFILE = {
    "name": "张佳琳",
    "birth": "2006.12",
    "gender": "女",
    "degree": "大学本科",
    "major": "信息管理与信息系统",
    "hometown": "河北省保定市",
    "phone": "177-1326-0649",
    "email": "1598136239@qq.com",
}

EDUCATION = {
    "school": "上海财经大学",
    "major": "信息管理与信息系统（本科）",
    "period": "2025.08 - 至今",
    "gpa": "大一上 GPA 3.40，专业排名前 15%；大一下 GPA 3.56，专业排名前 19%",
    "core_courses": [
        ("程序设计基础", 3.7),
        ("高级程序设计与实验", 3.7),
        ("Python程序设计", 4.0),
    ],
    "ongoing": ["数据库", "管理信息系统", "数据结构"],
}

EXPERIENCES = [
    {
        "period": "2026.06 - 至今",
        "org": "院文艺部",
        "role": "部长",
        "points": [
            "独立撰写学院选课指南宣传推文，整理选课重点、流程说明与注意事项，输出结构化科普内容。",
            "制作宣传内容并通过宣讲形式系统化输出部门信息，完成部门招新落地。",
        ],
    },
    {
        "period": "2025.09 - 2026.06",
        "org": "院文艺部",
        "role": "部员",
        "points": [
            "协助策划蓝园杯、学院迎新晚会等大型文艺活动，参与方案设计、流程彩排与现场调度，单场活动覆盖数百名师生。",
            "联动部门成员完成多场文体活动筹备，协调分工对接各方，锻炼高效沟通与任务推进能力。",
        ],
    },
]

AWARDS = [
    {
        "name": "上财“财青杯”本科招生宣传征文大赛 三等奖",
        "desc": "梳理整合招生相关素材，提炼关键信息，输出逻辑清晰的书面文稿，锻炼信息归纳能力。",
    },
]

CERTS = [
    ("英语四级", "518分"),
    ("全国计算机二级证书", "WPS Office 高级应用与设计"),
]

VOLUNTEER = [
    ("上海市第十人民医院", "志愿者", "协助现场挂号引导、咨询答疑，锻炼耐心与沟通能力。"),
    ("上海自然博物馆", "志愿者", "参与场馆游客引导服务，配合完成现场秩序维护工作。"),
]

SELF_EVAL = (
    "信息管理与信息系统专业大二本科生，学业成绩稳步提升，拥有学生团队管理与大型文艺活动执行经验。"
    "做事踏实细致，学习能力强。暂无实习经历，希望在实习岗位中将专业知识应用到实际工作，认真完成分配的各项任务。"
)

# 六个板块（已删除「技能自评」）
SECTIONS = [
    ("🎓 教育背景", "教育背景"),
    ("💼 实践经历", "实践经历"),
    ("🏆 荣誉证书", "荣誉证书"),
    ("🤝 志愿服务", "志愿服务"),
    ("✍️ 自我评价", "自我评价"),
    ("📋 记录管理", "记录管理"),
]


def load_data() -> pd.DataFrame:
    if CSV_PATH.exists():
        try:
            df = pd.read_csv(CSV_PATH)
            for col in COLUMNS:
                if col not in df.columns:
                    df[col] = ""
            return df[COLUMNS]
        except Exception:
            return pd.DataFrame(columns=COLUMNS)
    else:
        return pd.DataFrame(columns=COLUMNS)


def save_data(df: pd.DataFrame):
    try:
        df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
    except Exception:
        pass


def input_form(df: pd.DataFrame) -> pd.DataFrame:
    with st.form("add_form", clear_on_submit=True):
        new = {}
        new["id"] = 0 if df.empty else int(df["id"].max()) + 1

        st.markdown("##### ➕ 添加一条求职 / 学习记录")
        col1, col2 = st.columns(2)
        with col1:
            new["title"] = st.text_input("标题 *", placeholder="例如：投递字节跳动数据分析实习生")
        with col2:
            CATEGORIES = ["求职投递", "学习计划", "竞赛证书", "项目实践", "其他"]
            new["category"] = st.selectbox("类别", CATEGORIES, index=0)

        new["notes"] = st.text_area(
            "备注（可选）",
            placeholder="关键信息、链接、进度或行动项…",
            height=100,
        )

        submitted = st.form_submit_button("保存", type="primary", width="stretch")

    if submitted:
        if not new["title"]:
            st.warning("标题不能为空哦～")
            return df
        new["created_at"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        df_new = pd.DataFrame(new, index=[0])
        df = pd.concat([df, df_new], ignore_index=True)
        save_data(df)
        st.success("已保存 ✅")
    return df


def render_header():
    st.title("📄 张佳琳 · 个人简历")
    st.caption("信息管理与信息系统 · 上海财经大学")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("大一上绩点", "3.40")
    c2.metric("大一上专业排名", "前 15%")
    c3.metric("大一下绩点", "3.56")
    c4.metric("大一下专业排名", "前 19%")

    st.divider()


def render_home():
    """首页概览：只显示六个板块的入口按钮"""
    st.subheader("🧭 板块导航")
    st.caption("点击下方按钮进入对应板块查看详情")

    col1, col2 = st.columns(2)
    for idx, (label, key) in enumerate(SECTIONS):
        target_col = col1 if idx % 2 == 0 else col2
        with target_col:
            if st.button(label, key=f"home_btn_{key}", width="stretch"):
                st.session_state["page"] = key
                st.rerun()


def render_profile():
    st.subheader("👤 基本信息")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**姓名：** {PROFILE['name']}")
        st.write(f"**性别：** {PROFILE['gender']}")
        st.write(f"**出生年月：** {PROFILE['birth']}")
    with col2:
        st.write(f"**学历：** {PROFILE['degree']}")
        st.write(f"**专业：** {PROFILE['major']}")
        st.write(f"**籍贯：** {PROFILE['hometown']}")
    with col3:
        st.write(f"**电话：** {PROFILE['phone']}")
        st.write(f"**邮箱：** {PROFILE['email']}")


def render_education():
    st.subheader("🎓 教育背景")
    st.markdown(f"**{EDUCATION['school']}** · {EDUCATION['major']} · {EDUCATION['period']}")
    st.write(EDUCATION["gpa"])

    st.markdown("**核心课程成绩：**")
    for name, score in EDUCATION["core_courses"]:
        st.progress(min(score / 4.0, 1.0), text=f"{name} — {score}")

    st.markdown("**正在修读：** " + "、".join(EDUCATION["ongoing"]))


def render_experience():
    st.subheader("💼 校园实践经历")
    for exp in EXPERIENCES:
        with st.expander(f"{exp['period']} · {exp['org']} · {exp['role']}", expanded=True):
            for p in exp["points"]:
                st.markdown(f"- {p}")


def render_awards_certs():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏆 竞赛与荣誉")
        for a in AWARDS:
            st.markdown(f"**{a['name']}**")
            st.caption(a["desc"])
    with col2:
        st.subheader("📜 技能证书")
        for name, detail in CERTS:
            st.markdown(f"- **{name}**：{detail}")


def render_volunteer():
    st.subheader("🤝 志愿服务")
    for org, role, desc in VOLUNTEER:
        st.markdown(f"**{org}** · {role}")
        st.caption(desc)


def render_self_eval():
    st.subheader("✍️ 自我评价")
    st.info(SELF_EVAL)


def render_download():
    st.subheader("⬇️ 下载简历")
    text = f"""张佳琳 · 个人简历

【基本信息】
姓名：{PROFILE['name']}    性别：{PROFILE['gender']}    出生年月：{PROFILE['birth']}
学历：{PROFILE['degree']}    专业：{PROFILE['major']}    籍贯：{PROFILE['hometown']}
电话：{PROFILE['phone']}    邮箱：{PROFILE['email']}

【教育背景】
{EDUCATION['school']} · {EDUCATION['major']} · {EDUCATION['period']}
{EDUCATION['gpa']}
核心课程：{'、'.join([f'{n}({s})' for n, s in EDUCATION['core_courses']])}
正在修读：{'、'.join(EDUCATION['ongoing'])}

【校园实践经历】
"""
    for exp in EXPERIENCES:
        text += f"\\n{exp['period']} · {exp['org']} · {exp['role']}\\n"
        for p in exp["points"]:
            text += f"  - {p}\\n"

    text += "\\n【竞赛与荣誉】\\n"
    for a in AWARDS:
        text += f"- {a['name']}：{a['desc']}\\n"

    text += "\\n【技能证书】\\n"
    for name, detail in CERTS:
        text += f"- {name}：{detail}\\n"

    text += "\\n【志愿服务】\\n"
    for org, role, desc in VOLUNTEER:
        text += f"- {org} · {role}：{desc}\\n"

    text += f"\\n【自我评价】\\n{SELF_EVAL}\\n"

    st.download_button(
        label="📥 下载 TXT 版简历",
        data=text.encode("utf-8"),
        file_name="张佳琳-个人简历.txt",
        mime="text/plain",
        width="stretch",
    )


def render_records(df: pd.DataFrame):
    st.subheader("📋 我的求职 / 学习记录")
    if df.empty:
        st.caption("暂无记录，使用上方表单添加第一条吧～")
    else:
        st.dataframe(df, width="stretch", hide_index=True)
        csv_bytes = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "📤 导出记录 CSV",
            data=csv_bytes,
            file_name="resume_records.csv",
            mime="text/csv",
            width="stretch",
        )


def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "首页概览"

    render_header()

    with st.sidebar:
        st.markdown("### 👩‍🎓 张佳琳")
        st.caption("上海财经大学 · 信息管理与信息系统")
        st.divider()

        options = ["🏠 首页概览"] + [label for label, _ in SECTIONS]
        current_label = "🏠 首页概览"
        for label, key in SECTIONS:
            if key == st.session_state["page"]:
                current_label = label
                break

        selected = st.radio(
            "📌 导航",
            options,
            index=options.index(current_label),
        )

        if selected == "🏠 首页概览":
            st.session_state["page"] = "首页概览"
        else:
            for label, key in SECTIONS:
                if label == selected:
                    st.session_state["page"] = key
                    break

        st.divider()
        st.caption("💡 小提示：可在「记录管理」中添加投递记录")

    df = load_data()
    page = st.session_state["page"]

    if page == "首页概览":
        render_profile()
        st.divider()
        render_home()
        st.divider()
        render_download()
    elif page == "教育背景":
        render_education()
    elif page == "实践经历":
        render_experience()
    elif page == "荣誉证书":
        render_awards_certs()
    elif page == "志愿服务":
        render_volunteer()
    elif page == "自我评价":
        render_self_eval()
    elif page == "记录管理":
        st.subheader("📋 求职 / 学习记录管理")
        df = input_form(df)
        st.divider()
        render_records(df)


if __name__ == "__main__":
    main()
