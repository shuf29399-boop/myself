# -*- coding: utf-8 -*-
from pathlib import Path
import json

from generate_test import render_html


ROOT = Path(__file__).parent
SOURCE = ROOT / "tests" / "city-fit" / "test_config.json"
SLUG = "city-blessing"
TITLE = "哪个城市最旺你？"


def build_config():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    data.update({
        "slug": SLUG,
        "theme": TITLE,
        "eyebrow": "CITY ENERGY MATCH TEST",
        "title": TITLE,
        "subtitle": "30 道题，测出最能放大你人生优势的城市",
        "subtitle_lines": [
            "30 道题，测出最能放大你人生优势的城市",
            "不是玄学预测，而是一份城市适配自我探索。",
        ],
        "intro": "有些城市会让你越住越有劲，有些城市条件再好，却总让你觉得使不上力。",
        "intro_paragraphs": [
            "有些城市会让你越住越有劲，有些城市条件再好，却总让你觉得使不上力。",
            "所谓“旺你”，不是一座城市替你改变命运，而是它的机会、节奏、关系和生活方式，刚好能接住你的优势。",
            "凭第一感觉完成 30 道题，看看哪一种城市气质更容易让你发光。",
        ],
        "value_statement": "测试会从机会驱动力、生活恢复力、连接方式和阶段目标四个维度，帮你找到更能放大优势、减少内耗的城市类型。",
        "dimensions": ["机会驱动力", "生活恢复力", "连接方式", "阶段目标"],
        "share_line": "真正旺你的城市，不替你改命，只让你的天赋更容易被看见。",
    })

    results = {
        "A": {
            "name": "上海｜机会放大型",
            "summary": "最旺你的，是信息密度高、规则清晰、能让能力快速被市场看见的城市。",
            "sections": [
                "你会在高标准、快反馈和多元人群中被激活。上海代表的不是繁华滤镜，而是专业、效率和持续更新的机会场。",
                "你的隐藏优势是目标感和适应力；主要卡点是容易把忙碌当成长，忽略身体、关系与现金流的边界。北京、深圳等高机会密度城市也可能适配你。",
                "未来 7 天：列出目标城市的 3 个真实机会、月度生活成本和 90 天验证目标，再决定是否出发。",
            ],
        },
        "B": {
            "name": "成都｜生活滋养型",
            "summary": "最旺你的，是有人情味、有烟火气，也允许你慢慢积累的城市。",
            "sections": [
                "你不是缺少野心，而是只有在日常不被透支时，才会稳定释放能力。成都代表松弛但不松散、热闹又能回到生活的城市气质。",
                "你的隐藏优势是长期经营与关系连接；主要卡点是可能因为熟悉和舒服，错过低成本的新尝试。长沙、重庆等生活感强的城市也可能适配你。",
                "未来 7 天：盘点当地能利用的人脉、空间和线上机会，启动一个不牺牲生活的增长项目。",
            ],
        },
        "C": {
            "name": "杭州｜弹性成长型",
            "summary": "最旺你的，是既连接新机会，又能保留个人节奏和生活边界的城市。",
            "sections": [
                "你不喜欢被迫在事业和生活之间二选一。杭州代表数字机会、灵活协作与自然生活可以并存的城市气质。",
                "你的隐藏优势是整合力和变通力；主要卡点是方案太多、比较太久。苏州、南京等兼顾产业与生活的城市也可能适配你。",
                "未来 7 天：设计一份 90 天城市实验，写清工作连接、居住成本、社交半径和复盘日期。",
            ],
        },
        "D": {
            "name": "青岛｜阶段安顿型",
            "summary": "最旺你的，是能配合人生阶段，让你进可成长、退可安顿的城市。",
            "sections": [
                "你真正需要的不是一座永远正确的城市，而是一位阶段合作者。青岛代表尺度适中、边界清楚、能同时容纳事业与生活的城市气质。",
                "你的隐藏优势是阶段判断和重新选择；主要卡点是目标不清时，迁徙可能变成反复重启。厦门、大连等舒展且有产业支点的城市也可能适配你。",
                "未来 7 天：写下未来两年的第一优先级、城市必须满足的 3 个条件，以及完成阶段任务后的离开条件。",
            ],
        },
    }
    data["results"] = results
    data["report_preview"] = {
        "enabled": True,
        "demo_unlocked": True,
        "label": "你的专属城市能量报告",
        "kicker": "CITY · MATCH REPORT",
        "unlock_title": "完整报告 · 查看你的城市适配分析",
        "unlock_text": "查看隐藏优势、主要卡点、适合路径和未来 7 天建议。",
        "button_text": "查看完整报告演示版",
        "reports": {
            "A": {"name": results["A"]["name"], "index_label": "机会放大指数", "base_score": 90, "summary": results["A"]["summary"], "core": "你适合把能力放进高密度市场，用更快的反馈、更专业的协作和更多元的机会，完成一次明显跃迁。", "gold": "旺你的不是城市光环，而是你的能力终于有了回声。", "locked": ["城市适配分析｜机会：你的选择显示，你会被竞争、优秀同行和高密度信息激活。上海成熟的行业分工与专业平台，更容易让能力获得清晰反馈。", "城市适配分析｜节奏：你能为重要目标承受一段高成本和快节奏，只要看得到成长回报，压力反而会转化为行动力。", "城市适配分析｜关系：你不依赖熟人环境，更愿意通过专业能力建立新连接；多元而边界清楚的人际方式，更符合你的独立倾向。", "你的隐藏优势：目标感强、学习快，进入高标准环境后反而更专注，也敢主动争取稀缺机会。", "需要留意：容易用高强度证明价值，把忙碌误认为成长，并低估房租、通勤、孤独与健康的长期成本。", "给你的城市建议：优先选择与你行业高度聚集的区域，准备至少 3—6 个月缓冲金；用收入增长、作品积累和健康状态作为去留指标，不必住在市中心证明自己。", "未来 7 天建议：列出上海能给你的 3 个真实机会，完成月度预算、目标岗位清单和 90 天验证计划。"]},
            "B": {"name": results["B"]["name"], "index_label": "生活滋养指数", "base_score": 88, "summary": results["B"]["summary"], "core": "稳定关系、低消耗日常和真实生活感，会让你的耐心、创造力与长期主义充分发挥。", "gold": "让你松弛下来的地方，才有余地让你慢慢变强。", "locked": ["城市适配分析｜生活：你的选择反复指向可控开销、舒适空间和真实日常。成都较强的生活感，能降低你维持生活所消耗的能量。", "城市适配分析｜节奏：你更擅长长期积累，而不是持续冲刺。相对松弛的节奏会让你保持耐心，把精力留给真正重要的工作和关系。", "城市适配分析｜关系：你重视熟悉感、陪伴与稳定社交。成都开放又有人情味的连接方式，更容易让你建立归属感。", "你的隐藏优势：擅长经营长期关系与稳定日常，能把生活底盘转化为持续创作、工作和成长的力量。", "需要留意：可能把熟悉等同于安全，在舒服里延迟行动，错过本可以低成本尝试的新机会。", "给你的城市建议：把成都当作生活基地，同时建立线上收入、个人品牌或区域服务；选择交通便利但不过度商业化的生活圈。", "未来 7 天建议：盘点本地可利用的 5 项资源，并启动一个不离开当地也能获得新收入或成长反馈的小项目。"]},
            "C": {"name": results["C"]["name"], "index_label": "弹性成长指数", "base_score": 87, "summary": results["C"]["summary"], "core": "你最需要的是选择权：既能连接新产业和新协作，也能保留恢复能量的生活空间。", "gold": "你不必牺牲生活，才能证明自己有野心。", "locked": ["城市适配分析｜机会：你的选择既需要成长，也不愿把生活全部交给竞争。杭州的数字产业、创业协作和灵活工作方式，能提供更轻盈的机会入口。", "城市适配分析｜节奏：你可以适应忙碌，但必须拥有固定恢复空间。城市与自然相连、核心区与周边层次丰富，更方便你调整生活强度。", "城市适配分析｜连接：你擅长线上线下组合，也能跨城市整合资源；杭州与长三角城市的连接，适合你的弹性发展方式。", "你的隐藏优势：整合力强、善于权衡，适合跨城协作、远程工作、主业加副业等组合式成长。", "需要留意：方案越多越容易停在比较阶段，用“再看看”延迟真正的验证。", "给你的城市建议：先确定稳定生活基地，再按固定频率连接行业活动与目标人群；选择能控制通勤、保留自然空间的居住区域。", "未来 7 天建议：完成一份 90 天杭州实验表，写清预算、工作连接、社交频率、生活半径和退出条件。"]},
            "D": {"name": results["D"]["name"], "index_label": "阶段适配指数", "base_score": 89, "summary": results["D"]["summary"], "core": "你不需要一次决定余生。先看清这一阶段最重要的任务，再让城市成为帮助你完成任务的合作者。", "gold": "城市不是终身答案，它只是你这一阶段的同行者。", "locked": ["城市适配分析｜城市尺度：你的选择显示，你既不想与机会完全断开，也不愿长期被超大城市挤压。青岛尺度适中，更容易兼顾发展与生活。", "城市适配分析｜阶段任务：你愿意在需要时冲刺，也懂得在完成积累后安顿。产业支点与舒展生活并存，适合把城市当作阶段合作者。", "城市适配分析｜归属：你需要清楚边界、稳定关系和可持续日常。海边城市的空间感与相对从容的节奏，更利于恢复能量。", "你的隐藏优势：阶段判断力强，能根据事业、关系和能量变化重新配置生活，不容易被单一成功标准绑住。", "需要留意：如果没有明确目标，迁徙可能变成逃避；每次换城市都从头开始，会消耗原本可以积累的复利。", "给你的城市建议：先确认青岛能否承接你的具体行业与收入需求；若岗位有限，可采用本地生活基地加跨城项目的组合。", "未来 7 天建议：定义未来两年的第一优先级，写下城市必须满足的 3 个条件、验证周期和完成任务后的去留标准。"]},
        },
    }
    return data


def build_markdown(data):
    lines = [f"# {TITLE}", "", "## 1. 基础信息", "", f"- slug：`{SLUG}`", f"- 主题：{TITLE}", f"- 页面标题：{TITLE}", f"- 副标题：{data['subtitle']}", "- 风格：城市选择 / 奶油白、灰绿、浅米色", "- 题目数量：30", "- 公开链接：待用户确认发布后填写", f"- 本地页面：{ROOT / 'tests' / SLUG / 'index.html'}", "- 封面图：待制作", "", "## 2. 开篇文案", "", f"顶部标签：{data['eyebrow']}", "", "副标题分行："]
    lines += [f"- {x}" for x in data["subtitle_lines"]]
    lines += ["", "开篇正文：", ""] + data["intro_paragraphs"] + ["", f"核心说明：{data['value_statement']}", "", f"传播金句：{data['share_line']}", "", "## 3. 测试维度", ""] + [f"- {x}" for x in data["dimensions"]] + ["", "## 4. 全部题目和选项", ""]
    for i, q in enumerate(data["questions"], 1):
        lines.append(f"{i}. {q['text']}")
        for j, opt in enumerate(q["options"]):
            lines.append(f"   - {'ABCD'[j]}. {opt['text']}")
        lines.append("")
    lines += ["## 5. 基础结果", ""]
    for key in "ABCD":
        r = data["results"][key]
        lines += [f"### {key}. {r['name']}", "", f"总结：{r['summary']}", "", f"分析：{' '.join(r['sections'])}", ""]
    lines += ["## 6. 完整报告演示版", ""]
    for key in "ABCD":
        r = data["report_preview"]["reports"][key]
        lines += [f"### {key}. {r['name']}", "", f"- 指数名：{r['index_label']}", f"- 基础分：{r['base_score']}", f"- 摘要：{r['summary']}", f"- 核心结论：{r['core']}", f"- 截图金句：{r['gold']}", "- 完整报告内容："] + [f"  - {x}" for x in r["locked"]] + [""]
    lines += ["## 7. 小红书发布素材", "", "### 爆款标题", "", "1. 哪个城市最旺你？30 道题测出你的城市能量场", "2. 不是北上广越大越好，真正旺你的城市有迹可循", "3. 测一测：上海、成都、杭州、青岛，谁最接得住你？", "4. 你不是不够努力，可能只是住错了城市", "5. 真正适合你的城市，会把你的优势越放越大", "6. 选城市别只看工资，先看它会不会消耗你", "7. 你的性格早就暴露了：哪座城市最旺你", "", "### 封面文字", "", "主标题：哪个城市最旺你？", "", "副标题：30 道题测出最能放大你优势的城市", "", "角标：上海 / 成都 / 杭州 / 青岛", "", "### 轮播图文案", "", "第 1 张：哪个城市最旺你？不是玄学，是城市适配。", "", "第 2 张：有些城市让你越住越有劲，有些城市却让你一直内耗。", "", "第 3 张：上海型——机会越密集，你越容易发光。", "", "第 4 张：成都型——生活先接住你，能力才能稳定长出来。", "", "第 5 张：杭州型——你要的不是二选一，而是事业和生活都能保留。", "", "第 6 张：青岛型——城市是阶段合作者，不必一次决定余生。", "", "第 7 张：想测的姐妹，评论区发“城市”，我发你入口。", "", "### 正文", "", "以前总觉得选城市要看工资、房价和名气，后来才发现：同一座城市，有人越住越有能量，有人却每天都在消耗。所谓“旺你”，不是玄学，而是这座城市的机会密度、生活节奏、关系方式，刚好能放大你的优势。做了一个 30 题的小测试，结果会匹配上海、成都、杭州、青岛四种城市气质，还会告诉你隐藏优势、主要卡点和未来 7 天建议。想测的姐妹，评论区发“城市”，我发你入口。", "", "### 置顶评论", "", "想测的姐妹，评论区发“城市”，我发你入口。测完记得回来告诉我，你是哪座城市型。", "", "### 评论区回复模板", "", "- 已收到，给你发入口啦。凭第一感觉选，会更接近真实状态。", "- 你这个结果很典型，不是城市替你改命，而是它更容易放大你的优势。", "- 建议重点看报告里的“主要卡点”和“未来 7 天建议”，比只看城市名更有用。", "", "### 标签", "", "#心理测试 #城市选择 #人生选择 #自我探索 #女生成长 #职业规划 #在哪座城市生活 #小红书测试", "", "## 8. 后续优化记录", "", "- 发布时间：", "- 发布平台：", "- 数据表现：", "- 评论/私信反馈：", "- 成交情况：", "- 下次优化：", ""]
    return "\n".join(lines)


def main():
    data = build_config()
    page_dir = ROOT / "tests" / SLUG
    page_dir.mkdir(parents=True, exist_ok=True)
    (page_dir / "test_config.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    background_css = """
  <style>
    @import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/lxgwwenkai-regular.css');
    @import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/lxgwwenkai-bold.css');
    html { background: #f3f0e7; }
    body {
      font-family: "LXGW WenKai", "PingFang SC", "Microsoft YaHei", sans-serif;
      color: #334037;
      background: transparent;
    }
    body::before {
      content: "";
      position: fixed;
      inset: 0;
      z-index: 0;
      pointer-events: none;
      opacity: 1;
      background-image:
        linear-gradient(rgba(255, 252, 244, 0.76), rgba(242, 246, 237, 0.82)),
        url('city-background.png');
      background-position: center top;
      background-size: auto 100vh;
      background-repeat: no-repeat;
      background-color: #f3f0e7;
    }
    .page { position: relative; z-index: 1; }
    h1, .report-name {
      font-family: "LXGW WenKai", "Songti SC", serif;
      color: #29382f;
      font-weight: 800;
      letter-spacing: 0.055em;
      text-shadow: 0 2px 18px rgba(255, 252, 240, 0.92);
    }
    h1 {
      font-size: clamp(38px, 8vw, 56px);
      line-height: 1.18;
    }
    .tag {
      color: #7b7456;
      font-family: "LXGW WenKai", "PingFang SC", sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.24em;
    }
    .subtitle {
      color: #59685e;
      font-family: "LXGW WenKai", "Songti SC", serif;
      font-weight: 600;
      letter-spacing: 0.025em;
    }
    .intro-panel p, .value {
      letter-spacing: 0.018em;
    }
    .question {
      color: #2f3e35;
      font-family: "LXGW WenKai", "Songti SC", serif;
      font-size: 22px;
      line-height: 1.65;
      letter-spacing: 0.025em;
    }
    .option {
      line-height: 1.65;
      letter-spacing: 0.01em;
    }
    .primary, .report-button {
      letter-spacing: 0.08em;
      box-shadow: 0 12px 28px rgba(63, 86, 71, 0.22);
    }
    .gold-line {
      color: #8a7043;
      font-family: "LXGW WenKai", "Songti SC", serif;
      font-size: 18px;
      line-height: 1.75;
    }
    .core-label, .full-report-title {
      letter-spacing: 0.08em;
    }
    .intro-panel {
      padding: 28px;
      border-radius: 24px;
      background: rgba(255, 253, 247, 0.68);
      box-shadow: 0 20px 60px rgba(55, 70, 60, 0.10);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }
    #quiz, #result {
      background: rgba(255, 253, 247, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
    }
    @media (max-width: 520px) {
      body::before { background-position: center top; background-size: auto 100vh; }
      .intro-panel { padding: 22px; }
    }
  </style>
"""
    page_html = render_html(data).replace("</head>", background_css + "</head>")
    (page_dir / "index.html").write_text(page_html, encoding="utf-8")
    text_path = ROOT / "01_测试完整文本库" / f"{SLUG}｜{TITLE}.md"
    text_path.write_text(build_markdown(data), encoding="utf-8")
    print(page_dir / "index.html")
    print(text_path)


if __name__ == "__main__":
    main()
