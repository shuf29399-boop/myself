from pathlib import Path
import json
import re

from generate_test import OUTPUT_DIR, render_html


BASE_DIR = Path(__file__).parent
SOURCE = BASE_DIR / "爆款标题测试题库10套.md"


TEST_META = [
    {
        "slug": "hard-or-change",
        "title": "你该继续硬撑，还是换一种活法？",
        "eyebrow": "LIFE RESET CHECK",
        "subtitle": "30 道题，看清你现在是该坚持，还是该转向",
        "style": "neutral-pace",
        "dimensions": ["能量状态", "方向适配", "现实压力", "转向勇气"],
        "share_line": "不是所有坚持都叫成长，有些只是太久没有听见自己。",
        "intro_paragraphs": [
            "你有没有过这种感觉：每天都在往前走，却越来越不像自己。",
            "你说服自己再坚持一下，可身体和情绪已经开始悄悄提醒你。",
            "这个测试会帮你分清：你是在真正深耕，还是在硬撑一段不适合的生活。",
        ],
        "value_statement": "这个测试会从能量状态、方向适配、现实压力、转向勇气四个维度，帮你判断：你现在更适合继续撑住，还是换一种活法。",
        "category": "life",
        "report_preview": "career-decision",
    },
    {
        "slug": "be-controlled",
        "title": "你会被哪种人反复拿捏？",
        "eyebrow": "RELATIONSHIP BLIND SPOT",
        "subtitle": "30 道题，看清你最容易在哪种关系里失去判断",
        "style": "soft-love",
        "dimensions": ["情绪牵引", "上头模式", "边界感", "安全感需求"],
        "share_line": "真正让你被拿捏的，往往不是对方多厉害，而是你太想被坚定选择。",
        "intro_paragraphs": [
            "有些人一出现，你就很难保持原来的节奏。",
            "你明知道对方忽冷忽热，却还是忍不住想确认自己是不是特别的那个。",
            "这个测试会帮你看清：你到底容易被哪种人、哪种关系模式反复牵动。",
        ],
        "value_statement": "这个测试会从情绪牵引、上头模式、边界感、安全感需求四个维度，帮你判断你最容易被哪类人拿捏。",
        "category": "love",
        "report_preview": "auto",
    },
    {
        "slug": "sensitive-type",
        "title": "你是哪种高敏感体质？",
        "eyebrow": "SENSITIVE ENERGY MAP",
        "subtitle": "30 道题，看懂你的敏感不是缺点，而是哪种天赋",
        "style": "soft-love",
        "dimensions": ["情绪感知", "环境感官", "关系共情", "边界恢复"],
        "share_line": "敏感不是麻烦，它只是提醒你：你的感受系统比别人更细。",
        "intro_paragraphs": [
            "你是不是经常因为一句话、一个眼神、一个氛围变化想很久？",
            "别人觉得没什么的细节，你却能很快捕捉到不对劲。",
            "这个测试会帮你分辨：你的高敏感更偏情绪、环境、关系，还是自我保护。",
        ],
        "value_statement": "这个测试会从情绪感知、环境感官、关系共情、边界恢复四个维度，帮你看懂自己的敏感类型。",
        "category": "sensitive",
    },
    {
        "slug": "hot-or-steady-love",
        "title": "你适合被热烈追求，还是被稳定陪伴？",
        "eyebrow": "LOVE NEEDS CHECK",
        "subtitle": "30 道题，看清你真正需要哪一种爱",
        "style": "soft-love",
        "dimensions": ["心动浓度", "陪伴需求", "安全感", "个人空间"],
        "share_line": "有人适合点燃你，有人适合安放你，关键是你真正需要哪一种。",
        "intro_paragraphs": [
            "热烈的喜欢很动人，稳定的陪伴也很珍贵。",
            "但不是每个人都适合高浓度的爱，也不是每个人都能在平淡里安心。",
            "这个测试会帮你看清：你更适合被热烈追求，还是被稳定陪伴。",
        ],
        "value_statement": "这个测试会从心动浓度、陪伴需求、安全感、个人空间四个维度，帮你判断你真正适合的爱。",
        "category": "love",
        "report_preview": "auto",
    },
    {
        "slug": "money-talent",
        "title": "一分钟测出你天生适合靠什么赚钱！",
        "eyebrow": "MONEY TALENT CHECK",
        "subtitle": "30 道题，看见你最容易变现的能力",
        "style": "neutral-pace",
        "dimensions": ["表达能力", "服务能力", "资源整合", "产品化能力"],
        "share_line": "你不是没有赚钱能力，只是可能还没把最轻松的能力放到正确位置。",
        "intro_paragraphs": [
            "很多人不是赚不到钱，而是不知道自己最适合靠什么赚钱。",
            "有的人适合内容表达，有的人适合服务陪伴，有的人适合整合资源，有的人适合把技能产品化。",
            "这个测试会帮你看见：你最值得放大的赚钱能力是什么。",
        ],
        "value_statement": "这个测试会从表达能力、服务能力、资源整合、产品化能力四个维度，帮你找到更适合自己的变现方向。",
        "category": "money",
        "report_preview": "auto",
    },
    {
        "slug": "life-script",
        "title": "你的性格已经替你选好了人生剧本！",
        "eyebrow": "LIFE SCRIPT MAP",
        "subtitle": "30 道题，看清你的性格正在把你带向哪里",
        "style": "neutral-pace",
        "dimensions": ["选择模式", "关系模式", "成长路径", "人生主线"],
        "share_line": "你的性格不是限制，它只是一直在替你选择熟悉的剧情。",
        "intro_paragraphs": [
            "你有没有发现，人生里有些情节会反复出现。",
            "相似的人、相似的选择、相似的卡点，总会把你带回熟悉的位置。",
            "这个测试会帮你看清：你的性格正在替你写下哪一种人生剧本。",
        ],
        "value_statement": "这个测试会从选择模式、关系模式、成长路径、人生主线四个维度，帮你看懂自己的性格剧本。",
        "category": "life",
        "report_preview": "auto",
    },
    {
        "slug": "wrong-person",
        "title": "测一测，你和哪类人注定走不长久！",
        "eyebrow": "RELATIONSHIP FIT CHECK",
        "subtitle": "30 道题，看清你最不适合消耗在哪类关系里",
        "style": "soft-love",
        "dimensions": ["相处边界", "沟通方式", "情绪消耗", "长期适配"],
        "share_line": "合适不是靠忍出来的，不合适也常常早有信号。",
        "intro_paragraphs": [
            "有些人不是不好，只是不适合你。",
            "你越努力磨合，越容易把自己变得不像自己。",
            "这个测试会帮你看清：你和哪类人最容易走不长久，也最容易被消耗。",
        ],
        "value_statement": "这个测试会从相处边界、沟通方式、情绪消耗、长期适配四个维度，帮你识别不适合你的关系类型。",
        "category": "love",
        "report_preview": "auto",
    },
    {
        "slug": "strong-or-growth-love",
        "title": "你适合强者恋爱，还是养成系恋爱？",
        "eyebrow": "LOVE ROLE CHECK",
        "subtitle": "30 道题，看清你在关系里更适合被托举，还是一起升级",
        "style": "soft-love",
        "dimensions": ["崇拜感", "参与感", "成长耐心", "关系平衡"],
        "share_line": "强者恋爱和养成系恋爱没有高低，只有适不适合你。",
        "intro_paragraphs": [
            "你是更容易被成熟强大的人吸引，还是会心动于一个人的潜力？",
            "有些关系让你安心，有些关系让你觉得自己很重要。",
            "这个测试会帮你看清：你更适合强者恋爱，还是养成系恋爱。",
        ],
        "value_statement": "这个测试会从崇拜感、参与感、成长耐心、关系平衡四个维度，帮你判断适合你的恋爱模式。",
        "category": "love",
        "report_preview": "auto",
    },
    {
        "slug": "like-signals",
        "title": "真正喜欢你的人，其实早有信号",
        "eyebrow": "LIKE SIGNAL CHECK",
        "subtitle": "30 道题，帮你分清好感、暧昧和真正喜欢",
        "style": "soft-love",
        "dimensions": ["语言表达", "持续行动", "稳定回应", "关系诚意"],
        "share_line": "真正喜欢你的人，不会只给你上头，也会给你安心。",
        "intro_paragraphs": [
            "你有没有分不清，对方是喜欢你，还是只是刚好会聊天？",
            "暧昧有时候很像喜欢，但真正的喜欢通常会有更稳定的信号。",
            "这个测试会帮你判断：你最容易相信哪些信号，又最容易忽略哪些细节。",
        ],
        "value_statement": "这个测试会从语言表达、持续行动、稳定回应、关系诚意四个维度，帮你看懂真正喜欢的信号。",
        "category": "love",
        "report_preview": "auto",
    },
    {
        "slug": "love-clarity",
        "title": "你的恋爱清醒度到了第几级？",
        "eyebrow": "LOVE CLARITY LEVEL",
        "subtitle": "30 道题，看清你在爱情里到底有多清醒",
        "style": "soft-love",
        "dimensions": ["边界感", "判断力", "自我价值", "及时止损"],
        "share_line": "恋爱清醒不是不心动，而是心动时也没有弄丢自己。",
        "intro_paragraphs": [
            "喜欢一个人之后，你还能不能守住自己的节奏？",
            "你能不能分清心动、执念、合适和长期可靠？",
            "这个测试会帮你看清：你的恋爱清醒度到了第几级。",
        ],
        "value_statement": "这个测试会从边界感、判断力、自我价值、及时止损四个维度，帮你判断你的恋爱清醒度。",
        "category": "love",
        "report_preview": "auto",
    },
    {
        "slug": "city-fit",
        "title": "你适合留在小城市，还是去大城市闯一闯？",
        "eyebrow": "CITY LIFE FIT TEST",
        "subtitle": "30 道题，看清哪一种城市更能接住你的人生",
        "style": "city-life",
        "dimensions": ["机会密度", "节奏耐受", "关系支持", "长期归属"],
        "share_line": "适合你的城市，不一定最繁华，但一定能让你的努力和生活彼此成全。",
        "intro_paragraphs": [
            "大城市有更多机会，也有更高的成本和更快的节奏。",
            "小城市离生活更近，却也可能让想突破的人感到空间有限。",
            "真正重要的不是哪里更好，而是哪一种城市能接住你现在的野心、关系和生活方式。",
        ],
        "value_statement": "这个测试会从机会密度、节奏耐受、关系支持、长期归属四个维度，帮你判断：你更适合在大城市拓展、小城市扎根，还是为自己设计一条更灵活的城市路径。",
        "category": "life",
        "report_preview": "city-fit",
    },
]


CITY_QUESTIONS = [
    ("如果两个城市收入差距明显，你更可能怎么选？", "去收入更高、机会更多的城市试一试", "留在生活成本更低、日子更稳的城市", "先远程或短住体验，再决定长期落点", "看人生阶段，年轻时闯一闯，以后再调整"),
    ("你理想中的通勤时间更接近哪一种？", "可以接受一小时左右，只要工作值得", "最好二十分钟内，把时间留给生活", "工作地点灵活，能自由安排最好", "目前能接受长通勤，未来希望慢下来"),
    ("面对陌生城市和新圈子，你通常是什么感觉？", "兴奋，陌生意味着新的可能", "有压力，我更依赖熟悉的人和环境", "短期新鲜，长期要看能否建立稳定连接", "阶段性愿意冒险，但不会一直漂着"),
    ("你对城市生活最看重什么？", "行业机会、资源和成长速度", "居住舒适、开销可控和烟火气", "既有机会，也能保留自己的生活节奏", "不同阶段满足不同需求，不必一次定终身"),
    ("周末更让你充电的方式是什么？", "看展、参加活动、认识不同的人", "陪家人朋友、逛熟悉的小店和公园", "一半探索城市，一半安静独处", "现在喜欢热闹，累了会回到安静生活"),
    ("如果家人希望你留在身边，你会怎么考虑？", "先争取自己的发展，距离可以想办法解决", "家人的陪伴很重要，我愿意把它放在前面", "寻找交通方便或能经常往返的折中城市", "先出去积累几年，再决定是否回到家人身边"),
    ("你能接受为了更好的机会频繁跳槽吗？", "能，职业上升期应该主动争取", "不太能，我更喜欢稳定积累和熟人环境", "可以换，但希望生活基地保持稳定", "年轻时可以，到了某个阶段会降低频率"),
    ("高房租会怎样影响你的选择？", "只要机会足够好，我愿意承担一段时间", "会明显降低幸福感，我更想住得宽松", "会计算收入、成长和生活质量的综合回报", "短期可以忍受，长期一定会换更舒服的落点"),
    ("你对独居在陌生城市的接受度如何？", "很高，我享受独立和自己建立生活", "比较低，有熟悉的人在身边会安心很多", "可以独居，但需要稳定社群和规律生活", "阶段性可以，长期还是想靠近重要的人"),
    ("哪种工作状态更能激发你？", "竞争强、变化快、优秀的人很多", "关系稳定、节奏可预期、能长期深耕", "主业稳定，同时保留线上或副业机会", "前期高强度积累，后期换取更多自主权"),
    ("当城市节奏很快时，你通常会怎样？", "会被带动，反而更有行动力", "容易疲惫，生活会失去自己的节奏", "能适应，但需要固定的恢复空间", "短期冲刺没问题，长期会主动降速"),
    ("你怎么看待熟人社会？", "有点束缚，我更喜欢匿名和多元的环境", "有安全感，办事和生活都更有人情味", "有支持也有边界，适度就好", "某些阶段需要逃离，某些阶段又会想念"),
    ("如果工作发展一般，但生活很舒服，你会满足吗？", "不会，我会担心自己错过成长窗口", "会，稳定舒服本身就是重要价值", "短期会，但仍会在线上寻找成长空间", "看阶段，先发展和先生活都可能是答案"),
    ("你更喜欢哪种社交环境？", "不断遇见新朋友和不同领域的人", "有几个认识很久、随时能见面的朋友", "小而稳定的圈子，也保留认识新人的机会", "人生前期扩大圈子，后来留下真正重要的人"),
    ("你对文化、医疗、教育资源的需求高吗？", "很高，资源密度会直接影响我的选择", "够用就好，我更在意日常便利和低压力", "关键资源需要可达，不必每天身处中心", "现在需求高，未来可能更看重舒适和陪伴"),
    ("哪种居住空间更让你有幸福感？", "位置方便的小房子，出门就是丰富生活", "宽敞安静的家，有阳光也有自己的空间", "不追求市中心，但交通和配套要平衡", "年轻时住得紧凑，未来想换更松弛的空间"),
    ("面对城市里的竞争，你更接近哪种状态？", "竞争会让我看见差距，也推动我成长", "长期竞争会消耗我，我更适合稳定节奏", "只在重要目标上竞争，其他地方保持松弛", "愿意集中拼几年，但不会把竞争当成终身状态"),
    ("如果事业机会和恋人所在地冲突，你会怎么选？", "优先抓住难得的事业窗口", "优先经营稳定关系和共同生活", "先尝试异地或双城，给双方一个验证期", "看关系和事业所处阶段，再决定谁先调整"),
    ("你最害怕哪一种城市生活？", "机会太少，几年后发现自己没有成长", "开销太大，一直忙却没有真正生活", "被迫二选一，失去调整空间", "在不合适的阶段，被一个城市长期困住"),
    ("你对生活便利的理解更接近什么？", "选择多、服务多、任何需求都能快速满足", "距离近、成本低、日常事情不折腾", "线上线下都方便，不必依赖城市中心", "目前追求效率，以后更想要简单和从容"),
    ("你愿意为梦想承受多久的不确定？", "三到五年，只要能看到成长和可能", "不想太久，我需要稳定生活作为底座", "会给自己明确期限和退出方案", "年轻时可以更久，之后会重新评估投入产出"),
    ("你希望孩子或未来家庭生活在哪里？", "资源丰富、选择多、视野更开阔的地方", "环境安稳、陪伴充足、生活压力较小的地方", "核心资源可达，但日常生活不必过度拥挤", "先根据事业发展，再为家庭阶段重新选择"),
    ("如果可以远程工作，你会住在哪里？", "仍住大城市，享受资源和人群密度", "搬到小城市，让收入更耐花、生活更舒服", "在不同城市短住，找到最适合自己的组合", "先体验几年流动生活，再选择长期基地"),
    ("你对城市身份和归属感的需求是什么？", "在哪里成长、被看见，哪里就是我的城市", "熟悉的方言、人情和生活方式让我安心", "归属感可以由自己建立，不只来自出生地", "归属会随阶段变化，我允许自己重新选择"),
    ("遇到职业瓶颈时，你第一反应是什么？", "换平台、换圈子，去机会更密集的地方", "留在熟悉环境，把生活和能力慢慢稳住", "先线上拓展资源，不急着搬家", "给自己一个外出窗口，验证后再决定去留"),
    ("你更希望别人怎样形容你的生活？", "有见识、有成长、一直在打开新可能", "踏实、舒服、有稳定的人和自己的小日子", "既有事业选择，也没有牺牲生活质量", "懂得在不同阶段选择最适合自己的节奏"),
    ("一座城市最能留住你的是什么？", "持续出现的新机会和优秀同行", "重要的人、熟悉感和低压力生活", "能兼顾工作发展与内心安稳的空间", "它是否适合我当下，而不是是否永远适合"),
    ("如果现在搬去另一座城市，你最需要什么底气？", "一份有上升空间的工作或清晰目标", "稳定收入、熟人支持和可控生活成本", "可进可退的计划，以及几个月缓冲金", "一个明确期限，知道何时复盘、何时调整"),
    ("你对未来五年的城市想象更接近哪一种？", "进入更大的平台，让能力和收入上一个台阶", "在喜欢的小城安顿下来，建立稳定生活", "拥有一个生活基地，同时连接更多城市机会", "先去需要我的地方成长，再回到想生活的地方"),
    ("做完这个测试，你最想确认什么？", "我是不是应该去更大的城市争取机会", "我是不是更适合留在小城市好好生活", "我能不能不二选一，设计自己的双城方案", "我现在适合闯，还是已经到了该安顿的阶段"),
]


CITY_RESULTS = {
    "A": {
        "name": "大城市拓展型",
        "summary": "你需要的不是单纯的热闹，而是更高密度的机会、信息和成长反馈。",
        "sections": [
            "你对变化、新资源和优秀同行有天然的敏感度。环境越开放、选择越丰富，你越容易被激活，也更愿意为长期上升承担一段时间的压力。",
            "适合你的是有行业聚集度、职业通道和多元生活的大城市。但要警惕把高强度当成上进，给自己设置清晰的收入、成长和健康底线。",
            "未来 7 天，列出你想去城市的 3 个真实机会，再计算房租、通勤和储备金。让向往从想象变成可验证的计划。",
        ],
    },
    "B": {
        "name": "小城市扎根型",
        "summary": "你真正看重的不是城市级别，而是生活能否稳定、松弛并与重要的人相连。",
        "sections": [
            "你更容易在熟悉关系、低生活成本和可控节奏里积累幸福感。对你来说，房间的阳光、家人的陪伴和有余力的日常，比持续竞争更重要。",
            "适合你的不是“随便躺平”，而是在小城市建立有成长性的生活：稳定主业、线上能力或一项可长期经营的副业，都会让你的选择更有底气。",
            "未来 7 天，盘点你所在城市能利用的资源与缺口，找出一件既能留在当地、又能继续增长收入或能力的事。",
        ],
    },
    "C": {
        "name": "双城弹性型",
        "summary": "你不适合被迫二选一，更适合把生活基地和事业机会分开设计。",
        "sections": [
            "你既需要成长空间，也不愿意把全部生活交给拥挤和高成本。你擅长权衡，更适合远程工作、阶段短住、通勤城市或“生活在小城，连接大城市资源”的组合。",
            "你的优势是灵活，卡点则是容易一直比较、迟迟不落地。真正有效的折中不是拖延，而是设定时间、预算和验证指标。",
            "未来 7 天，设计一个 90 天双城实验：确定生活基地、工作连接方式、往返频率和复盘日期。",
        ],
    },
    "D": {
        "name": "阶段迁徙型",
        "summary": "你适合的城市会随人生阶段变化，现在的答案不必成为一生的答案。",
        "sections": [
            "你愿意在需要成长时去更大的地方，也能在需要安顿时回到更舒服的生活。你真正擅长的是看见阶段任务，而不是用一个城市证明自己。",
            "你适合给每次迁徙一个明确目的：积累履历、提高收入、建立关系或恢复生活。目标完成后，就允许自己重新选择。",
            "未来 7 天，写下你未来 2 年最重要的阶段目标，并判断哪座城市最能帮助它发生，而不是哪座城市听起来更体面。",
        ],
    },
}


CITY_REPORTS = {
    "A": {"name": "大城市拓展型", "index_label": "机会拓展指数", "base_score": 88, "summary": CITY_RESULTS["A"]["summary"], "core": "你适合去机会更密集的地方，不是因为小城市不够好，而是你的行动力需要更大的舞台和更快的真实反馈。", "gold": "你想去的不是大城市，你想去的是更大的可能。", "locked": ["你的城市优势：对新环境适应快，能从信息、人群和竞争中获得动力。", "你的潜在消耗：容易把忙碌误认为成长，并低估通勤、房租和孤独的长期成本。", "适合你的路径：优先选择行业密度高、成长通道清晰的城市，而不是只看城市名气。", "未来 7 天建议：完成目标城市的机会清单、生活预算和三个月行动计划。"]},
    "B": {"name": "小城市扎根型", "index_label": "生活扎根指数", "base_score": 86, "summary": CITY_RESULTS["B"]["summary"], "core": "你不是没有野心，你只是更希望成长能发生在不牺牲生活的前提下。稳定关系、低成本和可控节奏，会让你的能力发挥得更久。", "gold": "你要的不是躺平，是一种不会把自己耗空的生活。", "locked": ["你的城市优势：擅长经营长期关系与稳定日常，容易形成可持续的生活系统。", "你的潜在卡点：可能因为害怕变化，错过本可以低成本尝试的新机会。", "适合你的路径：以小城市为生活底座，同时发展线上工作、个人品牌或区域服务。", "未来 7 天建议：找到一个不必离开当地，也能增加收入或成长反馈的小项目。"]},
    "C": {"name": "双城弹性型", "index_label": "城市弹性指数", "base_score": 84, "summary": CITY_RESULTS["C"]["summary"], "core": "你真正想要的是选择权：既能连接大城市的机会，也能保留让自己恢复能量的生活基地。", "gold": "你不必在野心和生活之间，只能选择一个。", "locked": ["你的城市优势：能看见不同城市的价值，适合远程、短住和跨城协作。", "你的潜在卡点：方案太多时容易停在比较阶段，没有真正测试任何一种。", "适合你的路径：建立稳定基地，再用固定频率连接目标城市的项目、人脉和资源。", "未来 7 天建议：做一份 90 天双城实验表，写清成本、频率、目标和退出条件。"]},
    "D": {"name": "阶段迁徙型", "index_label": "阶段适配指数", "base_score": 87, "summary": CITY_RESULTS["D"]["summary"], "core": "你不需要一次决定余生。对你而言，城市是完成阶段任务的容器，而不是必须终身坚持的身份。", "gold": "城市不是终身答案，它只是你这一阶段的合作者。", "locked": ["你的城市优势：能根据事业、关系和能量变化重新安排生活，不容易被单一标准绑住。", "你的潜在卡点：如果没有阶段目标，迁徙容易变成逃避和反复重启。", "适合你的路径：每次选择城市前，先写清这两年要完成的核心任务和离开条件。", "未来 7 天建议：定义未来两年的第一优先级，再用它筛选城市，而不是反过来。"]},
}


OPTION_BANKS = {
    "life": [
        ("现实压力和安全感", "A"),
        ("自由感和新的可能性", "B"),
        ("能量状态和情绪消耗", "C"),
        ("方向规划和长期反馈", "D"),
    ],
    "love": [
        ("情绪波动和上头感", "A"),
        ("稳定回应和安全感", "B"),
        ("长期适配和边界感", "C"),
        ("自我感受和真实需求", "D"),
    ],
    "sensitive": [
        ("别人的情绪和语气变化", "A"),
        ("环境、声音、气味和细节", "B"),
        ("关系里的共情和责任感", "C"),
        ("独处、边界和自我恢复", "D"),
    ],
    "money": [
        ("表达、内容和个人影响力", "A"),
        ("服务、陪伴和解决具体问题", "B"),
        ("资源整合、信息差和链接机会", "C"),
        ("技能产品化、模板和标准化交付", "D"),
    ],
}


FREQUENCY_OPTIONS = [
    ("经常会，而且很容易影响我的状态", "A"),
    ("偶尔会，但我通常能慢慢调整回来", "B"),
    ("很少会，我更习惯先观察和判断", "C"),
    ("说不清，要看对象、环境和当时状态", "D"),
]


CHOICE_OPTIONS = [
    ("我更偏向前一种，这更像我现在的真实状态", "A"),
    ("我更偏向后一种，那种感受对我影响更大", "B"),
    ("两种都有，我经常在中间摇摆", "C"),
    ("都不完全准确，我需要具体情况具体判断", "D"),
]


ACTION_OPTIONS = [
    ("先稳住现实，不急着做大改变", "A"),
    ("先做一个小尝试，看看有没有新可能", "B"),
    ("先停下来恢复状态，别继续消耗自己", "C"),
    ("先把问题拆清楚，再决定下一步", "D"),
]


LOVE_ACTION_OPTIONS = [
    ("我会很在意，也容易开始反复想", "A"),
    ("我会看对方有没有持续、稳定的行动", "B"),
    ("我会先观察，不急着给关系下结论", "C"),
    ("我会问自己舒服不舒服，先守住边界", "D"),
]


MONEY_ACTION_OPTIONS = [
    ("先用内容表达，把自己的观点发出去", "A"),
    ("先做小服务，验证别人是否愿意付费", "B"),
    ("先找需求和资源，看哪里能撮合成交", "C"),
    ("先整理成模板或产品，降低重复交付成本", "D"),
]


def compact_fragment(text):
    text = re.sub(r"^[你我他她TAta是否会不会有没有能不能是不是]*", "", text)
    text = text.strip(" ，,。？?！!、：:")
    return text[:24] or "这种感受"


def split_choice_question(line):
    if "还是" not in line:
        return None
    left, right = line.split("还是", 1)
    left = compact_fragment(left)
    right = compact_fragment(right)
    if len(left) < 2 or len(right) < 2:
        return None
    return [
        (f"更偏向「{left}」", "A"),
        (f"更偏向「{right}」", "B"),
        ("两种都有，我会在不同阶段摇摆", "C"),
        ("都不完全像我，我更看具体情境", "D"),
    ]


def is_frequency_question(line):
    return any(word in line for word in ["会不会", "有没有", "是否", "能不能", "是不是", "会因为", "容易"])


def is_action_question(line):
    return any(word in line for word in ["怎么", "如何", "先", "开始", "处理", "选择", "改变", "做"])


def build_options(line, category, index):
    split_options = split_choice_question(line)
    if split_options:
        return split_options

    if any(word in line for word in ["哪种", "哪个", "哪类", "什么", "哪里", "哪一"]):
        base = OPTION_BANKS[category]
        starters = [
            "最像我的是",
            "我最在意的是",
            "最容易影响我的是",
            "我最需要先看清的是",
        ]
        return [(f"{starters[(index + i) % len(starters)]}：{text}", option_type) for i, (text, option_type) in enumerate(base)]

    fragment = compact_fragment(line)

    if is_frequency_question(line):
        return [
            (f"经常会，尤其在「{fragment}」这类事情上很明显", "A"),
            (f"偶尔会，但我能慢慢从「{fragment}」里调整回来", "B"),
            (f"很少会，我面对「{fragment}」时通常比较清醒", "C"),
            (f"说不清，要看「{fragment}」发生在什么情境里", "D"),
        ]

    if is_action_question(line):
        if category == "love":
            return [(f"{text}，再处理「{fragment}」", option_type) for text, option_type in LOVE_ACTION_OPTIONS]
        if category == "money":
            return [(f"{text}，先从「{fragment}」切入", option_type) for text, option_type in MONEY_ACTION_OPTIONS]
        return [(f"{text}，再面对「{fragment}」", option_type) for text, option_type in ACTION_OPTIONS]

    base = OPTION_BANKS[category]
    tones = [
        "非常符合",
        "有一点符合",
        "不太符合",
        "暂时说不清",
    ]
    return [(f"{tone}：{text}", option_type) for tone, (text, option_type) in zip(tones, base)]


RESULTS = {
    "life": {
        "A": ("稳定硬撑型", "你很能扛，也很重视现实安全感。", "你的优势是靠谱、负责、能坚持，但你也容易把“不能停”误认为“还适合”。接下来最重要的是确认：这份坚持有没有真实反馈。"),
        "B": ("转向重启型", "你内心已经开始渴望新的活法。", "你不是冲动，而是已经感觉到旧节奏不再适配。适合先做低成本试错，给自己一个小入口，而不是立刻推翻全部生活。"),
        "C": ("能量修复型", "你现在最需要的不是答案，而是把状态补回来。", "当人太累时，任何选择都会看起来很难。你适合先减少消耗，恢复一点掌控感，再判断要继续还是转向。"),
        "D": ("清醒规划型", "你适合用更聪明的方式调整人生节奏。", "你并不想盲目放弃，也不想一直硬撑。你真正需要的是计划、边界和一个可验证的小行动。"),
    },
    "love": {
        "A": ("情绪上头型", "你很容易被对方的回应、距离和态度牵动。", "你的喜欢很真，也很投入，但要小心把不确定感当成心动。真正适合你的关系，不该让你一直猜。"),
        "B": ("稳定安全型", "你最需要的是被认真对待和稳定放在心上。", "你适合长期、清晰、有行动感的关系。比起刺激，你更需要一个说到做到、持续回应你的人。"),
        "C": ("清醒观察型", "你会心动，但也会看这个人值不值得长期相处。", "你的判断力是优势。只是别让过度理性把真实感受全部压掉，合适也需要一点松弛和靠近。"),
        "D": ("自我边界型", "你正在学会把注意力从对方身上收回自己。", "你真正需要的关系，是让你更像自己，而不是一直委屈、讨好、证明。你的边界感会帮你筛掉不适合的人。"),
    },
    "sensitive": {
        "A": ("情绪雷达型", "你能很快察觉别人语气和情绪的变化。", "你的感受力很细，但不要把所有变化都自动归因到自己身上。学会区分别人的情绪和你的责任，会让你轻松很多。"),
        "B": ("环境感官型", "你对声音、光线、气味和空间氛围特别敏锐。", "你需要更稳定、舒服的环境来保存能量。对你来说，减少刺激不是矫情，而是有效管理自己。"),
        "C": ("共情吸收型", "你很容易理解别人，也容易把别人的情绪带回自己身上。", "你的温柔是能力，但需要边界保护。不是每一种痛苦都需要你亲自承接。"),
        "D": ("边界恢复型", "你敏感，但也正在发展自我保护能力。", "你最适合先建立恢复系统，比如独处、书写、减少无效社交。你的敏感会在边界里变成天赋。"),
    },
    "money": {
        "A": ("内容表达型", "你适合靠表达、观点、审美或内容影响力赚钱。", "你需要把自己的经验和观察稳定输出。低价产品、测评、咨询入口、内容账号都适合作为起步方式。"),
        "B": ("服务陪伴型", "你适合靠解决具体问题和提供陪伴型服务变现。", "你的价值在于让别人感觉被理解、被带着走。适合做咨询、陪跑、社群服务或细分人群方案。"),
        "C": ("资源整合型", "你适合靠信息差、链接能力和项目协作赚钱。", "你不一定要亲自做所有事，但你要学会发现需求、组织资源、促成成交。"),
        "D": ("技能产品型", "你适合把技能、方法或经验打包成可重复交付的产品。", "你的优势在于把复杂东西整理清楚。适合做模板、工具包、课程、小程序或标准化服务。"),
    },
}


CAREER_DECISION_REPORTS = {
    "A": {
        "name": "稳定承压型",
        "index_label": "稳定承压指数",
        "base_score": 82,
        "summary": "你不是没有野心，你只是更需要先确认脚下是稳的。",
        "core": "你现在的疲惫，不是因为你不够努力，而是你一直在用“稳定”和“负责”保护自己。你真正需要的不是立刻推翻生活，而是找到一个不会把你耗空的升级入口。",
        "gold": "你不是不想改变，你只是不能在没有安全感的时候冒险。",
        "locked": [
            "你的隐藏优势：你有很强的长期执行力，适合把一件事做深，而不是频繁换方向。",
            "你的主要卡点：你太容易把稳定等同于安全，结果把真正想要的东西压到很后面。",
            "适合你的下一步：先保留主线收入，同时开启一个低风险副线测试，不要用裸辞证明勇气。",
            "未来 7 天建议：列出一个最小副线动作，比如发 1 条内容、整理 1 个服务、联系 1 个可能客户。",
        ],
    },
    "B": {
        "name": "向上突围型",
        "index_label": "向上突围指数",
        "base_score": 86,
        "summary": "你不是想躺平，你只是选错了用力方向。",
        "core": "你现在的疲惫，不是因为不想拼，而是因为你一直在用力，但没用在能让你往上走的地方。你需要的不是继续硬撑，而是换一个更能放大你能力的位置。",
        "gold": "你不是想躺平，你只是走错了方向。",
        "locked": [
            "你的隐藏优势：你对机会很敏感，也有不甘心的力量，适合在变化里找到新入口。",
            "你的主要卡点：你想得很多，但容易等到完全确定才开始，结果错过最适合试错的窗口。",
            "适合你的下一步：不要一下子换人生，先做一个能验证市场反馈的小项目。",
            "未来 7 天建议：选一个你最想尝试的方向，做出一个可以给别人看的最小作品。",
        ],
    },
    "C": {
        "name": "能量修复型",
        "index_label": "能量透支指数",
        "base_score": 79,
        "summary": "你不是不行，你只是已经累到很难再判断。",
        "core": "你现在最需要的不是继续逼自己做决定，而是先把能量补回来。人在透支状态下，看什么都像没有出路；等状态恢复一点，你会重新看见选择。",
        "gold": "你不是没有方向，你只是太累了。",
        "locked": [
            "你的隐藏优势：你很会复盘，也能从经历里提炼方法，只是现在能量被消耗太多。",
            "你的主要卡点：你容易把低能量误判成自己没有能力，于是越焦虑越难启动。",
            "适合你的下一步：先停止一个持续消耗你的任务、关系或习惯。",
            "未来 7 天建议：只做一件能恢复掌控感的小事，不追求翻盘，先把自己接回来。",
        ],
    },
    "D": {
        "name": "清醒重构型",
        "index_label": "方向重构指数",
        "base_score": 84,
        "summary": "你不是要逃离现在，而是需要重新设计自己的路径。",
        "core": "你已经意识到，单纯坚持或者彻底放弃都不是答案。你真正需要的是把旧目标拆开，重新组合成一个更适合当下能力、资源和节奏的方案。",
        "gold": "你需要的不是推翻人生，而是重构路径。",
        "locked": [
            "你的隐藏优势：你有判断力，也有规划意识，适合用系统方法解决卡住的问题。",
            "你的主要卡点：你容易想得太完整，导致行动启动得太慢。",
            "适合你的下一步：把未来目标拆成三个层级：必须保住、可以尝试、暂时放下。",
            "未来 7 天建议：写一张路径重构表，把精力从消耗项挪到真正有反馈的事情上。",
        ],
    },
}


REPORT_TEMPLATES = {
    "life": {
        "label": "你的专属自我探索报告",
        "kicker": "SELF · REPORT",
        "index": "人生路径指数",
        "core_prefix": "你现在真正需要看清的，不是别人眼里的标准答案，而是这条路到底有没有让你更靠近自己。",
        "locked": [
            "你的隐藏优势：你有复盘和调整能力，只要看清主线，就能把经历变成下一步的判断力。",
            "你的主要卡点：你容易把别人的期待当成自己的方向，于是越努力越不确定。",
            "适合你的下一步：先把必须坚持、可以尝试、需要放下的事情分开，不要把所有压力混在一起。",
            "未来 7 天建议：选一件能带来真实反馈的小事，先让生活重新产生一点掌控感。",
        ],
    },
    "love": {
        "label": "你的专属关系报告",
        "kicker": "LOVE · REPORT",
        "index": "关系清醒指数",
        "core_prefix": "你在关系里最需要看清的，不是谁更主动，而是谁能让你在喜欢里也不弄丢自己。",
        "locked": [
            "你的隐藏需求：你真正想要的不是一时上头，而是被稳定看见、被认真回应。",
            "你的关系卡点：你容易被某些瞬间打动，却忽略长期相处里最关键的边界和一致性。",
            "适合你的相处模式：不要只看对方说了什么，要看他是否持续、稳定、尊重你的节奏。",
            "未来 7 天建议：把注意力从猜对方转回观察自己，记录一次让你舒服和一次让你不安的细节。",
        ],
    },
    "money": {
        "label": "你的专属赚钱能力报告",
        "kicker": "MONEY · REPORT",
        "index": "变现潜力指数",
        "core_prefix": "你不是没有赚钱能力，而是需要找到最适合自己性格、资源和表达方式的变现入口。",
        "locked": [
            "你的隐藏优势：你有可以被产品化或服务化的能力，只是过去可能把它当成普通经验。",
            "你的赚钱卡点：你容易停在想法阶段，没有把能力变成别人能理解、能购买的小产品。",
            "适合你的变现方式：先从一个低价、小交付、好验证的产品开始，不要一上来做太复杂。",
            "未来 7 天建议：写出一个你能帮别人解决的小问题，并设计一个 1.9-9.9 元的最小交付。",
        ],
    },
}


REPORT_SLUG_OVERRIDES = {
    "be-controlled": {
        "index": "被拿捏风险指数",
        "gold": "真正让你被拿捏的，往往是你太想被坚定选择。",
        "core_prefix": "你要看清的不是对方有多会拿捏，而是你在哪个瞬间最容易把边界交出去。",
    },
    "hot-or-steady-love": {
        "index": "亲密需求指数",
        "gold": "有人适合点燃你，有人适合安放你。",
        "core_prefix": "你真正需要的爱，不一定是最热烈的那种，而是能让你长期安心做自己的那种。",
    },
    "money-talent": {
        "index": "赚钱潜力指数",
        "gold": "你不是没有赚钱能力，只是还没把轻松的能力放到正确位置。",
        "core_prefix": "你最值得放大的赚钱方式，通常藏在别人经常向你求助、而你做起来并不费力的地方。",
    },
    "life-script": {
        "index": "人生剧本指数",
        "gold": "你的性格不是限制，它只是一直在替你选择熟悉的剧情。",
        "core_prefix": "你反复遇到的选择和关系，可能不是偶然，而是你的性格模式在悄悄推着剧情往前走。",
    },
    "wrong-person": {
        "index": "关系适配风险指数",
        "gold": "不合适的人，不是靠忍就能走长久。",
        "core_prefix": "你需要识别的不是谁好谁坏，而是哪类相处方式会持续消耗你的安全感和自我感。",
    },
    "strong-or-growth-love": {
        "index": "恋爱模式适配指数",
        "gold": "强者恋爱和养成系恋爱没有高低，只有适不适合你。",
        "core_prefix": "你在关系里真正需要的位置，决定了你适合被托举、并肩成长，还是慢慢参与彼此升级。",
    },
    "like-signals": {
        "index": "喜欢信号识别指数",
        "gold": "真正喜欢你的人，不会只给你上头，也会给你安心。",
        "core_prefix": "你需要分清的是：对方是在制造暧昧情绪，还是在用稳定行动表达真正的喜欢。",
    },
    "love-clarity": {
        "index": "恋爱清醒指数",
        "gold": "恋爱清醒不是不心动，而是心动时也没有弄丢自己。",
        "core_prefix": "你的清醒度，体现在喜欢一个人之后，还能不能看见自己的边界、需求和真实感受。",
    },
}


def build_auto_report_preview(meta, results):
    template = REPORT_TEMPLATES[meta["category"]]
    override = REPORT_SLUG_OVERRIDES.get(meta["slug"], {})
    reports = {}
    score_map = {"A": 82, "B": 86, "C": 79, "D": 84}
    for key, result in results.items():
        reports[key] = {
            "name": result["name"],
            "index_label": override.get("index", template["index"]),
            "base_score": score_map[key],
            "summary": result["summary"],
            "core": f"{override.get('core_prefix', template['core_prefix'])} {result['sections'][0]}",
            "gold": override.get("gold", result["summary"]),
            "locked": template["locked"],
        }
    return {
        "enabled": True,
        "demo_unlocked": True,
        "label": template["label"],
        "kicker": template["kicker"],
        "unlock_title": "完整报告 · 查看你的专属分析",
        "unlock_text": "完整报告将展开你的隐藏优势、主要卡点、适合路径和未来 7 天建议。",
        "button_text": "查看完整报告演示版",
        "reports": reports,
    }


def parse_sections():
    text = SOURCE.read_text(encoding="utf-8")
    sections = []
    current = None
    for line in text.splitlines():
        header = re.match(r"^##\s+\d+\.\s+(.+)$", line)
        question = re.match(r"^\d+\.\s+(.+)$", line)
        if header:
            current = {"title": header.group(1).strip(), "questions": []}
            sections.append(current)
        elif question and current is not None:
            current["questions"].append(question.group(1).strip())
    return sections


def build_questions(lines, category):
    return [
        {
            "text": line,
            "options": [{"text": text, "type": option_type} for text, option_type in build_options(line, category, index)],
        }
        for index, line in enumerate(lines[:30])
    ]


def build_city_questions():
    return [
        {
            "text": row[0],
            "options": [
                {"text": row[1], "type": "A"},
                {"text": row[2], "type": "B"},
                {"text": row[3], "type": "C"},
                {"text": row[4], "type": "D"},
            ],
        }
        for row in CITY_QUESTIONS
    ]


def build_results(category):
    result = {}
    for key, (name, summary, section) in RESULTS[category].items():
        result[key] = {
            "name": name,
            "summary": summary,
            "sections": [
                section,
                "你可以把这个结果当成一个提醒：不是给自己贴标签，而是看清现在最值得调整的地方。",
                "接下来 7 天，选一个最小行动去验证它。真正有用的测试，不是让你立刻改变人生，而是让你更愿意靠近自己。",
            ],
        }
    return result


def build_config(meta, question_lines):
    category = meta["category"]
    config = {
        "slug": meta["slug"],
        "theme": meta["title"],
        "eyebrow": meta["eyebrow"],
        "title": meta["title"],
        "subtitle": meta["subtitle"],
        "subtitle_lines": [
            meta["subtitle"],
            "不用纠结标准答案，凭第一感觉选就好。",
        ],
        "price_hint": "娱乐测试，仅供自我探索参考，不构成心理或职业诊断。",
        "intro": meta["intro_paragraphs"][0],
        "intro_paragraphs": meta["intro_paragraphs"],
        "value_statement": meta["value_statement"],
        "dimensions": meta["dimensions"],
        "style": meta["style"],
        "share_line": meta["share_line"],
        "questions": build_city_questions() if meta.get("report_preview") == "city-fit" else build_questions(question_lines, category),
        "results": CITY_RESULTS if meta.get("report_preview") == "city-fit" else build_results(category),
    }
    if meta.get("report_preview") == "career-decision":
        config["report_preview"] = {
            "enabled": True,
            "demo_unlocked": True,
            "label": "你的专属决策报告",
            "kicker": "CAREER · REPORT",
            "unlock_title": "完整报告 · 解锁你的专属决策分析",
            "unlock_text": "完整报告将展开你的隐藏优势、主要卡点、适合的行动路径和未来 7 天调整建议。",
            "button_text": "查看完整报告演示版",
            "reports": CAREER_DECISION_REPORTS,
        }
        config["results"] = build_results(category)
        for key, report in CAREER_DECISION_REPORTS.items():
            config["results"][key]["name"] = report["name"]
            config["results"][key]["summary"] = report["summary"]
            config["results"][key]["sections"] = [report["core"]]
    elif meta.get("report_preview") == "auto":
        config["report_preview"] = build_auto_report_preview(meta, config["results"])
    elif meta.get("report_preview") == "city-fit":
        config["report_preview"] = {
            "enabled": True,
            "demo_unlocked": True,
            "label": "你的专属城市适配报告",
            "kicker": "CITY · REPORT",
            "unlock_title": "完整报告 · 查看你的城市适配分析",
            "unlock_text": "完整报告将展开你的城市优势、潜在消耗、适合路径和未来 7 天建议。",
            "button_text": "查看完整报告演示版",
            "reports": CITY_REPORTS,
        }
    return config


def normalize_title(title):
    title = title.replace("测一测，", "").replace("一分钟测出", "")
    return re.sub(r"[\s，,？?！!、：:]", "", title)


def main():
    sections = parse_sections()
    by_title = {section["title"]: section["questions"] for section in sections}
    generated = []
    for meta in TEST_META:
        question_lines = by_title.get(meta["title"])
        if question_lines is None:
            wanted = normalize_title(meta["title"])
            for source_title, source_questions in by_title.items():
                source = normalize_title(source_title)
                if source.startswith(wanted) or wanted in source or source in wanted:
                    question_lines = source_questions
                    break
        if not question_lines or len(question_lines) < 30:
            raise RuntimeError(f"题目不足 30 道：{meta['title']}")
        config = build_config(meta, question_lines)
        page_dir = OUTPUT_DIR / meta["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "test_config.json").write_text(
            json.dumps(config, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        (page_dir / "index.html").write_text(render_html(config), encoding="utf-8")
        generated.append(meta["slug"])

    print(f"已生成 {len(generated)} 套测试：")
    for slug in generated:
        print(f"- {slug}")


if __name__ == "__main__":
    main()
