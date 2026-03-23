#!/usr/bin/env python3
"""Add English translations and IAST transliterations to Lanka Kand dohas 81-121."""

import json
import sys

INPUT = r"c:/_work/RamayanaPath/data/tulsidas/lanka-kand.json"

# Map: (doha_number, verse_id) -> (transliteration, translation)
UPDATES = {
    # === DOHA 81 ===
    ("la-81-c1",): (
        "sura brahmādi siddha muni nānā. dekhata rana nabha caḍhe bimānā..\nhamahū umā rahe tehi saṃgā. dekhata rāma carita rana raṃgā..",
        "Gods headed by Brahma, Siddhas, and many sages ascended their aerial chariots in the sky to watch the battle. O Uma, I too was present among them, witnessing the colorful spectacle of Rama's deeds in battle."
    ),
    ("la-81-c2",): (
        "subhaṭa samara rasa duhu disi māte. kapi jayasīla rāma bala tāte..\neka eka sana bhirahi pacārahi. ekanha eka mardi mahi pārahi..",
        "Warriors on both sides were intoxicated with the thrill of battle. The monkeys were victorious by Rama's strength. They challenged each other one-on-one, and crushing their opponents, dashed them to the ground."
    ),
    ("la-81-c3",): (
        "mārahi kāṭahi dharahi pachārahi. sīsa tori sīsanha sana mārahi..\nudara bidārahi bhujā upārahi. gahi pada avani paṭaki bhaṭa ḍārahi..",
        "They struck, slashed, seized, and threw down their foes. They tore off heads and struck them against other heads. They ripped open bellies, tore off arms, and grabbing enemies by the feet, dashed them to the ground."
    ),
    ("la-81-c4",): (
        "nisicara bhaṭa mahi gāḍahi bhālū. ūpara ḍhāri dehi bahu bālū..\nbīra balimukha juddha biruddhe. dekhiata bipula kāla janu kruddhe..",
        "The bears buried demon warriors in the earth and heaped sand over them. The brave monkey warriors, fierce in battle, looked like many forms of angry Death himself."
    ),
    ("la-81-ch",): (
        "kruddhe kṛtāṃta samāna kapi tana stravata sonita rājahīṃ.\nmardahi nisācara kaṭaka bhaṭa balavanta ghana jimi gājahīṃ..\nmārahi capeṭanhi ḍāṭi dātanhi kāṭi lātanhi mījahīṃ.\ncikkarahi markaṭa bhālu chala bala karahi jehi khala chījahīṃ..\ndhari gāla phārahi ura bidārahi gala aṃtāvari melahīṃ.\nprahlādapati janu bibidha tanu dhari samara aṃgana khelahīṃ..\ndharu māru kāṭu pachāru ghora girā gagana mahi bhari rahī.\njaya rāma jo tṛna te kulisa kara kulisa te kara tṛna sahī..",
        "Furious as Death incarnate, the monkeys shone with blood streaming from their bodies. They crushed the demon army — mighty warriors thundering like clouds. They struck with slaps, bit with teeth, kicked and squeezed. Monkeys and bears roared, using cunning and strength to wear down the wicked. They seized and tore open cheeks, ripped open chests, and twined their entrails around necks — as if Narasimha (Lord of Prahlada) had taken many forms to sport in the arena of battle. The dreadful cry 'Seize! Kill! Cut! Throw down!' filled heaven and earth. Glory to Rama, who can make grass into thunderbolts and thunderbolts into grass!"
    ),
    ("la-81-d",): (
        "nija dala bicalata dekhesi bīsa bhujāṃ dasa cāpa.\nratha caḍhi caleu dasānana phirahu phirahu kari dāpa..81..",
        "Seeing his own army faltering, the ten-headed Ravana mounted his chariot with twenty arms and ten bows, shouting boastfully: 'Turn back! Turn back!'"
    ),

    # === DOHA 82 ===
    ("la-82-c1",): (
        "dhāyau parama kruddha dasakaṃdhara. sanmukha cale hūha dai baṃdara..\ngahi kara pādapa upala pahārā. ḍārenhi tā para ekahi bārā..",
        "The supremely enraged Ravana charged forward. The monkeys advanced to meet him with war cries. Seizing trees, rocks, and boulders in their hands, they hurled them all at once upon him."
    ),
    ("la-82-c2",): (
        "lāgahi saila bajra tana tāsū. khaṃḍa khaṃḍa hoi phūṭahi āsū..\ncalā na acala rahā ratha ropī. rana durmada rāvana ati kopī..",
        "Mountains struck his thunderbolt-hard body but shattered to pieces. He did not budge, standing firm on his chariot — Ravana, invincible in battle and supremely enraged."
    ),
    ("la-82-c3",): (
        "ita uta jhapaṭi dapaṭi kapi jodhā. mardai lāga bhayau ati krodhā..\ncale parāi bhālu kapi nānā. trāhi trāhi aṃgada hanumānā..",
        "Darting here and there, he rebuked and began crushing the monkey warriors in extreme rage. Many bears and monkeys fled, crying: 'Save us! Save us, Angad! Hanuman!'"
    ),
    ("la-82-c4",): (
        "pāhi pāhi raghubīra gosāī. yaha khala khāi kāla kī nāī..\ntehi dekhe kapi sakala parāne. dasahuṃ cāpa sāyaka saṃdhāne..",
        "'Protect us, protect us, O Lord Raghubir! This wretch devours us like Death itself!' Seeing all the monkeys fleeing, Ravana strung arrows on all ten of his bows."
    ),
    ("la-82-ch",): (
        "saṃdhāni dhanu sara nikara chāḍesi uraga jimi uḍi lāgahīṃ.\nrahe pūri sara dharanī gagana disi bidisi kahaṃ kapi bhāgahīṃ..\nbhayo ati kolāhala bikala kapi dala bhālu bolahi āture.\nraghubīra karunā siṃdhu ārata baṃdhu jana racchaka hare..",
        "Drawing his bows, he released showers of arrows that flew and struck like serpents. Arrows filled the earth, sky, and every direction — where could the monkeys flee? A great tumult arose; the monkey and bear army was distressed and cried out in anguish: 'O Raghubir, ocean of mercy, protector of the afflicted and devoted — save us, O Lord!'"
    ),
    ("la-82-d",): (
        "nija dala bikala dekhi kaṭi kasi niṣaṃga dhanu hātha.\nlachimanacale kruddha hoi nāi rāma pada mātha..82..",
        "Seeing his own army in distress, Lakshmana girded his waist, took quiver and bow in hand, and advanced wrathfully after bowing his head at Rama's feet."
    ),

    # === DOHA 83 ===
    ("la-83-c1",): (
        "re khala kā mārasi kapi bhālū. mohi biloku tora maiṃ kālū..\nkhojata raheuṃ tohi sutaghātī. āju nipāti juḍāvauṃ chātī..",
        "'O villain, why do you strike monkeys and bears? Look at me — I am your Death! I have been searching for you, slayer of my father's sons. Today I shall slay you and cool my heart!'"
    ),
    ("la-83-c2",): (
        "asa kahi chāḍesi bāna pracaṃḍā. lachimana kie sakala sata khaṃḍā..\nkoṭinha āyudha rāvana ḍāre. tila pravāna kari kāṭi nivāre..",
        "So saying, Lakshmana released fierce arrows. He cut all of Ravana's shafts into a hundred pieces. Ravana hurled millions of weapons, but Lakshmana cut them to sesame-sized fragments and neutralized them."
    ),
    ("la-83-c3",): (
        "puni nija bānanha kīnha prahārā. syaṃdanu bhaṃji sārathī mārā..\nsata sata sara māre dasa bhālā. giri sṛṃganha janu prabisahi byālā..",
        "Then Lakshmana struck with his own arrows, shattering Ravana's chariot and slaying his charioteer. He shot a hundred arrows into each of the ten foreheads — as if serpents were entering mountain peaks."
    ),
    ("la-83-c4",): (
        "puni sata sara mārā ura māhīṃ. pareu dharani tala sudhi kachu nāhīṃ..\nuṭhā prabala puni muruchā jāgī. chāḍisi brahma dīnhi jo sāṃgī..",
        "Then he shot a hundred arrows into Ravana's chest, who fell to the ground utterly senseless. When the powerful demon revived from his swoon, he hurled the spear that Brahma had given him."
    ),
    ("la-83-ch",): (
        "so brahma datta pracaṃḍa sakti anaṃta ura lāgī sahī.\nparyau bīra bikala uṭhāva dasamukha atula bala mahimā rahī..\nbrahmāṃḍa bhavana birāja jākeṃ eka sira jimi raja kanī.\ntehi caha uṭhāvana mūḍha rāvana jāna nahiṃ tribhuana dhanī..",
        "That terrible spear given by Brahma struck Lakshmana (the infinite Shesha) full in the chest. The hero fell unconscious. The ten-headed Ravana tried to lift him, priding himself on his matchless strength. But he in whose single head the entire universe resides like a mere speck of dust — that Lord of the three worlds — how could the fool Ravana lift him?"
    ),
    ("la-83-d",): (
        "dekhi pavanasuta dhāyau bolata bacana kaṭhora.\nāvata kapihi hanyau tehi muṣṭi prahāra praghora..83..",
        "Seeing this, Hanuman rushed forward, speaking harsh words. As the monkey approached, Ravana struck him with a terrible blow of his fist."
    ),

    # === DOHA 84 ===
    ("la-84-c1",): (
        "jānu ṭeki kapi bhūmi na girā. uṭhā saṃbhāri bahuta risa bharā..\nmuṭhikā eka tāhi kapi mārā. pareu saila janu bajra prahārā..",
        "Bracing on one knee, the monkey did not fall to the ground. He steadied himself, filled with immense rage. Hanuman struck Ravana with a single punch — he fell like a mountain struck by a thunderbolt."
    ),
    ("la-84-c2",): (
        "muruchā gai bahori so jāgā. kapi bala bipula sarāhana lāgā..\ndhiga dhiga mama pauruṣa dhiga mohī. jauṃ taiṃ jiata rahesi suradrohī..",
        "When his swoon passed and he revived, Ravana began praising the monkey's great strength. 'Shame, shame on my valor! Shame on me — that you still live, O enemy of the gods!'"
    ),
    ("la-84-c3",): (
        "asa kahi lachimana kahuṃ kapi lyāyau. dekhi dasānana bisamaya pāyau..\nkaha raghubīra samujhu jiyaṃ bhrātā. tumha kṛtāṃta bhacchaka sura trātā..",
        "So saying, Hanuman brought Lakshmana back to Rama. Seeing this, Ravana was astounded. Rama said: 'Take heart, brother — you are the devourer of Death itself and the protector of the gods.'"
    ),
    ("la-84-c4",): (
        "sunata bacana uṭhi baiṭha kṛpālā. gaī gagana so sakti karālā..\npuni kodaṃḍa bāna gahi dhāe. ripu sanmukha ati ātura āe..",
        "Hearing these words, the compassionate Lakshmana sat up. That terrible spear flew back to the sky. Then, seizing his bow and arrows, Lakshmana rushed eagerly to face the enemy once more."
    ),
    ("la-84-ch",): (
        "ātura bahori bibhaṃji syaṃdana sūta hati byākula kiyau.\ngir yau dharani dasakaṃdhara bikalatara bāna sata bedhyau hiyau..\nsārathī dūsara ghāli ratha tehi turata laṃkā lai gayau.\nraghubīra baṃdhu pratāpa puṃja bahori prabhu caranani nayau..",
        "In haste, Lakshmana shattered Ravana's chariot and killed the charioteer, throwing him into confusion. The ten-headed Ravana fell to the earth, pierced by a hundred arrows in his heart. A second charioteer placed him in another chariot and quickly took him to Lanka. Then that embodiment of valor, the brother of Raghubir, returned and bowed at his Lord's feet."
    ),
    ("la-84-d",): (
        "uhāṃ dasānana jāgi kari karai lāga kachu jagya.\nrāma birodha bijaya caha saṭha haṭha basa ati agya..84..",
        "There in Lanka, Ravana recovered consciousness and began performing a ritual sacrifice, hoping to gain victory against Rama — the fool, stubborn and utterly ignorant."
    ),

    # === DOHA 85 ===
    ("la-85-c1",): (
        "ihāṃ bibhīṣana saba sudhi pāī. sapadi jāi raghupatihi sunāī..\nnātha karai rāvana eka jāgā. siddha bhaeṃ nahi marihi abhāgā..",
        "Here Vibhishana learned all the details and immediately went to inform Rama. 'Lord, Ravana is performing a sacrificial rite. If it is completed, the wretch will become invincible and cannot be killed.'"
    ),
    ("la-85-c2",): (
        "paṭhavahu nātha begi bhaṭa baṃdara. karahi bidhaṃsa āva dasakaṃdhara..\nprāta hota prabhu subhaṭa paṭhāe. hanumadādi aṃgada saba dhāe..",
        "'Send warriors and monkeys quickly, my Lord. Let them disrupt the sacrifice before Ravana completes it.' At dawn, the Lord dispatched his champions. Hanuman, Angad, and all rushed forth."
    ),
    ("la-85-c3",): (
        "kautuka kūdi caḍhe kapi laṃkā. paiṭhe rāvana bhavana asaṃkā..\njagya karata jabahīṃ so dekhā. sakala kapinha bhā krodha bisēṣā..",
        "The monkeys playfully leaped into Lanka and fearlessly entered Ravana's palace. When they saw him performing the sacrifice, all the monkeys were filled with extreme rage."
    ),
    ("la-85-c4",): (
        "rana te nilaja bhāji gṛha āvā. ihāṃ āi baka dhyāna lagāvā..\nasa kahi aṃgada mārā lātā. citava na saṭha svāratha mana rātā..",
        "'Shameless one, you fled from the battlefield and came home! And here you sit pretending to meditate like a crane!' So saying, Angad kicked him. But the fool, absorbed in selfish purpose, did not even look up."
    ),
    ("la-85-ch",): (
        "nahi citava jaba kari kopa kapi gahi dasana lātanha mārahi.\ndhari kesa nāri nikāri bāhera te atidīna pukārahīṃ..\ntaba uṭheu kruddha kṛtāṃta sama gahi carana bānara ḍāraī.\nehi bīca kapinha bidhaṃsa kṛta makha dekhi mana mahuṃ hāraī..",
        "When he would not look up, the enraged monkeys bit him and kicked him. They dragged his women out by the hair, and those women cried out most piteously. Then Ravana rose, furious as Death, and seizing monkeys by the feet, hurled them away. But in the meanwhile the monkeys had destroyed the sacrifice, and seeing this, Ravana felt defeat in his heart."
    ),
    ("la-85-d",): (
        "jagya bidhaṃsi kusala kapi āe raghupati pāsa.\ncaleu nisācara krurdda hoi tyāgi jivana kai āsa..85..",
        "Having destroyed the sacrifice, the monkeys returned safely to Rama. The demon set forth again in fury, having abandoned all hope of life."
    ),

    # === DOHA 86 ===
    ("la-86-c1",): (
        "calata hohi ati asubha bhayaṃkara. baiṭhahi gīdha uḍāi siranhi para..\nbhayau kālabasa kāhu na mānā. kahesi bajāvahu juddha nisānā..",
        "As Ravana set out, most terrible and inauspicious omens occurred — vultures alighted on his heads. But being under the sway of Death, he heeded no one. He commanded: 'Sound the battle drums!'"
    ),
    ("la-86-c2",): (
        "calī tamīcara anī apārā. bahu gaja ratha padāti asavārā..\nprabhu sanmukha dhāe khala kaisēṃ. salabha samūha anala kahaṃ jaisēṃ..",
        "The boundless demon army marched forth — with many elephants, chariots, foot soldiers, and horsemen. The villains rushed toward the Lord like swarms of moths flying into a flame."
    ),
    ("la-86-c3",): (
        "ihāṃ devatanha astuti kīnhī. dāruna bipati hamahi ehi dīnhī..\naba jani rāma khelāvahu ehī. atisaya dukhita hoti baidehī..",
        "Meanwhile the gods prayed: 'This wretch has brought us terrible calamity. Now please, O Rama, toy with him no longer — Vaidehi (Sita) suffers exceedingly.'"
    ),
    ("la-86-c4",): (
        "deva bacana suni prabhu musakānā. uṭhi raghubīra sudhāre bānā..\njaṭā jūṭa dṛḍha bāṃdhai māthe. sohahi sumana bīca bica gāthe..",
        "Hearing the gods' words, the Lord smiled. Raghubir arose and adjusted his arrows. He firmly tied his matted locks upon his head, adorned with flowers woven in between — how beautiful they looked!"
    ),
    ("la-86-c5",): (
        "aruna nayana bārida tanu syāmā. akhila loka locanābhirāmā..\nkaṭitaṭa parikara kasyau niṣaṃgā. kara kodaṃḍa kaṭhina sāraṃgā..",
        "His eyes were ruddy, his body dark as a rain cloud, a delight to the eyes of all the worlds. At his waist he fastened the quiver belt, and in his hand he held his mighty bow Sharanga."
    ),
    ("la-86-ch",): (
        "sāraṃga kara suṃdara niṣaṃga silīmukhākara kaṭi kasyau.\nbhujadaṃḍa pīna manoharāyata ura dharāsura pada lasyau..\nkaha dāsa tulasī jabahiṃ prabhu sara cāpa kara pherana lage.\nbrahmāṃḍa diggaja kamaṭha ahi mahi siṃdhu bhūdhara ḍagamage..",
        "With his bow in hand, his beautiful quiver full of arrows fastened at his waist, his stout and lovely long arms, and the mark of the demon he slew upon his chest — says the servant Tulsi — when the Lord began to twirl his bow and arrows in hand, the universe, the elephants of the quarters, the cosmic tortoise, the serpent Shesha, the earth, the oceans, and the mountains all trembled."
    ),
    ("la-86-d",): (
        "sobhā dekhi haraṣi sura baraṣahi sumana apāra.\njaya jaya jaya karunānidhi chabi bala guna āgāra..86..",
        "Seeing his splendor, the delighted gods showered countless flowers, crying: 'Victory, victory, victory to the Ocean of Mercy, the abode of beauty, strength, and virtue!'"
    ),

    # === DOHA 87 ===
    ("la-87-c1",): (
        "ehīṃ bīca nisācara anī. kasamasāta āī ati ghanī..\ndekhi cale sanmukha kapi bhaṭṭā. pralayakāla ke janu ghana ghaṭṭā..",
        "Meanwhile the demon army advanced, teeming and restless. Seeing them, the monkey warriors moved forward to meet them — like masses of clouds at the time of cosmic dissolution."
    ),
    ("la-87-c2",): (
        "bahu kṛpāna taravāri camaṃkahi. janu dahaṃ disi dāminīṃ damaṃkahi..\ngaja ratha turaga cikāra kaṭhorā. garjahi manahuṃ balāhaka ghorā..",
        "Many scimitars and swords flashed, as if lightning blazed in all ten directions. The harsh cries of elephants, chariots, and horses roared like terrifying thunderclouds."
    ),
    ("la-87-c3",): (
        "kapi laṃgūra bipula nabha chāe. manahuṃ iṃdradhanu ue suhāe..\nuṭhai dhūri mānahuṃ jaladhārā. bāna buṃda bhai bṛṣṭi apārā..",
        "Countless monkey tails covered the sky like beautiful rainbows appearing. Dust rose like streams of water, and the arrows fell in an endless rain."
    ),
    ("la-87-c4",): (
        "duhuṃ disi parbata karahi prahārā. bajrapāta janu bārahi bārā..\nraghupati kopi bāna jhari lāī. ghāyala bhai nisicara samudāī..",
        "Both sides hurled mountains at each other — like thunderbolt strikes again and again. Rama in anger let loose a torrent of arrows, and the entire demon host was wounded."
    ),
    ("la-87-c5",): (
        "lāgata bāna bīra cikkarahīṃ. ghurmi ghurmi jahaṃ tahaṃ mahi parahīṃ..\nstravahi saila janu nirjhara bhārī. sonita sari kādara bhayakārī..",
        "Struck by arrows, the warriors shrieked, reeling and falling everywhere on the ground. Blood streamed from their bodies like mighty waterfalls from mountains — a river of blood, terrifying to the cowardly."
    ),
    ("la-87-ch",): (
        "kādara bhayaṃkara rudhira saritā calī parama apāvanī.\ndou kūla dala ratha reta cakra abarta bahati bhayāvanī..\njala jaṃtugaja padacara turaga khara bibidha bāhana ko gane.\nsara sakti tomara sarpa cāpa taraṃga carma kamaṭha ghane..",
        "A terrifying river of blood flowed, most impure and frightful. The two armies formed its banks, chariots its sand, and whirlpools its eddies. Its waters were elephants, foot soldiers, horses, and donkeys — who could count the various vehicles? Arrows, spears, and lances were its serpents; bows its waves; shields its turtles — all crowded together."
    ),
    ("la-87-d",): (
        "bīra parahi janu tīra taru majjā bahu baha phena.\nkādara dekhi ḍarahi tahaṃ subhaṭanha ke mana cena..87..",
        "Fallen warriors were like trees along its banks; marrow was its foam. The cowardly trembled at the sight, but the hearts of brave warriors were at ease."
    ),

    # === DOHA 88 ===
    ("la-88-c1",): (
        "majjahi bhūta pisāca betālā. pramatha mahā jhoṭiṃga karālā..\nkāka kaṃka lai bhujā uḍāhīṃ. eka te chīni eka lai khāhīṃ..",
        "Ghosts, goblins, vampires, and terrible fiends bathed in that river. Crows and herons flew off carrying arms; snatching from one another, they feasted."
    ),
    ("la-88-c2",): (
        "eka kahahi aisiū sauṃghāī. saṭhahu tumhāra daridra na jāī..\nkahaṃrata bhaṭa ghāyala taṭa gire. jahaṃ tahaṃ manahuṃ ardhajala pare..",
        "'Even with such abundance, you fools, your poverty won't end!' they said. Wounded warriors lay fallen on the banks here and there, like half-submerged logs."
    ),
    ("la-88-c3",): (
        "khaiṃcahi gīdha āṃta taṭa bhae. janu baṃsī khelata cita dae..\nbahu bhaṭa bahahi caḍhe khaga jāhīṃ. janu nāvari khelahi sari māhīṃ..",
        "Vultures on the banks pulled out entrails as if fishing with lines, absorbed in the sport. Many warriors floated downstream with birds riding on them, as if boating on the river."
    ),
    ("la-88-c4",): (
        "jogini bhari bhari khappara saṃcahi. bhūta pisāca badhū nabha naṃcahīṃ..\nbhaṭa kapāla karatāla bajāvahi. cāmuṃḍā nānā bidhi gāvahi..",
        "Yoginis filled their skull-bowls again and again, hoarding blood. Demonesses danced in the sky. Warrior skulls served as cymbals, and Chamundas sang in many ways."
    ),
    ("la-88-c5",): (
        "jaṃbuka nikara kaṭakkaṭa kaṭṭahi. khāhi huāhi aghāhi dapaṭṭahi..\nkoṭinha ruṃḍa muṃḍa binu ḍollahi. sīsa pare mahi jaya jaya bollahi..",
        "Packs of jackals gnawed on bones; they ate, howled, gorged, and snarled. Millions of headless trunks rolled about, while severed heads lying on the ground cried: 'Victory! Victory!'"
    ),
    ("la-88-ch",): (
        "bollahi jo jaya jaya muṃḍa ruṃḍa pracaṃḍa sira binu dhāvahīṃ.\nkhapparinhi khagga alujjhi jujjhahi subhaṭa bhaṭanhi ḍhahāvahīṃ..\nbānara nisācara nikara mardahi rāma bala darpita bhae.\nsaṃgrāma aṃgana subhaṭa sovahi rāma sara nikaranhi hae..",
        "Severed heads cried 'Victory! Victory!' while headless mighty trunks charged on. With skull-shields and swords they fought on furiously, toppling other warriors. Monkeys, emboldened by Rama's strength, crushed hordes of demons. Champions slept forever on the battlefield, slain by Rama's arrows."
    ),
    ("la-88-d",): (
        "rāvana hṛdayaṃ bicārā bhā nisicara saṃghāra.\nmaiṃ akelā kapi bhālu bahu māyā karauṃ apāra..88..",
        "Ravana pondered in his heart: 'My demons have been annihilated. I am alone against many monkeys and bears — I shall employ boundless sorcery.'"
    ),

    # === DOHA 89 ===
    ("la-89-c1",): (
        "devanha prabhuhi payādeṃ dekhā. upajā ura ati chobha bisēṣā..\nsurapati nija ratha turata paṭhāvā. haraṣa sahita mātalī lai āvā..",
        "The gods saw the Lord on foot and felt great distress in their hearts. Indra immediately sent his own chariot, and Matali joyfully brought it."
    ),
    ("la-89-c2",): (
        "teja puṃja ratha dibya anūpā. haraṣi caḍhe kosalapura bhūpā..\ncaṃcala turaga manohara cārī. ajara amara mana sama gatikārī..",
        "The chariot was a mass of radiance, divine and incomparable. The king of Ayodhya joyfully mounted it. Its four beautiful, spirited horses were ageless, immortal, and swift as thought."
    ),
    ("la-89-c3",): (
        "rathārūḍha raghunāthahi dekhī. dhāe kapi balu pāi bisēṣī..\nsahī na jāi kapinhi kai mārī. taba rāvana māyā bistārī..",
        "Seeing Raghunath mounted on the chariot, the monkeys charged with renewed vigor. Unable to endure the monkeys' onslaught, Ravana then spread his sorcery."
    ),
    ("la-89-c4",): (
        "so māyā raghubīrahi bāṃcī. lachimanakapi nha so mānī sāṃcī..\ndekhī kapinha nisācara anī. anuja sahita bahu kosaladhanī..",
        "That sorcery did not fool Raghubir, but Lakshmana and the monkeys took it as real. The monkeys saw in the demon army many forms of the Lord of Kosala along with his brother."
    ),
    ("la-89-ch",): (
        "bahu rāma lachimana dekhi markaṭa bhālu mana ati apaḍare.\njanu citra likhita sameta lachimana jahaṃ so tahaṃ citavahi khare..\nnija sena cakita biloki haṃsi sara cāpa saji kosala dhanī.\nmāyā harī hari nimiṣa mahuṃ haraṣī sakala markaṭa anī..",
        "Seeing many Ramas and Lakshmanas, the monkeys and bears were terrified. Like painted pictures, they stood frozen, staring wherever they saw a Rama and Lakshmana. Seeing his own army bewildered, the Lord of Kosala smiled, readied his bow and arrows, and in the blink of an eye, Hari destroyed the sorcery. The entire monkey army rejoiced."
    ),
    ("la-89-d",): (
        "bahuri rāma saba tana citai bole bacana gaṃbhīra.\ndvaṃdajuddha dekhahu sakala śramita bhae ati bīra..89..",
        "Then Rama surveyed all his warriors and spoke in a solemn voice: 'All you mighty heroes are weary. Now watch this single combat!'"
    ),

    # === DOHA 90 ===
    ("la-90-c1",): (
        "asa kahi ratha raghunātha calāvā. bipra carana paṃkaja siru nāvā..\ntaba laṃkesa krodha ura chāvā. garjata tarjata sanmukha dhāvā..",
        "So saying, Raghunath drove his chariot forward, first bowing his head at the lotus feet of the Brahmins. Then the lord of Lanka, fury filling his heart, charged forward roaring and threatening."
    ),
    ("la-90-c2",): (
        "jītehu je bhaṭa saṃjuga māhīṃ. sunu tāpasa maiṃ tinha sama nāhīṃ..\nrāvana nāma jagata jasa jānā. lokapajā keṃ baṃdīkhānā..",
        "'Those warriors you defeated in battle — hear me, O ascetic, I am not like them! My name is Ravana, famous throughout the world. The guardians of the directions are prisoners in my dungeon.'"
    ),
    ("la-90-c3",): (
        "khara dūṣana birādha tumha mārā. badhehu byādha iva bāli bicārā..\nnisicara nikara subhaṭa saṃghārehu. kuṃbhakarana ghananādahi mārehu..",
        "'You killed Khara, Dushana, and Viradha. You slew poor Vali like a hunter. You destroyed hosts of demon champions and killed Kumbhakarna and Meghnad.'"
    ),
    ("la-90-c4",): (
        "āju bayaru sabu leuṃ nibāhī. jauṃ rana bhūpa bhāji nahiṃ jāhīṃ..\nāju karauṃ khalu kāla havāle. parehu kaṭhina rāvana ke pāle..",
        "'Today I shall settle all scores — if you do not flee from the battle, O king! Today I shall consign you to Death, wretch. You have fallen into the clutches of the terrible Ravana!'"
    ),
    ("la-90-c5",): (
        "suni durbacana kālabasa jānā. bihaṃsi bacana kaha kṛpānidhānā..\nsatya satya saba tava prabhutāī. jalpasi jani dekhāu manusāī..",
        "Hearing these harsh words and knowing Ravana to be under the sway of Death, the treasury of mercy smiled and said: 'True, true — all your glory is real. But stop boasting and show your valor in action.'"
    ),
    ("la-90-ch",): (
        "jani jalpanā kari sujasu nāsahi nīti sunahi karahi chamā.\nsaṃsāra mahaṃ pūruṣa tribidha pāṭala rasāla panasa samā..\neka sumanaprada eka sumana phala eka phalai kevala lāgahīṃ.\neka kahahi kahahi karahi apara eka karahi kahata na bāgahīṃ..",
        "'Do not destroy your fair name through idle boasting. Hear wisdom and practice forbearance. In this world there are three kinds of men — like the magnolia, the mango, and the jackfruit. One gives only flowers, another gives flowers and fruit, and one gives only fruit. One kind only talks, another talks and acts, and a third acts without talking at all.'"
    ),
    ("la-90-d",): (
        "rāma bacana suni bihaṃsā mohi sikhāvata gyāna.\nbayaru karata nahiṃ taba ḍare aba lāge priya prāna..90..",
        "Hearing Rama's words, Ravana laughed: 'You dare teach me wisdom? When you made enmity with me, you had no fear — but now your life has become dear to you!'"
    ),

    # === DOHA 91 ===
    ("la-91-c1",): (
        "kahi durbacana kruddha dasakaṃdhara. kulisa samāna lāga chāṃḍai sara..\nnānākāra silīmukha dhāe. disi aru bidisi gagana mahi chāe..",
        "Uttering harsh words, the enraged Ravana began releasing arrows hard as thunderbolts. Arrows of many kinds flew forth, covering the sky, earth, and every direction."
    ),
    ("la-91-c2",): (
        "pāvaka sara chāṃḍeu raghubīrā. chana mahuṃ jare nisācara tīrā..\nchāḍisi tībra sakti khisiāī. bāna saṃga prabhu pheri calāī..",
        "Raghubir released a fire-arrow, and in an instant all the demon's shafts were burned. Ravana angrily hurled a fierce spear, but the Lord sent it back with his own arrow."
    ),
    ("la-91-c3",): (
        "koṭika cakra trisūla pabārai. binu prayāsa prabhu kāṭi nivārai..\nniphala hohi rāvana sara kaisēṃ. khala ke sakala manoratha jaisēṃ..",
        "Ravana hurled millions of discuses and tridents, but the Lord cut them down effortlessly. Ravana's arrows became fruitless, just as all the desires of a wicked person come to nothing."
    ),
    ("la-91-c4",): (
        "taba sata bāna sārathī māresi. pareu bhūmi jaya rāma pukāresi..\nrāma kṛpā kari sūta uṭhāvā. taba prabhu parama krodha kahuṃ pāvā..",
        "Then Rama struck the charioteer with a hundred arrows. He fell to the ground crying 'Victory to Rama!' Rama mercifully revived the charioteer. Then the Lord was seized with supreme anger."
    ),
    ("la-91-ch",): (
        "bhae kruddha juddha biruddha raghupati trona sāyaka kasamase.\nkodaṃḍa dhuni ati caṃḍa suni manujāda saba māruta grase..\nmaṃdodarī ura kaṃpa kaṃpati kamaṭha bhū bhūdhara trase.\ncikkarahi diggaja dasana gahi mahi dekhi kautuka sura haṃse..",
        "Enraged in battle, Raghupati's quiver and arrows trembled with eagerness. Hearing the terrible twang of his bow, all the demons were paralyzed with fear. Mandodari's heart trembled; the cosmic tortoise, the earth, and the mountains shook. The elephants of the quarters trumpeted, gripping the earth with their teeth. Seeing this spectacle, the gods laughed with delight."
    ),
    ("la-91-d",): (
        "tāneu cāpa śravana lagi chāṃḍe bisikha karāla.\nrāma māragana gana cale lahalahāta janu byāla..91..",
        "Rama drew his bow to his ear and released terrible arrows. Rama's shafts sped forth, writhing like serpents."
    ),

    # === DOHA 92 ===
    ("la-92-c1",): (
        "cale bāna sapaccha janu uragā. prathamahi hateu sārathī turagā..\nratha bibhaṃji hati ketu patākā. garjā ati aṃtara bala thākā..",
        "The arrows flew like winged serpents. First they slew the charioteer and horses. They shattered the chariot and struck down the banner and flag. Ravana roared, but inwardly his strength was spent."
    ),
    ("la-92-c2",): (
        "turata āna ratha caḍhi khisiānā. astra sastra chāṃḍesi bidhi nānā..\nbiphala hohi saba udyama tāke. jimi paradroha nirata manasā ke..",
        "He quickly mounted another chariot, infuriated, and discharged weapons and missiles of many kinds. But all his efforts proved futile — like the schemes of one absorbed in harming others."
    ),
    ("la-92-c3",): (
        "taba rāvana dasa sūla calāvā. bāji cāri mahi māri girāvā..\nturaga uṭhāi kopi raghunāyaka. khaiṃci sarāsana chāṃḍe sāyaka..",
        "Then Ravana hurled ten tridents and struck down the four horses to the ground. Raghunayak raised the horses back up and, full of wrath, drew his bow and released his arrows."
    ),
    ("la-92-c4",): (
        "rāvana sira saroja banacārī. cali raghubīra silīmukha dhārī..\ndasa dasa bāna bhāla dasa māre. nisari gae cale rudhira panāre..",
        "Raghubir's arrows sped forth like bees visiting the lotuses of Ravana's heads. He shot ten arrows into each of the ten foreheads. They pierced through and emerged, streaming with blood."
    ),
    ("la-92-c5",): (
        "stravata rudhira dhāyau balavānā. prabhu puni kṛta dhanu sara saṃdhānā..\ntīsa tīra raghubīra pabāre. bhujanha sameta sīsa mahi pāre..",
        "Streaming with blood, the mighty Ravana charged. The Lord fitted arrows to his bow once more. Raghubir released thirty arrows and sent the heads along with the arms crashing to the ground."
    ),
    ("la-92-c6",): (
        "kāṭatahīṃ puni bhae nabīne. rāma bahori bhujā sira chīne..\nprabhu bahu bāra bāhu sira hae. kaṭata jhaṭiti puni nūtana bhae..",
        "No sooner were they cut than they grew back new. Rama again severed the arms and heads. The Lord cut them many times, but they instantly grew back anew."
    ),
    ("la-92-c7",): (
        "puni puni prabhu kāṭata bhuja sīsā. ati kautukī kosalādhīsā..\nrahe chāi nabha sira aru bāhū. mānahuṃ amita ketu aru rāhū..",
        "Again and again the Lord cut the arms and heads — the king of Kosala was most playful. The sky was covered with heads and arms, as if there were countless Ketus and Rahus."
    ),
    ("la-92-ch",): (
        "janu rāhu ketu aneka nabha patha stravata sonita dhāvahīṃ.\nraghubīra tīra pracaṃḍa lāgahi bhūmi girana na pāvahīṃ..\neka eka sara sira nikara chede nabha uḍata imi sohahīṃ.\njanu kopi dinakara kara nikara jahaṃ tahaṃ bidhuntuda pohahīṃ..",
        "Like many Rahus and Ketus, heads streamed with blood as they flew through the sky. Struck by Raghubir's fierce arrows, they could not reach the ground. Each arrow severed clusters of heads, which flying through the sky looked splendid — as if the angry sun's rays were piercing Rahus in every direction."
    ),
    ("la-92-d",): (
        "jimi jimi prabhu hara tāsu sira timi timi hohi apāra.\nsevata biṣaya bibaradha jimi nita nita nūtana māra..92..",
        "The more the Lord cut his heads, the more they multiplied without end — like the ever-new torments of worldly pleasures that increase the more one indulges them."
    ),

    # === DOHA 93 ===
    ("la-93-c1",): (
        "dasamukha dekhi siranhi kai bāḍhī. bisarā marana bhaī risa gāḍhī..\ngarjeu mūḍha mahā abhimānī. dhāyau dasahu sarāsana tānī..",
        "Seeing his heads multiply, Ravana forgot about death and was filled with deep rage. The fool, full of supreme arrogance, roared and charged with all ten bows drawn."
    ),
    ("la-93-c2",): (
        "samara bhūmi dasakaṃdhara kopyau. baraṣi bāna raghupati ratha topyau..\ndaṃḍa eka ratha dekhi na pareū. janu nihāra mahuṃ dinakara dureū..",
        "On the battlefield, the enraged Ravana showered arrows and covered Rama's chariot. For a moment the chariot could not be seen — as if the sun were hidden in mist."
    ),
    ("la-93-c3",): (
        "hāhākāra suranha jaba kīnhā. taba prabhu kopi kāramuka līnhā..\nsara nivāri ripu ke sira kāṭe. te disi bidisi gagana mahi pāṭe..",
        "When the gods raised a cry of alarm, the Lord angrily took up his bow. He warded off the enemy's shafts and cut his heads, which were scattered in every direction across the sky and earth."
    ),
    ("la-93-c4",): (
        "kāṭe sira nabha māraga dhāvahi. jaya jaya dhuni kari bhaya upajāvahi..\nkahaṃ lachimana sugrīva kapīsā. kahaṃ raghubīra kosalādhīsā..",
        "The severed heads flew through the sky, crying 'Victory! Victory!' and striking terror. They called out: 'Where is Lakshmana? Where is Sugriva, king of monkeys? Where is Raghubir, lord of Kosala?'"
    ),
    ("la-93-ch",): (
        "kahaṃ rāmu kahi sira nikara dhāe dekhi markaṭa bhaji cale.\nsaṃdhāni dhanu raghubaṃsamani haṃsi saranha sira bedhe bhale..\nsira mālikā kara kālikā gahi bṛṃda bṛṃdanhi bahu milīṃ.\nkari rudhira sari majjanu manahuṃ saṃgrāma baṭa pūjana calīṃ..",
        "Shouting 'Where is Rama?', clusters of heads charged. Seeing this, monkeys fled. The jewel of Raghu's race smiled, drew his bow, and pierced the heads well with his arrows. Kali goddesses gathered the heads into garlands, assembled in groups, and bathed in the river of blood — as if going to worship the Banyan tree of battle."
    ),
    ("la-93-d",): (
        "puni dasakaṃṭha kruddha hoi chāṃḍī sakti pracaṃḍa.\ncalī bibhīṣana sanmukha manahuṃ kāla kara daṃḍa..93..",
        "Then the furious ten-headed Ravana hurled a terrible spear that flew toward Vibhishana — like the rod of Death himself."
    ),

    # === DOHA 94 ===
    ("la-94-c1",): (
        "āvata dekhi sakti ati ghorā. pranatārti bhaṃjana pana morā..\nturata bibhīṣana pācheṃ melā. sanmukha rāma saheu soi selā..",
        "Seeing the dreadful spear approaching, Rama said: 'My vow is to destroy the suffering of those who seek refuge in me.' He instantly placed Vibhishana behind him and himself faced and received that spear."
    ),
    ("la-94-c2",): (
        "lāgi sakti muruchā kachu bhaī. prabhu kṛta khela suranha bikalāī..\ndekhi bibhīṣana prabhu śrama pāyau. gahi kara gadā kruddha hoi dhāyau..",
        "The spear struck and the Lord feigned a brief swoon — a mere sport, though it distressed the gods. Seeing the Lord in pain, Vibhishana seized his mace and charged in fury."
    ),
    ("la-94-c3",): (
        "re kubhāgya saṭha maṃda kubuddhe. taiṃ sura nara muni nāga biruddhe..\nsādara siva kahuṃ sīsa caḍhāe. eka eka ke koṭinhi pāe..",
        "'O wretched fool, dull-witted and evil-minded! You have warred against gods, men, sages, and serpent-kings. You devotedly offered your heads to Shiva and received millions of boons for each one.'"
    ),
    ("la-94-c4",): (
        "tehi kārana khala aba lagi bāṃcyau. aba tava kālu sīsa para nācyau..\nrāma bimukha saṭha cahasi saṃpadā. asa kahi hanesi mājha ura gadā..",
        "'That is why, wretch, you have survived till now. But now Death dances upon your head. Fool, you turn away from Rama yet crave prosperity!' So saying, Vibhishana struck him on the chest with his mace."
    ),
    ("la-94-ch",): (
        "ura mājha gadā prahāra ghora kaṭhora lāgata mahi par yau.\ndasa badana sonita stravata puni saṃbhāri dhāyau risa bhar yau..\ndvau bhire atibala mallajuddha biruddha eku ekahi hanai.\nraghubīra bala darpita bibhīṣanu ghāli nahiṃ tā kahuṃ ganai..",
        "The fierce mace-blow struck him hard on the chest and he fell to the ground. Blood streamed from his ten mouths. He recovered and charged again, filled with rage. The two clashed in a mighty wrestling match, each striking the other. Vibhishana, emboldened by Raghubir's strength, struck repeatedly without fear."
    ),
    ("la-94-d",): (
        "umā bibhīṣanu rāvanahi sanmukha citava ki kāu.\nso aba bhirata kāla jyoṃ śrīraghubīra prabhāu..94..",
        "O Uma, would Vibhishana ever dare look Ravana in the face? Yet now he fought him like Death itself — such is the power of Shri Raghubir!"
    ),

    # === DOHA 95 ===
    ("la-95-c1",): (
        "dekhā śramita bibhīṣanu bhārī. dhāyau hanūmāna giri dhārī..\nratha turaṃga sārathī nipātā. hṛdaya mājha tehi māresi lātā..",
        "Seeing Vibhishana greatly exhausted, Hanuman rushed forward bearing a mountain. He demolished the chariot, horses, and charioteer, and kicked Ravana hard in the chest."
    ),
    ("la-95-c2",): (
        "ṭhāḍha rahā ati kaṃpita gātā. gayau bibhīṣanu jahaṃ janatrātā..\npuni rāvana kapi hateu pacārī. caleu gagana kapi pūṃcha pasārī..",
        "Ravana stood trembling in every limb. Vibhishana retreated to where the protector of devotees stood. Then Ravana struck the monkey with a challenge. Hanuman soared into the sky with his tail outstretched."
    ),
    ("la-95-c3",): (
        "gahisi pūṃcha kapi sahita uḍānā. puni phiri bhireu prabala hanumānā..\nlarata akāsa jugala sama jodhā. ekahi eku hanata kari krodhā..",
        "Ravana grabbed his tail, but the monkey flew up carrying him. Then the mighty Hanuman turned and grappled again. The two equally matched warriors fought in the sky, each striking the other in fury."
    ),
    ("la-95-c4",): (
        "sohahi nabha chala bala bahu karahīṃ. kajjala giri sumeru janu larahīṃ..\nbudhi bala nisicara parai na pār yau. taba māruta suta prabhu saṃbhār yau..",
        "They looked splendid in the sky, employing many tricks and feats of strength — as if Mount Kailash and Mount Sumeru were fighting. When the demon could not be overcome by wit or strength, Hanuman remembered his Lord."
    ),
    ("la-95-ch",): (
        "saṃbhāri śrīraghubīra dhīra pacāri kapi rāvanu hanyau.\nmahi parata puni uṭhi larata devanha jugala kahuṃ jaya jaya bhanyau..\nhanumaṃta saṃkaṭa dekhi markaṭa bhālu krodhātura cale.\nrana matta rāvana sakala subhaṭa pracaṃḍa bhuja bala dalamale..",
        "Remembering Shri Raghubir, the steadfast Hanuman challenged and struck Ravana, who fell to earth but rose again to fight. The gods cried 'Victory!' to both. Seeing Hanuman in danger, monkeys and bears rushed forward in anger. But the battle-drunk Ravana crushed all the mighty champions with the strength of his arms."
    ),
    ("la-95-d",): (
        "taba raghubīra pacāre dhāe kīsa pracaṃḍa.\nkapi bala prabala dekhi tehi kīnha pragaṭa pāṣaṃḍa..95..",
        "Then at Raghubir's command, fierce monkeys charged forward. Seeing the monkeys' overwhelming strength, Ravana resorted to open sorcery."
    ),

    # === DOHA 96 ===
    ("la-96-c1",): (
        "aṃtaradhāna bhayau chana ekā. puni pragaṭe khala rūpa anekā..\nraghupati kaṭaka bhālu kapi jete. jahaṃ tahaṃ pragaṭa dasānana tete..",
        "Ravana vanished for an instant. Then the villain appeared in countless forms — as many Ravanas as there were bears and monkeys in Rama's army, he manifested everywhere."
    ),
    ("la-96-c2",): (
        "dekhe kapinha amita dasasīsā. jahaṃ tahaṃ bhaje bhālu aru kīsā..\nbhāge bānara dharahi na dhīrā. trāhi trāhi lachimana raghubīrā..",
        "The monkeys saw countless ten-headed Ravanas everywhere. Bears and monkeys fled in all directions. The monkeys ran without courage, crying: 'Save us! Save us, Lakshmana! Raghubir!'"
    ),
    ("la-96-c3",): (
        "dahaṃ disi dhāvahi koṭinha rāvana. garjahi ghora kaṭhora bhayāvana..\nḍare sakala sura cale parāī. jaya kai āsa tajahu aba bhāī..",
        "Millions of Ravanas rushed in all ten directions, roaring fiercely and terrifyingly. All the gods were frightened and began to flee: 'Abandon hope of victory now, brothers!'"
    ),
    ("la-96-c4",): (
        "saba sura jīte eka dasakaṃdhara. aba bahu bhae takahu giri kaṃdara..\nrahe biraṃci saṃbhu muni gyānī. jinha jinha prabhu mahimā kachu jānī..",
        "'Even one Ravana conquered all the gods — now there are many! Seek refuge in mountain caves!' Only Brahma, Shambhu, and the wise sages remained — those who knew something of the Lord's glory."
    ),
    ("la-96-ch",): (
        "jānā pratāpa te rahe nirbhaya kapinhi ripu māne phure.\ncale bicali markaṭa bhālu sakala kṛpāla pāhi bhayāture..\nhanumaṃta aṃgada nīla nala atibala larata rana bāṃkure.\nmardahi dasānana koṭi koṭinha kapaṭa bhū bhaṭa aṃkure..",
        "Those who knew the Lord's power remained fearless. The monkeys believed the enemies to be real. Monkeys and bears all wavered and cried in terror: 'O merciful Lord, protect us!' But Hanuman, Angad, Nila, Nala, and other mighty warriors fought on valiantly, crushing millions upon millions of the illusory demon warriors."
    ),
    ("la-96-d",): (
        "sura bānara dekhe bikala haṃsyau kosalādhīsa.\nsaji sāraṃga eka sara hate sakala dasasīsa..96..",
        "Seeing the gods and monkeys distressed, the king of Kosala smiled. Drawing his bow Sharanga, with a single arrow he destroyed all the illusory Ravanas."
    ),

    # === DOHA 97 ===
    ("la-97-c1",): (
        "prabhu chana mahuṃ māyā saba kāṭī. jimi rabi ueṃ jāhi tama phāṭī..\nrāvanu eku dekhi sura haraṣe. phire sumana bahu prabhu para baraṣe..",
        "The Lord destroyed all the sorcery in an instant — as darkness vanishes when the sun rises. Seeing only one Ravana remaining, the gods rejoiced and showered abundant flowers on the Lord."
    ),
    ("la-97-c2",): (
        "bhuja uṭhāi raghupati kapi phere. phire eka ekanha taba ṭere..\nprabhu balu pāi bhālu kapi dhāe. tarala tamaki saṃjuga mahi āe..",
        "Raghupati raised his arm and rallied the monkeys. They returned, calling out to one another. Strengthened by the Lord's power, bears and monkeys charged, rushing fiercely back into the battlefield."
    ),
    ("la-97-c3",): (
        "astuti karata devatanhi dekheṃ. bhayauṃ eka maiṃ inha ke lekheṃ..\nsaṭhahu sadā tumha mora marāyala. asa kahi kopi gagana para dhāyala..",
        "Seeing the gods praising Rama, Ravana thought: 'So in their reckoning I have become just one again!' He said: 'Fools! You are always getting killed by me!' So saying, he angrily rushed up to the sky."
    ),
    ("la-97-c4",): (
        "hāhākāra karata sura bhāge. khalahu jāhu kahaṃ moreṃ āge..\ndekhi bikala sura aṃgada dhāyau. kūdi carana gahi bhūmi girāyau..",
        "The gods fled crying out in alarm. 'Where will you go, fools, from before me?' But seeing the gods in distress, Angad leaped up, seized Ravana's feet, and threw him to the ground."
    ),
    ("la-97-ch",): (
        "gahi bhūmi pār yau lāta mār yau bālisuta prabhu pahi gayau.\nsaṃbhāri uṭhi dasakaṃṭha ghora kaṭhora rava garjata bhayau..\nkari dāpa cāpa caḍhāi dasa saṃdhāni sara bahu baraṣaī.\nkie sakala bhaṭa ghāyala bhayākula dekhi nija bala haraṣaī..",
        "He seized him, threw him to the ground, and kicked him. Then Angad (Vali's son) returned to the Lord. Ravana recovered, rose, and roared with a terrible, harsh sound. Boasting, he drew all ten bows, fitted arrows, and released a torrent. He wounded all the warriors and made them fearful; seeing his own prowess, he rejoiced."
    ),
    ("la-97-d",): (
        "taba raghupati rāvana ke sīsa bhujā sara cāpa.\nkāṭe bahuta baḍhe puni jimi tīratha kara pāpa..97..",
        "Then Raghupati cut Ravana's heads, arms, arrows, and bows — but they grew back in profusion, like sins committed at a holy place."
    ),

    # === DOHA 98 ===
    ("la-98-c1",): (
        "sira bhuja bāḍhi dekhi ripu kerī. bhālu kapinha risa bhaī ghanerī..\nmarai na mūḍha kaṭeu bhuja sīsā. dhāe kopi bhālu bhaṭa kīsā..",
        "Seeing the enemy's heads and arms keep multiplying, the bears and monkeys were filled with great anger. 'The fool does not die though his arms and heads are cut!' The bears and monkey warriors charged in fury."
    ),
    ("la-98-c2",): (
        "bālitanaya māruti nala nīlā. bānarar āja dubida balasīlā..\nbiṭapa mahīdhara karahi prahārā. soi giri taru gahi kapinha so mārā..",
        "Angad (Vali's son), Hanuman, Nala, Nila, the monkey king Sugriva, and Jambavan — mighty in strength — struck with trees and mountains. But Ravana seized those same mountains and trees and hurled them back at the monkeys."
    ),
    ("la-98-c3",): (
        "eka nakhanhi ripu bapuṣa bidārī. bhagicale hi eka lātanhi mārī..\ntaba nala nīla siranhi caḍhi gayaū. nakhanhi lilāra bidārata bhayaū..",
        "Some monkeys tore the enemy's body with their nails; others kicked him and ran away. Then Nala and Nila climbed onto his heads and began tearing his foreheads with their nails."
    ),
    ("la-98-c4",): (
        "rudhira dekhi biṣāda ura bhārī. tinhahi dharana kahuṃ bhujā pasārī..\ngahe na jāhi karanha para phirahīṃ. janu juga madhupa kamala bana carahīṃ..",
        "Seeing blood, Ravana felt deep dismay. He stretched out his arms to catch them, but they could not be caught — they kept darting over his hands, like a pair of bees flitting about in a lotus garden."
    ),
    ("la-98-c5",): (
        "kopi kūdi dvau dharesi bahorī. mahi paṭakata bhaje bhujā marorī..\npuni sakopa dasa dhanu kara līnhe. saranha māri ghāyala kapi kīnhe..",
        "In anger he leaped and seized them both. He dashed them to the ground and they fled with twisted arms. Then in rage Ravana took ten bows in hand and wounded the monkeys with his arrows."
    ),
    ("la-98-c6",): (
        "hanumadādi muruchita kari baṃdara. pāi pradoṣa haraṣa dasakaṃdhara..\nmuruchita dekhi sakala kapi bīrā. jāmavaṃta dhāyau ranadhīrā..",
        "Having rendered Hanuman and other monkeys unconscious, Ravana rejoiced as evening fell. Seeing all the monkey heroes unconscious, Jambavan, steady in battle, charged forward."
    ),
    ("la-98-c7",): (
        "saṃga bhālu bhūdhara taru dhārī. mārana lage pacāri pacārī..\nbhayau kruddha rāvana balavānā. gahi pada mahi paṭakai bhaṭa nānā..",
        "Accompanied by bears carrying mountains and trees, he began striking Ravana with fierce challenges. The mighty Ravana grew furious and, seizing warriors by the feet, dashed them to the ground."
    ),
    ("la-98-c8",): (
        "dekhi bhālupati nija dala ghātā. kopi mājha ura māresi lātā..",
        "Seeing his own army being destroyed, Jambavan (the bear chief) angrily kicked Ravana hard in the chest."
    ),
    ("la-98-ch",): (
        "ura lāta ghāta pracaṃḍa lāgata bikala ratha te mahi parā.\ngahi bhālu bīsahuṃ kara manahuṃ kamalanhi base nisi madhukara..\nmuruchita biloki bahori pada hati bhālupati prabhu pahi gayau.\nnisi jāni syaṃdana ghāli tehi taba sūta jatanu karata bhayau..",
        "The fierce kick struck his chest and he fell dazed from his chariot to the ground. He grabbed the bear with all twenty hands — like bees settling on lotuses at night. Seeing him unconscious, Jambavan kicked him again and went back to the Lord. Recognizing it was night, the charioteer placed Ravana in his chariot and began tending to him."
    ),
    ("la-98-d",): (
        "muruchā bigata bhālu kapi saba āe prabhu pāsa.\nnisicara sakala rāvanahi gheri rahe ati trāsa..98..",
        "Recovering from their swoons, all the bears and monkeys came to the Lord. Meanwhile all the demons surrounded Ravana, filled with great fear."
    ),

    # === DOHA 99 ===
    ("la-99-c1",): (
        "tehī nisi sītā pahi jāī. trijaṭā kahi saba kathā sunāī..\nsira bhuja bāḍhi sunata ripu kerī. sītā ura bhai trāsa ghanerī..",
        "That very night, Trijata went to Sita and narrated the entire story. Hearing that the enemy's heads and arms kept growing back, Sita's heart was filled with great fear."
    ),
    ("la-99-c2",): (
        "mukha malīna upajī mana ciṃtā. trijaṭā sana bolī taba sītā..\nhoihi kahā kahasi kina mātā. kehi bidhi marihi bisva dukhad ātā..",
        "Her face grew pale and worry arose in her mind. Then Sita spoke to Trijata: 'What will happen? Why don't you tell me, mother? How will this tormentor of the world be killed?'"
    ),
    ("la-99-c3",): (
        "raghupati sara sira kaṭehuṃ na maraī. bidhi biparīta carita saba karaī..\nmora abhāgya jiāvata ohī. jehi hau hari pada kamala bichohī..",
        "'Rama's arrows cut his heads but he does not die. Fate does everything in reverse. My ill fortune keeps him alive — he who has separated me from the lotus feet of my Lord.'"
    ),
    ("la-99-c4",): (
        "jehi kṛta kapaṭa kanaka mṛga jhūṭhā. ajahuṃ so daiva mohi para rūṭhā..\njehi bidhi mohi dukha dusaha sahāe. lachimana kahuṃ kaṭu bacana kahāe..",
        "'The fate that created the false golden deer is still angry with me. The destiny that made me suffer unbearable sorrow and forced me to speak harsh words to Lakshmana—'"
    ),
    ("la-99-c5",): (
        "raghupati biraha sabiṣa sara bhārī. taki taki māra bāra bahu mārī..\naisēhuṃ dukha jo rākha mama prānā. soi bidhi tāhi jiāva na ānā..",
        "'Separation from Rama has struck me like heavy poisoned arrows, aimed and shot again and again. Yet the fate that preserved my life through even such agony — that same fate keeps Ravana alive!'"
    ),
    ("la-99-c6",): (
        "bahu bidhi kara bilāpa jānakī. kari kari surati kṛpānidhāna kī..\nkaha trijaṭā sunu rājakumārī. ura sara lāgata marai surārī..",
        "Janaki lamented in many ways, remembering the treasury of mercy again and again. Trijata said: 'Listen, O princess — the enemy of the gods can only die when an arrow strikes his heart.'"
    ),
    ("la-99-c7",): (
        "prabhu tāte ura hatai na tehī. ehi ke hṛdayaṃ basati baidehī..",
        "'The Lord therefore does not strike his heart, because you, Vaidehi, dwell in Ravana's heart.'"
    ),
    ("la-99-ch",): (
        "ehi ke hṛdayaṃ basa jānakī jānakī ura mama bāsa hai.\nmama udara bhuana aneka lāgata bāna saba kara nāsa hai..\nsuni bacana haraṣa biṣāda mana ati dekhi puni trijaṭāṃ kahā.\naba marihi ripu ehi bidhi sunahi suṃdari tajahi saṃsaya mahā..",
        "'In his heart dwells Janaki; in Janaki's heart is my abode. In my belly are countless worlds — if an arrow strikes there, all would be destroyed.' Hearing these words, Sita felt both joy and sorrow. Then seeing her state, Trijata spoke again: 'Now the enemy will die in this manner — listen, O beautiful one, and abandon your great doubt.'"
    ),
    ("la-99-d",): (
        "kāṭata sira hoihi bikala chuṭi jāihi tava dhyāna.\ntaba rāvanahi hṛdaya mahuṃ marihahi rāmu sujāna..99..",
        "'When his heads are being cut and he is dazed, his meditation on you will break. Then the wise Rama will strike Ravana in the heart and slay him.'"
    ),

    # === DOHA 100 ===
    ("la-100-c1",): (
        "asa kahi bahuta bhāṃti samujhāī. puni trijaṭā nija bhavana sidhāī..\nrāma subhāu sumiri baidehī. upajī biraha bithā ati tehī..",
        "So saying, Trijata consoled Sita in many ways and then returned to her own dwelling. Vaidehi remembered Rama's gentle nature, and intense pangs of separation arose in her heart."
    ),
    ("la-100-c2",): (
        "nisihi sasihi niṃdati bahu bhāṃtī. juga sama bhaī sirāti na rātī..\nkarati bilāpa manahi mana bhārī. rāma birahaṃ jānakī dukhārī..",
        "She blamed the night and the moon in many ways — the night seemed like an age and would not end. She lamented deeply within her heart, Janaki grieving in separation from Rama."
    ),
    ("la-100-c3",): (
        "jaba ati bhayau biraha ura dāhū. pharakeu bāma nayana aru bāhū..\nsaguna bicāri dharī mana dhīrā. aba milihahi kṛpāla raghubīrā..",
        "When the burning anguish of separation became extreme, her left eye and left arm throbbed. Reading this auspicious omen, she took heart: 'Now the merciful Raghubir will come to me.'"
    ),
    ("la-100-c4",): (
        "ihāṃ ardhanisi rāvanu jāgā. nija sārathi sana khījhana lāgā..\nsaṭha ranabhūmi chaḍāisi mohī. dhiga dhiga adhama maṃdamati tohī..",
        "Meanwhile, Ravana woke at midnight and began berating his charioteer: 'Fool, you removed me from the battlefield! Shame, shame on you, wretch — dull-witted one!'"
    ),
    ("la-100-c5",): (
        "tehi pada gahi bahu bidhi samujhāvā. bhauru bhaeṃ ratha caḍhi puni dhāvā..\nsuni āgavanu dasānana kerā. kapi dala kharabhara bhayau ghanerā..",
        "The charioteer clasped his feet and explained at length. At dawn, Ravana mounted his chariot and charged again. Hearing of Ravana's approach, a great commotion arose in the monkey army."
    ),
    ("la-100-c6",): (
        "jahaṃ tahaṃ bhūdhara biṭapa upārī. dhāe kaṭakaṭāi bhaṭa bhārī..",
        "The mighty warriors uprooted mountains and trees everywhere and charged, gnashing their teeth."
    ),
    ("la-100-ch",): (
        "dhāe jo markaṭa bikaṭa bhālu karāla kara bhūdhara dharā.\nati kopa karahi prahāra mārata bhaji cale rajanīcarā..\nbicalāi dala balavanta kīsanha gheri puni rāvanu liyau.\ncahuṃ disi capeṭanhi māri nakhanhi bidāri tanu byākula kiyau..",
        "Fearsome monkeys and terrible bears charged, carrying mountains in their hands. They struck with great fury, and the demons fled. The powerful monkeys routed the army and surrounded Ravana. From all four sides they struck with slaps and tore his body with their nails, leaving him bewildered."
    ),
    ("la-100-d",): (
        "dekhi mahā markaṭa prabala rāvana kīnha bicāra.\naṃtarahita hoi nimiṣa mahuṃ kṛta māyā bistāra..100..",
        "Seeing the great monkeys' overwhelming power, Ravana devised a plan. He vanished in an instant and spread his vast sorcery."
    ),

    # === DOHA 101 ===
    ("la-101-ch",): (
        "jaba kīnha tehi pāṣaṃḍa. bhae pragaṭa jaṃtu pracaṃḍa..\nbetāla bhūta pisāca. kara dhareṃ dhanu nārāca..1..\njogini gaheṃ karabāla. eka hātha manuja kapāla..\nkari sadya sonita pāna. nācahi karahi bahu gāna..2..\ndharu māru bolahi ghora. rahi pūri dhuni cahuṃ ora..\nmukha bāi dhāvahi khāna. taba lage kīsa parāna..3..\njahaṃ jāhi markaṭa bhāgi. tahaṃ barata dekhahi āgi..\nbhae bikala bānara bhālu. puni lāga baraṣai bālū..4..\njahaṃ tahaṃ thakita kari kīsa. garjeu bahuri dasasīsa..\nlachimana kapīsa sameta. bhae sakala bīra aceta..5..\nhā rāma hā raghunātha. kahi subhaṭa mījahi hātha..\nehi bidhi sakala bala tori. tehi kīnha kapaṭa bahori..6..\npragaṭesi bipula hanumāna. dhāe gahe pāṣāna..\ntinha rāmu ghere jāi. cahuṃ disi barūtha banāi..7..\nmārahu dharahu jani jāi. kaṭakaṭahi pūṃcha uṭhāi..\ndahaṃ disi laṃgūra birāja. tehi madhya kosalarāja..8..\ntehi madhya kosalarāja suṃdara syāma tana sobhā lahī.\njanu iṃdradhanuṣa aneka kī bara bāri tuṃga tamālahī..\nprabhu dekhi haraṣa biṣāda ura sura badata jaya jaya jaya karī.\nraghubīra ekahi tīra kopi nimeṣa mahuṃ māyā harī..1..\nmāyā bigata kapi bhālu haraṣe biṭapa giri gahi saba phire.\nsara nikara chāḍe rāma rāvana bāhu sira puni mahi gire..\nśrīrāma rāvana samara carita aneka kalpa jo gāvahīṃ.\nsata seṣa sārada nigama kabi teu tadapi pāra na pāvahīṃ..2..",
        "When Ravana performed his sorcery, terrible creatures appeared — vampires, ghosts, and goblins, armed with bows and arrows. Yoginis wielded swords, carrying human skulls in one hand, drinking fresh blood, dancing and singing. The dreadful cry 'Seize! Kill!' filled every direction. They ran open-mouthed to devour, and the monkeys began to flee. Wherever monkeys ran, they saw blazing fires. Monkeys and bears were distraught; then sand began to rain down. Having exhausted the monkeys everywhere, Ravana roared. Lakshmana, the monkey king, and all warriors fell unconscious. 'Alas Rama! Alas Raghunath!' cried the champions, wringing their hands. Having broken all resistance, Ravana then created another illusion — he manifested many forms of Hanuman that charged with boulders, surrounding Rama from all sides. 'Strike! Seize! Don't let him go!' they snarled with raised tails. Monkeys surrounded him on all sides, and in their midst stood the Lord of Kosala — his dark, beautiful body resplendent as a tall Tamala tree amid many splendid rainbows. Seeing the Lord, the gods felt both joy and fear, and they cried: 'Victory! Victory! Victory!' Raghubir in anger, with a single arrow, destroyed all the sorcery in the blink of an eye. With the sorcery gone, monkeys and bears rejoiced, seized trees and mountains, and rallied. Rama released a volley of arrows, and Ravana's arms and heads fell to the ground once more. The battle between Shri Rama and Ravana — even if a hundred Sheshas, Saraswatis, Vedas, and poets were to sing of it for many eons, they still could not reach its end."
    ),
    ("la-101-d",): (
        "tāke guna gana kachu kahe jaḍamati tulasīdāsa.\njimi nija bala anurūpa te māchī uḍai akāsa..101(ka)..\nkāṭe sira bhuja bāra bahu marata na bhaṭa laṃkesa.\nprabhu krīḍata sura siddha muni byākula dekhi kalesa..101(kha)..",
        "Of those infinite exploits, the dull-witted Tulsidas has told but a few — just as a fly soars in the sky only according to its own small strength. Though Rama cut Ravana's heads and arms many times, the lord of Lanka would not die. The Lord was merely sporting, but the gods, Siddhas, and sages were distressed seeing this torment."
    ),

    # === DOHA 102 ===
    ("la-102-c1",): (
        "kāṭata baḍhahi sīsa samudāī. jimi prati lābha lobha adhikāī..\nmarai na ripu śrama bhayau bisēṣā. rāma bibhīṣana tana taba dekhā..",
        "The heads kept multiplying when cut — like greed increasing with each gain. The enemy would not die; the Lord showed signs of exertion. Then Rama looked toward Vibhishana."
    ),
    ("la-102-c2",): (
        "umā kāla mara jākīṃ īchā. so prabhu jana kara prīti parīchā..\nsunu sarbagya carācara nāyaka. pranatapāla sura muni sukhadāyaka..",
        "O Uma, Death itself dies at whose wish — that Lord was merely testing his devotee's love. 'Listen, O omniscient one, Lord of all animate and inanimate creation, protector of the surrendered, giver of joy to gods and sages.'"
    ),
    ("la-102-c3",): (
        "nābhikuṃḍa piyūṣa basa yākeṃ. nātha jiata rāvanu bala tākeṃ..\nsunata bibhīṣana bacana kṛpālā. haraṣi gahe kara bāna karālā..",
        "'In the navel of this demon lies a pool of ambrosia, my Lord — by its power Ravana lives.' Hearing Vibhishana's words, the merciful Lord joyfully took up his terrible arrows."
    ),
    ("la-102-c4",): (
        "asubha hona lāge taba nānā. rovahi khara sṛkāla bahu svānā..\nbolahi khaga jaga ārati hetū. pragaṭa bhae nabha jahaṃ tahaṃ ketū..",
        "Then many inauspicious omens began to appear. Donkeys, jackals, and many dogs howled. Birds cried out foreboding the world's sorrow. Comets appeared in the sky in every direction."
    ),
    ("la-102-c5",): (
        "dasa disi dāha hona ati lāgā. bhayau paraba binu rabi uparāgā..\nmaṃdodarī ura kaṃpati bhārī. pratimā stravahi nayana maga bārī..",
        "Fires blazed in all ten directions. An eclipse of the sun occurred without any occasion. Mandodari's heart trembled greatly. Temple idols shed tears from their eyes."
    ),
    ("la-102-ch",): (
        "pratimā rudahi pabipāta nabha ati bāta baha ḍolati mahī.\nbaraṣahi balāhaka rudhira kaca raja asubha ati saka ko kahī..\nutapāta amita biloki nabha sura bikala bolahi jaya jae.\nsura sabhaya jāni kṛpāla raghupati cāpa sara jorata bhae..",
        "Idols wept, thunderbolts fell from the sky, fierce winds blew, and the earth shook. Clouds rained blood, hair, and dust — the inauspicious signs were beyond description. Seeing countless portents in the sky, the distressed gods cried: 'Victory! Victory!' Knowing the gods were afraid, the merciful Lord Raghupati began fitting arrows to his bow."
    ),
    ("la-102-d",): (
        "khaici sarāsana śravana lagi chāḍe sara ekatīsa.\nraghunāyaka sāyaka cale mānahuṃ kāla phanīsa..102..",
        "Drawing his bow to his ear, Rama released thirty-one arrows. The shafts of Raghunayak sped forth like the serpent-king of Death."
    ),

    # === DOHA 103 ===
    ("la-103-c1",): (
        "sāyaka eka nābhi sara soṣā. apara lage bhuja sira kari roṣā..\nlai sira bāhu cale nārācā. sira bhuja hīna ruṃḍa mahi nācā..",
        "One arrow dried up the pool of nectar in Ravana's navel. The others struck his arms and heads in fury. The arrows carried away the heads and arms. The headless, armless trunk danced on the earth."
    ),
    ("la-103-c2",): (
        "dharani dhasai dhara dhāva pracaṃḍā. taba sara hati prabhu kṛta dui khaṃḍā..\ngarjeu marata ghora rava bhārī. kahāṃ rāmu rana hatauṃ pacārī..",
        "The trunk crashed into the earth as it ran with tremendous force. Then the Lord struck it with arrows and split it in two. Dying, Ravana roared with a terrible, mighty sound: 'Where is Rama? Let me challenge and slay him in battle!'"
    ),
    ("la-103-c3",): (
        "ḍolī bhūmi girata dasakaṃdhara. chubhita siṃdhu sari diggaja bhūdhara..\ndharani pareu dvau khaṃḍa baḍhāī. cāpi bhālu markaṭa samudāī..",
        "The earth shook as Ravana fell. Oceans, rivers, the elephants of the quarters, and mountains were disturbed. He fell upon the ground, his two halves expanding, crushing hosts of bears and monkeys beneath him."
    ),
    ("la-103-c4",): (
        "maṃdodarī āgeṃ bhuja sīsā. dhari sara cale jahāṃ jagadīsā..\nprabise saba niṣaṃga mahu jāī. dekhi suranha duṃdubhīṃ bajāī..",
        "Ravana's heads and arms, carried by the arrows, flew to Mandodari's presence, while the arrows themselves returned to the Lord of the universe and entered back into his quiver. Seeing this, the gods sounded their drums of victory."
    ),
    ("la-103-c5",): (
        "tāsu teja samāna prabhu ānana. haraṣe dekhi saṃbhu caturānana..\njaya jaya dhuni pūrī brahmaṃḍā. jaya raghubīra prabala bhujadaṃḍā..",
        "Ravana's radiance merged into the Lord's face. Seeing this, Shiva and Brahma rejoiced. The cry of 'Victory! Victory!' filled the entire universe: 'Victory to Raghubir of mighty arms!'"
    ),
    ("la-103-c6",): (
        "baraṣahi sumana deva muni bṛṃdā. jaya kṛpāla jaya jayati mukuṃdā..",
        "Hosts of gods and sages showered flowers: 'Victory to the merciful one! Victory, victory to Mukunda (the Liberator)!'"
    ),
    ("la-103-ch",): (
        "jaya kṛpā kaṃda mukuṃda dvaṃda harana sarana sukhaprada prabho.\nkhala dala bidārana parama kārana kārunīka sadā bibho..\nsura sumana baraṣahi haraṣa saṃkula bāja duṃdubhi gahagahī.\nsaṃgrāma aṃgana rāma aṃga anaṃga bahu sobhā lahī..\nsira jaṭā mukuṭa prasūna bica bica ati manohara rājahīṃ.\njanu nīlagiri para taḍita paṭala sameta uḍugana bhrājahīṃ..\nbhujadaṃḍa sara kodaṃḍa pherata rudhira kana tana ati bane.\njanu rāyamunīṃ tamāla para baiṭhīṃ bipula sukha āpane..",
        "Victory to the root of mercy, Mukunda, destroyer of duality, giver of happiness to those who seek refuge, O Lord! Destroyer of the hosts of the wicked, supreme cause of all causes, ever compassionate, all-pervading Lord! The gods joyfully showered flowers as drums thundered. On the battlefield, Rama's body was adorned with the beauty of countless Cupids. His matted locks, crown, and flowers woven in between looked most enchanting — like a dark mountain with flashes of lightning and hosts of stars shining upon it. As he twirled his mighty arms, arrows, and bow, drops of blood adorned his body beautifully — like scarlet Rayamuni birds perched on a Tamala tree, enjoying supreme bliss."
    ),
    ("la-103-d",): (
        "kṛpādṛṣṭi kari prabhu abhaya kie sura bṛṃda.\nbhālu kīsa saba haraṣe jaya sukha dhāma mukuṃda..103..",
        "With his compassionate glance, the Lord made all the hosts of gods fearless. All the bears and monkeys rejoiced: 'Victory to Mukunda, the abode of bliss!'"
    ),

    # === DOHA 104 ===
    ("la-104-c1",): (
        "pati sira dekhata maṃdodarī. muruchita bikala dharani khasi parī..\njubati bṛṃda rovata uṭhi dhāīṃ. tehi uṭhāi rāvana pahi āī..",
        "Seeing her husband's severed heads, Mandodari fainted and fell to the ground in anguish. A host of women rose weeping and rushed to her. They lifted her and brought her to Ravana's body."
    ),
    ("la-104-c2",): (
        "pati gati dekhi te karahi pukārā. chūṭe kaca nahi bapuṣa saṃbhārā..\nura tāḍanā karahi bidhi nānā. rovata karahi pratāpa bakhānā..",
        "Seeing their lord's fate, they wailed aloud. Their hair came loose and they could not compose themselves. They beat their breasts in many ways, weeping and recounting his glories."
    ),
    ("la-104-c3",): (
        "tava bala nātha ḍola nita dharanī. teja hīna pāvaka sasi taranī..\nseṣa kamaṭha sahi sakahi na bhārā. so tanu bhūmi pareu bhari chārā..",
        "'By your might, O lord, the earth ever trembled. Fire, moon, and sun lost their luster before you. Shesha and the cosmic tortoise could not bear your weight. That very body now lies on the ground covered in dust!'"
    ),
    ("la-104-c4",): (
        "baruna kubera suresa samīrā. rana sanmukha dhari kāhuṃ na dhīrā..\nbhujabala jitehu kāla jama sāīṃ. āju parehu anātha kī nāīṃ..",
        "'Varuna, Kubera, Indra, and the Wind-god — none dared face you in battle. By your arm-strength you conquered even Death and Yama. Yet today you lie fallen like an orphan!'"
    ),
    ("la-104-c5",): (
        "jagata bidita tumhārī prabhutāī. suta parijana bala barani na jāī..\nrāma bimukha asa hāla tumhārā. rahā na kou kula rovanihārā..",
        "'The whole world knew your sovereignty. The might of your sons and kinsmen was beyond description. Yet being hostile to Rama, this is your fate — not one of your clan is left to weep for you!'"
    ),
    ("la-104-c6",): (
        "tava basa bidhi prapaṃca saba nāthā. sabhaya disipa nita nāvahi māthā..\naba tava sira bhuja jaṃbuka khāhīṃ. rāma bimukha yaha anucita nāhīṃ..",
        "'The entire creation was under your sway, O lord. The terrified guardians of the directions ever bowed their heads before you. Now jackals devour your heads and arms — but for one hostile to Rama, this is not undeserved.'"
    ),
    ("la-104-c7",): (
        "kāla bibasa pati kahā na mānā. aga jaga nāthu manuja kari jānā..",
        "'Driven by fate, my husband heeded no counsel. He took the Lord of all creation — animate and inanimate — to be a mere mortal.'"
    ),
    ("la-104-ch",): (
        "jānyau manuja kari danuja kānana dahana pāvaka hari svayaṃ.\njehi namata siva brahmādi sura piya bhajēhu nahi karunāmayaṃ..\nājanma te paradroha rata pāpaughamaya tava tanu ayaṃ.\ntumhahū diyau nija dhāma rāma namāmi brahma nirāmayaṃ..",
        "'You mistook for a mortal the very Hari who is the fire that consumes the forest of demons. You did not worship the compassionate Lord before whom Shiva, Brahma, and all gods bow, O my dear husband. From birth you were devoted to harming others; this body of yours was a mass of sin. Yet even to you, Rama has granted his own divine abode! I bow to Rama, the Supreme Brahman, free from all affliction.'"
    ),
    ("la-104-d",): (
        "ahaha nātha raghunātha sama kṛpāsiṃdhu nahi āna.\njogi bṛṃda durlabha gati tohi dīnhi bhagavāna..104..",
        "'Alas, O lord! There is no other ocean of mercy equal to Raghunath. The state that is unattainable even for hosts of yogis — that the Lord has bestowed upon you!'"
    ),

    # === DOHA 105 ===
    ("la-105-c1",): (
        "maṃdodarī bacana suni kānā. sura muni siddha sabanha sukha mānā..\naja mahesa nārada sanakādī. je munibara paramārathabādī..",
        "Hearing Mandodari's words, gods, sages, and Siddhas all were pleased. Brahma, Maheshwar, Narada, Sanaka, and other great sages who speak of the highest truth—"
    ),
    ("la-105-c2",): (
        "bhari locana raghupatihi nihārī. prema magana saba bhae sukhārī..\nrudana karata dekhīṃ saba nārī. gayau bibhīṣanu mana dukha bhārī..",
        "— gazed at Raghupati with eyes full of love, immersed in bliss and joy. Then seeing all the women weeping, Vibhishana went to them with deep sorrow in his heart."
    ),
    ("la-105-c3",): (
        "baṃdhu dasā biloki dukha kīnhā. taba prabhu anujahi āyasu dīnhā..\nlachimana tehi bahu bidhi samujhāyau. bahuri bibhīṣana prabhu pahi āyau..",
        "He grieved seeing his brother's state. Then the Lord gave instructions to his younger brother. Lakshmana consoled Vibhishana in many ways. Then Vibhishana returned to the Lord."
    ),
    ("la-105-c4",): (
        "kṛpādṛṣṭi prabhu tāhi bilokā. karahu kriyā parihari saba sokā..\nkīnhi kriyā prabhu āyasu mānī. bidhivata desa kāla jiyaṃ jānī..",
        "The Lord looked at him with compassionate eyes: 'Perform the funeral rites and cast off all grief.' Obeying the Lord's command, Vibhishana performed the rites according to proper custom, mindful of place and time."
    ),
    ("la-105-d",): (
        "maṃdodarī ādi saba dei tilāṃjali tāhi.\nbhavana gaī raghupati guna gana baranata mana māhi..105..",
        "Mandodari and all the queens offered libations of water to the departed. Then they returned to the palace, praising Raghupati's virtues in their hearts."
    ),

    # === DOHA 106 ===
    ("la-106-c1",): (
        "āi bibhīṣana puni siru nāyau. kṛpāsiṃdhu taba anuja bolāyau..\ntumha kapīsa aṃgada nala nīlā. jāmavaṃta māruti nayasīlā..",
        "Vibhishana came and bowed his head again. The ocean of mercy then called his younger brother: 'You, along with the monkey king Sugriva, Angad, Nala, Nila, Jambavan, and the virtuous Hanuman—'"
    ),
    ("la-106-c2",): (
        "saba mili jāhu bibhīṣana sāthā. sārehu tilaka kaheu raghunāthā..\npitā bacana maiṃ nagara na āvauṃ. āpu sarisa kapi anuja paṭhāvauṃ..",
        "'— go together with Vibhishana and perform his coronation,' said Raghunath. 'My father's vow prevents me from entering a city. I send monkeys and my brother, who are dear as myself.'"
    ),
    ("la-106-c3",): (
        "turata cale kapi suni prabhu bacanā. kīnhī jāi tilaka kī racanā..\nsādara siṃhāsana baiṭhārī. tilaka sāri astuti anusārī..",
        "Hearing the Lord's words, the monkeys set out at once. Going to Lanka, they arranged the coronation ceremony. They reverently seated Vibhishana on the throne, applied the sacred tilak, and offered hymns of praise."
    ),
    ("la-106-c4",): (
        "jori pāni sabahīṃ sira nāe. sahita bibhīṣana prabhu pahi āe..\ntaba raghubīra boli kapi līnhe. kahi priya bacana sukhī saba kīnhe..",
        "All joined their palms and bowed their heads, then came with Vibhishana to the Lord. Then Raghubir called all the monkeys and made them happy with loving words."
    ),
    ("la-106-ch",): (
        "kie sukhī kahi bānī sudhā sama bala tumhāreṃ ripu hayau.\npāyau bibhīṣana rāja tihuṃ pura jasu tumhāro nita nayau..\nmohi sahita subha kīrati tumhārī parama prīti jo gāihai.\nsaṃsāra siṃdhu apāra pāra prayāsa binu nara pāihai..",
        "He gladdened them with words sweet as nectar: 'By your strength the enemy has been slain. Vibhishana has received the kingdom, and your fame is ever new in all three worlds. Whoever sings with supreme love this glorious account of your deeds along with mine shall cross the boundless ocean of worldly existence without effort.'"
    ),
    ("la-106-d",): (
        "prabhu ke bacana śravana suni nahi aghāhi kapi puṃja.\nbāra bāra sira nāvahi gahahi sakala pada kaṃja..106..",
        "Hearing the Lord's words, the multitude of monkeys could not have enough. Again and again they bowed their heads and clasped his lotus feet."
    ),

    # === DOHA 107 ===
    ("la-107-c1",): (
        "puni prabhu boli liyau hanumānā. laṃkā jāhu kaheu bhagavānā..\nsamācāra jānakihi sunāvehu. tāsu kusala lai tumha cali āvahu..",
        "Then the Lord summoned Hanuman. The blessed Lord said: 'Go to Lanka. Convey the news to Janaki. Bring back tidings of her well-being and return quickly.'"
    ),
    ("la-107-c2",): (
        "taba hanumaṃta nagara mahuṃ āe. suni nisicarī nisācara dhāe..\nbahu prakāra tinha pūjā kīnhī. janakasutā dekhāi puni dīnhī..",
        "Then Hanuman entered the city. Hearing of his arrival, demonesses and demons rushed to him. They honored him in many ways and then led him to see Janaki's daughter."
    ),
    ("la-107-c3",): (
        "dūrahi te pranāma kapi kīnhā. raghupati dūta jānakīṃ cīnhā..\nkahahu tāta prabhu kṛpāniketā. kusala anuja kapi senā sametā..",
        "From a distance the monkey bowed. Janaki recognized him as Raghupati's messenger. 'Tell me, dear one — is the Lord, that abode of mercy, well? And his brother, and the monkey army?'"
    ),
    ("la-107-c4",): (
        "saba bidhi kusala kosalandhīsā. mātu samara jītyau dasasīsā..\nabicala rāju bibhīṣana pāyau. suni kapi bacana haraṣa ura chāyau..",
        "'The Lord of Kosala is well in every way, O mother. He has conquered the ten-headed Ravana in battle. Vibhishana has received an everlasting kingdom.' Hearing the monkey's words, joy flooded Sita's heart."
    ),
    ("la-107-ch",): (
        "ati haraṣa mana tana pulaka locana sajala kaha puni puni ramā.\nkā deuṃ tohi treloka mahuṃ kapi kimapi nahiṃ bānī samā..\nsunu mātu maiṃ pāyau akhila jaga rāju āju na saṃsayaṃ.\nrana jīti ripudala baṃdhu juta pasyāmi rāmamanāmayaṃ..",
        "Overjoyed in heart and body, with hair standing on end and eyes brimming with tears, Sita said again and again: 'What can I give you, O monkey? In all the three worlds there is nothing worthy enough, no words adequate.' Hanuman replied: 'Listen, mother — today I have gained sovereignty over the entire world, without doubt. Having conquered the enemy host in battle, I behold Rama, free from all affliction, together with his brother.'"
    ),
    ("la-107-d",): (
        "sunu suta sadaguna sakala tava hṛdayaṃ basahu hanumaṃta.\nsānukūla kosalapati rahahuṃ sameta anaṃta..107..",
        "Sita blessed him: 'Listen, my son — may all noble virtues dwell in your heart, O Hanuman! May the Lord of Kosala, along with the eternal Shesha (Lakshmana), be ever favorable to you.'"
    ),

    # === DOHA 108 ===
    ("la-108-c1",): (
        "aba soi jatana karahu tumha tātā. dekhauṃ nayana syāma mṛdu gātā..\ntaba hanumāna rāma pahi jāī. janakasutā kai kusala sunāī..",
        "'Now do whatever is needed, dear one, so that I may see his dark, gentle form with my own eyes.' Then Hanuman went to Rama and reported Sita's well-being."
    ),
    ("la-108-c2",): (
        "suni saṃdesu bhānukulabhūṣana. boli lie jubarāja bibhīṣana..\nmārutasuta ke saṃga sidhāvahu. sādara janakasutahi lai āvahu..",
        "Hearing the message, the ornament of the solar dynasty summoned Crown Prince Vibhishana: 'Go with Hanuman and bring Janaki's daughter here with due respect.'"
    ),
    ("la-108-c3",): (
        "turatahi sakala gae jahaṃ sītā. sevahi saba nisicarīṃ binītā..\nbegi bibhīṣana tinhahi sikhāyau. tinha bahu bidhi majjana karavāyau..",
        "They all went at once to where Sita was. Demonesses were serving her humbly. Vibhishana quickly instructed them, and they bathed Sita elaborately in many ways."
    ),
    ("la-108-c4",): (
        "bahu prakāra bhūṣana pahirāe. sibikā rucira sāji puni lyāe..\ntā para haraṣi caḍhī baidehī. sumiri rāma sukhadhāma sanehī..",
        "They adorned her with ornaments of many kinds. Then they prepared a beautiful palanquin and brought it. Vaidehi joyfully mounted it, remembering Rama, the beloved abode of happiness."
    ),
    ("la-108-c5",): (
        "betapāni racchaka cahuṃ pāsā. cale sakala mana parama hulāsā..\ndekhana bhālu kīsa saba āe. racchaka kopi nivārana dhāe..",
        "Guards with staffs attended her on all four sides. All proceeded with supreme joy in their hearts. Bears and monkeys all came to see her, but the guards angrily rushed to turn them away."
    ),
    ("la-108-c6",): (
        "kaha raghubīra kahā mama mānahu. sītahi sakhā payādeṃ ānahu..\ndekhahu kapi jananī kī nāīṃ. bihasi kahā raghunātha gosāī..",
        "Raghubir said: 'Accept my command. Bring Sita on foot, friends. Let the monkeys see her as they would their own mother.' So spoke Lord Raghunath with a smile."
    ),
    ("la-108-c7",): (
        "suni prabhu bacana bhālu kapi haraṣe. nabha te suranha sumana bahu baraṣe..\nsītā prathama anala mahuṃ rākhī. pragaṭa kīnhi caha aṃtara sākhī..",
        "Hearing the Lord's words, the bears and monkeys rejoiced. The gods showered many flowers from the sky. Sita had first been placed in the fire (as a shadow form); now the Lord wished to reveal her with the inner truth as witness."
    ),
    ("la-108-d",): (
        "tehi kārana karunānidhi kahe kachuka durbāda.\nsunata jātudhānīṃ saba lāgīṃ karai biṣāda..108..",
        "For this reason, the ocean of compassion spoke some harsh words. Hearing them, all the demonesses began to grieve."
    ),

    # === DOHA 109 ===
    ("la-109-c1",): (
        "prabhu ke bacana sīsa dhari sītā. bolī mana krama bacana punītā..\nlachimana hohu dharama ke negī. pāvaka pragaṭa karahu tumha begī..",
        "Receiving the Lord's words upon her head, Sita spoke — pure in thought, deed, and word: 'Lakshmana, be the witness of dharma. Quickly kindle the sacred fire.'"
    ),
    ("la-109-c2",): (
        "suni lachimana sītā kai bānī. biraha bibeka dharama niti sānī..\nlocana sajala jori kara doū. prabhu sana kachu kahi sakata na oū..",
        "Hearing Sita's words — imbued with love, discernment, righteousness, and wisdom — Lakshmana's eyes filled with tears. Joining both hands, he could say nothing to the Lord."
    ),
    ("la-109-c3",): (
        "dekhi rāma rukha lachimana dhāe. pāvaka pragaṭi kāṭha bahu lāe..\npāvaka prabala dekhi baidehī. hṛdayaṃ haraṣa nahiṃ bhaya kachu tehī..",
        "Understanding Rama's intent, Lakshmana rushed and kindled a blazing fire with much firewood. Seeing the mighty blaze, Vaidehi felt joy in her heart and no fear whatsoever."
    ),
    ("la-109-c4",): (
        "jauṃ mana baca krama mama ura māhīṃ. taji raghubīra āna gati nāhīṃ..\ntau kṛsānu saba kai gati jānā. mo kahuṃ hou śrīkhaṃḍa samānā..",
        "'If in thought, word, and deed, there is no refuge in my heart other than Raghubir, then let the fire — which knows the truth of all — become cool as sandalwood for me.'"
    ),
    ("la-109-ch",): (
        "śrīkhaṃḍa sama pāvaka prabesa kiyau sumiri prabhu maithilī.\njaya kosalesa mahesa baṃdita carana rati ati nirmalī..\npratibimba aru laukika kalaṃka pracaṃḍa pāvaka mahuṃ jare.\nprabhu carita kāhuṃ na lakhe nabha sura siddha muni dekhahi khare..1..\ndhari rūpa pāvaka pāni gahi śrī satya śruti jaga bidita jo.\njimi chīrasāgara iṃdirā rāmahi samarpī āni so..\nso rāma bāma bibhāga rājati rucira ati sobhā bhalī.\nnava nīla nīraja nikaṭa mānahuṃ kanaka paṃkaja kī kalī..2..",
        "Remembering the Lord, Maithili entered the fire as if it were sandalwood. 'Victory to the Lord of Kosala, whose feet are worshipped by Maheshwar!' — her devotion was most pure. The shadow-form and all worldly aspersions were consumed in the blazing fire. No one fathomed the Lord's divine play — gods, Siddhas, and sages watched standing in the sky. Then Fire, assuming a form and taking her hand, presented the true Shri (Sita) — she who is known to the Vedas and the world as eternal. Just as Lakshmi arose from the Ocean of Milk, so Fire presented her to Rama. She shone on Rama's left side, beautiful and resplendent — like a golden lotus bud beside a fresh dark blue lotus."
    ),
    ("la-109-d",): (
        "baraṣahi sumana haraṣi suna bājahi gagana nisāna.\ngāvahi kinnara surabadhū nācahi caḍhīṃ bimāna..109(ka)..\njanakasutā sameta prabhu sobhā amita apāra.\ndekhi bhālu kapi haraṣe jaya raghupati sukha sāra..109(kha)..",
        "Flowers rained down in joy; celestial drums sounded in the sky. Kinnaras sang and heavenly nymphs danced, mounted on their aerial chariots. The Lord's beauty together with Janaki's daughter was infinite and boundless. Seeing them, bears and monkeys rejoiced: 'Victory to Raghupati, the essence of bliss!'"
    ),

    # === DOHA 110 ===
    ("la-110-c1",): (
        "taba raghupati anusāsana pāī. mātalī caleu carana siru nāī..\nāe deva sadā svārathī. bacana kahahi janu paramārathī..",
        "Then, receiving Raghupati's permission, Matali departed, bowing his head at the Lord's feet. The ever-selfish gods arrived, speaking words as if they were great spiritual seekers."
    ),
    ("la-110-c2",): (
        "dīna baṃdhu dayāla ragharāyā. deva kīnhi devanha para dāyā..\nbisva droha rata yaha khala kāmī. nija agha gayau kumāragagāmī..",
        "'O Raghuray, friend of the lowly, compassionate one! Lord, you have shown mercy to the gods! This wicked, lustful demon, devoted to hostility toward the world, has met his end — the one who walked the path of evil.'"
    ),
    ("la-110-c3",): (
        "tumha samarūpa brahma abināsī. sadā ekarasa sahaja udāsī..\nakala aguna aja anagha anāmaya. ajita amoghasakti karunāmaya..",
        "'You are the formless, imperishable Brahman — ever uniform, naturally detached. You are without parts, without attributes, unborn, sinless, free from affliction, unconquered, of infallible power, and compassionate.'"
    ),
    ("la-110-c4",): (
        "mīna kamaṭha sūkara naraharī. bāmana parasurāma bapu dharī..\njaba jaba nātha suranha dukhu pāyau. nānā tanu dhari tumhaiṃ nasāyau..",
        "'You assumed the forms of Fish, Tortoise, Boar, Man-Lion, Dwarf, and Parashurama. Whenever, O Lord, the gods have suffered, you have taken various forms and destroyed their enemies.'"
    ),
    ("la-110-c5",): (
        "yaha khala malina sadā suradrohī. kāma lobha mada rata ati kohī..\nadhama siromaṇi tava pada pāvā. yaha hamare mana bisamaya āvā..",
        "'This wretch — ever impure, hostile to gods, addicted to lust, greed, pride, and extreme anger — the very crest-jewel of the wicked — attained your divine abode. This fills our minds with wonder.'"
    ),
    ("la-110-c6",): (
        "hama devatā parama adhikārī. svāratha rata prabhu bhagati bisārī..\nbhava prabāhaṃ saṃtata hama pare. aba prabhu pāhi sarana anusare..",
        "'We gods are supremely privileged, yet devoted to self-interest, we have forgotten devotion to you, Lord. We have been caught forever in the stream of worldly existence. Now protect us, Lord — we have come to your refuge.'"
    ),
    ("la-110-d",): (
        "kari binatī sura siddha saba rahe jahaṃ tahaṃ kara jori.\nati saprema tana pulaki bidhi astuti karata bahori..110..",
        "Having made their supplication, all gods and Siddhas stood with folded hands everywhere. Then Brahma, his body thrilling with deep love, began his hymn of praise."
    ),

    # === DOHA 111 ===
    ("la-111-ch",): (
        "jaya rāma sadā sukhadhāma hare. raghunāyaka sāyaka cāpa dhare..\nbhava bārana dārana siṃha prabho. guna sāgara nāgara nātha bibho..\ntana kāma aneka anūpa chabī. guna gāvata siddha munīṃdra kabī..\njasu pāvana rāvana nāga mahā. khaganātha jathā kari kopa gahā..\njana raṃjana bhaṃjana soka bhayaṃ. gatakrodha sadā prabhu bodhamayaṃ..\navatāra udāra apāra gunaṃ. mahi bhāra bibhaṃjana gyānaghanaṃ..\naja byāpakamekamanādi sadā. karunākara rāma namāmi mudā..\nraghubaṃsa bibhūṣana dūṣana hā. kṛta bhūpa bibhīṣana dīna rahā..\nguna gyāna nidhāna amāna ajaṃ. nita rāma namāmi bibhuṃ birajaṃ..\nbhujadaṃḍa pracaṃḍa pratāpa balaṃ. khala bṛṃda nikaṃda mahā kusalaṃ..\nbinu kārana dīna dayāla hitaṃ. chabi dhāma namāmi ramā sahitaṃ..\nbhava tārana kārana kāja paraṃ. mana saṃbhava dāruna doṣa haraṃ..\nsara cāpa manohara trona dharaṃ. jarajāruna locana bhūpabaraṃ..\nsukha maṃdira suṃdara śrīramanaṃ. mada māra mudhā mamatā samanaṃ..\nanavadya akhaṃḍa na gocara go. sabarūpa sadā saba hoi na go..\niti beda badaṃti na daṃtakathā. rabi ātapa bhinnamabhinna jathā..\nkṛtakṛtya bibho saba bānara e. nirakhanti tavānana sādara e..\ndhiga jīvana deva sarīra hare. tava bhakti binā bhava bhūli pare..\naba dīna dayāla dayā kariai. mati mori bibhedakarī hariai..\njehi te biparīta kriyā kariai. dukha so sukha māni sukhī cariai..\nkhala khaṃḍana maṃḍana ramya chamā. pada paṃkaja sevita saṃbhu umā..\nnṛpa nāyaka de baradānamidaṃ. caranāṃbuja prema sadā subhadaṃ..",
        "Victory to Rama, the eternal abode of bliss, O Hari! Raghunayak who bears arrows and bow! O Lord, you are the lion that tears apart the elephant of worldly existence. Ocean of virtues, most adept Lord, all-pervading one! Your body possesses the incomparable beauty of countless Cupids. Siddhas, great sages, and poets sing your virtues. Your pure fame — you seized the great serpent Ravana as Garuda seizes a snake. You delight your devotees and destroy their grief and fear. Ever free from anger, you are the Lord full of wisdom. Your incarnation is generous, your virtues infinite. You destroy the burden of the earth; you are the embodiment of knowledge. Unborn, all-pervading, one without a second, beginningless, eternal — I bow to Rama, the mine of compassion, with joy! Ornament of the Raghu dynasty, slayer of Dushana, you have made the lowly Vibhishana a king. Treasure-house of virtue and knowledge, free from pride, unborn — I ever bow to Rama, the all-pervading, the pure. Your mighty arms possess tremendous valor and power; you destroy hosts of the wicked with supreme skill. Without any cause, you are compassionate and benevolent to the lowly. I bow to the abode of beauty, together with Rama (Lakshmi). You are the cause of liberation from worldly existence, the supreme purpose. You remove the terrible faults born of the mind. You bear charming arrows, bow, and quiver; your reddish eyes are like lotuses — O best of kings! Temple of bliss, beautiful, beloved of Shri, you subdue pride, Cupid, delusion, and attachment. Faultless, undivided, beyond the reach of senses — you are all forms, you are always everything, yet you are none of these. Thus speak the Vedas — this is no mere legend — just as sunlight is both different and non-different from the sun. O all-pervading Lord, all these monkeys are now fulfilled — they gaze upon your face with reverence. Shame on our lives, O Lord — we gods, robbers of Shri — without your devotion, we wander lost in worldly existence. Now, O friend of the lowly, be compassionate. Remove my intellect that creates false distinctions — the intellect due to which one acts perversely, considering sorrow as happiness and living in delusion. O destroyer of the wicked, adorner of beautiful forgiveness, whose lotus feet are served by Shambhu and Uma — O king of kings, grant this boon: eternal love for your lotus feet, ever auspicious!"
    ),
    ("la-111-d",): (
        "binaya kīnhi caturānana prema pulaka ati gāta.\nsobhāsiṃdhu bilokatalocana nahīṃ aghāta..111..",
        "Brahma made this humble prayer, his body thrilling with intense love. Gazing upon the ocean of beauty, his eyes could never have enough."
    ),

    # === DOHA 112 ===
    ("la-112-c1",): (
        "tehi avasara dasaratha tahaṃ āe. tanaya biloki nayana jala chāe..\nanuja sahita prabhu baṃdana kīnhā. āsirabāda pitāṃ taba dīnhā..",
        "At that moment, Dasharatha arrived there. Seeing his sons, his eyes filled with tears. The Lord, along with his brother, paid obeisance. Then the father gave his blessings."
    ),
    ("la-112-c2",): (
        "tāta sakala tava punya prabhāū. jītyau ajaya nisācara rāū..\nsuni suta bacana prīti ati bāḍhī. nayana salila romāvali ṭhāḍhī..",
        "'Son, this is entirely the power of your merit — you have conquered the invincible demon king.' Hearing his son's words, the father's love overflowed. Tears streamed from his eyes and his hair stood on end."
    ),
    ("la-112-c3",): (
        "raghupati prathama prema anumānā. citai pitahi dīnheu dṛḍha gyānā..\ntāte umā moccha nahiṃ pāyau. dasaratha bheda bhagati mana lāyau..",
        "Raghupati first gauged his father's love, then gazing at him, bestowed firm spiritual knowledge. Therefore, O Uma, Dasharatha did not attain final liberation (moksha) — he had fixed his mind on devotion with a sense of distinction (seeing Rama as his son)."
    ),
    ("la-112-c4",): (
        "sagunopāsaka moccha na lehīṃ. tinha kahuṃ rāma bhagati nija dehīṃ..\nbāra bāra kari prabhuhi pranāmā. dasaratha haraṣi gae suradhāmā..",
        "Devotees of the personal God do not seek liberation; to them Rama gives his own devotion. Bowing to the Lord again and again, Dasharatha joyfully departed to the abode of the gods."
    ),
    ("la-112-d",): (
        "anuja jānakī sahita prabhu kusala kosalādhīsa.\nsobhā dekhi haraṣi mana astuti kara sura īsa..112..",
        "Seeing the Lord of Kosala safe and well with his brother and Janaki, and beholding his splendor, Indra, king of gods, joyfully offered his praises."
    ),

    # === DOHA 113 ===
    ("la-113-ch",): (
        "jaya rāma sobhā dhāma. dāyaka pranata biśrāma..\ndhṛta trona bara sara cāpa. bhujadaṃḍa prabala pratāpa..1..\njaya dūṣanāri kharāri. mardana nisācara dhāri..\nyaha duṣṭa māreu nātha. bhae deva sakala sanātha..2..\njaya harana dharanī bhāra. mahimā udāra apāra..\njaya rāvanāri kṛpāla. kie jātudhāna bihāla..3..\nlaṃkesa ati bala garba. kie basya sura gaṃdharba..\nmuni siddha nara khaga nāga. haṭhi paṃtha saba keṃ lāga..4..\nparadroha rata ati duṣṭa. pāyau so phalu pāpiṣṭa..\naba sunahu dīna dayāla. rājīva nayana bisāla..5..\nmohi rahā ati abhimāna. nahi kou mohi samāna..\naba dekhi prabhu pada kaṃja. gata māna prada dukha puṃja..6..\nkou brahma nirguna dhyāva. abyakta jehi śruti gāva..\nmohi bhāva kosala bhūpa. śrīrāma saguna sarūpa..7..\nbaidehī anuja sameta. mama hṛdayaṃ karahu niketa..\nmohi jānie nija dāsa. de bhakti ramānivāsa..8..\nde bhakti ramānivāsa trāsa harana sarana sukhadāyakaṃ.\nsukha dhāma rāma namāmi kāma aneka chabi raghunāyakaṃ..\nsura bṛṃda raṃjana dvaṃda bhaṃjana manuja tanu atulitabalaṃ.\nbrahmādi saṃkara sebya rāma namāmi karunā komalaṃ..",
        "Victory to Rama, abode of beauty, giver of rest to the humble! He bears quiver, excellent arrows, and bow; his mighty arms possess supreme valor. Victory to the slayer of Dushana and Khara, crusher of demons! You have slain this villain, O Lord, and made all the gods safe. Victory to the reliever of earth's burden — your glory is generous and boundless! Victory to the slayer of Ravana, O merciful one — you have devastated the demons! The lord of Lanka, proud of his great strength, had enslaved gods, Gandharvas, sages, Siddhas, men, birds, and serpents — stubbornly obstructing everyone's path. This most wicked one, devoted to harming others — the worst sinner — has received his just fruit. Now hear me, O friend of the lowly, with your large lotus eyes. I was full of great pride — I thought none was my equal. Now, seeing the Lord's lotus feet, my pride has gone and so has the mass of sorrow it caused. Some meditate on the attributeless Brahman — the unmanifest one whom the Vedas sing. But I love the personal form of Shri Rama, the king of Kosala. Together with Vaidehi and your brother, make your abode in my heart. Consider me your own servant and grant me devotion, O dwelling-place of Rama (Lakshmi)! Grant devotion, O abode of Lakshmi, destroyer of fear, giver of happiness to those who seek refuge! I bow to Rama, the abode of bliss, Raghunayak of incomparable beauty like countless Cupids! Delighter of the hosts of gods, destroyer of duality, who assumed a human body of matchless strength — I bow to Rama, worshipped by Brahma, Shankara, and all — tender with compassion!"
    ),
    ("la-113-d",): (
        "aba kari kṛpā biloki mohi āyasu dehu kṛpāla.\nkāha karauṃ suni priya bacana bole dīnadayāla..113..",
        "'Now look upon me with grace and give your command, O merciful one. What shall I do?' Hearing these loving words, the friend of the lowly spoke."
    ),

    # === DOHA 114 ===
    ("la-114-c1",): (
        "sunu surapati kapi bhālu hamāre. pare bhūmi nisacaranhi je māre..\nmama hita lāgi taje inha prānā. sakala jiāu suresa sujānā..",
        "'Listen, O king of gods — my monkeys and bears lie fallen on the ground, slain by the demons. For my sake they gave their lives. Revive them all, O wise Indra.'"
    ),
    ("la-114-c2",): (
        "sunu khagesa prabhu kai yaha bānī. ati agādha jānahi muni gyānī..\nprabhu saka tribhuana māri jiāī. kevala sakrahi dīnhi baḍāī..",
        "Listen, O Garuda — the Lord's words were profoundly deep; only wise sages understand them. The Lord himself could kill and revive the three worlds, yet he graciously gave Indra the honor."
    ),
    ("la-114-c3",): (
        "sudhā baraṣi kapi bhālu jiāe. haraṣi uṭhe saba prabhu pahi āe..\nsudhābṛṣṭi bhai duhu dala ūpara. jie bhālu kapi nahi rajanīcara..",
        "Indra showered nectar and revived the bears and monkeys. They all rose joyfully and came to the Lord. The nectar rain fell on both armies, but only the bears and monkeys revived — not the demons."
    ),
    ("la-114-c4",): (
        "rāmākāra bhae tinha ke mana. mukta bhae chūṭe bhava baṃdhana..\nsura aṃsika saba kapi aru rīchā. jie sakala raghupati kīṃ īchā..",
        "The minds of the dead demons had become absorbed in Rama's form — they were liberated, freed from the bonds of worldly existence. All the monkeys and bears — who were partial incarnations of gods — lived again by Raghupati's will."
    ),
    ("la-114-c5",): (
        "rāma sarisa ko dīna hitakārī. kīnhe mukuta nisācara jhārī..\nkhala mala dhāma kāma rata rāvana. gati pāī jo munibara pāva na..",
        "Who is as compassionate to the lowly as Rama? He liberated even hosts of demons! Ravana — the abode of sin, devoted to lust and wickedness — attained a state that even the greatest sages cannot reach."
    ),
    ("la-114-d",): (
        "sumana baraṣi saba sura cale caḍhi caḍhi rucira bimāna.\ndekhi suavasaru prabhu pahi āyau saṃbhu sujāna..114(ka)..\nparama prīti kara jori juga nalina nayana bhari bāri.\npulakita tana gadagada girāṃ binaya karata tripurāri..114(kha)..",
        "All the gods showered flowers and departed, ascending their beautiful chariots. Seeing the right moment, the wise Shambhu came to the Lord. With supreme love, joining both lotus-like hands, eyes brimming with tears, body thrilling, and voice choked with emotion, the destroyer of Tripura made his prayer."
    ),

    # === DOHA 115 ===
    ("la-115-ch",): (
        "māmabhirakṣaya raghukula nāyaka. dhṛta bara cāpa rucira kara sāyaka..\nmoha mahā ghana paṭala prabhaṃjana. saṃsaya bipina anala sura raṃjana..1..\naguna saguna guna maṃdira suṃdara. bhrama tama prabala pratāpa divākara..\nkāma krodha mada gaja paṃcānana. basahu niraṃtara jana mana kānana..2..\nbiṣaya manoratha puṃja kaṃja bana. prabala tuṣāra udāra pāra mana..\nbhava bāridhi maṃdara paramaṃ dara. bāraya tāraya saṃsṛti dustara..3..\nsyāma gāta rājīva bilocana. dīna baṃdhu pranatārti mocana..\nanuja jānakī sahita niraṃtara. basahu rāma nṛpa mama ura aṃtara..4..\nmuni raṃjana mahi maṃḍala maṃḍana. tulasidāsa prabhu trāsa bikhaṃḍana..5..",
        "Protect me, O leader of the Raghu dynasty! You who bear a splendid bow and beautiful arrows in your hands. You are the mighty wind that disperses the dense clouds of delusion, the fire that burns the forest of doubt, the delighter of gods. Both attributeless and with attributes, beautiful temple of all virtues, you are the powerful sun that dispels the darkness of error. You are the lion against the elephants of lust, anger, and pride — dwell forever in the forest of your devotees' hearts. You are the severe frost against the lotus-garden of worldly desires — generous, taking one beyond the mind. You are the Mount Mandara for churning the ocean of existence, O supreme Lord — you check and ferry across this impassable worldly stream. Dark-bodied, lotus-eyed, friend of the lowly, deliverer of the afflicted who seek refuge — together with your brother and Janaki, dwell forever within my heart, O King Rama! Delighter of sages, ornament of the earth — says Tulsidas — O Lord, destroyer of all fear!"
    ),
    ("la-115-d",): (
        "nātha jabahiṃ kosalapurīṃ hoihi tilaka tumhāra.\nkṛpāsiṃdhu maiṃ āuba dekhana carita udāra..115..",
        "'O Lord, when your coronation takes place in the city of Kosala, I, the ocean of mercy's servant, shall come to witness your generous deeds.'"
    ),

    # === DOHA 116 ===
    ("la-116-c1",): (
        "kari binatī jaba saṃbhu sidhāe. taba prabhu nikaṭa bibhīṣanu āe..\nnāi carana siru kaha mṛdu bānī. binaya sunahu prabhu sāraṃgapānī..",
        "When Shambhu had made his prayer and departed, Vibhishana approached the Lord. Bowing his head at the Lord's feet, he spoke gently: 'Hear my supplication, O Lord who bears the Sharanga bow.'"
    ),
    ("la-116-c2",): (
        "sakula sadala prabhu rāvana mār yau. pāvana jasa tribhuvana bistār yau..\ndīna malīna hīna mati jātī. mo para kṛpā kīnhi bahu bhāṃtī..",
        "'O Lord, you have slain Ravana along with his clan and army. Your pure fame has spread across the three worlds. Upon me — lowly, tainted, of poor intellect and low birth — you have bestowed mercy in so many ways.'"
    ),
    ("la-116-c3",): (
        "aba jana gṛha punīta prabhu kīje. majjanu kariā samara śrama chīje..\ndekhi kosa maṃdira saṃpadā. dehu kṛpāla kapinha kahuṃ mudā..",
        "'Now sanctify your servant's home, Lord. Bathe and relieve the fatigue of battle. See the treasure-houses, palaces, and riches — give them to the monkeys for their delight, O merciful one.'"
    ),
    ("la-116-c4",): (
        "saba bidhi nātha mohi apanāia. puni mohi sahita avadhapura jāia..\nsunata bacana mṛdu dīnadayālā. sajala bhae dvau nayana bisālā..",
        "'Accept me in every way, O Lord, and then take me with you to Ayodhya.' Hearing these gentle words, the friend of the lowly — his two large eyes filled with tears."
    ),
    ("la-116-d",): (
        "tora kosa gṛha mora saba satya bacana sunu bhrāta.\nbharata dasā sumirata mohi nimiṣa kalpa sama jāta..116(ka)..\ntāpasa beṣa gāta kṛsa japata niraṃtara mohi.\ndekhauṃ begi so jatanu karu sakhā nihorauṃ tohi..116(kha)..\nbīteṃ avadhi jāuṃ jauṃ jiata na pāvauṃ bīra.\nsumirata anuja prīti prabhu puni puni pulaka sarīra..116(ga)..\nkarehu kalpa bhari rāju tumha mohi sumirehu mana māhi.\npuni mama dhāma pāihahu jahāṃ saṃta saba jāhi..116(gha)..",
        "'Your treasure and home are all mine — hear this true word, O brother. Remembering Bharat's condition, every moment seems like an age to me. He wears ascetic garb, his body is emaciated, and he constantly chants my name. Let me see him quickly — make arrangements, my friend, I implore you! If I go beyond the appointed time, he will not remain alive, O hero.' Remembering his brother's love, the Lord's body thrilled again and again. 'Rule for an entire cosmic age, and remember me in your heart. Then you shall attain my abode, where all the saints go.'"
    ),

    # === DOHA 117 ===
    ("la-117-c1",): (
        "sunata bibhīṣana bacana rāma ke. haraṣi gahe pada kṛpādhāma ke..\nbānara bhālu sakala haraṣāne. gahi prabhu pada guna bimala bakhāne..",
        "Hearing Rama's words, Vibhishana joyfully clasped the feet of the abode of mercy. All the monkeys and bears rejoiced, clasping the Lord's feet and praising his pure virtues."
    ),
    ("la-117-c2",): (
        "bahuri bibhīṣana bhavana sidhāyau. mani gana basana bimāna bharāyau..\nlai puṣpaka prabhu āgeṃ rākhā. haṃsi kari kṛpāsiṃdhu taba bhāṣā..",
        "Then Vibhishana went to his palace and loaded the Pushpak Viman (flying chariot) with jewels and garments. He brought the Pushpak and placed it before the Lord. The ocean of mercy then spoke with a smile."
    ),
    ("la-117-c3",): (
        "caḍhi bimāna sunu sakhā bibhīṣana. gagana jāi baraṣahu paṭa bhūṣana..\nnabha para jāi bibhīṣana tabahī. baraṣi die mani aṃbara sabahī..",
        "'Board the flying chariot, listen, friend Vibhishana — go up to the sky and shower garments and ornaments!' Vibhishana immediately went up to the sky and showered jewels and garments upon all."
    ),
    ("la-117-c4",): (
        "joi joi mana bhāvai soi lehīṃ. mani mukha meli ḍāri kapi dehīṃ..\nhaṃse rāmu śrī anuja sametā. parama kautukī kṛpā niketā..",
        "Whatever pleased their hearts, the monkeys took. They put gems in their mouths and threw them away. Rama laughed together with Sita and his brother — the supremely playful abode of mercy."
    ),
    ("la-117-d",): (
        "muni jehi dhyāna na pāvahi neti neti kaha beda.\nkṛpāsiṃdhu soi kapinha sana karata aneka binoda..117(ka)..\numā joga japa dāna tapa nānā makha brata nema.\nrāma kṛpā nahi karahi tasī jasī niṣkevala prema..117(kha)..",
        "The one whom sages cannot reach through meditation, whom the Vedas describe only as 'not this, not this' — that very ocean of mercy was sporting with the monkeys in many ways. O Uma, yoga, chanting, charity, austerity, many sacrifices, vows, and observances — none of these accomplish what pure, selfless love for Rama can."
    ),

    # === DOHA 118 ===
    ("la-118-c1",): (
        "bhālu kapinha paṭa bhūṣana pāe. pahiri pahiri raghupati pahi āe..\nnānā jinasa dekhi saba kīsā. puni puni haṃsata kosalādhīsā..",
        "The bears and monkeys received garments and ornaments. They put them on in various ways and came to Raghupati. Seeing all the monkeys decked out in various kinds of finery, the Lord of Kosala laughed again and again."
    ),
    ("la-118-c2",): (
        "citai sabanhi para kīnhi dāyā. bole mṛdula bacana raghurāyā..\ntumhareṃ bala maiṃ rāvanu mār yau. tilaka bibhīṣana kahaṃ puni sār yau..",
        "Gazing at them all with compassion, Raghuray spoke tender words: 'By your strength I have slain Ravana and performed Vibhishana's coronation.'"
    ),
    ("la-118-c3",): (
        "nija nija gṛha aba tumha saba jāhū. sumirehu mohi ḍarapahu jani kāhū..\nsunata bacana premākula bānara. jori pāni bole saba sādara..",
        "'Now all of you return to your own homes. Remember me and fear nothing.' Hearing these words, the monkeys were overwhelmed with love. Joining their palms, they all spoke respectfully."
    ),
    ("la-118-c4",): (
        "prabhu joi kahahu tumhahi saba sohā. hamare hota bacana suni mohā..\ndīna jāni kapi kie sanāthā. tumha treloka īsa raghunāthā..",
        "'O Lord, whatever you say becomes you well. But hearing these words, we are bewildered. Knowing us to be lowly, you gave us your protection. You are the Lord of the three worlds, O Raghunath!'"
    ),
    ("la-118-c5",): (
        "suni prabhu bacana lāja hama marahīṃ. masaka kahūṃ khagapati hita karahīṃ..\ndekhi rāma rukha bānara rīchā. prema magana nahiṃ gṛha kai īchā..",
        "'Hearing your words, we die of shame. Does Garuda (king of birds) ever serve a mosquito? (Yet you, Lord of all, have served us!)' Seeing Rama's mood, the monkeys and bears were drowned in love and had no desire to go home."
    ),
    ("la-118-d",): (
        "prabhu prerita kapi bhālu saba rāma rūpa ura rākhi.\nharaṣa biṣāda sahita cale binaya bibidha bidhi bhāṣi..118(ka)..\nkapipati nīla rīchapati aṃgada nala hanumāna.\nsahita bibhīṣana apara je jūthapa kapi balavāna..118(kha)..\nkahi na sakahi kachu prema basa bhari bhari locana bāri.\nsanmukha citavahi rāma tana nayana nimeṣa nivāri..118(ga)..",
        "Prompted by the Lord, all the monkeys and bears — keeping Rama's form in their hearts — departed with mingled joy and sorrow, offering prayers in many ways. The monkey king Sugriva, Nila, the bear chief Jambavan, Angad, Nala, Hanuman, Vibhishana, and other mighty monkey commanders — they could say nothing, overcome by love, their eyes brimming with tears. They gazed at Rama's form without blinking."
    ),

    # === DOHA 119 ===
    ("la-119-c1",): (
        "atisaya prīti dekha raghurāī. linhe sakala bimāna caḍhāī..\nmana mahuṃ bipra carana siru nāyau. uttara disihi bimāna calāyau..",
        "Seeing their extreme love, Raghuray took them all aboard the flying chariot. Bowing his head in his heart to the Brahmins, he directed the Pushpak northward."
    ),
    ("la-119-c2",): (
        "calata bimāna kolāhala hoī. jaya raghubīra kahai sabu koī..\nsiṃhāsana ati ucca manohara. śrī sameta prabhu baiṭhai tā para..",
        "As the chariot flew, a great tumult arose with everyone crying: 'Victory to Raghubir!' There was a most exalted and beautiful throne upon it, and the Lord sat upon it together with Sita."
    ),
    ("la-119-c3",): (
        "rājata rāmu sahita bhāminī. meru sṛṃga janu ghana dāminī..\nrucira bimānu caleu ati ātura. kīnhī sumana bṛṣṭi haraṣe sura..",
        "Rama shone with his beloved consort like lightning upon the peak of Mount Meru. The beautiful chariot flew with great speed. The delighted gods showered flowers."
    ),
    ("la-119-c4",): (
        "parama sukhada calī tribidha bayārī. sāgara sara sari nirmala bārī..\nsaguna hohisṃ udara cahuṃ pāsā. mana prasanna nirmala nabha āsā..",
        "The most pleasant breeze blew from all three directions. The waters of oceans, lakes, and rivers became pure and clear. Auspicious omens appeared on all sides; minds were joyful and the sky was clear."
    ),
    ("la-119-c5",): (
        "kaha raghubīra dekhu rana sītā. lachimana ihāṃ hatyau iṃdrajītā..\nhanūmāna aṃgada ke māre. rana mahi pare nisācara bhāre..",
        "Raghubir said: 'See the battlefield, Sita. Here Lakshmana slew Indrajit. Here lie the many demons struck down by Hanuman and Angad.'"
    ),
    ("la-119-c6",): (
        "kuṃbhakarana rāvana dvau bhāī. ihāṃ hate sura muni dukhadāī..",
        "'Kumbhakarna and Ravana, the two brothers — here they were slain, those tormentors of gods and sages.'"
    ),
    ("la-119-d",): (
        "ihāṃ setu bāṃdhyau aru thāpeuṃ siva sukha dhāma.\nsītā sahita kṛpānidhi saṃbhuhi kīnha pranāma..119(ka)..\njahaṃ jahaṃ kṛpāsiṃdhu bana kīnha bāsa biśrāma.\nsakala dekhāe jānakihi kahe sabanha ke nāma..119(kha)..",
        "'Here the bridge was built and I established the shrine of Shiva, the abode of bliss.' Together with Sita, the ocean of mercy bowed to Shambhu. Wherever the ocean of mercy had rested in the forest, he showed everything to Janaki and told her the names of all the places."
    ),

    # === DOHA 120 ===
    ("la-120-c1",): (
        "turata bimāna tahāṃ cali āvā. daṃḍaka bana jahaṃ parama suhāvā..\nkuṃbhajādi munināyaka nānā. gae rāmu saba keṃ asthānā..",
        "The flying chariot quickly came to the Dandaka forest, supremely beautiful. Rama visited the hermitages of Agastya (the Pot-born) and many other great sages."
    ),
    ("la-120-c2",): (
        "sakala riṣinha sana pāi asīsā. citrakūṭa āe jagadīsā..\ntahaṃ kari muninha kera saṃtoṣā. calā bimānu tahaṃ te chokhā..",
        "Receiving blessings from all the sages, the Lord of the universe came to Chitrakut. Having satisfied the sages there, the splendid chariot flew on."
    ),
    ("la-120-c3",): (
        "bahuri rāma jānakihi dekhāī. yamunā kali mala harani suhāī..\npuni dekhī surasarī punītā. rāma kahā pranāma karu sītā..",
        "Then Rama showed Janaki the Yamuna — beautiful, destroyer of the impurities of the Kali age. Then they beheld the sacred Ganga. Rama said: 'Bow in reverence, Sita.'"
    ),
    ("la-120-c4",): (
        "tīrathapati puni dekhu prayāgā. nirakhata janma koṭi agha bhāgā..\ndekhu parama pāvani puni benī. harani soka hari loka nisenī..",
        "'Behold the king of pilgrimage sites — Prayag! Merely seeing it destroys the sins of millions of births. And see the supremely sacred Triveni confluence — the destroyer of grief, the stairway to Hari's abode.'"
    ),
    ("la-120-c5",): (
        "puni dekhu avadhapurī ati pāvani. tribidha tāpa bhava roga nasāvani..",
        "'Now behold the most sacred city of Ayodhya — destroyer of the three kinds of suffering and the disease of worldly existence.'"
    ),
    ("la-120-d",): (
        "sītā sahita avadha kahuṃ kīnha kṛpāla pranāma.\nsajala nayana tana pulakita puni puni haraṣita rāma..120(ka)..\npuni prabhu āi tribenīṃ haraṣita majjanu kīnha.\nkapinha sahita bipranhi kahuṃ dāna bibidha bidhi dīnha..120(kha)..",
        "Together with Sita, the merciful Lord bowed toward Ayodhya. His eyes filled with tears, his body thrilled, and Rama rejoiced again and again. Then the Lord came to the Triveni and joyfully bathed. Along with the monkeys, he gave various kinds of gifts to the Brahmins."
    ),

    # === DOHA 121 ===
    ("la-121-c1",): (
        "prabhu hanumaṃtahi kahā bujhāī. dhari baṭu rūpa avadhapura jāī..\nbharatahi kusala hamāri sunāehu. samācāra lai tumha cali āehu..",
        "The Lord explained to Hanuman: 'Assuming the form of a Brahmin student, go to Ayodhya. Tell Bharat of my well-being and bring back news. Return quickly.'"
    ),
    ("la-121-c2",): (
        "turata pavanasuta gavanata bhayau. taba prabhu bharadvāja pahi gayaū..\nnānā bidhi muni pūjā kīnhī. astutī kari puni āsiṣa dīnhī..",
        "Hanuman departed at once. Then the Lord went to Sage Bharadvaj's hermitage. The sage worshipped him in many ways and, after offering praises, gave his blessings."
    ),
    ("la-121-c3",): (
        "muni pada baṃdi jugala kara jorī. caḍhi bimāna prabhu cale bahorī..\nihāṃ niṣāda sunā prabhu āe. nāva nāva kahaṃ loga bolāe..",
        "Bowing at the sage's feet with both hands joined, the Lord boarded the chariot and flew on. Meanwhile, the Nishad chief heard that the Lord had come. He called out to the people: 'Bring boats! Bring boats!'"
    ),
    ("la-121-c4",): (
        "surasari nāghi jāna taba āyau. utareu taṭa prabhu āyasu pāyau..\ntaba sītāṃ pūjī surasarī. bahu prakāra puni carananhi parī..",
        "The Pushpak crossed the Ganga and arrived. It landed on the bank at the Lord's command. Then Sita worshipped the Ganga in many ways and fell at her feet."
    ),
    ("la-121-c5",): (
        "dīnhi asīsa haraṣi mana gaṃgā. suṃdari tava ahivāta abhaṃgā..\nsunata guhā dhāyau premākula. āyau nikaṭa parama sukha saṃkula..",
        "The Ganga blessed her, delighted at heart: 'O beautiful one, may your married life be eternal!' Hearing of the Lord's arrival, Guha rushed forth, overcome with love. He came near, filled with supreme joy."
    ),
    ("la-121-c6",): (
        "prabhuhi sahita biloki baidehī. pareu avanī tana sudhi nahi tehī..\nprīti parama biloki raghurāī. haraṣi uṭhāi liyau ura lāī..",
        "Beholding Vaidehi together with the Lord, Guha fell to the ground, losing all consciousness. Seeing his supreme love, Raghuray joyfully raised him and embraced him."
    ),
    ("la-121-ch",): (
        "liyau hṛdayaṃ lāi kṛpā nidhāna sujāna rāyaṃ ramāpatī.\nbaiṭhāri parama samīpa būjhī kusala so kara bīnatī..\naba kusala pada paṃkaja biloki biraṃci saṃkara sebya je.\nsukha dhāma pūranakāma rāma namāmi rāma namāmi te..1..\nsaba bhāṃti adhama niṣāda so hari bharata jyoṃ ura lāiyau.\nmatimandatulasīdāsa so prabhu moha basa bisarāiyau..\nyaha rāvanāri caritra pāvana rāma pada ratiprada sadā.\nkāmādiharabig yānakara sura siddha muni gāvahi mudā..2..",
        "The ocean of mercy, the all-knowing king, the Lord of Rama (Lakshmi), embraced Guha to his heart. He seated him very near and asked about his welfare. Guha made his supplication: 'Now all is well, seeing your lotus feet — those which Brahma and Shankara worship. O Rama, abode of bliss, fulfilled in all desires — I bow to Rama, I bow to you!' In every way the lowliest of men was the Nishad — yet Hari embraced him to his heart just as he did Bharat. The dull-witted Tulsidas has forgotten that same Lord under the spell of delusion. This sacred story of the slayer of Ravana ever bestows love for Rama's feet. It destroys lust and other vices, it grants spiritual knowledge — gods, Siddhas, and sages sing it with joy."
    ),
    ("la-121-d",): (
        "samara bijaya raghubīra ke carita je sunahi sujāna.\nbijaya bibeka bibhūti nita tinhahi dehi bhagavāna..121(ka)..\nyaha kalikāla malāyatana mana kari dekhu bicāra.\nśrīraghunātha nāma taji nāhina āna adhāra..121(kha)..",
        "Those wise souls who hear the tale of Raghubir's victory in battle — the Lord ever bestows upon them victory, discernment, and glory. This Kali age is the abode of all impurity — reflect upon it in your mind. Abandoning the name of Shri Raghunath, there is no other refuge."
    ),
}

def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for group in data["dohaGroups"]:
        dn = group["dohaNumber"]
        if dn < 81 or dn > 121:
            continue
        for verse in group["verses"]:
            vid = verse["id"]
            key = (vid,)
            if key in UPDATES:
                trans_lit, trans = UPDATES[key]
                verse["transliteration"] = trans_lit
                verse["translation"] = trans
                updated += 1

    with open(INPUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {updated} verses across dohas 81-121.")
    print(f"Total keys in UPDATES: {len(UPDATES)}")

if __name__ == "__main__":
    main()
