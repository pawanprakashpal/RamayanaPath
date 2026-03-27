import json

with open(r'c:/_work/RamayanaPath/data/tulsidas/uttar-kand.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build a map of verse id -> {translation, transliteration}
updates = {
    # === DOHA GROUP 106 ===
    "ut-106-c1": {
        "transliteration": "eka bāra gura līnha bolāī. mohi nīti bahu bhāṃti sikhāī.\nsiva sevā kara phala suta soī. abirala bhagati rāma pada hoī.",
        "translation": "Once my Guru called me and instructed me in morality in many ways. He said, 'The fruit of serving Shiva, my son, is unceasing devotion at the feet of Rama.'"
    },
    "ut-106-c2": {
        "transliteration": "rāmahi bhajahiṃ tāta siva dhātā. nara pāvaṃra kai ketika bātā.\njāsu carana aja siva anurāgī. tātu drohāṃ sukha cahasi abhāgī.",
        "translation": "'Shiva and Brahma themselves worship Rama, my son — what then of mere mortals? To whose feet even Brahma and Shiva are devoted — O wretch, you seek happiness by opposing your own father!'"
    },
    "ut-106-c3": {
        "transliteration": "hara kahuṃ hari sevaka gura kahēū. suni khaganātha hṛdaya mama dahēū.\nadhama jāti maiṃ bidyā pāeṃ. bhayauṃ jathā ahi dūdha piāeṃ.",
        "translation": "My Guru called Shiva a servant of Hari. Hearing this, O king of birds, my heart burned with rage. Low-born as I was, gaining learning only made me worse — like a serpent fed on milk."
    },
    "ut-106-c4": {
        "transliteration": "mānī kuṭila kubhāgya kujātī. gura kara droha karauṃ dinu rātī.\nati dayāla gura svalpa na krodhā. puni puni mohi sikhāva subodhā.",
        "translation": "Proud, crooked, ill-fated and low-born, I harbored hostility toward my Guru day and night. Yet my exceedingly kind Guru felt not the slightest anger and repeatedly gave me good counsel."
    },
    "ut-106-c5": {
        "transliteration": "jehi te nīca baṛāī pāvā. so prathamahi hati tāhi nasāvā.\ndhūma anala saṃbhava sunu bhāī. tehi bujhāva ghana padavī pāī.",
        "translation": "'A base person first destroys the very one from whom he received his greatness. Listen, brother — smoke, which is born of fire, extinguishes that very fire when it attains the status of a cloud.'"
    },
    "ut-106-c6": {
        "transliteration": "raja maga parī nirādara rahaī. saba kara pada prahāra nita sahaī.\nmaruta uṛāva prathama tehi bharaī. puni nṛpa nayana kirīṭanhi paraī.",
        "translation": "'Dust lies on the road, despised, enduring the kicks of all. But when the wind lifts it up, it first fills the eyes and settles on the crowns of kings.'"
    },
    "ut-106-c7": {
        "transliteration": "sunu khagapati asa samujhi prasaṃgā. budha nahiṃ karahiṃ adhama kara saṃgā.\nkabi kobida gāvahiṃ asī nītī. khala sana kalaha na bhala nahiṃ prītī.",
        "translation": "'Listen, O lord of birds — understanding this, the wise do not keep company with the base. Poets and scholars declare this principle: with the wicked, neither quarrel nor friendship is good.'"
    },
    "ut-106-c8": {
        "transliteration": "udāsīna nita rahia gosāīṃ. khala pariharia svāna kī nāīṃ.\nmaiṃ khala hṛdayaṃ kapaṭa kuṭilāī. gura hita kahai na mohi sohāī.",
        "translation": "'One should always remain indifferent toward the wicked, O Lord, and shun them like dogs.' But I was wicked at heart, full of deceit and crookedness; my Guru's wise counsel did not please me."
    },
    "ut-106-d": {
        "transliteration": "eka bāra hara maṃdira japata raheuṃ siva nāma.\ngura āyau abhimāna teṃ uṭhi nahiṃ kīnha pranāma.\nso dayāla nahiṃ kaheu kachu ura na roṣa lavalesa.\nati agha gura apamānatā sahi nahiṃ sake mahesa.",
        "translation": "Once, in the temple of Shiva, I sat chanting Shiva's name. My Guru came, but out of pride I did not rise to bow. That compassionate soul said nothing; there was not a trace of anger in his heart. But the great sin of disrespecting one's Guru — Lord Shiva himself could not tolerate it."
    },

    # === DOHA GROUP 107 ===
    "ut-107-c1": {
        "transliteration": "maṃdira mājha bhaī nabha bānī. re hatabhāgya agya abhimānī.\njadyapi tava gura keṃ nahiṃ krodhā. ati kṛpāla cita samyak bodhā.",
        "translation": "A voice resounded from the sky within the temple: 'O unfortunate, ignorant and arrogant one! Although your Guru has no anger — he is exceedingly merciful and possesses perfect wisdom —'"
    },
    "ut-107-c2": {
        "transliteration": "tadapi sāpa saṭha daihauṃ tohī. nīti birodha sohāi na mohī.\njauṃ nahiṃ daṃḍa karauṃ khala torā. bhraṣṭa hoi śrutimāraga morā.",
        "translation": "'— yet I shall curse you, O fool! Violation of right conduct does not please Me. If I do not punish you, O wretch, the path of the scriptures established by Me will be corrupted.'"
    },
    "ut-107-c3": {
        "transliteration": "je saṭha gura sana iriṣā karahīṃ. raurava naraka koṭi juga parahīṃ.\ntrijaga joni puni dharahiṃ sarīrā. ayuta janma bhari pāvahiṃ pīrā.",
        "translation": "'Those fools who bear malice toward their Guru fall into the Raurava hell for millions of ages. Then they take birth in the three lower species and suffer pain for ten thousand births.'"
    },
    "ut-107-c4": {
        "transliteration": "baiṭha rahesi ajagara iva pāpī. sarpa hohi khala mala mati byāpī.\nmahā biṭapa koṭara mahuṃ jāī. rahu adhamādhama adhagati pāī.",
        "translation": "'You sat still like a python, O sinner! Become a serpent, O wretch, your mind steeped in impurity. Go and dwell in the hollow of a great tree, O lowest of the low, having attained the worst fate.'"
    },
    "ut-107-d": {
        "transliteration": "hāhākāra kīnha gura dāruna suni siva sāpa.\nkaṃpita mohi biloki ati ura upajā paritāpa.\nkari daṃḍavata saprema dvija siva sanmukha kara jori.\nbinaya karata gadagada svara samujhi ghora gati mori.",
        "translation": "My Guru cried out in anguish hearing Shiva's terrible curse. Seeing me trembling, great compassion arose in his heart. The loving Brahmin prostrated before Shiva with folded hands, making his supplication in a choked voice, realizing my dreadful fate."
    },

    # === DOHA GROUP 108 ===
    "ut-108-ch": {
        "transliteration": "namāmīśamīśāna nirvāṇarūpaṃ. vibhuṃ vyāpakaṃ brahma vedasvarūpaṃ.\nnijaṃ nirguṇaṃ nirvikalpaṃ nirīhaṃ. cidākāśamākāśavāsaṃ bhaje'haṃ.\nnirākāramoṃkāramūlaṃ turīyaṃ. girā gyāna gotītamīśaṃ girīśaṃ.\nkarālaṃ mahākāla kālaṃ kṛpālaṃ. guṇāgāra saṃsārapāraṃ nato'haṃ.\ntuṣārādri saṃkāśa gauraṃ gabhīraṃ. manobhūta koṭi prabhā śrī śarīraṃ.\nsphurannmauli kallolini cāru gaṃgā. lasadbhālabālendu kaṃṭhe bhujaṃgā.\ncalatkuṃḍalaṃ bhrū sunetraṃ viśālaṃ. prasannānanaṃ nīlakaṃṭhaṃ dayālaṃ.\nmṛgādhīśacarmāmbaraṃ muṇḍamālaṃ. priyaṃ śaṃkaraṃ sarvanāthaṃ bhajāmi.\npracaṃḍaṃ prakṛṣṭaṃ pragalbhaṃ pareśaṃ. akhaṃḍaṃ ajaṃ bhānukoṭiprakāśaṃ.\ntrayaḥśūla nirmūlanaṃ śūlapāṇiṃ. bhaje'haṃ bhavānīpatiṃ bhāvagamyaṃ.\nkalātīta kalyāṇa kalpāntakārī. sadā sajjanānandadātā purārī.\ncidānandasaṃdoha mohāpahārī. prasīda prasīda prabho manmathārī.\nna yāvad umānātha pādāravindaṃ. bhajaṃtīha loke pare vā narāṇāṃ.\nna tāvatsukhaṃ śānti saṃtāpanāśaṃ. prasīda prabho sarvabhūtādhivāsaṃ.\nna jānāmi yogaṃ japaṃ naiva pūjāṃ. nato'haṃ sadā sarvadā śambhu tubhyaṃ.\njarā janma duḥkhaugha tātapyamānaṃ. prabho pāhi āpannamāmīśa śambho.",
        "translation": "I bow to the Lord of lords, the embodiment of liberation, the all-pervading, omnipresent Brahman in the form of the Vedas. I worship Him who is self-existent, attributeless, beyond thought, desireless, the conscious ether, dwelling in space. I bow to the formless One, rooted in Om, the fourth state beyond speech, knowledge and senses — the Lord of mountains. I bow to the fierce One, the destroyer of even great Death, the merciful, the abode of virtues, who is beyond worldly existence. His body is fair as snow-capped mountains, deep and unfathomable, radiant with the splendor of millions of Kamadevas. The beautiful Ganga plays on His matted locks; a crescent moon adorns His forehead, serpents encircle His neck. With swinging earrings, beautiful brows, large eyes, a cheerful face, a blue throat, and merciful nature — wearing a lion-skin garment and a garland of skulls — I worship my beloved Shankara, the Lord of all. I worship the fierce, supreme, bold Lord of lords — undivided, unborn, radiant as millions of suns — the trident-bearer who uproots the three afflictions, the consort of Bhavani, attainable through devotion. O destroyer of Tripura, beyond time, ever auspicious, who brings about the end of creation, ever bestowing bliss on the virtuous, who removes the delusion of conscious bliss — be gracious, be gracious, O Lord, slayer of Kamadeva! So long as people in this world or the next do not worship the lotus feet of Uma's Lord, there is no happiness, no peace, no end of suffering. Be gracious, O Lord who dwells in all beings! I know neither yoga, nor chanting, nor worship — I simply bow to you always and forever, O Shambhu. O Lord, protect this helpless one, scorched by the flood of old age, birth and sorrow — O Isha, O Shambho!"
    },
    "ut-108-sl": {
        "transliteration": "rudrāṣṭakamidaṃ proktaṃ vipreṇa haratoṣaye.\nye paṭhanti narā bhaktyā teṣāṃ śambhuḥ prasīdati.",
        "translation": "This Rudrashtakam was composed by the Brahmin to please Hara (Shiva). Those who recite it with devotion — Lord Shambhu is pleased with them."
    },
    "ut-108-d": {
        "transliteration": "suni binatī sarbagya siva dekhi bipra anurāgu.\npuni maṃdira nabhavānī bhai dvijabara bara māgu.\njauṃ prasanna prabhu mo para nātha dīna para nehu.\nnija pada bhagati dei prabhu puni dūsara bara dehu.\ntava māyā basa jīva jaṛa saṃtata phirai bhulāna.\ntehi para krodha na karia prabhu kṛpā siṃdhu bhagavāna.\nsaṃkara dīnadayāla aba ehi para hohu kṛpāla.\nsāpa anugraha hoi jehiṃ nātha thorehīṃ kāla.",
        "translation": "Hearing his prayer, the all-knowing Shiva saw the Brahmin's devotion. Again a divine voice spoke from within the temple: 'O best of Brahmins, ask a boon.' 'If You are pleased with me, O Lord, if You have love for the lowly — grant me devotion to Your feet, Lord, and then give me a second boon. The inert soul, under the sway of Your maya, wanders perpetually in delusion — be not angry with him, O Lord, O ocean of mercy, O God! O Shankara, O merciful to the humble, now be gracious to this one, so that the curse may turn into a blessing, O Lord, in a short time.'"
    },

    # === DOHA GROUP 109 ===
    "ut-109-c1": {
        "transliteration": "ehi kara hoi parama kalyānā. soi karahu aba kṛpānidhānā.\nbipragirā suni parahita sānī. evamstu iti bhaī nabhavānī.",
        "translation": "'Do that which will bring about the supreme welfare of this one, O treasury of mercy.' Hearing the Brahmin's words, steeped in compassion for others, a voice from the sky said, 'So be it!'"
    },
    "ut-109-c2": {
        "transliteration": "jadapi kīnha ehiṃ dāruna pāpā. maiṃ puni dīnha kopa kari sāpā.\ntadapi tumhāra sādhutā dekhī. karihauṃ ehi para kṛpā bisēṣī.",
        "translation": "'Although he has committed a terrible sin, and I too cursed him in anger — yet seeing your saintliness, I shall bestow special grace upon him.'"
    },
    "ut-109-c3": {
        "transliteration": "chamāsīla je para upakārī. te dvija mohi priya jathā kharārī.\nmora śrāpa dvija byartha na jāihi. janma sahasa avasya yaha pāihi.",
        "translation": "'Those Brahmins who are forgiving and benevolent to others are as dear to Me as the slayer of the demon Khara (Rama). My curse, O Brahmin, shall not go in vain — he will surely undergo a thousand births.'"
    },
    "ut-109-c4": {
        "transliteration": "janamata marata dusaha dukha hoī. ahi svalpau nahiṃ byāpihi soī.\nkavaneuṃ janma miṭihi nahiṃ gyānā. sunahi sūdra mama bacana pravānā.",
        "translation": "'But the unbearable pain of birth and death — even the slightest of it shall not afflict him. In no birth shall his spiritual knowledge be lost. Listen, O Shudra, to My authoritative words:'"
    },
    "ut-109-c5": {
        "transliteration": "raghupati purīṃ janma taba bhayaū. puni taiṃ mama sevāṃ mana dayaū.\npurī prabhāva anugraha moreṃ. rāma bhagati upajihi ura toreṃ.",
        "translation": "'You shall be born in the city of the Lord of the Raghus (Ayodhya). Then you shall devote your mind to My worship. By the power of that holy city and by My grace, devotion to Rama shall arise in your heart.'"
    },
    "ut-109-c6": {
        "transliteration": "sunu mama bacana satya aba bhāī. haritoṣana brata dvija sevakāī.\naba jani karahi bipra apamānā. jānehu saṃta anaṃta samānā.",
        "translation": "'Listen to My true words now, brother: the vow that pleases Hari is service to the Brahmins. Henceforth never insult a Brahmin — know the saints to be equal to the Infinite Lord.'"
    },
    "ut-109-c7": {
        "transliteration": "iṃdra kulisa mama sūla bisālā. kāladaṃḍa hari cakra karālā.\njo inha kara mārā nahiṃ maraī. bipradroha pāvaka so jaraī.",
        "translation": "'Indra's thunderbolt, My great trident, the rod of Death, Hari's terrible discus — he who is not slain by these is still consumed by the fire of hostility toward Brahmins.'"
    },
    "ut-109-c8": {
        "transliteration": "asa bibeka rākhehu mana māhīṃ. tumha kahaṃ jaga durlabha kachu nāhīṃ.\naurau eka āsiṣā morī. apratihata gati hoihi torī.",
        "translation": "'Keep this wisdom in your heart — then nothing in the world shall be unattainable for you. And here is one more blessing of Mine: your movement shall be unobstructed everywhere.'"
    },
    "ut-109-d": {
        "transliteration": "suni siva bacana haraṣi gura evamastu iti bhāṣi.\nmohi prabodhi gayau gṛha saṃbhu carana ura rākhi.\nprerita kāla bidhi giri jāi bhayauṃ maiṃ byāla.\npuni prayāsa binu so tanu tajeuṃ gaeṃ kachu kāla.\njoi tanu dharauṃ tajauṃ puni anāyāsa harijāna.\njimi nūtana paṭa pahirai nara pariharai purāna.\nsivaṃ rākhī śruti nīti aru maiṃ nahiṃ pāvā klesa.\nehi bidhi dhareuṃ bibidha tanu gyāna na gayau khagesa.",
        "translation": "Hearing Shiva's words, my Guru joyfully said 'So be it!' He consoled me and went home, enshrining Shambhu's feet in his heart. Impelled by fate and destiny, I went to the mountains and became a serpent. Then after some time I shed that body effortlessly. Whatever body I assumed and then abandoned, O servant of Hari — it was as easy as a man putting on new clothes and discarding old ones. Shiva upheld the scriptural law, and yet I suffered no pain. Thus I took on various bodies, but my spiritual knowledge never departed, O king of birds."
    },

    # === DOHA GROUP 110 ===
    "ut-110-c1": {
        "transliteration": "trijaga deva nara joi tanu dharauṃ. tahaṃ tahaṃ rāma bhajana anusarūṃ.\neka sūla mohi bisara na kāū. gura kara komala sīla subhāū.",
        "translation": "In whatever body I took birth — among animals, gods or humans — everywhere I continued worshipping Rama. One pang never left me: the memory of my Guru's gentle and gracious nature."
    },
    "ut-110-c2": {
        "transliteration": "carama deha dvija kai maiṃ pāī. sura durlabha purāna śruti gāī.\nkhelauṃ tahūṃ bālakanha mīlā. karauṃ sakala raghunāyaka līlā.",
        "translation": "At last I obtained the body of a Brahmin — rare even for gods, as the Puranas and Vedas declare. Even in childhood I would play with other boys, enacting all the sports of the Lord of the Raghus."
    },
    "ut-110-c3": {
        "transliteration": "prauṛha bhaeṃ mohi pitā paṛhāvā. samajhauṃ sunauṃ gunauṃ nahiṃ bhāvā.\nmana te sakala bāsanā bhāgī. kevala rāma carana laya lāgī.",
        "translation": "When I grew older, my father had me educated. I would understand and listen and reflect, but it held no appeal. All worldly desires fled from my mind — my heart was absorbed solely in the feet of Rama."
    },
    "ut-110-c4": {
        "transliteration": "kahu khagesa asa kavana abhāgī. kharī seva suradhenuhi tyāgī.\nprema magana mohi kachu na sohāī. hāreu pitā paṛhāi paṛhāī.",
        "translation": "Tell me, O king of birds, who would be so unfortunate as to abandon the wish-fulfilling cow and tend a she-ass? Immersed in divine love, nothing else appealed to me, and my father grew weary of trying to educate me."
    },
    "ut-110-c5": {
        "transliteration": "bhae kālabasa jaba pitu mātā. maiṃ bana gayauṃ bhajana janatrātā.\njahaṃ jahaṃ bipina munīsvara pāvauṃ. āśrama jāi jāi siru nāvauṃ.",
        "translation": "When my father and mother passed away, I went to the forest to worship the Protector of devotees. Wherever in the forest I found great sages, I would go to their hermitages and bow my head."
    },
    "ut-110-c6": {
        "transliteration": "būjhata tinhahi rāma guna gāhā. kahahiṃ sunauṃ haraṣita khaganāhā.\nsunata phirauṃ hari guna anubādā. abyāhata gati saṃbhu prasādā.",
        "translation": "I would ask them about the glories of Rama's virtues. They would narrate them and I would listen with delight, O lord of birds. I wandered about hearing the praises of Hari's virtues, my movements unobstructed by Shambhu's grace."
    },
    "ut-110-c7": {
        "transliteration": "chūṭī tribidha īṣanā gāṛhī. eka lālasā ura ati bāṛhī.\nrāma carana bārija jaba dekhauṃ. taba nija janma saphala kari lekhauṃ.",
        "translation": "The three intense desires (for progeny, wealth and fame) had left me completely. One longing alone grew exceedingly in my heart: 'When shall I behold the lotus feet of Rama? Then alone shall I count my birth as fruitful.'"
    },
    "ut-110-c8": {
        "transliteration": "jehi pūṃchauṃ soi muni asa kahaī. īsvara sarba bhūtamaya ahaī.\nnirguṇa mata nahiṃ mohi sohāī. saguṇa brahma rati ura adhikāī.",
        "translation": "Whomever I asked, every sage said the same thing: 'God pervades all beings.' But the formless doctrine did not appeal to me — my heart held an abiding love for the personal form of Brahman."
    },
    "ut-110-d": {
        "transliteration": "gura ke bacana surati kari rāma carana manu lāga.\nraghupati jasa gāvata phirauṃ chana chana nava anurāga.\nmeru sikhara baṭa chāyāṃ muni lomasa āsīna.\ndekhi carana siru nāyauṃ bacana kaheuṃ ati dīna.\nsuni mama bacana binīta mṛdu muni kṛpāla khagarāja.\nmohi sādara pūṃchata bhae dvija āyahu kehi kāja.\ntaba maiṃ kahā kṛpānidhi tumha sarbagya sujāna.\nsaguṇa brahma avarādhana mohi kahahu bhagavāna.",
        "translation": "Remembering my Guru's words, my mind became fixed on Rama's feet. I wandered about singing the glories of the Lord of the Raghus, with love renewed every moment. On the peak of Mount Meru, in the shade of a banyan tree, sat the sage Lomasa. Seeing him, I bowed at his feet and spoke in most humble words. Hearing my gentle and humble speech, the merciful sage asked, O king of birds: 'O Brahmin, for what purpose have you come?' Then I said, 'O treasury of mercy, you are all-knowing and wise — please teach me the worship of the personal Brahman, O Lord.'"
    },

    # === DOHA GROUP 111 ===
    "ut-111-c1": {
        "transliteration": "taba muniṣa raghupati guna gāthā. kahe kachu sādara khaganāthā.\nbrahmagȳāna rata muni bigyāni. mohi parama adhikārī jānī.",
        "translation": "Then the great sage narrated some of the glorious deeds of the Lord of the Raghus, O lord of birds, with respect. But the sage, devoted to the knowledge of Brahman and learned in spiritual science, considered me a fit candidate for higher teaching."
    },
    "ut-111-c2": {
        "transliteration": "lāge karana brahma upadesā. aja adveta aguṇa hṛdayesā.\nakala anīha anāma arupā. anubhava gamya akhaṃḍa anūpā.",
        "translation": "He began to expound the doctrine of Brahman — unborn, non-dual, attributeless, the Lord of the heart; beyond the senses, desireless, nameless, formless, knowable only through experience, indivisible and incomparable."
    },
    "ut-111-c3": {
        "transliteration": "mana gotīta amala abināsī. nirbikāra niravadhi sukha rāsī.\nso taiṃ tāhi tohi nahiṃ bhedā. bāri bīci iva gāvahi bedā.",
        "translation": "'That Brahman is beyond mind and senses, pure, indestructible, changeless, and a limitless treasury of bliss. You are that — there is no difference between you and That, just as there is no difference between water and its wave, so declare the Vedas.'"
    },
    "ut-111-c4": {
        "transliteration": "bibidha bhāṃti mohi muni samujhāvā. nirguṇa mata mama hṛdayaṃ na āvā.\npuni maiṃ kaheuṃ nāi pada sīsā. saguṇa upāsana kahahu munīsā.",
        "translation": "The sage explained to me in various ways, but the formless doctrine would not enter my heart. Then I said, bowing my head at his feet, 'Please teach me the worship of the personal God, O great sage.'"
    },
    "ut-111-c5": {
        "transliteration": "rāma bhagati jala mama mana mīnā. kimi bilagāi munīsa prabīnā.\nsoi upadesa kahahu kari dāyā. nija nayananhi dekhauṃ raghurāyā.",
        "translation": "'My mind is like a fish in the water of Rama's devotion — how can it be separated, O wise sage? Give me that teaching, by your grace, by which I may behold the Lord of the Raghus with my own eyes.'"
    },
    "ut-111-c6": {
        "transliteration": "bhari locana biloki avadhesā. taba sunihauṃ nirguṇa upadesā.\nmuni puni kahi harikathā anūpā. khaṃḍi saguṇa mata aguṇa nirūpā.",
        "translation": "'When I have filled my eyes with the sight of the Lord of Ayodhya, then I shall listen to the formless teaching.' But the sage again narrated the incomparable story of Hari, refuted the personal doctrine and established the impersonal one."
    },
    "ut-111-c7": {
        "transliteration": "taba maiṃ nirguṇa mata kara dūrī. saguṇa nirūpauṃ kari haṭha bhūrī.\nuttara pratiuttara maiṃ kīnhā. muni tana bhae krodha ke cīnhā.",
        "translation": "Then I set aside the impersonal doctrine and stubbornly upheld the personal. I engaged in argument and counter-argument. Signs of anger appeared on the sage's person."
    },
    "ut-111-c8": {
        "transliteration": "sunu prabhu bahuta avagyā kieṃ. upaja krodha gyāninha ke hieṃ.\nati saṃgharaṣana jauṃ kara koī. anala pragaṭa caṃdana te hoī.",
        "translation": "Listen, Lord — even in the hearts of the wise, anger arises when they are greatly disrespected. If one rubs even sandalwood excessively, fire blazes forth from it."
    },
    "ut-111-d": {
        "transliteration": "bāraṃbāra sakopa muni karai nirupana gyāna.\nmaiṃ apaneṃ mana baiṭha taba karauṃ bibidha anumāna.\nkrodha ki dvetabuddhi binu dvaita ki binu agyāna.\nmāyābasa parichinna jaṛa jīva ki īsa samāna.",
        "translation": "Again and again the angry sage expounded the path of knowledge. But I, sitting within my own mind, drew various inferences: 'Can there be anger without a sense of duality? And can there be duality without ignorance? Can the finite, inert soul, bound by maya, be the same as God?'"
    },

    # === DOHA GROUP 112 ===
    "ut-112-c1": {
        "transliteration": "kabahuṃ ki dukha saba kara hita tākeṃ. tehi ki daridra parasa mani jākeṃ.\nparadrohī kī hohi nisaṃkā. kāmī puni ki rahahiṃ akalaṃkā.",
        "translation": "'Can one who seeks the welfare of all ever be sorrowful? Can one who possesses the philosopher's stone ever be poor? Can those who plot against others ever be free from fear? Can the lustful ever remain untarnished?'"
    },
    "ut-112-c2": {
        "transliteration": "baṃsa ki raha dvija anahita kīnheṃ. karma ki hohiṃ svarūpahi cīnheṃ.\nkāhū sumati ki khala saṃga jāmī. subha gati pāva ki paratriẏa gāmī.",
        "translation": "'Can a dynasty survive when Brahmins are wronged? Can karma bind one who has realized the Self? Can good sense arise from the company of the wicked? Can an adulterer attain a good end?'"
    },
    "ut-112-c3": {
        "transliteration": "bhava ki parahiṃ paramātmā biṃdaka. sukhī ki hohiṃ kabahuṃ harinindaka.\nrāju ki rahai nīti binu jāneṃ. agha ki rahahiṃ haricarita bakhāneṃ.",
        "translation": "'Can those who have realized the Supreme Self fall back into worldly existence? Can those who slander Hari ever be happy? Can a kingdom endure without knowledge of statecraft? Can sins persist when one narrates Hari's deeds?'"
    },
    "ut-112-c4": {
        "transliteration": "pāvana jasa ki punya binu hoī. binu agha ajasa ki pāvai koī.\nlābhu ki kichu hari bhagati samānā. jehi gāvahiṃ śruti saṃta purānā.",
        "translation": "'Can one gain a holy reputation without merit? Can anyone earn infamy without sin? Is there any gain equal to devotion to Hari, which the Vedas, saints and Puranas extol?'"
    },
    "ut-112-c5": {
        "transliteration": "hāni ki jaga ehi sama kichu bhāī. bhajia na rāmahi nara tanu pāī.\nagha ki pisunata sama kachu ānā. dharma ki dayā sarisa harijānā.",
        "translation": "'Is there any loss in the world as great as this, brother — to obtain a human body and not worship Rama? Is there any sin like slander? Is there any virtue like compassion, O servant of Hari?'"
    },
    "ut-112-c6": {
        "transliteration": "ehi bidhi amiti juguti mana gunauṃ. muni upadesa na sādara sunauṃ.\npuni puni saguṇa paccha maiṃ ropā. taba muni boleu bacana sakopā.",
        "translation": "In this manner I pondered countless arguments in my mind and did not respectfully heed the sage's teachings. Again and again I upheld the cause of the personal God. Then the sage spoke wrathful words:"
    },
    "ut-112-c7": {
        "transliteration": "mūṛha parama sikha deuṃ na mānasi. uttara pratiuttara bahu ānasi.\nsatya bacana bisvāsa na karahī. bāyasa iva sabahī te ḍarahī.",
        "translation": "'O supreme fool, you do not heed my teaching! You bring up endless arguments and counter-arguments. You do not trust my true words — like a crow, you are suspicious of everything.'"
    },
    "ut-112-c8": {
        "transliteration": "saṭha svapaccha taba hṛdayaṃ bisālā. sapadi hohi pacchī caṃḍālā.\nlīnha śrāpa maiṃ sīsa caṛhāī. nahiṃ kachu bhaya na dīnatā āī.",
        "translation": "'O fool, since love for your own side fills your heart so greatly, become at once a bird — the most despised of them!' I accepted the curse upon my head with neither fear nor dejection."
    },
    "ut-112-d": {
        "transliteration": "turata bhayauṃ maiṃ kāga taba puni muni pada siru nāi.\nsumiri rāma raghubaṃsa mani haraṣita caleuṃ uṛāi.\numā je rāma carana rata bigata kāma mada krodha.\nnija prabhumaya dekhahiṃ jagata kehi sana karahiṃ birodha.",
        "translation": "Instantly I became a crow. Then, bowing my head at the sage's feet and remembering Rama, the jewel of the Raghu dynasty, I flew away joyfully. (Shiva says:) O Uma, those who are devoted to Rama's feet, free from desire, pride and anger — they see the whole world as pervaded by their Lord; with whom would they quarrel?"
    },

    # === DOHA GROUP 113 ===
    "ut-113-c1": {
        "transliteration": "sunu khagesa nahiṃ kachu riṣi dūṣana. ura preraka raghubaṃsa bibhūṣana.\nkṛpāsiṃdhu muni mati kari bhorī. līnhi prema paricchā morī.",
        "translation": "Listen, O king of birds — there was no fault of the sage. The Ornament of the Raghu dynasty, who inspires all hearts, made the sage's mind confused and thus tested my love."
    },
    "ut-113-c2": {
        "transliteration": "mana baca krama mohi nija jana jānā. muni mati puni pherī bhagavānā.\nriṣi mama mahata sīlatā dekhī. rāma carana bisvāsa bisēṣī.",
        "translation": "The Lord recognized me as His own servant in thought, word and deed, and then restored the sage's understanding. The sage, seeing my great virtue and my extraordinary faith in Rama's feet,"
    },
    "ut-113-c3": {
        "transliteration": "ati bisamaya puni puni pachitāī. sādara muni mohi līnha bolāī.\nmama paritoṣa bibidha bidhi kīnhā. haraṣita rāmamaṃtra taba dīnhā.",
        "translation": "was greatly astonished and repented again and again. The sage respectfully called me back and appeased me in various ways. Then, delighted, he gave me the Rama-mantra."
    },
    "ut-113-c4": {
        "transliteration": "bālakarūpa rāma kara dhyānā. kaheu mohi muni kṛpānidhānā.\nsuṃdara sukhada mihi ati bhāvā. so prathamahiṃ maiṃ tumhahi sunāvā.",
        "translation": "The compassionate sage taught me to meditate on the child-form of Rama. It was beautiful and blissful and I loved it deeply — that is the very meditation I described to you at the beginning."
    },
    "ut-113-c5": {
        "transliteration": "muni mohi kachuka kāla tahaṃ rākhā. rāmacaritamānasa taba bhāṣā.\nsādara mohi yaha kathā sunāī. puni bole muni girā suhāī.",
        "translation": "The sage kept me there for some time and then narrated the Ramcharitmanas. He told me this story with great respect, and then the sage spoke these beautiful words:"
    },
    "ut-113-c6": {
        "transliteration": "rāmacarita sara gupta suhāvā. saṃbhu prasāda tāta maiṃ pāvā.\ntohi nija bhagata rāma kara jānī. tāte maiṃ saba kaheuṃ bakhānī.",
        "translation": "'This beautiful and hidden lake of Rama's deeds I received by the grace of Shambhu, my son. Knowing you to be a true devotee of Rama, I have narrated all of it to you.'"
    },
    "ut-113-c7": {
        "transliteration": "rāma bhagati jinha keṃ ura nāhīṃ. kabahuṃ na tāta kahia tinha pāhīṃ.\nmuni mohi bibidha bhāṃti samujhāvā. maiṃ saprema muni pada siru nāvā.",
        "translation": "'Never tell this to those who have no devotion to Rama in their hearts, my son.' The sage counseled me in various ways, and I lovingly bowed my head at his feet."
    },
    "ut-113-c8": {
        "transliteration": "nija kara kamala parasi mama sīsā. haraṣita āsiṣa dīnha munīsā.\nrāma bhagati abirala ura toreṃ. basihi sadā prasāda aba moreṃ.",
        "translation": "Touching my head with his lotus hand, the great sage joyfully gave me his blessing: 'Unceasing devotion to Rama shall forever dwell in your heart by my grace.'"
    },
    "ut-113-d": {
        "transliteration": "sadā rāma priya hohu tumha subha guṇa bhavana amāna.\nkāmarūpa iccdhāmarana gyāna birāga nidhāna.\njeṃhi āśrama tumha basaba puni sumirata śrībhagavaṃta.\nbyāpihi tahaṃ na abidyā jojana eka prajaṃta.",
        "translation": "'May you be ever dear to Rama, an abode of noble virtues, free from pride, able to assume any form at will, dying only when you choose, a treasury of wisdom and detachment. And in whatever hermitage you dwell, remembering the blessed Lord, ignorance shall not prevail within a radius of one yojana around it.'"
    },

    # === DOHA GROUP 114 ===
    "ut-114-c1": {
        "transliteration": "kāla karma guṇa doṣa subhāū. kachu dukha tumhahi na byāpihi kāū.\nrāma rahasya lalita bidhi nānā. gupta pragaṭa itihāsa purānā.",
        "translation": "'Time, karma, virtues, faults and natural temperament — no sorrow shall ever afflict you. The beautiful mysteries of Rama in various forms — both hidden and revealed in the histories and Puranas —'"
    },
    "ut-114-c2": {
        "transliteration": "binu śrama tumha jānaba saba soū. nita nava neha rāma pada hoū.\njo icchā karihuhu mana māhīṃ. hari prasāda kachu durlabha nāhīṃ.",
        "translation": "'— you shall know all of these effortlessly. May ever-new love for Rama's feet arise in you. Whatever desire you cherish in your heart — by Hari's grace, nothing shall be unattainable.'"
    },
    "ut-114-c3": {
        "transliteration": "suni muni āsiṣa sunu matidhīrā. brahmagirā bhai gagana gaṃbhīrā.\nevamastu tava baca muni gyānī. yaha mama bhagata karma mana bānī.",
        "translation": "Hearing the sage's blessings, listen O steadfast one — a deep divine voice resounded from the sky: 'So be it, O wise sage, as you have spoken! This one is My devotee in deed, mind and speech.'"
    },
    "ut-114-c4": {
        "transliteration": "suni nabhagirā haraṣa mohi bhayaū. prema magana saba saṃsaya gayaū.\nkari binatī muni āyasu pāī. pada saroja puni puni siru nāī.",
        "translation": "Hearing the divine voice, I was filled with joy. Immersed in love, all my doubts vanished. Making my obeisance and receiving the sage's permission, I bowed again and again at his lotus feet."
    },
    "ut-114-c5": {
        "transliteration": "haraṣa sahita ehiṃ āśrama āyauṃ. prabhu prasāda durlabha bara pāyauṃ.\nihāṃ basata mohi sunu khaga īsā. bīte kalapa sāta aru bīsā.",
        "translation": "With joy I came to this hermitage and received rare boons by the Lord's grace. Listen, O lord of birds — I have been living here for twenty-seven kalpas."
    },
    "ut-114-c6": {
        "transliteration": "karauṃ sadā raghupati guna gānā. sādara sunahiṃ bihaṃga sujānā.\njaba jaba avadhapurīṃ raghubīrā. dharahiṃ bhagata hita manuja sarīrā.",
        "translation": "I constantly sing the virtues of the Lord of the Raghus, and wise birds listen with reverence. Whenever the Hero of the Raghus takes on a human form in the city of Ayodhya for the sake of His devotees,"
    },
    "ut-114-c7": {
        "transliteration": "taba taba jāi rāma pura rahaūṃ. sisulīlā biloki sukha lahaūṃ.\npuni ura rākhi rāma sisurūpā. nija āśrama āvauṃ khagabhūpā.",
        "translation": "then I go and dwell in Rama's city, and find joy beholding His childhood sports. Then, treasuring Rama's child-form in my heart, I return to my own hermitage, O king of birds."
    },
    "ut-114-c8": {
        "transliteration": "kathā sakala maiṃ tumhahi sunāī. kāga deha jehiṃ kārana pāī.\nkahiuṃ tāta saba prasna tumhārī. rāma bhagati mahimā ati bhārī.",
        "translation": "I have told you the entire story of why I obtained the body of a crow. I have answered all your questions, my son — the glory of devotion to Rama is exceedingly great."
    },
    "ut-114-d": {
        "transliteration": "tāte yaha tana mohi priya bhayau rāma pada neha.\nnija prabhu darasana pāyauṃ gae sakala saṃdeha.\nbhagati paccha haṭha kari raheuṃ dīnhi mahāriṣi sāpa.\nmuni durlabha bara pāyauṃ dekhahu bhajana pratāpa.",
        "translation": "Therefore this body is dear to me, for through it I gained love for Rama's feet. I obtained the vision of my Lord and all doubts departed. I stubbornly upheld the cause of devotion and received the great sage's curse — yet I obtained boons rare even for sages. Behold the power of worship!"
    },

    # === DOHA GROUP 115 ===
    "ut-115-c1": {
        "transliteration": "je asī bhagati jāni pariharahīṃ. kevala gyāna hetu śrama karahīṃ.\nte jaṛa kāmadhenu gṛhaṃ tyāgī. khojata āku phirahiṃ paya lāgī.",
        "translation": "Those who knowingly abandon such devotion and toil solely for the sake of knowledge — those fools are like one who leaves a wish-fulfilling cow at home and wanders about seeking milkweed for its milk."
    },
    "ut-115-c2": {
        "transliteration": "sunu khagesa hari bhagati bihāī. je sukha cāhahiṃ āna upāī.\nte saṭha mahāsiṃdhu binu taranī. pairi pāra cāhahiṃ jaṛa karanī.",
        "translation": "Listen, O king of birds — those who abandon devotion to Hari and seek happiness by other means, those fools wish to swim across the great ocean without a boat — a foolish endeavor indeed."
    },
    "ut-115-c3": {
        "transliteration": "suni bhasuṃḍi ke bacana bhavānī. boleu garuṛa haraṣi mṛdu bānī.\ntava prasāda prabhu mama ura māhīṃ. saṃsaya soka moha bhrama nāhīṃ.",
        "translation": "(Shiva says:) Hearing Bhushundi's words, O Bhavani, Garuda spoke with delight in gentle tones: 'By your grace, O Lord, within my heart there remains no doubt, no sorrow, no delusion, no confusion.'"
    },
    "ut-115-c4": {
        "transliteration": "suneuṃ punīta rāma guna grāmā. tumharī kṛpāṃ laheuṃ biśrāmā.\neka bāta prabhu pūṃchauṃ tohī. kahahu bujhāi kṛpānidhi mohī.",
        "translation": "'I have heard the sacred collection of Rama's virtues. By your grace I have found peace. I ask you one more thing, O Lord — please explain it to me, O treasury of mercy.'"
    },
    "ut-115-c5": {
        "transliteration": "kahahiṃ saṃta muni beda purānā. nahiṃ kachu durlabha gyāna samānā.\nsoi muni tumha sana kaheu gosāīṃ. nahiṃ ādarahu bhagati kī nāīṃ.",
        "translation": "'Saints, sages, Vedas and Puranas all say that nothing is as rare as spiritual knowledge. That very knowledge the sage offered you, O master — yet you did not honor it the way you honored devotion.'"
    },
    "ut-115-c6": {
        "transliteration": "gyānahi bhagatihi aṃtara ketā. sakala kahahu prabhu kṛpā niketā.\nsuni uragāri bacana sukha mānā. sādara boleu kāga sujānā.",
        "translation": "'What is the difference between knowledge and devotion? Please tell me everything, O abode of mercy.' Hearing the enemy of serpents (Garuda) speak, the wise crow (Bhushundi) was pleased and spoke respectfully:"
    },
    "ut-115-c7": {
        "transliteration": "bhagatihi gyānahi nahiṃ kachu bhedā. ubhaya harahiṃ bhava saṃbhava khedā.\nnātha munīsa kahahiṃ kachu aṃtara. sāvadhāna sou sunu bihaṃgabara.",
        "translation": "'Between devotion and knowledge there is no difference at all — both remove the suffering born of worldly existence. However, the great sages do speak of some distinction — listen to that attentively, O best of birds.'"
    },
    "ut-115-c8": {
        "transliteration": "gyāna birāga joga bigyānā. e saba puruṣa sunahu harijānā.\npuruṣa pratāpa prabala saba bhāṃtī. abalā abala sahaja jaṛa jātī.",
        "translation": "'Knowledge, detachment, yoga and spiritual science — these are all masculine, listen O servant of Hari. The power of the masculine is mighty in every way, while the feminine is naturally weak, feeble and inert.'"
    },
    "ut-115-d": {
        "transliteration": "puruṣa tyāgi saka nārihi jo birakta mati dhīra.\nna tu kāmī biṣayābasa bimukha jo pada raghubīra.\nsou muni gyānanidhāna mṛganayanī bidhu mukha nirakhi.\nbibasa hoi harijāna nāri biṣṇu māyā pragaṭa.",
        "translation": "'A man can renounce a woman only if he is dispassionate and steadfast of mind — but not a lustful person, enslaved by sense-objects, who has turned away from the feet of Raghubira. Even a sage who is a storehouse of knowledge, upon beholding the moon-like face of a doe-eyed woman, becomes helpless, O servant of Hari — for woman is the manifest form of Vishnu's maya.'"
    },

    # === DOHA GROUP 116 ===
    "ut-116-c1": {
        "transliteration": "ihāṃ na pacchapāta kachu rākhauṃ. beda purāna saṃta mata bhāṣauṃ.\nmoha na nāri nāri keṃ rūpā. pannagāri yaha rīti anūpā.",
        "translation": "'I hold no bias here — I speak the view of the Vedas, Puranas and saints. It is not woman herself that deludes, nor her form, O enemy of serpents — this is a unique principle.'"
    },
    "ut-116-c2": {
        "transliteration": "māyā bhagati sunahu tumha doū. nāri barga jānai saba koū.\npuni raghubīrahi bhagati piārī. māyā khalu nartakī bicārī.",
        "translation": "'Maya and Bhakti — listen — both are of the feminine class, as everyone knows. But devotion is dear to the Hero of the Raghus, while poor Maya is merely a dancing-girl.'"
    },
    "ut-116-c3": {
        "transliteration": "bhagatihi sānukūla raghurāyā. tāte tehi ḍarapati ati māyā.\nrāma bhagati nirupama nirupādhī. basai jāsu ura sadā abādhī.",
        "translation": "'The Lord of the Raghus is favorably disposed toward devotion, and therefore Maya is greatly afraid of it. In whose heart the incomparable and unconditional devotion to Rama abides perpetually and unobstructed —'"
    },
    "ut-116-c4": {
        "transliteration": "tehi biloki māyā sakucāī. kari na sakai kachu nija prabhutāī.\nasa bicāri je muni bigyānī. jācahīṃ bhagati sakala sukha khānī.",
        "translation": "'— beholding that person, Maya shrinks back and cannot exercise her power. Reflecting thus, wise and enlightened sages seek devotion, which is the mine of all happiness.'"
    },
    "ut-116-d": {
        "transliteration": "yaha rahasya raghunātha kara begi na jānai koi.\njo jānai raghupati kṛpāṃ sapanehūṃ moha na hoi.\naurau gyāna bhagati kara bheda sunahu suprabīna.\njo suni hoi rāma pada prīti sadā abichīna.",
        "translation": "'This secret of the Lord of the Raghus is not easily known by anyone. But one who knows it, by Raghupati's grace, shall never experience delusion even in a dream. Now hear another difference between knowledge and devotion, O most wise one — hearing which, unbroken love for Rama's feet shall always arise.'"
    },

    # === DOHA GROUP 117 ===
    "ut-117-c1": {
        "transliteration": "sunahu tāta yaha akatha kahānī. samujhata banai na jāi bakhānī.\nīsvara aṃsa jīva abināsī. cetana amala sahaja sukha rāsī.",
        "translation": "'Listen, my son, to this indescribable tale — it can be understood but cannot be fully told. The individual soul is an eternal portion of God — conscious, pure, and by nature a treasure of bliss.'"
    },
    "ut-117-c2": {
        "transliteration": "so māyābasa bhayau gosāīṃ. baṃdhyo kīra marakaṭa kī nāī.\njaṛa cetanahi graṃthi pari gaī. jadapi mṛṣā chūṭata kaṭhinaī.",
        "translation": "'That soul came under the sway of Maya, O master — bound like a parrot or a monkey. A knot was tied between the inert (matter) and the conscious (soul). Although it is false, it is extremely difficult to untie.'"
    },
    "ut-117-c3": {
        "transliteration": "taba te jīva bhayau saṃsārī. chūṭa na graṃthi na hoi sukhārī.\nśruti purāna bahu kaheu upāī. chūṭa na adhika adhika arujhāī.",
        "translation": "'From that time the soul became a worldly being. The knot would not break and there was no happiness. The Vedas and Puranas prescribed many remedies, but the knot only became more and more entangled.'"
    },
    "ut-117-c4": {
        "transliteration": "jīva hṛdayaṃ tama moha bisēṣī. graṃthi chūṭa kimi parai na dekhī.\nasa saṃjoga īsa jaba karaī. tabahuṃ kadācit so niruaraī.",
        "translation": "'The soul's heart is enveloped in the deep darkness of delusion — the knot cannot even be seen, let alone untied. Only when God creates the right combination of circumstances does it sometimes come undone.'"
    },
    "ut-117-c5": {
        "transliteration": "sāttvika śraddhā dhenu suhāī. jauṃ hari kṛpāṃ hṛdayaṃ basa āī.\njapa tapa brata jama niyama apārā. je śruti kaha subha dharma acārā.",
        "translation": "'When, by Hari's grace, the beautiful cow of sattvic faith takes up residence in one's heart — then the various practices of chanting, austerity, vows, self-restraints and observances, all the righteous conduct that the Vedas prescribe —'"
    },
    "ut-117-c6": {
        "transliteration": "tei tṛna harita carai jaba gāī. bhāva baccha sisu pāi peṃhāī.\nnoi nibṛtti pātra bisvāsā. nirmala mana ahīra nija dāsā.",
        "translation": "'— these serve as green grass for that cow to graze upon. When the calf of devotion is placed beside her to stimulate the flow of milk, the milking-pail is renunciation, faith is the strainer, and the pure-minded cowherd is one's own self as God's servant.'"
    },
    "ut-117-c7": {
        "transliteration": "parama dharmamaya paya duhi bhāī. avaṭai anala akāma banāī.\ntoṣa maruta taba chamāṃ juṛāvai. dhṛti sama jāvanu dei jamāvai.",
        "translation": "'One milks the supreme righteous milk, brother, and boils it over the fire of desirelessness. Then the breeze of contentment cools it, and patience acts as the rennet to curdle it.'"
    },
    "ut-117-c8": {
        "transliteration": "muditāṃ mathai bicāra mathānī. dama adhāra raju satya subānī.\ntaba mathi kāṛhi lei navanītā. bimala birāga subhaga supunītā.",
        "translation": "'Then with the churning-rod of reflection, in the joy of meditation, using the rope of self-control supported by the cord of truth and noble speech — one churns and extracts the butter of pure, beautiful and holy detachment.'"
    },
    "ut-117-d": {
        "transliteration": "joga agini kari pragaṭa taba karma subhāsubha lāi.\nbuddhi sirāvaiṃ gyāna ghṛta mamatā mala jari jāi.\ntaba bigyānarūpini buddhi bisada ghṛta pāi.\ncitta diā bhari dharai dṛṛha samatā diaṭi banāi.\ntīni avasthā tīni guṇa tehi kapāsa teṃ kāṛhi.\ntūla turīya saṃvāri puni bātī karai sugāṛhi.\nehi bidhi lesai dīpa teja rāsi bigyānamaya.\njātahiṃ jāsu samīpa jarahiṃ madādika salabha saba.",
        "translation": "'Then, kindling the fire of yoga and feeding it with good and bad karma, one renders the ghee of knowledge through the intellect, and the impurity of attachment is burned away. Then the intellect, in the form of spiritual science, having obtained the clarified ghee, fills the lamp of the mind firmly, making the base of equanimity. From the cotton of the three states (waking, dreaming, deep sleep) and the three gunas, one extracts the cotton-wool of the fourth state (turiya) and fashions it into a well-made wick. In this way, one lights the lamp — a mass of radiance, full of spiritual wisdom. The moment moths like pride and other vices approach it, they are consumed.'"
    },

    # === DOHA GROUP 118 ===
    "ut-118-c1": {
        "transliteration": "sohamasmi iti bṛtti akhaṃḍā. dīpa sikhā soi parama pracaṃḍā.\nātama anubhava sukha suprakāsā. taba bhava mūla bheda bhrama nāsā.",
        "translation": "'The unbroken awareness of \"I am That\" (Soham) — that is the supremely blazing flame of the lamp. In the radiance of self-realization and its bliss, the root of worldly existence — the delusion of difference — is destroyed.'"
    },
    "ut-118-c2": {
        "transliteration": "prabala abidyā kara parivārā. moha ādi tama miṭai apārā.\ntaba soi buddhi pāi uṃjiārā. ura gṛhaṃ baiṭhi graṃthi niruvārā.",
        "translation": "'The infinite darkness of delusion and the powerful family of ignorance are all dispelled. Then that intellect, having gained this light, sits within the house of the heart and begins to untie the knot.'"
    },
    "ut-118-c3": {
        "transliteration": "chorana graṃthi pāva jauṃ soī. taba yaha jīva kṛtārtha hoī.\nchorata graṃthi jāni khagarāyā. bighna aneka karai taba māyā.",
        "translation": "'If the intellect succeeds in loosening the knot, then the soul becomes truly fulfilled. But knowing the knot is being loosened, O king of birds, Maya creates many obstacles.'"
    },
    "ut-118-c4": {
        "transliteration": "riddhi siddhi prerai bahu bhāī. buddhahi lobha dikhāvahiṃ āī.\nkala bala chala kari jāhiṃ samīpā. aṃcala bāta bujhāvahiṃ dīpā.",
        "translation": "'She sends forth many mystic powers and accomplishments, brother — they come and display temptations before the intellect. Through art, force and deception they approach and try to extinguish the lamp with the breeze of their garment-hems.'"
    },
    "ut-118-c5": {
        "transliteration": "hoi buddhi jauṃ parama sayānī. tinha tana citava na anahita jānī.\njauṃ tehi bighna buddhi nahiṃ bādhī. tau bahori sura karahiṃ upādhī.",
        "translation": "'If the intellect is supremely wise, it does not even glance at them, knowing them to be harmful. If these obstacles fail to hinder the intellect, then the gods create further troubles.'"
    },
    "ut-118-c6": {
        "transliteration": "iṃdrīṃ dvāra jharokhā nānā. tahaṃ tahaṃ sura baiṭhe kari thānā.\nāvata dekhahiṃ biṣaya bayārī. te haṭhi dehī kapāṭa ughārī.",
        "translation": "'The senses are the many windows and doors of the body — at each one the gods have stationed themselves. When they see the breeze of sense-objects approaching, they forcibly throw open the shutters.'"
    },
    "ut-118-c7": {
        "transliteration": "jaba so prabhaṃjana ura gṛhaṃ jāī. tabahiṃ dīpa bigyāna bujhāī.\ngraṃthi na chūṭi miṭā so prakāsā. buddhi bikala bhaī biṣaya batāsā.",
        "translation": "'When that gust of wind enters the house of the heart, the lamp of spiritual knowledge is immediately extinguished. The knot remains unbroken, the light fades away, and the intellect becomes bewildered by the wind of sense-objects.'"
    },
    "ut-118-c8": {
        "transliteration": "iṃdrinha suranha na gyāna sohāī. biṣaya bhoga para prīti sadāī.\nbiṣaya samīra buddhi kṛta bhorī. tehi bidhi dīpa ko bāra bahorī.",
        "translation": "'The senses and their presiding gods do not welcome knowledge — their love is always fixed on sensory enjoyment. When the wind of sense-objects has thus confounded the intellect, who can relight that lamp?'"
    },
    "ut-118-d": {
        "transliteration": "taba phiri jīva bibidha bidhi pāvai saṃsṛti klesa.\nhari māyā ati dustara tari na jāi bihagesa.\nkahata kaṭhina samujhata kaṭhina sādhana kaṭhina bibeka.\nhoi ghunācchara nyāya jauṃ puni pratyūha aneka.",
        "translation": "'Then the soul once again suffers the afflictions of worldly existence in various ways. Hari's Maya is exceedingly difficult to cross — it cannot be crossed, O king of birds. The path of knowledge is difficult to describe, difficult to understand, and difficult to practice. Even if by the rarest of chances it succeeds (like worms accidentally forming letters), there are still countless obstacles.'"
    },

    # === DOHA GROUP 119 ===
    "ut-119-c1": {
        "transliteration": "gyāna paṃtha kṛpāna kai dhārā. parata khagesa hoi nahiṃ bārā.\njo nirbighna paṃtha nirbahaī. so kaivalya parama pada lahaī.",
        "translation": "'The path of knowledge is like the edge of a sword — one can slip at any moment, O king of birds. But one who traverses this path without obstacles attains the supreme state of liberation.'"
    },
    "ut-119-c2": {
        "transliteration": "ati durlabha kaivalya parama pada. saṃta purāna nigama āgama bada.\nrāma bhajata soi mukuti gosāī. anaicchita āvai bariāī.",
        "translation": "'That supreme state of liberation is exceedingly rare — so say the saints, Puranas, Vedas and Agamas. But by worshipping Rama, that very liberation, O master, comes uninvited and forces itself upon the devotee.'"
    },
    "ut-119-c3": {
        "transliteration": "jimi thala binu jala rahi na sakāī. koṭi bhāṃti kou karai upāī.\ntathā moccha sukha sunu khagarāī. rahi na sakai hari bhagati bihāī.",
        "translation": "'Just as water cannot exist without a surface beneath it, no matter what millions of efforts one makes — so too, listen O king of birds, the bliss of liberation cannot exist apart from devotion to Hari.'"
    },
    "ut-119-c4": {
        "transliteration": "asa bicāri hari bhagata sayāne. mukti nirādara bhagati lubhāne.\nbhagati karata binu jatana prayāsā. saṃsṛti mūla abidyā nāsā.",
        "translation": "'Reflecting thus, wise devotees of Hari disregard liberation and are captivated by devotion. Through devotion alone, without any toilsome effort, the root of worldly existence — ignorance — is destroyed.'"
    },
    "ut-119-c5": {
        "transliteration": "bhojana karia tṛpiti hita lāgī. jimi so asana pacavai jaṭharāgī.\nasī haribhagati sugama sukhadāī. ko asa mūṛha na jāhi sohāī.",
        "translation": "'One eats food for the sake of satisfaction, and the digestive fire automatically digests it. Such is devotion to Hari — easy and bliss-giving. Who is so foolish that it does not appeal to them?'"
    },
    "ut-119-d": {
        "transliteration": "sevaka sebya bhāva binu bhava na taria uragāri.\nbhajahu rāma pada paṃkaja asa siddhāṃta bicāri.\njo cetana kahaṃ jaṛa karai jaṛahi karai caitanya.\nasa samartha raghunāyakahi bhajahiṃ jīva te dhanya.",
        "translation": "'Without the relationship of servant and master, the ocean of worldly existence cannot be crossed, O enemy of serpents. Worship the lotus feet of Rama, having reflected on this settled truth. He who can make the conscious inert and the inert conscious — those souls who worship such an omnipotent Lord of the Raghus are truly blessed.'"
    },

    # === DOHA GROUP 120 ===
    "ut-120-c1": {
        "transliteration": "kaheuṃ gyāna siddhāṃta bujhāī. sunahu bhagati mani kai prabhutāī.\nrāma bhagati ciṃtāmani suṃdara. basai garuṛa jāke ura aṃtara.",
        "translation": "'I have explained to you the essence of knowledge. Now hear the glory of the jewel of devotion. Devotion to Rama is a beautiful wish-fulfilling gem, O Garuda, dwelling within the heart.'"
    },
    "ut-120-c2": {
        "transliteration": "parama prakāsa rūpa dina rātī. nahiṃ kachu cahia diā ghṛta bātī.\nmoha daridra nikaṭa nahiṃ āvā. lobha bāta nahiṃ tāhi bujhāvā.",
        "translation": "'It is supremely radiant, day and night — it needs no lamp, no ghee, no wick. The poverty of delusion cannot come near it, and the wind of greed cannot extinguish it.'"
    },
    "ut-120-c3": {
        "transliteration": "prabala abidyā tama miṭi jāī. hārahiṃ sakala salabha samudāī.\nkhala kāmādi nikaṭa nahiṃ jāhīṃ. basai bhagati jāke ura māhīṃ.",
        "translation": "'The mighty darkness of ignorance is dispelled, and all the moths of vice are defeated. The wicked ones — lust and the rest — dare not come near one in whose heart devotion resides.'"
    },
    "ut-120-c4": {
        "transliteration": "garala sudhāsama ari hita hoī. tehi mani binu sukha pāva na koī.\nbyāpahiṃ mānasa roga na bhārī. jinha ke basa saba jīva dukhārī.",
        "translation": "'Poison becomes like nectar, and enemies become friends. Without this gem, no one finds happiness. The grievous diseases of the mind — which keep all souls in misery — cannot afflict one who possesses it.'"
    },
    "ut-120-c5": {
        "transliteration": "rāma bhagati mani ura basa jākeṃ. dukha lavalesa na sapanehūṃ tākeṃ.\ncatura siromaṇi tei jaga māhīṃ. je mani lāgi sujatana karāhīṃ.",
        "translation": "'One in whose heart the gem of Rama-devotion dwells — not even a trace of sorrow touches them, even in dreams. The wisest of the wise in this world are those who make diligent effort to obtain this gem.'"
    },
    "ut-120-c6": {
        "transliteration": "so mani jadapi pragaṭa jaga ahaī. rāma kṛpā binu nahiṃ kou lahaī.\nsugama upāya pāibe kere. nara hatabhāgya dehiṃ bhaṭamere.",
        "translation": "'Although this gem is openly present in the world, without Rama's grace no one obtains it. The means of obtaining it are easy, yet ill-fated people turn away from them.'"
    },
    "ut-120-c7": {
        "transliteration": "pāvana parbata beda purānā. rāma kathā rucirākara nānā.\nmarmī sajjana sumati kudārī. gyāna birāga nayana uragārī.",
        "translation": "'The holy mountains are the Vedas and Puranas, and the beautiful mines within them are the many narratives of Rama. Discerning saints are the skillful miners, knowledge and detachment are their eyes, O enemy of serpents.'"
    },
    "ut-120-c8": {
        "transliteration": "bhāva sahita khojai jo prānī. pāva bhagati mani saba sukha khānī.\nmoreṃ mana prabhu asa bisvāsā. rāma te adhika rāma kara dāsā.",
        "translation": "'The person who searches with sincere feeling obtains the gem of devotion, the mine of all happiness. In my heart, O Lord, there is this firm conviction: Rama's servant is even greater than Rama Himself.'"
    },
    "ut-120-c9": {
        "transliteration": "rāma siṃdhu ghana sajjana dhīrā. caṃdana taru hari saṃta samīrā.\nsaba kara phala hari bhagati suhāī. so binu saṃta na kāhūṃ pāī.",
        "translation": "'Rama is the ocean, the steadfast saints are the clouds, the sandalwood tree is Hari, and the saints are the breeze. The fruit of all endeavors is the beautiful devotion to Hari, and that is not obtained by anyone without the company of saints.'"
    },
    "ut-120-c10": {
        "transliteration": "asa bicāri joi kara satasaṃgā. rāma bhagati tehi sulabha bihaṃgā.",
        "translation": "'Reflecting thus, whoever keeps the company of saints — devotion to Rama becomes easy for them, O bird.'"
    },
    "ut-120-d": {
        "transliteration": "brahma payonidhi maṃdara gyāna saṃta sura āhiṃ.\nkathā sudhā mathi kāṛhahiṃ bhagati madhuratā jāhiṃ.\nbirati carma asi gyāna mada lobha moha ripu māri.\njaya pāia so hari bhagati dekhu khagesa bicāri.",
        "translation": "'Brahman is the milk-ocean, knowledge is Mount Mandara, and the saints are the gods. By churning, they extract the nectar of the sacred narrative, whose sweetness is devotion. With the shield of dispassion and the sword of knowledge, slaying the enemies of pride, greed and delusion — the victory that is won is devotion to Hari. See this clearly, O king of birds!'"
    },

    # === DOHA GROUP 121 ===
    "ut-121-c1": {
        "transliteration": "puni saprema boleu khagarāū. jauṃ kṛpāla mohi ūpara bhāū.\nnātha mohi nija sevaka jānī. sapta prasna kahahu bakhānī.",
        "translation": "Then the king of birds (Garuda) spoke again with love: 'If you are gracious and bear affection for me, O Lord — knowing me as your servant, please answer seven questions in detail.'"
    },
    "ut-121-c2": {
        "transliteration": "prathamahiṃ kahahu nātha matidhīrā. saba te durlabha kavana sarīrā.\nbaṛa dukha kavana kavana sukha bhārī. sou saṃchepahiṃ kahahu bicārī.",
        "translation": "'First tell me, O steadfast Lord, which body is the rarest of all? What is the greatest sorrow and what the greatest happiness? Please tell me these briefly, after reflection.'"
    },
    "ut-121-c3": {
        "transliteration": "saṃta asaṃta marama tumha jānahu. tinha kara sahaja subhāva bakhānahu.\nkavana punya śruti bidita bisālā. kahahu kavana agha parama karālā.",
        "translation": "'You know the innermost nature of saints and sinners — describe their natural dispositions. What is the greatest merit, well known in the scriptures? And what is the most terrible sin?'"
    },
    "ut-121-c4": {
        "transliteration": "mānasa roga kahahu samujhāī. tumha sarbagya kṛpā adhikāī.\ntāta sunahu sādara ati prītī. maiṃ saṃchepa kahauṃ yaha nītī.",
        "translation": "'Explain to me the diseases of the mind — you are all-knowing and exceedingly merciful.' 'Listen, my son, with great respect and love — I shall tell you these truths in brief.'"
    },
    "ut-121-c5": {
        "transliteration": "nara tana sama nahiṃ kavaniu dehī. jīva carācara jācata tehī.\nnarga svarga apabarga nisēnī. gyāna birāga bhagati subha denī.",
        "translation": "'No body is comparable to the human body — all creatures, moving and still, yearn for it. It is the ladder to hell, heaven or liberation — bestowing knowledge, detachment and devotion.'"
    },
    "ut-121-c6": {
        "transliteration": "so tanu dhari hari bhajahiṃ na je nara. hohiṃ biṣaya rata maṃda maṃda tara.\nkāṃca kirici badaleṃ te lehī. kara te ḍāri parasa mani dehīṃ.",
        "translation": "'Those who, having obtained this body, do not worship Hari but remain engrossed in sensory pleasures — the dullest of the dull — are like those who trade away the philosopher's stone for bits of broken glass.'"
    },
    "ut-121-c7": {
        "transliteration": "nahiṃ daridra sama dukha jaga māhīṃ. saṃta milana sama sukha jaga nāhīṃ.\npara upakāra bacana mana kāyā. saṃta sahaja subhāu khagarāyā.",
        "translation": "'There is no suffering in the world like poverty, and no happiness in the world like meeting saints. Benevolence toward others in word, thought and deed — this is the natural disposition of saints, O king of birds.'"
    },
    "ut-121-c8": {
        "transliteration": "saṃta sahahiṃ dukha parahita lāgī. paradukha hetu asaṃta abhāgī.\nbhūrja tarū sama saṃta kṛpālā. parahita niti saha bipati bisālā.",
        "translation": "'Saints endure suffering for the good of others; the wretched wicked cause suffering to others. Merciful saints are like the birch tree — always serving others and bearing great calamities for their sake.'"
    },
    "ut-121-c9": {
        "transliteration": "sana iva khala para baṃdhana karaī. khāla kaṛhāi bipati sahi maraī.\nkhala binu svāratha para apakārī. ahi mūṣaka iva sunu uragārī.",
        "translation": "'Like hemp, the wicked bind others — their skin is stripped off and they die enduring hardship. The wicked harm others without any self-interest — like serpents and mice, listen, O enemy of serpents.'"
    },
    "ut-121-c10": {
        "transliteration": "para saṃpadā bināsi nasāhīṃ. jimi sasi hati hima upala bilāhīṃ.\nduṣṭa udaya jaga ārati hetū. jathā prasiddha adhama graha ketū.",
        "translation": "'They destroy the wealth of others and perish themselves — like hailstones that kill crops and then melt away. The rise of the wicked causes suffering in the world, just as the infamous malefic planet Ketu is well known.'"
    },
    "ut-121-c11": {
        "transliteration": "saṃta udaya saṃtata sukhakārī. bisva sukhada jimi iṃdu tamārī.\nparama dharma śruti bidita ahiṃsā. para niṃdā sama agha na garīsā.",
        "translation": "'The rise of saints always brings happiness, delighting the world like the moon and the sun. The supreme dharma, as declared by the Vedas, is non-violence. There is no sin as grave as slandering others.'"
    },
    "ut-121-c12": {
        "transliteration": "hara gura niṃdaka dādura hoī. janma sahastra pāva tana soī.\ndvija niṃdaka bahu naraka bhoga kari. jaga janamai bāyasa sarīra dhari.",
        "translation": "'One who slanders Shiva or the Guru becomes a frog and suffers in that body for a thousand births. One who slanders Brahmins, after suffering in many hells, is reborn in the world in the body of a crow.'"
    },
    "ut-121-c13": {
        "transliteration": "sura śruti niṃdaka je abhimānī. raurava naraka parahiṃ te prānī.\nhohi ulūka saṃta niṃdā rata. moha nisā priya gyāna bhānu gata.",
        "translation": "'Those proud beings who slander the gods and the Vedas fall into the Raurava hell. Those who delight in slandering saints become owls — they love the night of delusion and shun the sun of knowledge.'"
    },
    "ut-121-c14": {
        "transliteration": "saba ke niṃdā je jaṛa karahīṃ. te camagādura hoi avatarihīṃ.\nsunahu tāta aba mānasa rogā. jinha te dukha pāvahiṃ saba logā.",
        "translation": "'Those fools who slander everyone are reborn as bats. Now listen, my son, to the diseases of the mind, which cause suffering to all people.'"
    },
    "ut-121-c15": {
        "transliteration": "moha sakala byādhinh kara mūlā. tinha te puni upajahiṃ bahu sūlā.\nkāma bāta kapha lobha apārā. krodha pitta nita chātī jārā.",
        "translation": "'Delusion is the root of all diseases — from it arise many pains. Lust is the vata (wind) humor, greed is the boundless kapha (phlegm), and anger is the pitta (bile) that constantly burns the chest.'"
    },
    "ut-121-c16": {
        "transliteration": "prīti karahiṃ jauṃ tīniu bhāī. upajai sanyapāta dukhādāī.\nbiṣaya manoratha durgama nānā. te saba sūla nāma ko jānā.",
        "translation": "'When all three combine in alliance, the painful sannipata fever (a deadly combination of all three humors) arises. The various unattainable desires for sense-objects — these are all pains whose names who can know?'"
    },
    "ut-121-c17": {
        "transliteration": "mamatā dādu kaṃḍu iriṣāī. haraṣa biṣāda garaha bahutāī.\npara sukha dekhi jarani soi chaī. kuṣṭha duṣṭatā mana kuṭilaī.",
        "translation": "'Attachment is eczema, jealousy is itching. Joy and sorrow are tumors of many kinds. Burning at the sight of others' happiness is consumption. Wickedness and crookedness of mind are leprosy.'"
    },
    "ut-121-c18": {
        "transliteration": "ahaṃkāra ati dukhada ḍamaruā. daṃbha kapaṭa mada māna neharuā.\ntṛṣṇā udarabṛddhi ati bhārī. tribidha īṣanā taruṇa tijārī.",
        "translation": "'Egoism is the exceedingly painful mumps. Hypocrisy, deceit, pride and vanity are eye diseases. Craving is a severe enlargement of the belly. The three desires (for wealth, progeny and fame) are a raging fever of three types.'"
    },
    "ut-121-c19": {
        "transliteration": "juga bidhi jvara matsara abibekā. kahaṃ lāgi kahauṃ kuroga anekā.",
        "translation": "'Envy and lack of discrimination are a two-fold fever. How far can I go on describing these countless diseases?'"
    },
    "ut-121-d": {
        "transliteration": "eka byādhi basa nara marahiṃ e asādhi bahu byādhi.\npīṛahiṃ saṃtata jīva kahuṃ so kimi lahai samādhi.\nnema dharma ācāra tapa gyāna jagya japa dāna.\nbheṣaja puni koṭinha nahiṃ roga jāhiṃ harijāna.",
        "translation": "'Men die from even a single disease — and these are many incurable diseases that constantly torment the soul. How then can it attain peace? Religious observances, dharma, right conduct, austerity, knowledge, sacrifice, chanting, charity — even millions of these remedies cannot cure these diseases, O servant of Hari.'"
    },

    # === DOHA GROUP 122 ===
    "ut-122-c1": {
        "transliteration": "ehi bidhi sakala jīva jaga rogī. soka haraṣa bhaya prīti biyogī.\nmānaka roga kachuka maiṃ gāe. hahiṃ saba keṃ lakhi biralenh pāe.",
        "translation": "'In this way, every soul in the world is diseased — afflicted by sorrow, joy, fear, love and separation. I have described some of the principal diseases; they exist in everyone but are recognized by few.'"
    },
    "ut-122-c2": {
        "transliteration": "jāne te chījahiṃ kachu pāpī. nāsa na pāvahiṃ jana paritāpī.\nbiṣaya kupathya pāi aṃkure. munihu hṛdayaṃ kā nara bāpure.",
        "translation": "'Those sinners who recognize them do diminish somewhat, but the diseases do not fully perish and continue to torment people. Given the unwholesome diet of sense-objects, they sprout again — even in the hearts of sages, let alone wretched ordinary men.'"
    },
    "ut-122-c3": {
        "transliteration": "rāma kṛpāṃ nāsahiṃ saba rogā. jauṃ ehi bhāṃti banai saṃyogā.\nsadguru baida bacana bisvāsā. saṃjama yaha na biṣaya kai āsā.",
        "translation": "'By Rama's grace all these diseases are cured, if the right combination comes together: faith in the words of a true Guru who is the physician; and the regimen is this — no craving for sense-objects.'"
    },
    "ut-122-c4": {
        "transliteration": "raghupati bhagati sajīvana mūrī. anūpāna śraddhā mati pūrī.\nehi bidhi bhalehi so roga nasāhīṃ. nāhiṃ ta jatana koṭi nahiṃ jāhīṃ.",
        "translation": "'Devotion to the Lord of the Raghus is the life-restoring herb; the vehicle (anupana) is faith with a pure mind. In this way alone are the diseases truly cured — otherwise, even millions of efforts cannot remove them.'"
    },
    "ut-122-c5": {
        "transliteration": "jānia taba mana biruja gosāṃī. jaba ura bala birāga adhikāī.\nsumati chudhā bāṛhai nita naī. biṣaya āsa durbalatā gaī.",
        "translation": "'Know the mind to be healthy, O master, when there is an abundance of strength and detachment in the heart, when the appetite for good sense grows ever new, and the weakness of desire for sense-objects has departed.'"
    },
    "ut-122-c6": {
        "transliteration": "bimala gyāna jala jaba so nahāī. taba raha rāma bhagati ura chāī.\nsiva aja suka sanakādika nārada. je muni brahma bicāra bisārada.",
        "translation": "'When one has bathed in the pure water of knowledge, then devotion to Rama abides fully in the heart. Shiva, Brahma, Shuka, the Sanakas, Narada — all those sages who are adept in the contemplation of Brahman —'"
    },
    "ut-122-c7": {
        "transliteration": "saba kara mata khaganāyaka ehā. karia rāma pada paṃkaja nehā.\nśruti purāna saba graṃtha kahāhīṃ. raghupati bhagati binā sukha nāhīṃ.",
        "translation": "'— the view of all of them, O king of birds, is this: one should cultivate love for the lotus feet of Rama. All the Vedas, Puranas and scriptures declare: without devotion to the Lord of the Raghus, there is no happiness.'"
    },
    "ut-122-c8": {
        "transliteration": "kamaṭha pīṭha jāmahiṃ baru bārā. baṃdhyā suta baru kāhuhi mārā.\nphūlahiṃ nabha baru bahubidhi phūlā. jīva na laha sukha hari pratikūlā.",
        "translation": "'Sooner may trees grow on a tortoise's back, or a barren woman's son kill someone, or flowers of many kinds bloom in the sky — but a soul turned against Hari shall never find happiness.'"
    },
    "ut-122-c9": {
        "transliteration": "tṛṣā jāi baru mṛgajala pānā. baru jāmahiṃ sasa sīsa biṣānā.\naṃdhakāru baru rabihi nasāvai. rāma bimukha na jīva sukha pāvai.",
        "translation": "'Sooner may thirst be quenched by drinking a mirage, or horns grow on a hare's head, or darkness destroy the sun — but a soul turned away from Rama shall never find happiness.'"
    },
    "ut-122-c10": {
        "transliteration": "hima te anala pragaṭa baru hoī. bimukha rāma sukha pāva na koī.",
        "translation": "'Sooner may fire emerge from ice — but no one who is averse to Rama can ever find happiness.'"
    },
    "ut-122-d": {
        "transliteration": "ubāri matheṃ ghṛta hoi baru sikatā te baru tela.\nbinu hari bhajana na bhava taria yaha siddhāṃta apela.\nmasakahi karai biraṃci prabhu ajahi masaka te hīna.\nasa bicāri taji saṃsaya rāmahi bhajahiṃ prabīna.",
        "translation": "'Sooner may butter come from churning water, or oil from sand — but without worshipping Hari, the ocean of worldly existence cannot be crossed. This is an irrefutable conclusion. The Lord can make a mosquito into Brahma, and Brahma into less than a mosquito. Reflecting thus, abandoning all doubt, the wise worship Rama.'"
    },
    "ut-122-sl": {
        "transliteration": "viniścritaṃ vadāmi te na anyathā vacāṃsi me.\nhariṃ narā bhajanti ye'tidustaraṃ taranti te.",
        "translation": "'I declare this with certainty — my words are not otherwise: those who worship Hari cross even the most impassable ocean of worldly existence.'"
    },

    # === DOHA GROUP 123 ===
    "ut-123-c1": {
        "transliteration": "kaheuṃ nātha hari carita anūpā. byāsa samāsa svamati anurūpā.\nśruti siddhāṃta ihai uragārī. rāma bhajia saba kāja bisārī.",
        "translation": "'I have narrated to you, O Lord, the incomparable deeds of Hari — both in detail and in summary, according to my own understanding. This is the settled conclusion of the Vedas, O enemy of serpents: worship Rama, forgetting all other concerns.'"
    },
    "ut-123-c2": {
        "transliteration": "prabhu raghupati taji seia kāhī. mohi se saṭha para mamatā jāhī.\ntumha bigyānarūpa nahiṃ mohā. nātha kīnhi mo para ati chohā.",
        "translation": "'Abandoning the Lord of the Raghus, whom else should one serve? Who would feel affection for a fool like me? You are the embodiment of wisdom and are free from delusion. O Lord, you have shown me exceedingly great kindness.'"
    },
    "ut-123-c3": {
        "transliteration": "pūchihuṃ rāma kathā ati pāvani. suka sanakādi saṃbhu mana bhāvani.\nsata saṃgati durlabha saṃsārā. nimiṣa daṃḍa bhari ekau bārā.",
        "translation": "'You asked me about the most sacred story of Rama — which delights the minds of Shuka, the Sanakas and Shambhu. The company of the good is rare in this world — even for a single moment or a brief instant.'"
    },
    "ut-123-c4": {
        "transliteration": "dekhu garuṛa nija hṛdayaṃ bicārī. maiṃ raghubīra bhajana adhikārī.\nsakunādhama saba bhāṃti apāvana. prabhu mohi kīnha bidita jaga pāvana.",
        "translation": "'Consider in your own heart, O Garuda — am I truly fit to worship the Hero of the Raghus? The lowest of birds, impure in every way — yet the Lord has made me known throughout the world as holy.'"
    },
    "ut-123-d": {
        "transliteration": "āju dhanya maiṃ dhanya ati jadyapi saba bidhi hīna.\nnija jana jāni rāma mohi saṃta samāgama dīna.\nnātha jathāmati bhāṣeuṃ rākheuṃ nahiṃ kachu goi.\ncarita siṃdhu raghunāyaka thāha ki pāvai koi.",
        "translation": "'Today I am blessed, supremely blessed, even though I am deficient in every way. Knowing me as His own, Rama granted me the company of saints. O Lord, I have spoken according to my understanding, hiding nothing. But the ocean of the deeds of the Lord of the Raghus — can anyone ever fathom its depths?'"
    },

    # === DOHA GROUP 124 ===
    "ut-124-c1": {
        "transliteration": "sumiri rāma ke guṇa gaṇa nānā. puni puni haraṣa bhusuṃḍi sujānā.\nmahimā nigama neti kari gāī. atulita bala pratāpa prabhutāī.",
        "translation": "Remembering the many hosts of Rama's virtues, the wise Bhushundi rejoiced again and again. The Vedas sing His glory only through 'neti' (not this, not this) — His strength, majesty and sovereignty are beyond compare."
    },
    "ut-124-c2": {
        "transliteration": "siva aja pūjya carana raghurāī. mo para kṛpā parama mṛdulāī.\nasa subhāu kahuṃ sunauṃ na dekhauṃ. kehi khagesa raghupati sama lekhauṃ.",
        "translation": "The feet of the Lord of the Raghus are worshipped by Shiva and Brahma — and upon me He shows mercy with supreme tenderness. Such a nature I have neither heard of nor seen anywhere — to whom, O king of birds, can I compare the Lord of the Raghus?"
    },
    "ut-124-c3": {
        "transliteration": "sādhaka siddha bimukta udāsī. kabi kobida kṛtagya saṃnyāsī.\njogī sūra sutāpasa gyānī. dharma nirata paṃḍita bigyānī.",
        "translation": "Seekers, perfected beings, the liberated, the dispassionate, poets, scholars, the grateful, renunciants, yogis, heroes, great ascetics, the wise, those established in dharma, learned pandits, men of spiritual science —"
    },
    "ut-124-c4": {
        "transliteration": "tarahiṃ na binu seeṃ mama svāmī. rāma namāmi namāmi namāmī.\nśaraṇa gaeṃ mo se agha rāsī. hohiṃ suddha namāmi abināsī.",
        "translation": "— none of them can cross without serving my Lord. I bow to Rama, I bow, I bow! Even heaps of sinners like me become pure by taking His refuge. I bow to the Imperishable One."
    },
    "ut-124-d": {
        "transliteration": "jāsu nāma bhava bheṣaja harana ghora traya sūla.\nso kṛpālu mohi to para sadā rahau anukūla.\nsuni bhusuṃḍi ke bacana subha dekhi rāma pada neha.\nboleu prema sahita girā garuṛa bigata saṃdeha.",
        "translation": "May He whose name is the remedy for worldly existence and the remover of the three terrible afflictions — may that merciful Lord always remain favorably disposed toward you and me! Hearing Bhushundi's auspicious words and seeing his love for Rama's feet, Garuda, now free of all doubt, spoke with loving words:"
    },

    # === DOHA GROUP 125 ===
    "ut-125-c1": {
        "transliteration": "mai kṛtkṛtya bhayauṃ tava bānī. suni raghubīra bhagati rasa sānī.\nrāma carana nūtana rati bhaī. māyā janita bipati saba gaī.",
        "translation": "'I am fulfilled by your words, steeped in the nectar of devotion to the Hero of the Raghus. A new love for Rama's feet has arisen in me, and all the afflictions born of Maya have departed.'"
    },
    "ut-125-c2": {
        "transliteration": "moha jaladhi bohita tumha bhae. mo kahaṃ nātha bibidha sukha dae.\nmo pahiṃ hoi na prati upakārā. baṃdauṃ tava pada bārahiṃ bārā.",
        "translation": "'You have been a ship across the ocean of delusion for me. You have given me manifold joys, O Lord. I am unable to repay your kindness — I bow at your feet again and again.'"
    },
    "ut-125-c3": {
        "transliteration": "pūrana kāma rāma anurāgī. tumha sama tāta na kou baṛabhāgī.\nsaṃta biṭapa saritā giri dharanī. para hita hetu sabanha kai karanī.",
        "translation": "'You are fulfilled in all desires, a lover of Rama — there is none as fortunate as you, my dear. Saints, trees, rivers, mountains and the earth — the actions of all these are for the welfare of others.'"
    },
    "ut-125-c4": {
        "transliteration": "saṃta hṛdaya navanīta samānā. kahā kabinha pari kahai na jānā.\nnija paritāpa dravai navanītā. para dukha dravahiṃ saṃta supunītā.",
        "translation": "'The heart of a saint is like butter — poets have said this, but they did not fully grasp the meaning. Butter melts from its own heat, but supremely pure saints melt at the suffering of others.'"
    },
    "ut-125-c5": {
        "transliteration": "jīvana janma suphala mama bhayaū. tava prasāda saṃsaya saba gayaū.\njānehu sadā mohi nija kiṃkara. puni puni umā kahai bihaṃgabara.",
        "translation": "'My life and birth have become fruitful. By your grace, all doubts have vanished. Always know me as your servant.' Again and again, O Uma (says Shiva), spoke the king of birds thus."
    },
    "ut-125-d": {
        "transliteration": "tāsu carana siru nāi kari prema sahita matidhīra.\ngayau garuṛa baikuṃṭha taba hṛdayaṃ rākhi raghubīra.\ngirijā saṃta samāgama sama na lābha kachu āna.\nbinu hari kṛpā na hoi so gāvahiṃ beda purāna.",
        "translation": "Bowing his head at Bhushundi's feet with love, the steadfast Garuda then departed for Vaikuntha, enshrining the Hero of the Raghus in his heart. O Girija (Parvati), there is no gain equal to the company of saints. Without Hari's grace, this does not come about — so sing the Vedas and Puranas."
    },

    # === DOHA GROUP 126 ===
    "ut-126-c1": {
        "transliteration": "kaheuṃ parama punīta itihāsā. sunata śravana chūṭahiṃ bhava pāsā.\npranata kalpataru karunā puṃjā. upajai prīti rāma pada kaṃjā.",
        "translation": "(Shiva says:) I have narrated this supremely sacred history — hearing it, the bonds of worldly existence are broken. He who is a wish-fulfilling tree for those who bow before Him, a mass of compassion — may love arise for the lotus feet of Rama."
    },
    "ut-126-c2": {
        "transliteration": "mana krama bacana janita agha jāī. sunahiṃ je kathā śravana mana lāī.\ntīrthāṭana sādhana samudāī. joga birāga gyāna nipuṇāī.",
        "translation": "The sins born of thought, deed and speech are washed away for those who listen to this story with their ears and mind attentive. Pilgrimages, the entire collection of spiritual practices, yoga, detachment, and mastery of knowledge —"
    },
    "ut-126-c3": {
        "transliteration": "nānā karma dharma brata dānā. saṃjama dama japa tapa makha nānā.\nbhūta dayā dvija gura sevakāī. bidyā binaya bibeka baṛāī.",
        "translation": "Various rituals, religious duties, vows, charity, self-restraint, sense-control, chanting, austerity, various sacrifices, compassion toward living beings, service to Brahmins and the Guru, learning, humility, discrimination and greatness —"
    },
    "ut-126-c4": {
        "transliteration": "jahaṃ lagi sādhana beda bakhānī. saba kara phala hari bhagati bhavānī.\nso raghunātha bhagati śruti gāī. rāma kṛpāṃ kāhūṃ eka pāī.",
        "translation": "all the spiritual practices that the Vedas describe — the fruit of them all is devotion to Hari, O Bhavani. That devotion to the Lord of the Raghus, which the Vedas sing of, has been attained by some rare soul through Rama's grace alone."
    },
    "ut-126-d": {
        "transliteration": "muni durlabha hari bhagati nara pāvahiṃ binahiṃ prayāsa.\nje yaha kathā niraṃtara sunahiṃ māni bisvāsa.",
        "translation": "Devotion to Hari, which is rare even for sages, is obtained effortlessly by those who constantly listen to this narrative with faith and trust."
    },

    # === DOHA GROUP 127 ===
    "ut-127-c1": {
        "transliteration": "soi sarbagya guṇī soi gyātā. soi mahī maṃḍita paṃḍita dātā.\ndharma parāyaṇa soi kula trātā. rāma carana jā kara mana rātā.",
        "translation": "He alone is all-knowing, he alone is virtuous, he alone is wise, he alone is a scholar who adorns the earth, a benefactor. He alone is devoted to dharma, he alone is the savior of his lineage — whose mind is absorbed in the feet of Rama."
    },
    "ut-127-c2": {
        "transliteration": "nīti nipuṇa soi parama sayānā. śruti siddhāṃta nīka tehiṃ jānā.\nsoi kabi kobida soi ranadhīrā. jo chala chāṛi bhajai raghubīrā.",
        "translation": "He alone is skilled in statecraft, he alone is supremely wise. He alone truly knows the settled conclusions of the Vedas. He alone is a poet, a scholar, and a hero in battle — who worships the Hero of the Raghus, abandoning all deceit."
    },
    "ut-127-c3": {
        "transliteration": "dhanya desa so jahaṃ surasarī. dhanya nāri pativrata anusarī.\ndhanya so bhūpu nīti jo karaī. dhanya so dvija nija dharma na ṭaraī.",
        "translation": "Blessed is the land where the Ganga flows. Blessed is the woman who follows the vow of devotion to her husband. Blessed is the king who rules with justice. Blessed is the Brahmin who does not swerve from his duty."
    },
    "ut-127-c4": {
        "transliteration": "so dhana dhanya prathama gati jākī. dhanya punya rata mati soi pākī.\ndhanya gharī soi jaba satasaṃgā. dhanya janma dvija bhagati abhaṃgā.",
        "translation": "Blessed is that wealth whose first use is for the good of others. Blessed and mature is that mind which delights in merit. Blessed is that hour when one is in the company of the good. Blessed is the birth of a Brahmin whose devotion is unbroken."
    },
    "ut-127-d": {
        "transliteration": "so kula dhanya umā sunu jagata pūjya supunīta.\nśrīraghubīra parāyaṇa jehi nara upaja binīta.",
        "translation": "That family is blessed, O Uma, listen — honored and most sacred in the world — in which is born a humble person devoted to the glorious Hero of the Raghus."
    },

    # === DOHA GROUP 128 ===
    "ut-128-c1": {
        "transliteration": "mati anurūpa kathā maiṃ bhāṣī. jadyapi prathama gupta kari rākhī.\ntava mana prīti dekhi adhikāī. taba maiṃ raghupati kathā sunāī.",
        "translation": "(Shiva says:) I have narrated this story according to my understanding, though I had previously kept it hidden. Seeing the exceeding love in your heart, I then narrated to you the story of the Lord of the Raghus."
    },
    "ut-128-c2": {
        "transliteration": "yaha na kahia saṭhahī haṭhasīlahi. jo mana lāi na suna hari līlahi.\nkahia na lobhihi krodhahi kāmihi. jo na bhajai sacarācara svāmihi.",
        "translation": "This should not be told to the obstinate fool who does not listen to Hari's divine play with an attentive mind. Nor should it be told to the greedy, the wrathful, or the lustful — those who do not worship the Lord of all animate and inanimate creation."
    },
    "ut-128-c3": {
        "transliteration": "dvija drohihi na sunāia kabahūṃ. surapati sarisa hoi nṛpa jabahūṃ.\nrāma kathā ke tei adhikārī. jinha keṃ satasaṃgati ati pyārī.",
        "translation": "It should never be told to one who is hostile to Brahmins, even if he be a king equal to Indra. Those alone are qualified to hear the story of Rama who dearly love the company of the righteous."
    },
    "ut-128-c4": {
        "transliteration": "gura pada prīti nīti rata jeī. dvija sevaka adhikārī teī.\ntā kahaṃ yaha bisēṣa sukhadāī. jāhi prāṇapriya śrīraghurāī.",
        "translation": "Those who love the Guru's feet and are devoted to righteous conduct, those who serve the Brahmins — they are qualified. This story is especially delightful for those to whom the glorious Lord of the Raghus is dearer than life itself."
    },
    "ut-128-d": {
        "transliteration": "rāma carana rati jo caha athavā pada nirbāna.\nbhāva sahita so yaha kathā karau śravaṇa puṭa pāna.",
        "translation": "Whoever desires love for Rama's feet, or the state of liberation — let them drink this story through the cups of their ears with sincere feeling."
    },

    # === DOHA GROUP 129 ===
    "ut-129-c1": {
        "transliteration": "rāma kathā girijā maiṃ baranī. kali mala samani manomala haranī.\nsaṃsṛti roga sajīvana mūrī. rāma kathā gāvahiṃ śruti sūrī.",
        "translation": "(Shiva says:) O Girija, I have narrated the story of Rama — it destroys the impurities of the Kali age and removes the defilements of the mind. The story of Rama is the life-restoring herb for the disease of worldly existence — so sing the Vedas and the sages."
    },
    "ut-129-c2": {
        "transliteration": "ehi mahaṃ rucira sapta sopānā. raghupati bhagati kera paṃthānā.\nati hari kṛpā jāhi para hoī. pāuṃ dei ehiṃ māraga soī.",
        "translation": "Within this (Ramcharitmanas) are the seven beautiful steps on the path of devotion to the Lord of the Raghus. Only one upon whom Hari's supreme grace descends sets foot upon this path."
    },
    "ut-129-c3": {
        "transliteration": "mana kāmanā siddhi nara pāvā. je yaha kathā kapaṭa taji gāvā.\nkahahiṃ sunahiṃ anumodana karahīṃ. te gopada iva bhavanidhi tarahīṃ.",
        "translation": "Those who, giving up deceit, sing this narrative attain the fulfillment of their heart's desires. Those who narrate it, listen to it, or rejoice in hearing it — they cross the ocean of worldly existence as easily as a cow's hoofprint (puddle)."
    },
    "ut-129-c4": {
        "transliteration": "suni saba kathā hṛdayaṃ ati bhāī. girijā bolī girā suhāī.\nnātha kṛpāṃ mama gata saṃdehā. rāma carana upajeu nava nehā.",
        "translation": "Having heard the entire story, which delighted her heart greatly, Girija (Parvati) spoke these beautiful words: 'By Your grace, O Lord, my doubts have vanished. A new love for Rama's feet has arisen in me.'"
    },
    "ut-129-d": {
        "transliteration": "maiṃ kṛtakṛtya bhaiuṃ aba tava prasāda bisvesa.\nupajī rāma bhagati dṛṛha bīte sakala kalesa.",
        "translation": "'I am now truly fulfilled, by Your grace, O Lord of the universe. Firm devotion to Rama has arisen in me, and all my afflictions have ended.'"
    },

    # === DOHA GROUP 130 ===
    "ut-130-c1": {
        "transliteration": "yaha subha saṃbhu umā saṃbādā. sukha saṃpādana samana biṣādā.\nbhava bhaṃjana gaṃjana saṃdehā. jana raṃjana sajjana priya ehā.",
        "translation": "This auspicious dialogue between Shambhu and Uma bestows happiness and dispels sorrow. It destroys worldly existence and shatters doubt. It delights the devotees and is dear to the virtuous."
    },
    "ut-130-c2": {
        "transliteration": "rāma upāsaka je jaga māhīṃ. ehi sama priya tinha ke kachu nāhīṃ.\nraghupati kṛpāṃ jathāmati gāvā. maiṃ yaha pāvana carita suhāvā.",
        "translation": "For the worshippers of Rama in this world, there is nothing as dear as this. By the grace of the Lord of the Raghus, I (Tulsidas) have sung this sacred and beautiful story according to my understanding."
    },
    "ut-130-c3": {
        "transliteration": "ehiṃ kalikāla na sādhana dūjā. joga jagya japa tapa brata pūjā.\nrāmahi sumiriya gāia rāmahi. saṃtata sunia rāma guṇa grāmahi.",
        "translation": "In this Kali age there is no other spiritual practice — neither yoga, nor sacrifice, nor chanting, nor austerity, nor vows, nor worship. Remember Rama, sing of Rama, and constantly listen to the multitude of Rama's virtues."
    },
    "ut-130-c4": {
        "transliteration": "jāsu patita pāvana baṛa bānā. gāvahiṃ kabi śruti saṃta purānā.\ntāhi bhajahi mana taji kuṭilāī. rāma bhajeṃ gati kehiṃ nahiṃ pāī.",
        "translation": "He whose great renown as the Purifier of the fallen is sung by poets, Vedas, saints and Puranas — worship Him with your mind, abandoning all crookedness. Who has not attained salvation by worshipping Rama?"
    },
    "ut-130-ch": {
        "transliteration": "pāī na kehiṃ gati patita pāvana rāma bhaji sunu saṭha manā.\nganikā ajāmila byādha gīdha gajādi khala tāre ghanā.\nābhīra jamana kirāta khasa svapacādi ati agharūpa je.\nkahi nāma bāraka tepi pāvana hohiṃ rāma namāmi te.\nraghubaṃsa bhūṣaṇa carita yaha nara kahahiṃ sunahiṃ je gāvahīṃ.\nkali mala manomala dhoi binu śrama rāma dhāma sidhāvahīṃ.\nsata paṃca caupāīṃ manohara jāni jo nara ura dharai.\ndāruṇa abidyā paṃca janita bikāra śrīraghubara harai.\nsuṃdara sujāna kṛpā nidhāna anātha para kara prīti jo.\nso eka rāma akāma hita nirbānaprada sama āna ko.\njākī kṛpā lavalesa te matimṃda tulasīdāsahūṃ.\npāyo parama biśrāmu rāma samāna prabhu nāhīṃ kahūṃ.",
        "translation": "Who has not attained salvation by worshipping Rama, the purifier of the fallen? Listen, O foolish mind! The courtesan (Ganika), Ajamila, the hunter, the vulture, the elephant and many other sinners were saved. Abhiras, Yavanas, Kiratas, Khasas, Chandals and others steeped in sin — even by uttering His name just once, they become pure. I bow to that Rama. This story of the Ornament of the Raghu dynasty — those who narrate it, hear it, or sing it — they wash away the impurities of the Kali age and the defilements of the mind, and proceed effortlessly to Rama's abode. Whoever treasures in their heart even five or seven of these beautiful chaupais — the glorious Lord of the Raghus removes the terrible distortions born of the five forms of ignorance. He who is beautiful, wise, a treasury of mercy, who loves the helpless — that one Rama, the selfless benefactor, the bestower of liberation — who else is His equal? By even a particle of whose grace, even the dull-witted Tulsidas has found supreme peace — there is no Lord anywhere equal to Rama."
    },
    "ut-130-d": {
        "transliteration": "mo sama dīna na dīna hita tumha samāna raghubīra.\nasa bicāri raghubaṃsa mani harahu biṣama bhava bhīra.\nkāmihi nāri piārī jimi lobhahi priya jimi dāma.\ntimi raghunātha niraṃtara priya lāgahu mohi rāma.",
        "translation": "There is no one as wretched as I, and no friend of the wretched equal to You, O Hero of the Raghus. Reflecting thus, O Jewel of the Raghu dynasty, deliver me from the terrible throng of worldly existence. As a woman is dear to the lustful, as wealth is dear to the greedy — so may You, O Lord of the Raghus, be perpetually dear to me, O Rama!"
    },
    "ut-130-sl": {
        "transliteration": "yatpūrvaṃ prabhuṇā kṛtaṃ sukavinā śrīśambhunā durgamaṃ\nśrēmadrāmapadābjabhaktimaniśam prāptyai tu rāmāyaṇaṃ.\nmatvā tadraghunāthanāmanirataṃ svāntastamaḥśāntaye\nbhāṣābaddhamidaṃ cakāra tulasīdāsastathā mānasaṃ.\npuṇyaṃ pāpaharaṃ sadā śivakaraṃ vijñānabhaktipadaṃ\nmāyāmohamalāpahaṃ suvimalaṃ premāmbupūraṃ śubhaṃ.\nśrēmadrāmacaritamānasamidaṃ bhaktyāvagāhanti ye\nte saṃsārapatanagaghorakiranairnaḥ dahyanti mānavāḥ.",
        "translation": "That which was formerly composed by the great poet Lord Shri Shambhu as the difficult Ramayana, for the attainment of unceasing devotion to the lotus feet of Shri Rama — reflecting upon that, and devoted to the name of the Lord of the Raghus, Tulsidas rendered this Manas (lake) into the vernacular language for the dispelling of the darkness of his own heart. This Shri Ramcharitmanas — meritorious, sin-destroying, ever-auspicious, bestowing wisdom and devotion, removing the impurities of Maya and delusion, supremely pure, overflowing with the waters of love, auspicious — those who immerse themselves in it with devotion are not scorched by the terrible rays of the sun of worldly existence."
    },
}

# Apply updates
for group in data["dohaGroups"]:
    for verse in group["verses"]:
        vid = verse["id"]
        if vid in updates:
            verse["transliteration"] = updates[vid]["transliteration"]
            verse["translation"] = updates[vid]["translation"]

with open(r'c:/_work/RamayanaPath/data/tulsidas/uttar-kand.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! Updated", len(updates), "verses.")
