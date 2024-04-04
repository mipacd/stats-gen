#channel list for finding chat messages
vtuber_list = ['AZKi Channel', 'Miko Ch. さくらみこ', 'Roboco Ch. - ロボ子', 'SoraCh. ときのそらチャンネル', 'Suisei Channel',
    'Mel Channel 夜空メル', 'Haato Channel 赤井はあと', 'フブキCh。白上フブキ', 'Matsuri Channel 夏色まつり', 'アキロゼCh。Vtuber/ホロライブ所属',
    'Shion Ch. 紫咲シオン', 'Aqua Ch. 湊あくあ', 'Nakiri Ayame Ch. 百鬼あやめ', 'Choco Ch. 癒月ちょこ', 'Choco subCh. 癒月ちょこ',
    'Subaru Ch. 大空スバル', 'Korone Ch. 戌神ころね', 'Mio Channel 大神ミオ', 'Okayu Ch. 猫又おかゆ', 'Noel Ch. 白銀ノエル',
    'Rushia Ch. 潤羽るしあ', 'Pekora Ch. 兎田ぺこら', 'Flare Ch. 不知火フレア', 'Marine Ch. 宝鐘マリン', 'Luna Ch. 姫森ルーナ',
    'Coco Ch. 桐生ココ', 'Watame Ch. 角巻わため', 'Kanata Ch. 天音かなた', 'Towa Ch. 常闇トワ', 'Lamy Ch. 雪花ラミィ', 'Nene Ch.桃鈴ねね',
    'Botan Ch.獅白ぼたん', 'Aloe Ch.魔乃アロエ', 'Polka Ch. 尾丸ポルカ', 'Aruran Ch. アルランディス', 'Rikka ch.律可', 'Kira Ch. 鏡見キラ',
    'Miyabi Ch. 花咲みやび', 'Izuru Ch. 奏手イヅル', 'Temma Ch. 岸堂天真', 'Roberu Ch. 夕刻ロベル', 'astel ch.アステル', 'Oga Ch.荒咬オウガ',
    'Shien Ch.影山シエン', 'Airani Iofifteen Channel', 'Moona Hoshinova hololive-ID', 'Ayunda Risu Ch.', '天野ピカミィ. Pikamee',
    '緋笠トモシカ - Tomoshika Hikasa -', '磁富モノエ', '月ノ美兎', 'でびでび・でびる', '鈴原るる【にじさんじ所属】', 'Hana Macchia Ch.【NIJISANJI ID】',
    '佃煮のりおちゃんねる【犬山たまき】', 'ひなたチャンネル', '星川サラ / Sara Hoshikawa', '勇気ちひろ', 'エルフのえる / にじさんじ所属', '樋口楓【にじさんじ所属】',
    'Shizuka Rin Official', '渋谷ハジメのはじめ支部', '鈴谷アキの陽だまりの庭', '《にじさんじ所属の女神》モイラ', '♥️♠️物述有栖♦️♣️', '伏見ガク【にじさんじ所属】',
    '家長むぎ【にじさんじ所属】', '森中花咲', '宇志海いちご', 'Yuhi Riri Official', '剣持刀也', 'Gilzaren III Season 2', '文野環【にじさんじの野良猫】ふみのたまき',
    '鈴鹿詩子 Utako Suzuka', 'Kanae Channel', '赤羽葉子ちゃんねる', '笹木咲 / Sasaki Saku', '闇夜乃モルル / Moruru Yamiyono', '本間ひまわり - Himawari Honma -',
    '魔界ノりりむ', 'Kuzuha Channel', '雪汝*setsuna channel', '椎名唯華', 'ドーラ', '花畑チャイカ', '八朔ゆず【にじさんじ】', '《IzumoKasumi》Project channel【にじさんじ】',
    '安土桃', '名伽尾アズマ', '鳴門こがね', '緑仙channel', 'シスター・クレア -SisterClaire-', 'Masaru Suzuki/Nijisanji', '轟京子/kyoko todoroki【にじさんじ】',
    '海夜叉神/黄泉波咲夜【にじさんじ】', '卯月コウ', '社築', '【にじさんじ】神田笑一', '雨森小夜', '鷹宮リオン', '飛鳥ひな【にじさんじ所属】', '舞元啓介', '竜胆 尊 / Rindou Mikoto',
    'ジョー・力一 Joe Rikiichi', '町田ちま【にじさんじ】', '月見しずく', '桜凛月', '遠北千南 / Achikita Chinami 【にじさんじ', '矢車りね - Rine Yaguruma -',
    '夢追翔のJUKE BOX', '黒井しば【にじさんじの犬】', '春崎エアル', '成瀬 鳴 / Naruse Naru【にじさんじ】', '童田明治-わらべだめいじー-', 'Kudou_chitose / 久遠千歳',
    '【3年0組】郡道美玲の教室', '小野町春香♨Onomachi Haruka にじさんじ', '語部紡', '瀬戸 美夜子 - Miyako Seto', 'Raito Channel-真堂雷斗/にじさんじ-',
    '御伽原 江良 / Otogibara Era【にじさんじ】', '戌亥とこ -Inui Toko-', 'アンジュ・カトリーナ - Ange Katrina -', 'リゼ・ヘルエスタ -Lize Helesta-',
    '三枝明那 / Saegusa Akina', '愛園 愛美/Aizono Manami', '雪城眞尋/Yukishiro Mahiro【にじさんじ所属】', 'エクス・アルビオ -Ex Albio-',
    'レヴィ・エリファ-Levi Elipha-', '葉山舞鈴 / Hayama Marin【にじさんじ所属】', 'ニュイ・ソシエール //[Nui Sociere]', '葉加瀬 冬雪 / Hakase Fuyuki',
    '加賀美 ハヤト/Hayato Kagami', '夜見れな/yorumi rena【にじさんじ所属】', '黛 灰 / Kai Mayuzumi【にじさんじ】', 'アルス・アルマル -ars almal- 【にじさんじ】',
    '相羽ういは〖Aiba Uiha〗にじさんじ所属', '天宮 こころ / Amamya Ch.', 'エリー・コニファー / Eli Conifer【にじさんじ】', 'ラトナ・プティ -Ratna Petit -にじさんじ所属',
    '早瀬 走 / Hayase Sou【にじさんじ所属】', '健屋花那【にじさんじ】KanaSukoya', 'シェリン・バーガンディ -Shellin Burgundy- 【にじさんじ】', 'フミ/にじさんじ',
    '山神 カルタ / Karuta Yamagami', '魔使マオ -matsukai mao-', 'えま★おうがすと', 'ルイス・キャミー', '不破 湊 / Fuwa Minato【にじさんじ】',
    '白雪 巴/Shirayuki Tomoe【にじさんじ】', 'Gwelu Os Gar 【nijisanji】', 'ましろ / Mashiro', '奈羅花 - Naraka -', '来栖 夏芽-kurusu natsume-【にじさんじ】',
    'フレン・E・ルスタリオ', 'メリッサ・キンレンカ', 'イブラヒム【にじさんじ】', '長尾 景 / Nagao Kei【にじさんじ】', '弦月 藤士郎 / Genzuki Tojiro【にじさんじ】',
    '甲斐田 晴 / Kaida Haru【にじさんじ】', '金魚坂めいろ', '空星きらめ/Sorahoshi Kirame【にじさんじ】', 'Asahina Akane / Virtual YouTuber【Nijisanji】',
    '周央 サンゴ / Suo Sango【にじさんじ】', '東堂コハク/ Todo Kohaku [にじさんじ]', '北小路ヒスイ / Kitakoji Hisui 【にじさんじ】', '西園チグサ / Nishizono Chigusa',
    'バーチャル債務者youtuber天開司', 'Fairys Channel', 'ZEA Cornelia【NIJISANJI ID】', 'Taka Radjiman【NIJISANJI ID】', 'Rai Galilei【NIJISANJI ID】',
    'Riksa Dhirendra【NIJISANJI ID】', 'Amicia Michella【NIJISANJI ID】', 'Miyu Ottavia 【NIJISANJI ID】', 'Azura Cecillia 【NIJISANJI ID】',
    'Layla Alstroemeria [NIJISANJI ID]', 'Nara Haramaung 【NIJISANJI ID】', 'Etna Crimson 【NIJISANJI ID】', 'Bonnivier Pranaja 【NIJISANJI ID】',
    'Siska Leontyne 【NIJISANJI ID】', 'Aadya【NIJISANJI EN】', 'Noor【NIJISANJI EN】', 'Vihaan【NIJISANJI EN】', 'Kurisu Channel 人見クリス',
    'Mori Calliope Ch. hololive-EN', 'Takanashi Kiara Ch. hololive-EN', "Ninomae Ina'nis Ch. hololive-EN", 'Gawr Gura Ch. hololive-EN',
    'Watson Amelia Ch. hololive-EN', 'Haachama Ch. 赤井はあと']

#name list for finding translations of the format <NAME: MSG>
vtuber_tl_list = ('azki:', 'miko:', 'roboco:', 'sora:', 'suisei:', 'mel:', 'haato:', 'haachama:', 'fubuki:', 'fbk:', 'matsuri:',
    'aki:', 'akirose:', 'shion:', 'aqua:', 'ayame:', 'choco:', 'subaru:', 'korone:', 'mio:', 'okayu:', 'noel:', 'rushia:', 'pekora:',
    'flare:', 'marine:', 'luna:', 'coco:', 'watame:', 'kanata:', 'towa:', 'lamy:', 'nene:', 'botan:', 'aloe:', 'polka:', 'aruran:',
    'rikka:', 'kira:', 'miyabi:', 'izuru:', 'temma:', 'roberu:', 'astel:', 'oga:', 'shien:', 'iofi:', 'moona:', 'risu:', 'haachama [', 'noel said' )
    
#known bad translators
tl_blist = ('TwoDigit User', 'Py', 'SillyMakesVids', 'Steve Wang', 'Panarchie', 'Titan Senpai', 'Crownless.Prince', 'Perun Gut', 'acr_8133', 'Razer', 'Anothr To', 'Your Pal, Max', '水寂天鏡老-Minasabi', 'レヨメエ', 'Andy', 'extazon', 'Blu3tato', 'Toby Fernando', 'Kento Nishi', 'Anonon Nonon', 'Gameh_Boi', 'Blu3tato')