#!/usr/bin/env python
talks = [{'istart': 0, 'iend': 3, 'talk': '谁？', 'module': 1, 'context': '克雷雅儿站住，大声问道。', 'speaker': '克雷雅儿'},
{'istart': 0, 'iend': 11, 'talk': '对不起。。。我。。。', 'module': 1, 'context': '少女显然很局促，她的眼睛在月光的照耀下很像一泓流光的清泉。', 'speaker': ''},
{'istart': 0, 'iend': 5, 'talk': '你是谁？', 'module': 1, 'context': '雅儿问道。这么晚了，怎么会有人在这里哭？', 'speaker': ''},
{'istart': 0, 'iend': 10, 'talk': '我。。我叫玲珑。。', 'module': 1, 'context': '少女的声音清脆如银铃一般，比刚才什么舞姬甜到化不开的嗓音好听多了。', 'speaker': ''},
{'istart': 0, 'iend': 18, 'talk': '玲珑，你是什么人？怎么会在这里哭？', 'module': 1, 'context': '雅儿问道，对这个柔柔弱弱的少女有一种莫名的好感。', 'speaker': ''},
{'istart': 0, 'iend': 16, 'talk': '我是四皇子殿下的奴婢，我。。。', 'module': 1, 'context': '玲珑的眼睛又一红，仿佛遇到了什么委屈的事。', 'speaker': ''},
{'istart': 16, 'iend': 37, 'talk': '你大概也是被欺负了吧，男人总是喜新厌旧。', 'module': 1, 'context': '雅儿找了个台阶坐下，叹了口气道：', 'speaker': ''},
{'istart': 0, 'iend': 19, 'talk': '不。。不是的。。主人对我很好的。。。', 'module': 1, 'context': '玲珑脸上一红，想要辩解道。', 'speaker': ''},
{'istart': 0, 'iend': 25, 'talk': '正好我也不想回去，遇到你也是一种缘分，过来坐吧。', 'module': 1, 'context': '雅儿向玲珑招手，她的动作仿佛具有魔力一般吸引着玲珑向前迈开步子，坐在雅儿身边。', 'speaker': ''},
{'istart': 0, 'iend': 14, 'talk': '这么说，你是喜欢风无极了？', 'module': 1, 'context': '雅儿翘起脚问道。', 'speaker': ''},
{'istart': 0, 'iend': 36, 'talk': '是。。我喜欢主人。。虽然他经常做出一副冷酷的样子，但内心其实很温柔呢。', 'module': 1, 'context': '玲珑的眼里流露出暖暖的爱意，唇角也挂着微笑。', 'speaker': ''},
{'istart': 59, 'iend': 65, 'talk': '可是。。。', 'module': 1, 'context': '玲珑又低下头，道：', 'speaker': ''},
{'istart': 75, 'iend': 126, 'talk': '我不知道主人是否喜欢我。。。也许玲珑根本配不上主人。。主人能让我留在他身边已经是莫大的恩宠了。。。。', 'module': 1, 'context': '幽幽的声音道出她内心的苦涩。', 'speaker': ''},
{'istart': 52, 'iend': 69, 'talk': '你想不想知道风无极到底爱不爱你？', 'module': 1, 'context': '“玲珑”克雷雅儿突然抓住她的手，打断了她的思绪。克雷雅儿看着她，棕色的眼眸直接对上玲珑清泉般明亮的眼睛。', 'speaker': '克雷雅儿'},
{'istart': 14, 'iend': 26, 'talk': '当然想啊。。可是。。。', 'module': 1, 'context': '玲珑的心脏漏跳一拍，喃喃道：', 'speaker': ''},
{'istart': 0, 'iend': 6, 'talk': '别可是了。', 'module': 1, 'context': '克雷雅儿直接打断她，', 'speaker': '克雷雅儿'},
{'istart': 17, 'iend': 23, 'talk': '我有办法。', 'module': 1, 'context': '坚定的语气让玲珑无法不相信她。', 'speaker': ''},
{'istart': 0, 'iend': 14, 'talk': '只要。。你有这个胆子。。。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 0, 'iend': 29, 'talk': '我。。愿意。。。不管付出什么代价。。。我愿意尝试。。。。', 'module': 1, 'context': '玲珑彷佛鼓足了很大的勇气一般，', 'speaker': ''},
{'istart': 45, 'iend': 74, 'talk': '就算知道了主人不喜欢我。。。那我。。。也可以死心了。。。', 'module': 0, 'context': '玲珑彷佛鼓足了很大的勇气一般，', 'speaker': ''},
{'istart': 16, 'iend': 25, 'talk': '那，就跟我走吧。', 'module': 1, 'context': '克雷雅儿笑笑，如女神般散发光芒，', 'speaker': '克雷雅儿'},
{'istart': 36, 'iend': 65, 'talk': '两位大人是来寻乐子的么？来我们这吧，是炎都最好的男娼馆~', 'module': 1, 'context': '走着，到了一座豪华的建筑门前，一个娘娘腔的打扮妖艳的男人立刻把她俩拦下。', 'speaker': ''},
{'istart': 80, 'iend': 98, 'talk': '什么类型的都有，包两位大人满意~~', 'module': 1, 'context': '边说还边向雅儿她们挤着媚眼，', 'speaker': ''},
{'istart': 22, 'iend': 52, 'talk': '本公子要干净乖巧的，天亮了还要马车把我们送回去，你这有么？', 'module': 1, 'context': '玲珑扑哧一声就笑出来了，雅儿饶有兴趣地问道：', 'speaker': ''},
{'istart': 33, 'iend': 47, 'talk': '有，有。两位大人请随我来。', 'module': 1, 'context': '娘娘腔男人一听有生意做，立刻笑开了花，脸上厚厚的脂粉都抖掉了一层：', 'speaker': ''},
{'istart': 40, 'iend': 107, 'talk': '两位大人，这四个是我们这姿容最上乘的小倌，都还未服侍过人。从小就好生调教着，绝对能让大人满意，不过。。。这价钱么。。。自然贵些。。。', 'module': 1, 'context': '雅儿和玲珑进入一个雅室，不一会老板带了四个看起来十三四岁，稚气未脱的美少年上来。', 'speaker': ''},
{'istart': 0, 'iend': 16, 'talk': '果然不错，都留下了，你出去吧。', 'module': 1, 'context': '雅儿淡淡地道。', 'speaker': ''},
{'istart': 15, 'iend': 25, 'talk': '奴才听候大人吩咐。', 'module': 1, 'context': '四个美少年单膝跪下，柔顺地道：', 'speaker': ''},
{'istart': 11, 'iend': 15, 'talk': '雅。。', 'module': 1, 'context': '玲珑紧张地回头看雅儿，', 'speaker': ''},
{'istart': 22, 'iend': 48, 'talk': '你们放心，我不会强迫你们做什么的。过来帮我锤锤腿。', 'module': 1, 'context': '雅儿倒是一副气定神闲的样子，半抬起眼睛，道：', 'speaker': ''},
{'istart': 15, 'iend': 26, 'talk': '我们在这里要做什么？', 'module': 1, 'context': '玲珑显然极不适应。她对雅儿说：', 'speaker': ''},
{'istart': 0, 'iend': 38, 'talk': '你放心。如果那个人在乎，便会花尽心思来寻你。如果不在乎。。。那你也知道了。', 'module': 1, 'context': '雅儿安心享受着美少年的按摩，慵懒地道。', 'speaker': ''},
{'istart': 0, 'iend': 16, 'talk': '这个时候，他们该结束了吧。。。', 'module': 1, 'context': '玲珑喃喃道，她不明白自己怎么会鬼使神差般地就答应了雅儿，不知道自己怎么就身处在了男娼馆，她如今做的一切都是不会被主人原谅的，也许是雅儿身上的气质太难以让人抗拒，也许是自己本来就不是个好奴儿，总之，不安也罢，焦虑也罢，她的内心，还是很渴望知道主人的想法，就算。。。就算要付出怎样的代价也好。。。。', 'speaker': ''},
{'istart': 19, 'iend': 95, 'talk': '没事的，天塌下来了有我和你一起顶着，再说了，如果风无极找来这里，不就证明他心里喜欢你，在乎你么。毕竟，丢了个奴婢对皇子来说又没什么大不了的，你明白么？', 'module': 1, 'context': '玲珑的脸色渐显憔悴，雅儿柔声安慰她道：', 'speaker': ''},
{'istart': 15, 'iend': 61, 'talk': '玲珑知道。不管主人他会怎么生气，但如果。。。如果主人能来找玲珑。。玲珑就是死也甘心了。。。', 'module': 1, 'context': '玲珑点点头，勉强对雅儿一笑道：', 'speaker': ''},
{'istart': 15, 'iend': 41, 'talk': '瞧你，这么没出息。怎么会让你死呢？最多不就打一顿。', 'module': 1, 'context': '雅儿用手指刮了一下玲珑的鼻子，', 'speaker': ''},
{'istart': 11, 'iend': 50, 'talk': '玲珑宁愿让主人打。。。虽然很痛。。但是每次主人给玲珑上药。。。都好温柔。。。', 'module': 1, 'context': '玲珑脸上一红，羞涩道：', 'speaker': ''},
{'istart': 0, 'iend': 8, 'talk': '你吸食幻樱散？', 'module': 1, 'context': '墨炎看着雅儿问道，平静的双眸中看不出一丝波澜。', 'speaker': '墨炎'},
{'istart': 0, 'iend': 5, 'talk': '我。。。', 'module': 1, 'context': '雅儿一时语塞，她的大脑还被轻微麻痹着，没有从那云雾中清醒过来，一时没反应过来墨炎和风无极怎么来了', 'speaker': '墨炎'},
{'istart': 47, 'iend': 58, 'talk': '奴婢参见陛下，主人。', 'module': 1, 'context': '玲珑看见两人走进来也是呆了片刻，不过她比雅儿反应的快，立时跪到了地上，清脆的声音里饱含了不安:', 'speaker': ''},
{'istart': 27, 'iend': 50, 'talk': '原来你还记得你有主人么，我看你在这挺舒服的。', 'module': 1, 'context': '风无极走向前两步，对着跪在地上的玲珑，嘲弄地笑了一声：', 'speaker': ''},
{'istart': 0, 'iend': 26, 'talk': '克雷雅儿，朕真是小看你了，没想到你的本事这样大啊。', 'module': 1, 'context': '墨炎说的不缓不急，却让人感到一股寒意。', 'speaker': '墨炎'},
{'istart': 15, 'iend': 51, 'talk': '陛下息怒，不关雅儿姐姐的事，一切都是奴婢的错。陛下请责罚奴婢一人就好。', 'module': 1, 'context': '玲珑看到这番情况，忙又磕头道：', 'speaker': ''},
{'istart': 0, 'iend': 4, 'talk': '放肆！', 'module': 1, 'context': '风无极怒斥道：', 'speaker': ''},
{'istart': 12, 'iend': 54, 'talk': '陛下没问你话，谁让你抢着答了。还如此大胆对克雷雅儿殿下不用敬称，规矩都到哪里去了！', 'module': 0, 'context': '风无极怒斥道：', 'speaker': ''},
{'istart': 0, 'iend': 6, 'talk': '奴婢该死，', 'module': 1, 'context': '玲珑浑身瑟缩，', 'speaker': ''},
{'istart': 14, 'iend': 24, 'talk': '请陛下，主人恕罪。', 'module': 0, 'context': '玲珑浑身瑟缩，', 'speaker': ''},
{'istart': 32, 'iend': 36, 'talk': '掌嘴。', 'module': 1, 'context': '风无极看着跪着发抖的玲珑，没有半点怜惜，懒懒的从口中吐出两个字，', 'speaker': ''},
{'istart': 78, 'iend': 87, 'talk': '玲珑！你做什么！', 'module': 1, 'context': '雅儿却被这清脆的巴掌声带回现实，发现玲珑居然跪着扇自己的耳光，原本清丽的面容都有了分明的指印！她忙并步走到玲珑面前，拦住她本要狠狠落在自己脸上的手，厉声道：', 'speaker': ''},
{'istart': 40, 'iend': 56, 'talk': '风无极！你怎么能如此对待玲珑！', 'module': 1, 'context': '玲珑抿嘴不语，羞辱的热泪顺着受伤的脸颊滑落下来。克雷雅儿回头对着风无极忿忿地说：', 'speaker': '克雷雅儿'},
{'istart': 8, 'iend': 33, 'talk': '克雷雅儿殿下，那你以为该怎么对待一个外逃的奴婢？', 'module': 1, 'context': '风无极皱皱眉头，', 'speaker': ''},
{'istart': 35, 'iend': 64, 'talk': '你们不要乱来，玲珑是我带出来的，她没有要逃跑。她没有错。', 'module': 1, 'context': '想到这个恐怖的场面，雅儿浑身一颤，忙用手护住玲珑，对着墨炎和风无极道：', 'speaker': '墨炎'},
{'istart': 13, 'iend': 56, 'talk': '克雷雅儿殿下，请你放开玲珑。玲珑比不上您的身份尊贵，您如此维护她，对她未必是件好事。', 'module': 1, 'context': '风无极面色一沉，低低的说：', 'speaker': ''},
{'istart': 9, 'iend': 43, 'talk': '墨炎，都是我的错，你们不要惩罚玲珑，我们。。。跟你们回宫便是。。。', 'module': 1, 'context': '雅儿转头看着墨炎，', 'speaker': '墨炎'},
{'istart': 28, 'iend': 32, 'talk': '回宫。', 'module': 1, 'context': '墨炎一直冷冷地看着她们二人，半晌无声。一会，他薄唇微动，', 'speaker': '墨炎'},
{'istart': 13, 'iend': 39, 'talk': '陛下，无极治下无方，给陛下添了麻烦，真是非常抱歉。', 'module': 1, 'context': '风无极对着墨炎微微躬身道：', 'speaker': '墨炎'},
{'istart': 49, 'iend': 70, 'talk': '风皇子早点回去休息吧，有事我们明日再议。', 'module': 1, 'context': '墨炎微微点头，道：', 'speaker': '墨炎'},
{'istart': 0, 'iend': 21, 'talk': '还有心情关心别人么，先关心一下你自己吧。', 'module': 1, 'context': '墨炎清冽的声音在耳边响起，', 'speaker': '墨炎'},
{'istart': 35, 'iend': 43, 'talk': '跟我来御书房。', 'module': 0, 'context': '墨炎清冽的声音在耳边响起，', 'speaker': '墨炎'},
{'istart': 12, 'iend': 33, 'talk': '这次又是为了什么？别跟我说你是助人为乐。', 'module': 1, 'context': '终于，墨炎喉咙微动，道：', 'speaker': '墨炎'},
{'istart': 8, 'iend': 14, 'talk': '不记得了。', 'module': 1, 'context': '雅儿撇撇嘴，道：', 'speaker': ''},
{'istart': 16, 'iend': 38, 'talk': '克雷雅儿，这个答案，可以视为你在挑衅我么？', 'module': 1, 'context': '墨炎眸光闪动，声音变得邪魅起来，', 'speaker': '墨炎'},
{'istart': 20, 'iend': 28, 'talk': '我没有挑衅你。', 'module': 1, 'context': '雅儿身上彷佛有微电流闪过，她压低声音道：', 'speaker': ''},
{'istart': 93, 'iend': 107, 'talk': '我的事情，我倒想见识见识。', 'module': 1, 'context': '墨炎笑了笑，俊逸的面庞在灯火的照映下更显邪凛，“背着我出宫，拐骗风无极的小奴隶，去男娼馆逍遥，服用幻樱散，问你原因就是”不记得“三个字，如果这些都不是在挑衅我，你还能做出什么称之为”挑衅', 'speaker': '墨炎'},
{'istart': 22, 'iend': 43, 'talk': '我给你定的规矩，还记得么？说给我听一遍。', 'module': 1, 'context': '墨炎低头，摩挲着戒指上的宝石，漫不经心地道：', 'speaker': '墨炎'},
{'istart': 22, 'iend': 36, 'talk': '第一。。不能挑衅陛下。。。', 'module': 1, 'context': '雅儿的手指都情不自禁的卷曲起来，她缓缓地道：', 'speaker': ''},
{'istart': 0, 'iend': 16, 'talk': '。。第二。。不能欺骗陛下。。。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 0, 'iend': 15, 'talk': '第三。。不能胡作非为。。。。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 0, 'iend': 15, 'talk': '第四。。不能自作主张。。。。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 0, 'iend': 7, 'talk': '。。。。。。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 0, 'iend': 14, 'talk': '第五。。要及时认错。。。。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 25, 'iend': 38, 'talk': '你看看自己都做了什么了！', 'module': 1, 'context': '墨炎按住长椅扶手，黑色的眸子仿佛黑曜石般散发光彩，', 'speaker': '墨炎'},
{'istart': 0, 'iend': 15, 'talk': '把书案收拾干净，自己趴上去。', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 0, 'iend': 10, 'talk': '八十下，自己数着。', 'module': 1, 'context': '墨炎冷冷地命令道，没有任何多余的话语。', 'speaker': '墨炎'},
{'istart': 0, 'iend': 7, 'talk': '啊！一。。。', 'module': 1, 'context': '尽管做好了准备，但这疼痛还是超出了想象的范围，雅儿不禁低呼出声，但没忘报数。', 'speaker': ''},
{'istart': 0, 'iend': 8, 'talk': '嗯。。。二。。', 'module': 1, 'context': '太痛了！不出声几乎不可能！', 'speaker': ''},
{'istart': 0, 'iend': 8, 'talk': '三。。呼呼。。', 'module': 1, 'context': '雅儿紧闭双目，痛的直喘气。', 'speaker': ''},
{'istart': 0, 'iend': 9, 'talk': '四。。。五。。。', 'module': 1, 'context': '雅儿艰难地报出数字，本来准备要受完八十下藤条的她现在就动摇了意志，觉得那实在是不可能的事。', 'speaker': ''},
{'istart': 0, 'iend': 9, 'talk': '啊~！！六。。。', 'module': 1, 'context': '雅儿难耐地扭动身子。', 'speaker': ''},
{'istart': 0, 'iend': 6, 'talk': '九。。十！', 'module': 1, 'context': '雅儿数完十下，好想求墨炎休息一下再打，可是她偏说不出口。', 'speaker': '墨炎'},
{'istart': 0, 'iend': 11, 'talk': '啊~！好痛~~！！！', 'module': 1, 'context': '雅儿痛呼起来，身子躬起，把臀部抬离了桌面。', 'speaker': ''},
{'istart': 0, 'iend': 4, 'talk': '报数。', 'module': 1, 'context': '墨炎冷冰冰地命令，用藤条压着雅儿的腰，让她重新在青玉书案上趴好。', 'speaker': '墨炎'},
{'istart': 0, 'iend': 4, 'talk': '十六！', 'module': 1, 'context': '雅儿忍住痛大声叫道。', 'speaker': ''},
{'istart': 0, 'iend': 4, 'talk': '十七！', 'module': 0, 'context': '', 'speaker': ''},
{'istart': 6, 'iend': 10, 'talk': '十八！', 'module': 1, 'context': '“嗖-啪！”', 'speaker': ''},
{'istart': 6, 'iend': 26, 'talk': '啊~~！十九。。。不要再打这边了。。。', 'module': 1, 'context': '“嗖-啪！”', 'speaker': ''},
{'istart': 6, 'iend': 14, 'talk': '啊~~！二十！', 'module': 1, 'context': '“嗖-啪！”', 'speaker': ''},
{'istart': 0, 'iend': 22, 'talk': '呜呜呜。。。好痛。。。不要打了。。。。。。', 'module': 1, 'context': '雅儿实在熬刑不过，开始哀求起来。', 'speaker': ''},
{'istart': 0, 'iend': 18, 'talk': '墨炎。。不要打了。。雅儿好痛。。。', 'module': 1, 'context': '雅儿开始撒娇，希望他能放过她。', 'speaker': ''},
{'istart': 31, 'iend': 82, 'talk': '你以为，每次做任何事都可以不负责任么？你以为，你只要撒个娇，讨个饶，别人就能原谅你做错的任何事了么？', 'module': 1, 'context': '墨炎漆黑的双眸里此时像蒙上了一层冰。他牵动唇角，冷冽的声音道：', 'speaker': '墨炎'},
{'istart': 0, 'iend': 9, 'talk': '啊~~！疼~~！', 'module': 1, 'context': '雅儿的眼角完全湿润着，她抓紧了书案的边缘，哭叫道。', 'speaker': ''},
{'istart': 0, 'iend': 13, 'talk': '呜呜。。呜。。好痛。。。', 'module': 1, 'context': '雅儿不停地抽泣，墨炎的大手在她的屁股游走，她幻想着这样意味着惩罚已经结束了。', 'speaker': '墨炎'},
{'istart': 0, 'iend': 3, 'talk': '啊！', 'module': 1, 'context': '雅儿痛的尖叫起来。', 'speaker': ''},
{'istart': 0, 'iend': 13, 'talk': '不要！不要！我求求你了！', 'module': 1, 'context': '雅儿用手撑住桌面，试图起身离开书案，她实在太想逃了！！！', 'speaker': ''},
{'istart': 0, 'iend': 5, 'talk': '啊！啊！', 'module': 1, 'context': '雅儿痛的不能说出连续的语句，只能短促地呼喊，在这急剧的疼痛中，她真的后悔万分！如果早知道这样，她绝对不会做出这些事，她绝对不会出宫，不会去男娼馆，不会去“诱惑”里糜烂地抽幻樱散！一时的任性和堕落居然给自己带来如此的痛苦！她真的后悔了！！！', 'speaker': ''},
{'istart': 0, 'iend': 50, 'talk': '你不要我了！。。。你要打死我了！。。。呜呜呜。。。。我认错了还不行么。。。。你要把我打死。。。。。', 'module': 1, 'context': '雅儿哭着喊着，都听不太清她说什么。', 'speaker': ''},
{'istart': 0, 'iend': 43, 'talk': '。。呜呜呜。。。。好痛。。。你不要打了。。。我要被打死了。。。呜。。。呜呜。。。。。', 'module': 1, 'context': '雅儿的话几乎被哭声淹没了，她哭得放肆，好像几千年累积的泪水冲破了禁锢的牢笼，倾泻出来。。。。。。', 'speaker': ''},
{'istart': 0, 'iend': 23, 'talk': '怎么了，这下贱的身子被养了两日，变得金贵了？', 'module': 1, 'context': '风无极冷冷的嘲讽，伸手拿过一件丝衣披在自己身上。', 'speaker': ''},
{'istart': 0, 'iend': 19, 'talk': '哼，你还倒在那是等我来伺候你怎么着。', 'module': 1, 'context': '风无极冷嗤道。', 'speaker': ''},
{'istart': 0, 'iend': 18, 'talk': '主人。。。您听玲珑解释。。。。。。', 'module': 1, 'context': '玲珑不由自主地脸上已经湿漉漉一片，以前主人惩罚的时候，再严厉她也会忍住不哭的，可如今，她不知道怎么的眼泪就不自觉地满脸都是。', 'speaker': ''},
{'istart': 0, 'iend': 24, 'talk': '你眼里根本就没有我这个主人，我还听你解释什么？', 'module': 1, 'context': '风无极冰冷的声音里蕴含了怒气。不同寻常的成长经历，让他变成一个对人戒心极重，寡情凉薄的人。最无法忍受的就是别人对自己的背叛。他的路太辛苦，每一步都如同走在刀锋上一样，让他早已习惯把自己的情感压抑到几乎没有。他要的东西太不一样，对身边的人，无论身份高低，都要花无数的心思应对辨别，信任是他身上早已干涸的资源。玲珑虽然只是一个女奴，但却是他身边为数不多能让自己放心的人，现在，她根本不把自己放在眼里了。风无极此次出行，有许多挑战，但是千万没想到的是，一切都还算顺利，居然在平时一贯柔顺的玲珑身上出了岔子。还好没有出什么事，否则他回国以后，又不知道要受到多少刁难。他没有第一时间处死她，已经是对她最大的仁慈了。', 'speaker': ''},
{'istart': 0, 'iend': 12, 'talk': '不是的。。。主人。。。', 'module': 1, 'context': '玲珑泣不成声，她好想对他说出自己的感觉，但彷佛时间气氛一切都不对。看他那么生气的样子，自己只觉得后悔万分，一定是自己把一切都给弄砸了。', 'speaker': ''},
{'istart': 0, 'iend': 34, 'talk': '你现在是不服我的管了是吧？也好，不听话的奴才我从来不要，你给我滚。', 'module': 1, 'context': '风无极解开了她手上的绳索。/`$]$?“_%U/w3M;I', 'speaker': ''},
{'istart': 0, 'iend': 37, 'talk': '不要，主人。。。是玲珑错了，您要怎么打怎么罚都行，不要抛弃玲珑。。。。。', 'module': 1, 'context': '玲珑顾不得胳膊完全没有恢复知觉，跪到风无极的脚下。怎么。。。怎么能是这样呢？明明，主人前一刻还到“诱惑”去找自己，说明主人在乎自己的呀！玲珑泪如雨下，觉得自己惹风无极生这么大的气，都要抛弃自己了，真的是罪该万死。', 'speaker': ''},
{'istart': 0, 'iend': 14, 'talk': '主人，你不要丢掉玲珑。。。', 'module': 1, 'context': '玲珑抱着风无极的腿求道：', 'speaker': ''},
{'istart': 27, 'iend': 107, 'talk': '玲珑真的没有不把主人放在眼里，是玲珑大胆，跑出去让主人担心，玲珑该死，玲珑知道错了。。。。。主人您怎么教训玲珑都行，只求您不要再生气了，不要丢掉玲珑。。。。。', 'module': 1, 'context': '玲珑边哭边求，可怜的样子让风无极也不由得心中一软。', 'speaker': ''},
{'istart': 11, 'iend': 41, 'talk': '那好，你去床上趴好，受不住今日的惩罚，便自己收拾东西滚吧。', 'module': 1, 'context': '片刻，风无极终于发话。', 'speaker': ''},
{'istart': 0, 'iend': 3, 'talk': '是。', 'module': 1, 'context': '玲珑无比柔顺地应道，主人肯惩罚自己，就不会再生气了。', 'speaker': ''},
{'istart': 0, 'iend': 9, 'talk': '嗯。。。嗯。。。', 'module': 1, 'context': '尽管用尽了全身力气，玲珑也无法抵御这疼痛。她的身子已经不自觉地开始躲避板子。', 'speaker': ''},
{'istart': 0, 'iend': 18, 'talk': '呜呜呜。。。主人。。对不起。。。。', 'module': 1, 'context': '玲珑的道歉是真心的，她知道主人承受着多大的压力，知道主人在乎自己才会如此惩罚自己，知道自己的所作所为让主人失望了。她不怕痛，只怕主人对自己心灰意冷。', 'speaker': ''},
{'istart': 0, 'iend': 22, 'talk': '。。对不起。。主人。。。是玲珑错了。。。。', 'module': 1, 'context': '玲珑哭的一抽一抽，哽咽着道歉，她宁愿风无极把所有的怒气和失望都发泄在自己的身上，也不要风无极自此以后又变得冷冷的对所有人。自己的主人有多不容易，玲珑知道，她在心里面心疼他，真心希望他开心，只是他不知道。', 'speaker': ''},
{'istart': 0, 'iend': 8, 'talk': '你。。恨我么？', 'module': 1, 'context': '让你的生活天翻地覆，让你被忽视，被羞辱，被*****，让你的脸上总是挂满泪珠。', 'speaker': ''},
{'istart': 0, 'iend': 7, 'talk': '不。。。不！', 'module': 1, 'context': '终于鼓足勇气，一双晶莹发亮的眼眸对上了那琉璃色的温柔，只有她才懂得的温柔。', 'speaker': ''},
{'istart': 0, 'iend': 8, 'talk': '主人，我爱你。', 'module': 1, 'context': '晶莹的眼眸辉映着灯光，闪耀出他从未见过的美丽光芒。', 'speaker': ''},
{'istart': 0, 'iend': 21, 'talk': '主人，我爱你。。。。玲珑，真的好喜欢你。', 'module': 1, 'context': '泪光盈睫的颜容，晕染着让人目眩神迷的红晕，那是让他一辈子也无法放弃的颜色。', 'speaker': ''},
]