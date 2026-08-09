# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime
import json


ROOT = Path(__file__).parent
SLUG = "greek-hero-type"
TITLE = "测出你的古希腊英雄人格"


DIMENSIONS = [
    {
        "key": "BW", "left": "B", "right": "W", "left_name": "剑锋", "right_name": "智谋",
        "questions": [
            ("危机突然出现时，你更自然的反应是？", "马上进入现场，用行动打开局面", "先观察全局，找到最关键的突破口"),
            ("面对强大的对手，你更相信什么？", "气势、勇气和正面交锋", "信息、策略和出其不意"),
            ("团队陷入停滞时，你通常会？", "率先行动，让所有人跟上节奏", "重新分析，调整大家的行动顺序"),
            ("你更欣赏哪一种胜利？", "在正面较量中凭实力赢下", "用聪明方法化解看似无解的问题"),
            ("意见冲突时，你更接近？", "把立场说清楚，直接解决分歧", "先理解各方目的，再寻找共同出口"),
            ("学习一项新技能时，你习惯？", "先上手尝试，在犯错中掌握", "先研究原理，理解后再开始"),
            ("如果要进入一座未知迷宫，你会？", "带好装备，边走边处理危险", "先寻找线索，推测迷宫的结构"),
            ("别人最常认可你的哪种能力？", "关键时刻敢站出来、敢承担", "复杂情况下仍能保持清醒"),
        ],
    },
    {
        "key": "GH", "left": "G", "right": "H", "left_name": "荣耀", "right_name": "内心",
        "questions": [
            ("什么最容易让你产生行动动力？", "完成高难度目标，证明自己的能力", "守护真正重要的人和信念"),
            ("想象多年后的自己，你更希望？", "拥有值得骄傲、被人记住的成就", "过着忠于内心、不后悔的生活"),
            ("受到质疑时，你更可能？", "用结果回应，让实力替自己说话", "先确认这件事是否仍符合我的内心"),
            ("你最难接受哪一种遗憾？", "明明有能力，却没有赢得应有的位置", "为了外界认可，失去了真实的自己"),
            ("选择工作或任务时，你更看重？", "挑战性、成长速度和上升空间", "意义感、兴趣和内心的认同"),
            ("成功对你来说更像什么？", "不断抵达更高的位置和更大的舞台", "能够按照相信的方式生活"),
            ("如果没有人会看见你的努力，你会？", "很难长期坚持，我需要明确的反馈", "只要值得，我仍愿意安静地完成"),
            ("哪句话更能点燃你？", "去赢下属于你的荣耀", "去守住你真正相信的东西"),
        ],
    },
    {
        "key": "AS", "left": "A", "right": "S", "left_name": "结盟", "right_name": "独行",
        "questions": [
            ("开启一段重要旅程时，你更希望？", "找到可靠伙伴，一起面对未知", "独自出发，保留完整的决定权"),
            ("遇到困难时，你通常？", "主动寻找资源，也愿意接受帮助", "先靠自己解决，不想轻易麻烦别人"),
            ("你更舒服的工作状态是？", "与人碰撞想法，共同推进目标", "拥有独立空间，按自己的节奏深入"),
            ("进入陌生环境后，你会先？", "认识可以合作和交流的人", "观察环境，建立自己的安全边界"),
            ("重要决定出现分歧时，你倾向？", "寻找能让关系继续前进的方案", "尊重差异，但坚持自己的判断"),
            ("你觉得力量更容易来自？", "彼此信任、分工和共同承诺", "不依赖外界也能稳定前进"),
            ("情绪低落时，什么更能帮助你？", "和理解我的人聊一聊", "一个人安静梳理和恢复"),
            ("你理想中的英雄更像？", "能召集伙伴、让每个人发挥力量", "能独自穿过荒野、保持方向"),
        ],
    },
    {
        "key": "FR", "left": "F", "right": "R", "left_name": "承命", "right_name": "逆命",
        "questions": [
            ("面对必须承担的责任，你更接近？", "既然轮到我，就把它认真完成", "先判断它是否合理，不盲目接受"),
            ("传统规则与你的想法冲突时，你会？", "先理解规则，再在其中寻找空间", "更愿意挑战规则，走自己的路线"),
            ("你怎么看待命运？", "有些课题无法选择，但可以选择如何完成", "所谓命运，也可以被行动重新改写"),
            ("团队需要有人接下困难任务时，你会？", "如果这是我的位置，我愿意承担", "除非认可目标，否则不会只因要求而接受"),
            ("面对已经安排好的稳定道路，你更可能？", "先走稳，再慢慢形成自己的方向", "如果不适合，会尽早离开重新选择"),
            ("什么更容易让你安心？", "知道自己的责任，并一步步完成", "知道任何时候都保留重新选择的权利"),
            ("经历挫折后，你更常告诉自己？", "这是旅程的一部分，我要完成这段考验", "这不是唯一剧本，我可以换一种走法"),
            ("如果神谕预告了你的未来，你会？", "认真理解它，并准备面对命运的考验", "把它当作提醒，但不会让它定义人生"),
        ],
    },
]


RESULTS = {
    "BGAF": ("荣耀统帅", "阿伽门农", "组织、决断与承担大局", "容易把胜利置于感受之上", "让目标与团队的真实需要同时被看见"),
    "BGAR": ("破局征服者", "伊阿宋", "召集资源、开创新局面", "可能为了目标忽略过程中的代价", "选择值得征服的远方，而不是被野心驱赶"),
    "BGSF": ("荣耀战士", "阿喀琉斯", "勇气、爆发力与极致投入", "自尊容易成为最敏感的软肋", "把力量用于真正重要的战斗"),
    "BGSR": ("狂飙挑战者", "柏勒洛丰", "敢于挑战不可能", "成功之后容易被更大的证明欲牵引", "在起飞前先确认自己为何出发"),
    "BHAF": ("城墙守护者", "赫克托耳", "忠诚、责任感与保护力量", "容易把自己的需要放到最后", "守护他人时，也为自己留下退路"),
    "BHAR": ("热血救援者", "忒修斯", "行动果断、愿意为人解决危机", "可能在情绪推动下接下不属于自己的战斗", "先分清使命与冲动，再进入迷宫"),
    "BHSF": ("使命行动者", "珀尔修斯", "目标清楚、关键时刻敢出手", "习惯替别人承担过多责任", "只接受真正属于你的英雄任务"),
    "BHSR": ("自由猎手", "阿塔兰忒", "独立、专注与清晰边界", "太习惯独自奔跑，不容易接受帮助", "自由地前进，也自由地与人同行"),
    "WGAF": ("智慧领航者", "涅斯托耳", "统筹全局、提供成熟判断", "过度稳妥时可能错过行动窗口", "让智慧成为启程的灯，而不是停留的理由"),
    "WGAR": ("文明盗火者", "普罗米修斯", "远见、创新和改变旧秩序", "容易独自承受改变带来的代价", "在改变世界之前先建立可持续的同盟"),
    "WGSF": ("孤高建造者", "代达罗斯", "创造、设计与解决技术难题", "聪明可能制造更复杂的迷宫", "不要只建造出口，也要确认它通向哪里"),
    "WGSR": ("命运博弈者", "西西弗斯", "韧性、洞察规则并寻找缝隙", "容易把反抗变成无休止的执念", "选择值得重复的坚持，也允许自己放下石头"),
    "WHAF": ("温柔导师", "喀戎", "理解、疗愈与帮助他人成长", "能治愈别人，却常忽略自己的伤口", "把给予自己的关怀放回生命中心"),
    "WHAR": ("灵魂歌者", "俄耳甫斯", "感受力、创造力与深度连接", "容易为了挽回失去而困在回望中", "相信爱，也接受有些旅程需要继续向前"),
    "WHSF": ("归航谋略家", "奥德修斯", "适应、判断与穿越复杂局面", "想得太远，可能错过眼前真实感受", "真正的归航是知道自己为何坚持"),
    "WHSR": ("荒野预言者", "卡珊德拉", "直觉、独立洞察与识别风险", "看得太清楚时容易产生无人理解感", "把预见转化成可以被听见的表达"),
}


def build_config():
    questions = []
    for dim in DIMENSIONS:
        for text, left, right in dim["questions"]:
            questions.append({
                "text": text, "dimension": dim["key"],
                "options": [
                    {"text": left, "side": dim["left"], "weight": 2},
                    {"text": f"大体更接近：{left}", "side": dim["left"], "weight": 1},
                    {"text": f"大体更接近：{right}", "side": dim["right"], "weight": 1},
                    {"text": right, "side": dim["right"], "weight": 2},
                ],
            })
    # Interleave dimensions so the scoring intent is less obvious.
    questions = [questions[i + j * 8] for i in range(8) for j in range(4)]
    return {
        "slug": SLUG, "title": TITLE,
        "subtitle": "32 道题，解锁你的四字母英雄原型",
        "dimensions": [{k: d[k] for k in ("key", "left", "right", "left_name", "right_name")} for d in DIMENSIONS],
        "questions": questions,
        "results": {k: {"name": v[0], "hero": v[1], "gift": v[2], "shadow": v[3], "quest": v[4]} for k, v in RESULTS.items()},
    }


def render_html(data):
    payload = json.dumps(data, ensure_ascii=False)
    generated = datetime.now().strftime("%Y-%m-%d")
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE}</title>
<style>
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/lxgwwenkai-regular.css');
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/lxgwwenkai-bold.css');
*{{box-sizing:border-box}}html{{background:#d9d1bf}}body{{margin:0;color:#292f31;font-family:"LXGW WenKai","PingFang SC",sans-serif;line-height:1.7}}
body:before{{content:"";position:fixed;inset:0;background:linear-gradient(rgba(251,246,232,.74),rgba(229,235,232,.82)),url('greek-hero-background.png') center top/auto 100vh no-repeat #ded7c7;z-index:0}}
.page{{position:relative;z-index:1;width:min(760px,100%);margin:auto;padding:42px 22px 56px}}.hero{{text-align:center;padding:30px 0}}.eyebrow{{color:#887144;letter-spacing:.22em;font-size:13px;font-weight:700}}
h1{{font-family:"LXGW WenKai",serif;font-size:clamp(39px,8vw,58px);line-height:1.18;margin:25px 0 15px;color:#263b44;text-shadow:0 2px 18px #fff9e9;font-weight:700}}.subtitle{{font-size:20px;color:#5f625d}}
.panel{{background:rgba(255,252,242,.88);border:1px solid rgba(138,112,65,.34);border-radius:24px;padding:28px;box-shadow:0 24px 70px rgba(42,51,53,.16);backdrop-filter:blur(14px)}}
.intro{{font-size:18px}}.dims{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:24px 0}}.dim{{padding:12px;text-align:center;border:1px solid #c4ad7d;border-radius:12px;background:rgba(255,255,255,.46);color:#67552f;font-weight:700}}
button{{font:inherit;cursor:pointer}}.primary{{width:100%;border:0;border-radius:14px;padding:16px;background:#31596a;color:white;font-weight:700;font-size:19px;box-shadow:0 12px 24px rgba(49,89,106,.22)}}
.hidden{{display:none}}.count{{font-size:14px;color:#817a6d}}.progress{{height:7px;background:#ded8ca;border-radius:99px;margin:13px 0 22px;overflow:hidden}}.bar{{height:100%;background:linear-gradient(90deg,#ae8240,#31596a);width:0;transition:.25s}}
.question{{font-size:22px;font-weight:700;margin-bottom:18px;color:#263b44}}.option{{display:block;width:100%;text-align:left;margin:10px 0;padding:14px 16px;border:1px solid #c9b98f;background:rgba(255,255,255,.78);border-radius:12px;color:#30393a;font-size:16px}}.option:hover{{border-color:#8d6d35;background:#fffaf0}}
.back{{border:0;background:transparent;color:#756442;margin-top:12px}}.code{{font-family:Georgia,serif;letter-spacing:.22em;color:#a1712b;font-size:20px;font-weight:700;text-align:center}}.result-name{{font-size:40px;line-height:1.2;text-align:center;color:#263b44;font-weight:700;margin:10px 0}}.hero-name{{text-align:center;color:#756442;font-size:18px}}
.quote{{text-align:center;font-size:20px;color:#8a5d2c;margin:24px 0;font-weight:700}}.metrics{{display:grid;gap:12px;margin:24px 0}}.metric-row{{display:grid;grid-template-columns:78px 1fr 78px;gap:10px;align-items:center;font-size:14px}}.metric-left{{text-align:left}}.metric-right{{text-align:right}}.track{{height:9px;background:#d8d4ca;border-radius:99px;overflow:hidden}}.fill{{height:100%;background:linear-gradient(90deg,#b18a4b,#31596a)}}
.section{{border-top:1px solid #d6cab0;padding-top:16px;margin-top:16px}}.section b{{color:#74592d}}.dimension-help{{display:grid;gap:10px;margin-top:12px}}.help-item{{padding:12px 14px;border-radius:10px;background:rgba(235,229,214,.6);font-size:15px}}.help-item strong{{color:#31596a}}.actions{{margin-top:24px}}.notice{{font-size:13px;color:#77746b;margin-top:18px;text-align:center}}@media(max-width:520px){{.page{{padding:28px 16px 44px}}.panel{{padding:21px}}.question{{font-size:20px}}}}
</style></head><body><main class="page"><section class="hero"><div class="eyebrow">HELLENIC HERO ARCHETYPE</div><h1>{TITLE}</h1><div class="subtitle">32 道题，解锁你的四字母英雄原型</div></section>
<section id="start" class="panel intro"><p>如果生活是一场史诗，你会靠勇气破局，还是凭智慧归航？你追逐荣耀，还是忠于内心？</p><p>这不是对古希腊人物的简单模仿，而是一份借神话原型看见自己的探索报告。</p><div class="dims"><div class="dim">剑锋 B · 智谋 W</div><div class="dim">荣耀 G · 内心 H</div><div class="dim">结盟 A · 独行 S</div><div class="dim">承命 F · 逆命 R</div></div><button class="primary" onclick="startTest()">进入英雄试炼</button><div class="notice">娱乐测试，仅供自我探索参考</div></section>
<section id="quiz" class="panel hidden"><div id="count" class="count"></div><div class="progress"><div id="bar" class="bar"></div></div><div id="question" class="question"></div><div id="options"></div><button class="back" onclick="back()">← 上一题</button></section>
<section id="result" class="panel hidden"></section><div class="notice">生成日期：{generated}</div></main>
<script>const TEST={payload};let current=0,answers=[];function show(id){{['start','quiz','result'].forEach(x=>document.getElementById(x).classList.add('hidden'));document.getElementById(id).classList.remove('hidden')}}function startTest(){{current=0;answers=[];show('quiz');render()}}function render(){{let q=TEST.questions[current];count.textContent=`第 ${{current+1}} / ${{TEST.questions.length}} 题`;bar.style.width=`${{current/TEST.questions.length*100}}%`;question.textContent=q.text;options.innerHTML=q.options.map((o,i)=>`<button class="option" onclick="choose(${{i}})">${{String.fromCharCode(65+i)}}. ${{o.text}}</button>`).join('')}}function choose(i){{answers[current]=TEST.questions[current].options[i];if(current<TEST.questions.length-1){{current++;render()}}else result()}}function back(){{if(current===0)show('start');else{{current--;render()}}}}
function result(){{let score={{B:0,W:0,G:0,H:0,A:0,S:0,F:0,R:0}};answers.forEach(a=>score[a.side]+=a.weight);let code=(score.B>=score.W?'B':'W')+(score.G>=score.H?'G':'H')+(score.A>=score.S?'A':'S')+(score.F>=score.R?'F':'R');let r=TEST.results[code];let dims=TEST.dimensions.map(d=>{{let total=score[d.left]+score[d.right],left=Math.round(score[d.left]/total*100),right=100-left;return `<div class="metric-row"><span class="metric-left">${{d.left_name}} ${{left}}%</span><div class="track"><div class="fill" style="width:${{left}}%"></div></div><span class="metric-right">${{right}}% ${{d.right_name}}</span></div>`}}).join('');let gold={{B:'你敢于进入战场',W:'你善于穿过迷雾',G:'你渴望留下荣耀',H:'你忠于内心回声',A:'你相信并肩的力量',S:'你守住独立的方向',F:'你愿意完成命运课题',R:'你敢于改写既定剧本'}};document.getElementById('result').innerHTML=`<div class="code">${{code}}</div><div class="result-name">${{r.name}}</div><div class="hero-name">代表原型 · ${{r.hero}}</div><div class="quote">「${{code.split('').map(x=>gold[x]).join('，')}}。」</div><div class="metrics">${{dims}}</div><div class="section"><b>四种人格倾向</b><div class="dimension-help"><div class="help-item"><strong>战斗方式｜剑锋 B · 智谋 W</strong><br>看你面对问题时，更习惯立即行动、正面突破，还是先观察局势、制定策略。</div><div class="help-item"><strong>行动动力｜荣耀 G · 内心 H</strong><br>看推动你前进的力量，更来自成就、认可和自我证明，还是感情、信念与真实感受。</div><div class="help-item"><strong>关系模式｜结盟 A · 独行 S</strong><br>看你更容易通过合作、连接获得力量，还是依靠个人判断和独立空间保持稳定。</div><div class="help-item"><strong>命运态度｜承命 F · 逆命 R</strong><br>看你倾向于接受责任、完成既定课题，还是质疑安排、亲自改写人生路线。</div></div></div><div class="section"><b>神话级天赋</b><br>${{r.gift}}</div><div class="section"><b>你的阿喀琉斯之踵</b><br>${{r.shadow}}</div><div class="section"><b>当前英雄任务</b><br>${{r.quest}}</div><div class="section"><b>未来 7 天建议</b><br>选择一件你一直回避、但与当前英雄任务有关的小事，把它拆成一次可以在七天内完成的行动。英雄人格不是命运标签，而是提醒你如何使用自己的力量。</div><div class="actions"><button class="primary" onclick="startTest()">重新测试</button></div>`;show('result')}}</script></body></html>'''


def build_markdown(data):
    lines = [f"# {TITLE}", "", "## 1. 基础信息", "", f"- slug：`{SLUG}`", f"- 页面标题：{TITLE}", f"- 副标题：{data['subtitle']}", "- 风格：古希腊神话 / 博物馆画册 / 爱琴海蓝与青铜金", "- 题目数量：32", "- 结果数量：16", "- 公开链接：待发布", f"- 本地页面：{ROOT / 'tests' / SLUG / 'index.html'}", "", "## 2. 测试维度", "", "- B 剑锋 / W 智谋", "- G 荣耀 / H 内心", "- A 结盟 / S 独行", "- F 承命 / R 逆命", "", "## 3. 全部题目和选项", ""]
    for i, q in enumerate(data["questions"], 1):
        lines.append(f"{i}. {q['text']}")
        for j, o in enumerate(q["options"]): lines.append(f"   - {'ABCD'[j]}. {o['text']}")
        lines.append("")
    lines += ["## 4. 十六种英雄人格", ""]
    for code, r in data["results"].items():
        lines += [f"### {code}｜{r['name']}", "", f"- 代表原型：{r['hero']}", f"- 神话级天赋：{r['gift']}", f"- 阿喀琉斯之踵：{r['shadow']}", f"- 当前英雄任务：{r['quest']}", ""]
    lines += ["## 5. 小红书发布素材", "", "### 标题", "", "1. 测一测，你是哪一种古希腊英雄人格", "2. 32 道题，解锁你的四字母英雄原型", "3. 你的天赋，也是你的阿喀琉斯之踵", "4. 如果生活是一场史诗，你会是哪位主角", "5. 不是 MBTI：这次测测你的希腊英雄代码", "", "### 正文", "", "做了一套古希腊神话英雄人格测试。它从战斗方式、行动力量、关系模式和命运态度四个维度，组合成 16 种英雄原型。不是知识问答，也不是命运预测，而是借神话人物看见自己正在使用的力量。想测的姐妹，评论区发“英雄”，我发你入口。", "", "### 置顶评论", "", "想测的姐妹，评论区发“英雄”，我发你入口。测完回来告诉我你的四字母代码。", "", "### 标签", "", "#心理测试 #古希腊神话 #人格测试 #英雄原型 #自我探索 #MBTI", "", "## 6. 后续优化记录", "", "- 发布时间：", "- 数据表现：", "- 用户反馈：", "- 下次优化：", ""]
    return "\n".join(lines)


def main():
    data = build_config()
    folder = ROOT / "tests" / SLUG
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "test_config.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / "index.html").write_text(render_html(data), encoding="utf-8")
    (ROOT / "01_测试完整文本库" / f"{SLUG}｜{TITLE}.md").write_text(build_markdown(data), encoding="utf-8")
    print(folder / "index.html")


if __name__ == "__main__": main()
