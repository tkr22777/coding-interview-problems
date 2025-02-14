package com.company;

import java.util.*;

class Solution {

    public List<Integer> findSubstring(String s, String[] words) {

        List<Integer> solution = new ArrayList<>();

        if (words.length == 0) {
            return solution;
        }

        int wordLen = words[0].length();

        Map<String, Integer> wordsMapping = new HashMap<>();

        for(int i = 0; i < words.length; i++) {
            if (wordsMapping.containsKey(words[i])) {
                wordsMapping.put(words[i], wordsMapping.get(words[i]) + 1); //word to index map
            } else {
                wordsMapping.put(words[i],1);
            }
        }

        final Map<Character,Integer> charsMap = new HashMap<>();
        for(int i = 0; i < words.length; i++) {
            for(int j=0; j < words[i].length(); j++) {
                Character charAtJ = words[i].charAt(j);
                if (charsMap.containsKey(charAtJ)) {
                    charsMap.put(charAtJ, charsMap.get(charAtJ) + 1);
                } else {
                    charsMap.put(charAtJ, 1);
                }
            }
        }

        //print(wordsMapping);
        //print(charsMap);
        //print("Char Map Size:" + charsMap.size() + " string size:" + s.length() + " words len" + wordLen + " total words:" + words.length);

        Map<Character,Integer> windowMap = new HashMap<>();
        int charCompleteCount = 0;

        for(int i = 0; i < s.length(); i++) {

            /*
            if (i%100 == 0) {
                //print("i: " + i + " char complete count:" + charCompleteCount + " window map :");
                //print(windowMap);
            }
             */

            if (i >= wordLen * words.length) {

                int j = i - wordLen * words.length; //to remove

                if (charsMap.containsKey(s.charAt(j))) {
                    windowMap.put(s.charAt(j), windowMap.get(s.charAt(j)) - 1);
                    if (windowMap.get(s.charAt(j)).intValue() == charsMap.get(s.charAt(j)).intValue() - 1) {
                        charCompleteCount--;
                    }
                }
            }

            if (!charsMap.containsKey(s.charAt(i))) {
                continue;
            }

            if (windowMap.containsKey(s.charAt(i))) {
                windowMap.put(s.charAt(i), windowMap.get(s.charAt(i)) + 1);
            } else {
                windowMap.put(s.charAt(i), 1);
            }

            //print("i: " + i + " char: " + s.charAt(i) + " char complete count:" + charCompleteCount + " chars count:" + charsMap.get(s.charAt(i)) + " window count:" + windowMap.get(s.charAt(i)));

            if (windowMap.get(s.charAt(i)).intValue() == charsMap.get(s.charAt(i)).intValue()) {
                charCompleteCount++;
            }

            if (charCompleteCount == charsMap.size()) {
                Map<String,Integer> windowWordsMapping = new HashMap<>();
                int start = i - words.length * wordLen + 1;
                int wordCounter = 0;
                while (start <= i) {
                    //print(windowWordsMapping);
                    String key = s.substring(start, start + wordLen);
                    if (!wordsMapping.containsKey(key)) {
                        break;
                    }
                    windowWordsMapping.computeIfAbsent(key, t -> 0);
                    windowWordsMapping.put(key, windowWordsMapping.get(key) + 1);
                    if (windowWordsMapping.get(key) == wordsMapping.get(key)) {
                        wordCounter++;
                    }
                    start += wordLen;
                }

                if (wordCounter == wordsMapping.size()) {
                    solution.add(i - words.length * wordLen + 1);
                }
            }
        }

        //print(solution);
        return solution;
    }

    public List<Integer> findSubstringB(String s, String[] words) {

        List<Integer> solution = new ArrayList<>();

        if (words.length == 0) {
            return solution;
        }

        int wordLen = words[0].length();

        //assume words.len = 2 and wordLen = 2 and string len is 6.
        //Then string expands from 0 to 5 and we would need to check 0 to 3, 1 to 4, 2 to 5 for 4 char based
        //Size of the checking array should have len of 3
        //Thus the formula should be str.len - wordLen + 1
        List<Integer>[] found = new List[s.length() - wordLen + 1];

        for (int i = 0 ; i < found.length; i++) {
            found[i] = new ArrayList();
            for (int j = 0; j < words.length; j++) {
                String subString = s.substring(i, i + wordLen);
                if (subString.equals(words[j])) {
                    found[i].add(j);
                }
            }
        }

        for (int i = 0; i < s.length() - (wordLen * words.length) + 1; i++) {
            if (found[i].size() > 0) {
                Set<Set<Integer>> indexSets = new HashSet<>();
                for (int j = i; j < i + wordLen * words.length ; j += wordLen) {

                    if (found[j] == null) {
                        break;
                    }

                    if (indexSets.size() == 0) {
                        indexSets.add(new HashSet<>());
                    }

                    if (found[j].size() < 2) {
                        for(Set<Integer> set: indexSets) {
                            set.addAll(found[j]);
                        }
                    } else {
                        Set<Set<Integer>> newIndexSets = new HashSet<>();
                        for (Integer index: found[j]) {
                            for (Set<Integer> indexSet: indexSets) {
                                Set<Integer> copiedIndexSet = new HashSet<>();
                                for (int indexVal: indexSet){
                                    copiedIndexSet.add(indexVal);
                                }
                                copiedIndexSet.add(index);
                                newIndexSets.add(copiedIndexSet);
                            }
                        }
                        indexSets = newIndexSets;
                    }
                }
                for (Set<Integer> integerSet: indexSets) {
                    if (integerSet.size() == words.length) {
                        solution.add(i);
                    }
                }
            }
        }

        return solution;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String[] words = {"word", "good", "best", "word"};
        solution.findSubstring("wordgoodgoodgoodbestword", words);

        String[] words2 = {"foo", "bar"};
        solution.findSubstring("barfoothefoobarman", words2);

        String[] words3 = {"bar", "foo", "the"};
        solution.findSubstring("barfoofoobarthefoobarman", words3);

        String[] words4 = {"a"};
        solution.findSubstring("a", words4);


        String str = "ejwwmybnorgshugzmoxopwuvshlcwasclobxmckcvtxfndeztdqiakfusswqsovdfwatanwxgtctyjvsmlcoxijrahivwfybbbudosawnfpmomgczirzscqvlaqhfqkithlhbodptvdhjljltckogcjsdbbktotnxgwyuapnxuwgfirbmdrvgapldsvwgqjfxggtixjhshnzphcemtzsvodygbxpriwqockyavfscvtsewyqpxlnnqnvrkmjtjbjllilinflkbfoxdhocsbpirmcbznuioevcojkdqvoraeqdlhffkwqbjsdkfxstdpxryixrdligpzldgtiqryuasxmxwgtcwsvwasngdwovxzafuixmjrobqbbnhwpdokcpfpxinlfmkfrfqrtzkhabidqszhxorzfypcjcnopzwigmbznmjnpttflsmjifknezrneedvgzfmnhoavxqksjreddpmibbodtbhzfehgluuukupjmbbvshzxyniaowdjamlfssndojyyephstlonsplrettspwepipwcjmfyvfybxiuqtkdlzqedjxxbvdsfurhedneauccrkyjfiptjfxmpxlssrkyldfriuvjranikluqtjjcoiqffdxaukagphzycvjtvwdhhxzagkevvuccxccuoccdkbboymjtimdrmerspxpktsmrwrlkvpnhqrvpdekmtpdfuxzjwpvqjjhfaupylefbvbsbhdncsshmrhxoyuejenqgjheulkxjnqkwvzznriclrbzryfaeuqkfxrbldyusoeoldpbwadhrgijeplijcvqbormrqglgmzsprtmryvkeevlthvflsvognbxfjilwkdndyzwwxgdbeqwlldyezmkopktzugxgkklimhhjqkmuaifnodtpredhqygmedtqpezboimeuyyujfjxkdmbjpizpqltvgknnlodtbhnbhjkmuhwxvzgmkhbcvvadhnssbvneecglnqxhavhvxpkjxlluilzpysjcnwguyofnhfvhaceztoiscumkhociglkvispihvyoatxcxbeqsmluixgsliatukrecgoldmzfhwkgaqzsckonjuhxdhqztjfxstjvikdrhpyjfxbjjryslfpqoiphrwfjqqhaamrjbrsiovrxmqsyxhqmritjeauwqbwtpqcqhvyyssvfknfhxvtodpzipueixdbntdfcaeatyyainfpkclbgaaqrwwzwbcjwiqzkwzfuxfclmsxpdyvfbnwxjytnaejivivriamhgqsskqhnqeurttrfrmstrbeokzhuzvbfmwywohmgogyhzpmsdemugqkspsmoppwbnwabdmiruibwznqcuczculujfiavzwynsyqxmarjkshjhxobandwyzggjibjgzyaaqxorqxbkenscbveqbaociwmqxxyzvyblypeongzrttvwqzmrccwkzidyfbxcaypyquodcpwxkstbthuvjqgialhfmgjohzoxvdaxuywfqrgmyahhtpqtazbphmfoluliznftodyguesshcacrsvutylalqrykehjuofisdookjhrljvedsywrlyccpaowjaqyfaqioesxnlkwgpbznzszyudpwrlgrdgwdyhucztsneqttsuirmjriohhgunzatyfrfzvgvptbgpwajgtysligupoqeoqxoyqtzozufvvlktnvahvsseymtpeyfvxttqosgpplkmxwgmsgtpantazppgnubmpwcdqkvhwfuvcahwibniohiqyywnuzzmxeppokxksrfwrpuzqhjgqryorwboxdauhrkxehiwaputeouwxdfoudcoagcxjcuqvenznxxnprgvhasffxtzaxpcfrcovwgrcwqptoekhmgpoywtxruxokcubekzcrqengviwbtgnzvdzrwwkqvacxwgdhffyvjldgvchoiwnfzoyvkiogisdfyjmfomcazigukqlumyzmnzjzhzfpslwsukykwckvktswjdqxdrlsqvsxwxpqkljeyjpulbswwmuhplfueqnvnhukgjarxlxvwmriqjgmxawmndhsvwnjdjvjtxcsjapfogpesxtpypenunfpjuyoevzztctecilqqbxkaqcyhiobvtqgqruumvvhxolbyzsqcrdchhdqprtkkjsccowrjtyjjmkhleanvfpemuublnnyzfabtxsestncfalqenfcswgerbfcqsapzdtscnzugmwlmidtxkvqhbuaecevwhmwkfqmvpgbefpqpsjmdecmixmmbsjxzwvjdmxydechlraajjmoqpcyoqmrjwoiumuzatydzcnktnkeyztoqvogodxxznhvzduzxudwwqhpftwdspuimioanlzobhjakgajafgzxpqckmhdbbnqmcszpuoqbztnftzgahhxwxbgkilnmzfydyxusnnvngksbjabqjaohdvrniezhmxmkxhemwbbclwdxwgngicplzgajmaryzfkyoqlkrmmfirchzrphveuwmvgaxzbwenvteifxuuefnimnadwxhruvoavlzyhfmeasmgrjawongccgfbgoualiaivbhcgvjjnxpggrewglalthmzvgziobrjeanlvyukwlscexbkibvdjhdgnepdiimmkcxhattwglbkicvsfswocbvphmtpwhcgjbnmxgidtlqcnnwtfujhvgzdussqbwynylzvtjapvqtidpdjkpshvrmqlhindhabubyokzdfrwqvnvgzkyhistydagsgnujiviyijdnabfxqbdqnexvwsvzvcsbrmkbkuzsdehghndyqjodnnblfwmaygdstotfkvxozgwhtbhlkvrzismnozqpfthajafuxekzlgigjpsukjvsdihrjzgovnreqwapdkoqswyclqyvbvpedzyoyedvuuamscbxnqnfmmjyehvidnoimmxmtcinwkbqmcobubjjpshucechrqrffqsyscnqoohcsxenypyqhfklloudgmklcejvgynwouzhtfwuuukdbwpmkjrqxeeaipxrokncholathupdetgaktmvmftqjvzyssocftjwemroghrncynmtchhhcaqxbqpthuaafwgrouaxonzocljeuslzsdwvuoodipdpnlhdihaywzmymxdjrqikughquwtenyucjdgrmipiidiwclhuepgyynoslhzahtdqwliktzsddaahohbszhqxxgripqlwlomjbwtuynydoakejmwkvojuwbfltqjfgxqhwkduzbxpdhtpvrzrfjndmsqfizmqxdxtpbpoemekvxzrrakwjxcxqsdasptruqmjtbaapgmkfnbwnlvzlxwdpzfjryanrmzmpzoefapmnsjdgecrdywsabctaegttffigupnwgakylngrrxurtotxqmzxvsqazajvrwsxyeyjteakeudzjxwbjvagnsjntskmocmpgkybqbnwvrwgoskzqkgffpsyhfmxhymqinrbohxlytsmoeleqrjvievpjipsgdkrqeuglrsjnmvdsihicsgkybcjltcswolpsfxdypmlbjotuxewskisnmczfgreuevnjssjifvlqlhkllifxrxkdbjlhcpegmtrelbosyajljvwwedtxbdccpnmreqaqjrxwulpunagwxesbilalrdniqbzxrbpcvmzpyqklsskpwctgqtrjwhrpisocwderqfiqxsdpkphjsapkvhvsqojyixaechvuoemmyqdlfkuzmlliugckuljfkljoshjhlvvlnywvjswvekfyqhjnsusefdtakejxbejrchoncklguqgnyrcslwztbstmycjziuskegagtlonducdogwbevugppsptdqbajmepmmizaycwcgmjeopbivsyphtvxvvgjbyxpgwpganjiaumojpyhhywosrmnouwpstgbrvhtlqcnmqbygbfnabesvshjmdbhyhirfrkqkmfwdgujhzyjdcbyuijjnkqluaczrnrbbwaeeupnwqzbsazplkyaxqorqsshhlljjlpphhedxdepgfgrqerpuhgmaawhnhqwsgnznrfmxjbdrkwjopylxezxgvetcvrwdewsxdeumhzfrvoilmvksuhyqltuimrnsphqslmgvmmojawwptghonigbdclqtbikiacwpjrbxhmzejozpypfixglatdvuogdoizdtsgsztsfcihtgwyqugeuahpuvvzmgarbsyuutmbxuisdfrvbxzxzhmuektssuktoknkfbmcwwubbnwenybmfqglaceuyqnoadzfenjcjfdlvcpiatuhjdujhaffqsvqvuxchgerokejovrqonxxstibunikiedfyahijobxyhimebctobsjudkqstbcxgixgrhpfiofpwruzvpqyjzvollheoldutddnksutjakhtghpxxnjykxjwgqmsvhnykclexepxqxqzghwfxfdhfmflesfabvanxlrurjtigkjotftqnwyskffpxlragrnfffawqtgyfpmzxfpkdpenxlewyxxgrkmwrmshhzfnorolyfxbvdrspxqnxnuoygkruczddgssygfymdcjgvdxutlrhffhnpyjuxmxefrelxezcgikdliyhvpocvvpkvagvmezrxffujeysplvavtjqjxsgujqsjznxforctwzecxyrkwufpdxadrgzczrnyelfschnagucguuqqqwitviynrypsrdswqxqsegulcwrwsjnihxedfcqychqumiscfkwmqqxunqrfbgqjdwmkyelbldxympctbzfupeocwhkypchuyvhybsbmvymjppfrqmlfrbkpjwpyyytytawuuyjrwxboogfessmltwdcssdqtwomymjskujjtmxiueopwacrwfuqazitvyhvlspvoaeipdsjhgyfjbxhityisidnhlksfznubucqxwaheamndjxmcxwufajmnveuwuoyosqnoqwvtjkwuhkzghvmjhawcfszbhzrbpgsidnbmxxihihnrfbamcyojqpkzodbejtmmipahojoysepzhpljpaugrghgjimtdahnpivdtlcnptnxjyiaafislqavamqgmxtdfoiaakorebqpbbpegawrqymqkewycsdjglkiwaacdqterkixkgraedtqirqmjtvsfhadhafktyrmkzmvidxmisfskvevpcnujqxrqedleuyowkjgphsxzzqlvujkwwgiodbfjesnbsbzcnftuzrvzjjudsgcqmmfpnmyrenuxotbbyvxyovzxgtcyzgqnsvcfhczoptnfnojnlinbfmylhdlijcvcxzjhdixuckaralemvsnbgooorayceuedtomzyjtctvtwgyiesxhynvogxnjdjphcftbefxgasawzagfugmuthjahylkhatlgpnkuksuesrduxkodwjzgubpsmzzmvkskzeglxaqrrvmrgcwcnvkhwzbibaxwnriowoavosminabvfxastkcrkdclgzjvqrjofjjvbyfragofeoazzeqljuypthkmywaffmcjkickqqsuhsviyovhitxeajqahshpejaqtcdkuvgdpclnsguabtgbfwdmrmbvydorfrbcokfdmtsgboidkpgpnmdeyhawkqqshtwxdbarwuxykgduxjlkxppwyruihkcqgynjcpbylayvgdqfpbqmshksyfbhrfxxemhgbkgmkhjtkzyzdqmxxwqvdtevyducpdksntgyaqtkrrkwiyuhukfadjvdnrievszilfinxbyrvknfihmetreydbcstkwoexwsfhfekfvfplmxszcosgovisnbemrjlndqwkvhqsofdbdychmupcsxvhazvrihhnxfyumonbvqeyoghccxfuwacxzxqkezxefxarnnujgyjugrzjoefmghjfhcrnbrtgouaehwnnxwkdplodpuqxdbemfwahptpfppjzowoltyqijfoabgzejerpatwponuefgdtcrgxswiddygeeflpjeelzccnsztxfyqhqyhkuppapvgvdtkmxraytcolbhkiiasaazkvqzvfxbaaxkoudovxrjkusxdazxaawmvoostlvvnsfbpjqkijvudpriqrfsrdfortimgdhtypunakzituezjyhbrpuksbamuiycngvlvpyvczfxvlwhjgicvempfobbwadkiavdswyuxdttoqaaykctprkwfmyeodowglzyjzuhencufcwdobydslazxadnftllhmjslfbrtdlahkgwlebdpdeofidldoymakfnpgekmsltcrrnxvspywfggjrmxryybdltmsfykstmlnzjitaipfoyohkmzimcozxardydxtpjgquoluzbznzqvlewtqyhryjldjoadgjlyfckzbnbootlzxhupieggntjxilcqxnocpyesnhjbauaxcvmkzusmodlyonoldequfunsbwudquaurogsiyhydswsimflrvfwruouskxjfzfynmrymyyqsvkajpnanvyepnzixyteyafnmwnbwmtojdpsucthxtopgpxgnsmnsrdhpskledapiricvdmtwaifrhnebzuttzckroywranbrvgmashxurelyrrbslxnmzyeowchwpjplrdnjlkfcoqdhheavbnhdlltjpahflwscafnnsspikuqszqpcdyfrkaabdigogatgiitadlinfyhgowjuvqlhrniuvrketfmboibttkgakohbmsvhigqztbvrsgxlnjndrqwmcdnntwofojpyrhamivfcdcotodwhvtuyyjlthbaxmrvfzxrhvzkydartfqbalxyjilepmemawjfxhzecyqcdswxxmaaxxyifmouauibstgpcfwgfmjlfhketkeshfcorqirmssfnbuqiqwqfhbmol";
        String[] words5 = {
                "toiscumkhociglkvispihvyoatxcx",
                "ndojyyephstlonsplrettspwepipw",
                "yzfkyoqlkrmmfirchzrphveuwmvga",
                "mxxihihnrfbamcyojqpkzodbejtmm",
                "fenjcjfdlvcpiatuhjdujhaffqsvq",
                "ehghndyqjodnnblfwmaygdstotfkv",
                "heoldutddnksutjakhtghpxxnjykx",
                "cvrwdewsxdeumhzfrvoilmvksuhyq",
                "ftqjvzyssocftjwemroghrncynmtc",
                "idiwclhuepgyynoslhzahtdqwlikt",
                "eurttrfrmstrbeokzhuzvbfmwywoh",
                "jxlluilzpysjcnwguyofnhfvhacez",
                "uskegagtlonducdogwbevugppsptd",
                "xmcxwufajmnveuwuoyosqnoqwvtjk",
                "wolpsfxdypmlbjotuxewskisnmczf",
                "fjryanrmzmpzoefapmnsjdgecrdyw",
                "jgmxawmndhsvwnjdjvjtxcsjapfog",
                "wuhkzghvmjhawcfszbhzrbpgsidnb",
                "yelbldxympctbzfupeocwhkypchuy",
                "vzduzxudwwqhpftwdspuimioanlzo",
                "bdpdeofidldoymakfnpgekmsltcrr",
                "fmyeodowglzyjzuhencufcwdobyds",
                "dhtypunakzituezjyhbrpuksbamui",
                "bdmiruibwznqcuczculujfiavzwyn",
                "eudzjxwbjvagnsjntskmocmpgkybq",
                "tuynydoakejmwkvojuwbfltqjfgxq",
                "psrdswqxqsegulcwrwsjnihxedfcq",
                "cokfdmtsgboidkpgpnmdeyhawkqqs",
                "fujhvgzdussqbwynylzvtjapvqtid",
                "rqeuglrsjnmvdsihicsgkybcjltcs",
                "vhybsbmvymjppfrqmlfrbkpjwpyyy",
                "aukagphzycvjtvwdhhxzagkevvucc",
                "hwkduzbxpdhtpvrzrfjndmsqfizmq",
                "ywnuzzmxeppokxksrfwrpuzqhjgqr",
                "qbajmepmmizaycwcgmjeopbivsyph",
                "uamscbxnqnfmmjyehvidnoimmxmtc",
                "nxvspywfggjrmxryybdltmsfykstm",
                "amrjbrsiovrxmqsyxhqmritjeauwq",
                "yorwboxdauhrkxehiwaputeouwxdf",
                "qkewycsdjglkiwaacdqterkixkgra",
                "ycngvlvpyvczfxvlwhjgicvempfob",
                "jgphsxzzqlvujkwwgiodbfjesnbsb",
                "mkxhemwbbclwdxwgngicplzgajmar",
                "mryvkeevlthvflsvognbxfjilwkdn",
                "mezrxffujeysplvavtjqjxsgujqsj",
                "rtotxqmzxvsqazajvrwsxyeyjteak",
                "sabctaegttffigupnwgakylngrrxu",
                "xccuoccdkbboymjtimdrmerspxpkt",
                "xusnnvngksbjabqjaohdvrniezhmx",
                "oyuejenqgjheulkxjnqkwvzznricl",
                "mxszcosgovisnbemrjlndqwkvhqso",
                "wsgnznrfmxjbdrkwjopylxezxgvet",
                "dxmisfskvevpcnujqxrqedleuyowk",
                "dhrgijeplijcvqbormrqglgmzsprt",
                "vuxchgerokejovrqonxxstibuniki",
                "lumyzmnzjzhzfpslwsukykwckvkts",
                "inwkbqmcobubjjpshucechrqrffqs",
                "ywtxruxokcubekzcrqengviwbtgnz",
                "ccpnmreqaqjrxwulpunagwxesbila",
                "pesxtpypenunfpjuyoevzztctecil",
                "sygfymdcjgvdxutlrhffhnpyjuxmx",
                "uisdfrvbxzxzhmuektssuktoknkfb",
                "cejvgynwouzhtfwuuukdbwpmkjrqx",
                "oudcoagcxjcuqvenznxxnprgvhasf",
                "sxnlkwgpbznzszyudpwrlgrdgwdyh",
                "qqbxkaqcyhiobvtqgqruumvvhxolb",
                "mkhleanvfpemuublnnyzfabtxsest",
                "bibaxwnriowoavosminabvfxastkc",
                "bcxgixgrhpfiofpwruzvpqyjzvoll",
                "lzccnsztxfyqhqyhkuppapvgvdtkm",
                "pdjkpshvrmqlhindhabubyokzdfrw",
                "qbbnhwpdokcpfpxinlfmkfrfqrtzk",
                "rnyelfschnagucguuqqqwitviynry",
                "qtrjwhrpisocwderqfiqxsdpkphjs",
                "vxttqosgpplkmxwgmsgtpantazppg",
                "tyisidnhlksfznubucqxwaheamndj",
                "kgaqzsckonjuhxdhqztjfxstjvikd",
                "jeuslzsdwvuoodipdpnlhdihaywzm",
                "vdzrwwkqvacxwgdhffyvjldgvchoi",
                "cftbefxgasawzagfugmuthjahylkh",
                "xraytcolbhkiiasaazkvqzvfxbaax",
                "oyqtzozufvvlktnvahvsseymtpeyf",
                "rnnujgyjugrzjoefmghjfhcrnbrtg",
                "rfzvgvptbgpwajgtysligupoqeoqx",
                "igbdclqtbikiacwpjrbxhmzejozpy",
                "dyzwwxgdbeqwlldyezmkopktzugxg",
                "hmetreydbcstkwoexwsfhfekfvfpl",
                "zcnftuzrvzjjudsgcqmmfpnmyrenu",
                "zzmvkskzeglxaqrrvmrgcwcnvkhwz",
                "vjswvekfyqhjnsusefdtakejxbejr",
                "rwwzwbcjwiqzkwzfuxfclmsxpdyvf",
                "fdbdychmupcsxvhazvrihhnxfyumo",
                "vdtevyducpdksntgyaqtkrrkwiyuh",
                "nbvqeyoghccxfuwacxzxqkezxefxa",
                "vpgbefpqpsjmdecmixmmbsjxzwvjd",
                "jwgqmsvhnykclexepxqxqzghwfxfd",
                "olyfxbvdrspxqnxnuoygkruczddgs",
                "qgmxtdfoiaakorebqpbbpegawrqym",
                "liaivbhcgvjjnxpggrewglalthmzv",
                "choncklguqgnyrcslwztbstmycjzi",
                "fpkdpenxlewyxxgrkmwrmshhzfnor",
                "hhhcaqxbqpthuaafwgrouaxonzocl",
                "ipahojoysepzhpljpaugrghgjimtd",
                "wosrmnouwpstgbrvhtlqcnmqbygbf",
                "nwyskffpxlragrnfffawqtgyfpmzx",
                "bcvvadhnssbvneecglnqxhavhvxpk",
                "hoavxqksjreddpmibbodtbhzfehgl",
                "lazxadnftllhmjslfbrtdlahkgwle",
                "uuukupjmbbvshzxyniaowdjamlfss",
                "tpqtazbphmfoluliznftodyguessh",
                "ychqumiscfkwmqqxunqrfbgqjdwmk",
                "rkdclgzjvqrjofjjvbyfragofeoaz",
                "pphhedxdepgfgrqerpuhgmaawhnhq",
                "cacrsvutylalqrykehjuofisdookj",
                "kyldfriuvjranikluqtjjcoiqffdx",
                "bnwvrwgoskzqkgffpsyhfmxhymqin",
                "uzmlliugckuljfkljoshjhlvvlnyw",
                "abfxqbdqnexvwsvzvcsbrmkbkuzsd",
                "xotbbyvxyovzxgtcyzgqnsvcfhczo",
                "bwtpqcqhvyyssvfknfhxvtodpzipu",
                "nsfbpjqkijvudpriqrfsrdfortimg",
                "tgwyqugeuahpuvvzmgarbsyuutmbx",
                "upnwqzbsazplkyaxqorqsshhlljjl",
                "edfyahijobxyhimebctobsjudkqst",
                "ialhfmgjohzoxvdaxuywfqrgmyahh",
                "jlhcpegmtrelbosyajljvwwedtxbd",
                "tpfppjzowoltyqijfoabgzejerpat",
                "mgogyhzpmsdemugqkspsmoppwbnwa",
                "nubmpwcdqkvhwfuvcahwibniohiqy",
                "ukfadjvdnrievszilfinxbyrvknfi",
                "dgnepdiimmkcxhattwglbkicvsfsw",
                "syqxmarjkshjhxobandwyzggjibjg",
                "bnwxjytnaejivivriamhgqsskqhnq",
                "hzyjdcbyuijjnkqluaczrnrbbwaee",
                "yscnqoohcsxenypyqhfklloudgmkl",
                "habidqszhxorzfypcjcnopzwigmbz",
                "wjdqxdrlsqvsxwxpqkljeyjpulbsw",
                "tytawuuyjrwxboogfessmltwdcssd",
                "pfixglatdvuogdoizdtsgsztsfcih",
                "apkvhvsqojyixaechvuoemmyqdlfk",
                "ouaehwnnxwkdplodpuqxdbemfwahp",
                "ixuckaralemvsnbgooorayceuedto",
                "ymxdjrqikughquwtenyucjdgrmipi",
                "smrwrlkvpnhqrvpdekmtpdfuxzjwp",
                "bhjakgajafgzxpqckmhdbbnqmcszp",
                "beqsmluixgsliatukrecgoldmzfhw",
                "greuevnjssjifvlqlhkllifxrxkdb",
                "yzsqcrdchhdqprtkkjsccowrjtyjj",
                "sviyovhitxeajqahshpejaqtcdkuv",
                "qtwomymjskujjtmxiueopwacrwfuq",
                "mzyjtctvtwgyiesxhynvogxnjdjph",
                "dyfbxcaypyquodcpwxkstbthuvjqg",
                "hfmflesfabvanxlrurjtigkjotftq",
                "mxydechlraajjmoqpcyoqmrjwoium",
                "nabesvshjmdbhyhirfrkqkmfwdguj",
                "bhrfxxemhgbkgmkhjtkzyzdqmxxwq",
                "gziobrjeanlvyukwlscexbkibvdjh",
                "mcwwubbnwenybmfqglaceuyqnoadz",
                "xyzvyblypeongzrttvwqzmrccwkzi",
                "ncfalqenfcswgerbfcqsapzdtscnz",
                "dtqpezboimeuyyujfjxkdmbjpizpq",
                "wmuhplfueqnvnhukgjarxlxvwmriq",
                "qwapdkoqswyclqyvbvpedzyoyedvu",
                "uoqbztnftzgahhxwxbgkilnmzfydy",
                "zsddaahohbszhqxxgripqlwlomjbw",
                "bwadkiavdswyuxdttoqaaykctprkw",
                "eixdbntdfcaeatyyainfpkclbgaaq",
                "nmjnpttflsmjifknezrneedvgzfmn",
                "avlzyhfmeasmgrjawongccgfbgoua",
                "kklimhhjqkmuaifnodtpredhqygme",
                "xzbwenvteifxuuefnimnadwxhruvo",
                "ugmwlmidtxkvqhbuaecevwhmwkfqm",
                "rhpyjfxbjjryslfpqoiphrwfjqqha",
                "eeaipxrokncholathupdetgaktmvm",
                "ltuimrnsphqslmgvmmojawwptghon",
                "azitvyhvlspvoaeipdsjhgyfjbxhi",
                "efrelxezcgikdliyhvpocvvpkvagv",
                "znxforctwzecxyrkwufpdxadrgzcz",
                "kcqgynjcpbylayvgdqfpbqmshksyf",
                "hrljvedsywrlyccpaowjaqyfaqioe",
                "cjmfyvfybxiuqtkdlzqedjxxbvdsf",
                "zeqljuypthkmywaffmcjkickqqsuh",
                "wnfzoyvkiogisdfyjmfomcazigukq",
                "zyaaqxorqxbkenscbveqbaociwmqx",
                "ahnpivdtlcnptnxjyiaafislqavam",
                "edtqirqmjtvsfhadhafktyrmkzmvi",
                "wponuefgdtcrgxswiddygeeflpjee",
                "xozgwhtbhlkvrzismnozqpfthajaf",
                "ptnfnojnlinbfmylhdlijcvcxzjhd",
                "uxekzlgigjpsukjvsdihrjzgovnre",
                "rbohxlytsmoeleqrjvievpjipsgdk",
                "fxtzaxpcfrcovwgrcwqptoekhmgpo",
                "tvxvvgjbyxpgwpganjiaumojpyhhy",
                "vqjjhfaupylefbvbsbhdncsshmrhx",
                "urhedneauccrkyjfiptjfxmpxlssr",
                "ltvgknnlodtbhnbhjkmuhwxvzgmkh",
                "ucztsneqttsuirmjriohhgunzatyf",
                "rbzryfaeuqkfxrbldyusoeoldpbwa",
                "atlgpnkuksuesrduxkodwjzgubpsm",
                "lrdniqbzxrbpcvmzpyqklsskpwctg",
                "qvnvgzkyhistydagsgnujiviyijdn",
                "uzatydzcnktnkeyztoqvogodxxznh",
                "ocbvphmtpwhcgjbnmxgidtlqcnnwt",
                "koudovxrjkusxdazxaawmvoostlvv",
                "ptruqmjtbaapgmkfnbwnlvzlxwdpz",
                "xdxtpbpoemekvxzrrakwjxcxqsdas",
                "gdpclnsguabtgbfwdmrmbvydorfrb",
                "htwxdbarwuxykgduxjlkxppwyruih"
        };
        new Solution().findSubstring(str, words5);

        String str = "ejwwmybnorgshugzmoxopwuvshlcwasclobxmckcvtxfndeztdqiakfusswqsovdfwatanwxgtctyjvsmlcoxijrahivwfybbbudosawnfpmomgczirzscqvlaqhfqkithlhbodptvdhjljltckogcjsdbbktotnxgwyuapnxuwgfirbmdrvgapldsvwgqjfxggtixjhshnzphcemtzsvodygbxpriwqockyavfscvtsewyqpxlnnqnvrkmjtjbjllilinflkbfoxdhocsbpirmcbznuioevcojkdqvoraeqdlhffkwqbjsdkfxstdpxryixrdligpzldgtiqryuasxmxwgtcwsvwasngdwovxzafuixmjrobqbbnhwpdokcpfpxinlfmkfrfqrtzkhabidqszhxorzfypcjcnopzwigmbznmjnpttflsmjifknezrneedvgzfmnhoavxqksjreddpmibbodtbhzfehgluuukupjmbbvshzxyniaowdjamlfssndojyyephstlonsplrettspwepipwcjmfyvfybxiuqtkdlzqedjxxbvdsfurhedneauccrkyjfiptjfxmpxlssrkyldfriuvjranikluqtjjcoiqffdxaukagphzycvjtvwdhhxzagkevvuccxccuoccdkbboymjtimdrmerspxpktsmrwrlkvpnhqrvpdekmtpdfuxzjwpvqjjhfaupylefbvbsbhdncsshmrhxoyuejenqgjheulkxjnqkwvzznriclrbzryfaeuqkfxrbldyusoeoldpbwadhrgijeplijcvqbormrqglgmzsprtmryvkeevlthvflsvognbxfjilwkdndyzwwxgdbeqwlldyezmkopktzugxgkklimhhjqkmuaifnodtpredhqygmedtqpezboimeuyyujfjxkdmbjpizpqltvgknnlodtbhnbhjkmuhwxvzgmkhbcvvadhnssbvneecglnqxhavhvxpkjxlluilzpysjcnwguyofnhfvhaceztoiscumkhociglkvispihvyoatxcxbeqsmluixgsliatukrecgoldmzfhwkgaqzsckonjuhxdhqztjfxstjvikdrhpyjfxbjjryslfpqoiphrwfjqqhaamrjbrsiovrxmqsyxhqmritjeauwqbwtpqcqhvyyssvfknfhxvtodpzipueixdbntdfcaeatyyainfpkclbgaaqrwwzwbcjwiqzkwzfuxfclmsxpdyvfbnwxjytnaejivivriamhgqsskqhnqeurttrfrmstrbeokzhuzvbfmwywohmgogyhzpmsdemugqkspsmoppwbnwabdmiruibwznqcuczculujfiavzwynsyqxmarjkshjhxobandwyzggjibjgzyaaqxorqxbkenscbveqbaociwmqxxyzvyblypeongzrttvwqzmrccwkzidyfbxcaypyquodcpwxkstbthuvjqgialhfmgjohzoxvdaxuywfqrgmyahhtpqtazbphmfoluliznftodyguesshcacrsvutylalqrykehjuofisdookjhrljvedsywrlyccpaowjaqyfaqioesxnlkwgpbznzszyudpwrlgrdgwdyhucztsneqttsuirmjriohhgunzatyfrfzvgvptbgpwajgtysligupoqeoqxoyqtzozufvvlktnvahvsseymtpeyfvxttqosgpplkmxwgmsgtpantazppgnubmpwcdqkvhwfuvcahwibniohiqyywnuzzmxeppokxksrfwrpuzqhjgqryorwboxdauhrkxehiwaputeouwxdfoudcoagcxjcuqvenznxxnprgvhasffxtzaxpcfrcovwgrcwqptoekhmgpoywtxruxokcubekzcrqengviwbtgnzvdzrwwkqvacxwgdhffyvjldgvchoiwnfzoyvkiogisdfyjmfomcazigukqlumyzmnzjzhzfpslwsukykwckvktswjdqxdrlsqvsxwxpqkljeyjpulbswwmuhplfueqnvnhukgjarxlxvwmriqjgmxawmndhsvwnjdjvjtxcsjapfogpesxtpypenunfpjuyoevzztctecilqqbxkaqcyhiobvtqgqruumvvhxolbyzsqcrdchhdqprtkkjsccowrjtyjjmkhleanvfpemuublnnyzfabtxsestncfalqenfcswgerbfcqsapzdtscnzugmwlmidtxkvqhbuaecevwhmwkfqmvpgbefpqpsjmdecmixmmbsjxzwvjdmxydechlraajjmoqpcyoqmrjwoiumuzatydzcnktnkeyztoqvogodxxznhvzduzxudwwqhpftwdspuimioanlzobhjakgajafgzxpqckmhdbbnqmcszpuoqbztnftzgahhxwxbgkilnmzfydyxusnnvngksbjabqjaohdvrniezhmxmkxhemwbbclwdxwgngicplzgajmaryzfkyoqlkrmmfirchzrphveuwmvgaxzbwenvteifxuuefnimnadwxhruvoavlzyhfmeasmgrjawongccgfbgoualiaivbhcgvjjnxpggrewglalthmzvgziobrjeanlvyukwlscexbkibvdjhdgnepdiimmkcxhattwglbkicvsfswocbvphmtpwhcgjbnmxgidtlqcnnwtfujhvgzdussqbwynylzvtjapvqtidpdjkpshvrmqlhindhabubyokzdfrwqvnvgzkyhistydagsgnujiviyijdnabfxqbdqnexvwsvzvcsbrmkbkuzsdehghndyqjodnnblfwmaygdstotfkvxozgwhtbhlkvrzismnozqpfthajafuxekzlgigjpsukjvsdihrjzgovnreqwapdkoqswyclqyvbvpedzyoyedvuuamscbxnqnfmmjyehvidnoimmxmtcinwkbqmcobubjjpshucechrqrffqsyscnqoohcsxenypyqhfklloudgmklcejvgynwouzhtfwuuukdbwpmkjrqxeeaipxrokncholathupdetgaktmvmftqjvzyssocftjwemroghrncynmtchhhcaqxbqpthuaafwgrouaxonzocljeuslzsdwvuoodipdpnlhdihaywzmymxdjrqikughquwtenyucjdgrmipiidiwclhuepgyynoslhzahtdqwliktzsddaahohbszhqxxgripqlwlomjbwtuynydoakejmwkvojuwbfltqjfgxqhwkduzbxpdhtpvrzrfjndmsqfizmqxdxtpbpoemekvxzrrakwjxcxqsdasptruqmjtbaapgmkfnbwnlvzlxwdpzfjryanrmzmpzoefapmnsjdgecrdywsabctaegttffigupnwgakylngrrxurtotxqmzxvsqazajvrwsxyeyjteakeudzjxwbjvagnsjntskmocmpgkybqbnwvrwgoskzqkgffpsyhfmxhymqinrbohxlytsmoeleqrjvievpjipsgdkrqeuglrsjnmvdsihicsgkybcjltcswolpsfxdypmlbjotuxewskisnmczfgreuevnjssjifvlqlhkllifxrxkdbjlhcpegmtrelbosyajljvwwedtxbdccpnmreqaqjrxwulpunagwxesbilalrdniqbzxrbpcvmzpyqklsskpwctgqtrjwhrpisocwderqfiqxsdpkphjsapkvhvsqojyixaechvuoemmyqdlfkuzmlliugckuljfkljoshjhlvvlnywvjswvekfyqhjnsusefdtakejxbejrchoncklguqgnyrcslwztbstmycjziuskegagtlonducdogwbevugppsptdqbajmepmmizaycwcgmjeopbivsyphtvxvvgjbyxpgwpganjiaumojpyhhywosrmnouwpstgbrvhtlqcnmqbygbfnabesvshjmdbhyhirfrkqkmfwdgujhzyjdcbyuijjnkqluaczrnrbbwaeeupnwqzbsazplkyaxqorqsshhlljjlpphhedxdepgfgrqerpuhgmaawhnhqwsgnznrfmxjbdrkwjopylxezxgvetcvrwdewsxdeumhzfrvoilmvksuhyqltuimrnsphqslmgvmmojawwptghonigbdclqtbikiacwpjrbxhmzejozpypfixglatdvuogdoizdtsgsztsfcihtgwyqugeuahpuvvzmgarbsyuutmbxuisdfrvbxzxzhmuektssuktoknkfbmcwwubbnwenybmfqglaceuyqnoadzfenjcjfdlvcpiatuhjdujhaffqsvqvuxchgerokejovrqonxxstibunikiedfyahijobxyhimebctobsjudkqstbcxgixgrhpfiofpwruzvpqyjzvollheoldutddnksutjakhtghpxxnjykxjwgqmsvhnykclexepxqxqzghwfxfdhfmflesfabvanxlrurjtigkjotftqnwyskffpxlragrnfffawqtgyfpmzxfpkdpenxlewyxxgrkmwrmshhzfnorolyfxbvdrspxqnxnuoygkruczddgssygfymdcjgvdxutlrhffhnpyjuxmxefrelxezcgikdliyhvpocvvpkvagvmezrxffujeysplvavtjqjxsgujqsjznxforctwzecxyrkwufpdxadrgzczrnyelfschnagucguuqqqwitviynrypsrdswqxqsegulcwrwsjnihxedfcqychqumiscfkwmqqxunqrfbgqjdwmkyelbldxympctbzfupeocwhkypchuyvhybsbmvymjppfrqmlfrbkpjwpyyytytawuuyjrwxboogfessmltwdcssdqtwomymjskujjtmxiueopwacrwfuqazitvyhvlspvoaeipdsjhgyfjbxhityisidnhlksfznubucqxwaheamndjxmcxwufajmnveuwuoyosqnoqwvtjkwuhkzghvmjhawcfszbhzrbpgsidnbmxxihihnrfbamcyojqpkzodbejtmmipahojoysepzhpljpaugrghgjimtdahnpivdtlcnptnxjyiaafislqavamqgmxtdfoiaakorebqpbbpegawrqymqkewycsdjglkiwaacdqterkixkgraedtqirqmjtvsfhadhafktyrmkzmvidxmisfskvevpcnujqxrqedleuyowkjgphsxzzqlvujkwwgiodbfjesnbsbzcnftuzrvzjjudsgcqmmfpnmyrenuxotbbyvxyovzxgtcyzgqnsvcfhczoptnfnojnlinbfmylhdlijcvcxzjhdixuckaralemvsnbgooorayceuedtomzyjtctvtwgyiesxhynvogxnjdjphcftbefxgasawzagfugmuthjahylkhatlgpnkuksuesrduxkodwjzgubpsmzzmvkskzeglxaqrrvmrgcwcnvkhwzbibaxwnriowoavosminabvfxastkcrkdclgzjvqrjofjjvbyfragofeoazzeqljuypthkmywaffmcjkickqqsuhsviyovhitxeajqahshpejaqtcdkuvgdpclnsguabtgbfwdmrmbvydorfrbcokfdmtsgboidkpgpnmdeyhawkqqshtwxdbarwuxykgduxjlkxppwyruihkcqgynjcpbylayvgdqfpbqmshksyfbhrfxxemhgbkgmkhjtkzyzdqmxxwqvdtevyducpdksntgyaqtkrrkwiyuhukfadjvdnrievszilfinxbyrvknfihmetreydbcstkwoexwsfhfekfvfplmxszcosgovisnbemrjlndqwkvhqsofdbdychmupcsxvhazvrihhnxfyumonbvqeyoghccxfuwacxzxqkezxefxarnnujgyjugrzjoefmghjfhcrnbrtgouaehwnnxwkdplodpuqxdbemfwahptpfppjzowoltyqijfoabgzejerpatwponuefgdtcrgxswiddygeeflpjeelzccnsztxfyqhqyhkuppapvgvdtkmxraytcolbhkiiasaazkvqzvfxbaaxkoudovxrjkusxdazxaawmvoostlvvnsfbpjqkijvudpriqrfsrdfortimgdhtypunakzituezjyhbrpuksbamuiycngvlvpyvczfxvlwhjgicvempfobbwadkiavdswyuxdttoqaaykctprkwfmyeodowglzyjzuhencufcwdobydslazxadnftllhmjslfbrtdlahkgwlebdpdeofidldoymakfnpgekmsltcrrnxvspywfggjrmxryybdltmsfykstmlnzjitaipfoyohkmzimcozxardydxtpjgquoluzbznzqvlewtqyhryjldjoadgjlyfckzbnbootlzxhupieggntjxilcqxnocpyesnhjbauaxcvmkzusmodlyonoldequfunsbwudquaurogsiyhydswsimflrvfwruouskxjfzfynmrymyyqsvkajpnanvyepnzixyteyafnmwnbwmtojdpsucthxtopgpxgnsmnsrdhpskledapiricvdmtwaifrhnebzuttzckroywranbrvgmashxurelyrrbslxnmzyeowchwpjplrdnjlkfcoqdhheavbnhdlltjpahflwscafnnsspikuqszqpcdyfrkaabdigogatgiitadlinfyhgowjuvqlhrniuvrketfmboibttkgakohbmsvhigqztbvrsgxlnjndrqwmcdnntwofojpyrhamivfcdcotodwhvtuyyjlthbaxmrvfzxrhvzkydartfqbalxyjilepmemawjfxhzecyqcdswxxmaaxxyifmouauibstgpcfwgfmjlfhketkeshfcorqirmssfnbuqiqwqfhbmol";
        String[] words5 = {
                "toiscumkhociglkvispihvyoatxcx",
                "ndojyyephstlonsplrettspwepipw",
                "yzfkyoqlkrmmfirchzrphveuwmvga",
                "mxxihihnrfbamcyojqpkzodbejtmm",
                "fenjcjfdlvcpiatuhjdujhaffqsvq",
                "ehghndyqjodnnblfwmaygdstotfkv",
                "heoldutddnksutjakhtghpxxnjykx",
                "cvrwdewsxdeumhzfrvoilmvksuhyq",
                "ftqjvzyssocftjwemroghrncynmtc",
                "idiwclhuepgyynoslhzahtdqwlikt",
                "eurttrfrmstrbeokzhuzvbfmwywoh",
                "jxlluilzpysjcnwguyofnhfvhacez",
                "uskegagtlonducdogwbevugppsptd",
                "xmcxwufajmnveuwuoyosqnoqwvtjk",
                "wolpsfxdypmlbjotuxewskisnmczf",
                "fjryanrmzmpzoefapmnsjdgecrdyw",
                "jgmxawmndhsvwnjdjvjtxcsjapfog",
                "wuhkzghvmjhawcfszbhzrbpgsidnb",
                "yelbldxympctbzfupeocwhkypchuy",
                "vzduzxudwwqhpftwdspuimioanlzo",
                "bdpdeofidldoymakfnpgekmsltcrr",
                "fmyeodowglzyjzuhencufcwdobyds",
                "dhtypunakzituezjyhbrpuksbamui",
                "bdmiruibwznqcuczculujfiavzwyn",
                "eudzjxwbjvagnsjntskmocmpgkybq",
                "tuynydoakejmwkvojuwbfltqjfgxq",
                "psrdswqxqsegulcwrwsjnihxedfcq",
                "cokfdmtsgboidkpgpnmdeyhawkqqs",
                "fujhvgzdussqbwynylzvtjapvqtid",
                "rqeuglrsjnmvdsihicsgkybcjltcs",
                "vhybsbmvymjppfrqmlfrbkpjwpyyy",
                "aukagphzycvjtvwdhhxzagkevvucc",
                "hwkduzbxpdhtpvrzrfjndmsqfizmq",
                "ywnuzzmxeppokxksrfwrpuzqhjgqr",
                "qbajmepmmizaycwcgmjeopbivsyph",
                "uamscbxnqnfmmjyehvidnoimmxmtc",
                "nxvspywfggjrmxryybdltmsfykstm",
                "amrjbrsiovrxmqsyxhqmritjeauwq",
                "yorwboxdauhrkxehiwaputeouwxdf",
                "qkewycsdjglkiwaacdqterkixkgra",
                "ycngvlvpyvczfxvlwhjgicvempfob",
                "jgphsxzzqlvujkwwgiodbfjesnbsb",
                "mkxhemwbbclwdxwgngicplzgajmar",
                "mryvkeevlthvflsvognbxfjilwkdn",
                "mezrxffujeysplvavtjqjxsgujqsj",
                "rtotxqmzxvsqazajvrwsxyeyjteak",
                "sabctaegttffigupnwgakylngrrxu",
                "xccuoccdkbboymjtimdrmerspxpkt",
                "xusnnvngksbjabqjaohdvrniezhmx",
                "oyuejenqgjheulkxjnqkwvzznricl",
                "mxszcosgovisnbemrjlndqwkvhqso",
                "wsgnznrfmxjbdrkwjopylxezxgvet",
                "dxmisfskvevpcnujqxrqedleuyowk",
                "dhrgijeplijcvqbormrqglgmzsprt",
                "vuxchgerokejovrqonxxstibuniki",
                "lumyzmnzjzhzfpslwsukykwckvkts",
                "inwkbqmcobubjjpshucechrqrffqs",
                "ywtxruxokcubekzcrqengviwbtgnz",
                "ccpnmreqaqjrxwulpunagwxesbila",
                "pesxtpypenunfpjuyoevzztctecil",
                "sygfymdcjgvdxutlrhffhnpyjuxmx",
                "uisdfrvbxzxzhmuektssuktoknkfb",
                "cejvgynwouzhtfwuuukdbwpmkjrqx",
                "oudcoagcxjcuqvenznxxnprgvhasf",
                "sxnlkwgpbznzszyudpwrlgrdgwdyh",
                "qqbxkaqcyhiobvtqgqruumvvhxolb",
                "mkhleanvfpemuublnnyzfabtxsest",
                "bibaxwnriowoavosminabvfxastkc",
                "bcxgixgrhpfiofpwruzvpqyjzvoll",
                "lzccnsztxfyqhqyhkuppapvgvdtkm",
                "pdjkpshvrmqlhindhabubyokzdfrw",
                "qbbnhwpdokcpfpxinlfmkfrfqrtzk",
                "rnyelfschnagucguuqqqwitviynry",
                "qtrjwhrpisocwderqfiqxsdpkphjs",
                "vxttqosgpplkmxwgmsgtpantazppg",
                "tyisidnhlksfznubucqxwaheamndj",
                "kgaqzsckonjuhxdhqztjfxstjvikd",
                "jeuslzsdwvuoodipdpnlhdihaywzm",
                "vdzrwwkqvacxwgdhffyvjldgvchoi",
                "cftbefxgasawzagfugmuthjahylkh",
                "xraytcolbhkiiasaazkvqzvfxbaax",
                "oyqtzozufvvlktnvahvsseymtpeyf",
                "rnnujgyjugrzjoefmghjfhcrnbrtg",
                "rfzvgvptbgpwajgtysligupoqeoqx",
                "igbdclqtbikiacwpjrbxhmzejozpy",
                "dyzwwxgdbeqwlldyezmkopktzugxg",
                "hmetreydbcstkwoexwsfhfekfvfpl",
                "zcnftuzrvzjjudsgcqmmfpnmyrenu",
                "zzmvkskzeglxaqrrvmrgcwcnvkhwz",
                "vjswvekfyqhjnsusefdtakejxbejr",
                "rwwzwbcjwiqzkwzfuxfclmsxpdyvf",
                "fdbdychmupcsxvhazvrihhnxfyumo",
                "vdtevyducpdksntgyaqtkrrkwiyuh",
                "nbvqeyoghccxfuwacxzxqkezxefxa",
                "vpgbefpqpsjmdecmixmmbsjxzwvjd",
                "jwgqmsvhnykclexepxqxqzghwfxfd",
                "olyfxbvdrspxqnxnuoygkruczddgs",
                "qgmxtdfoiaakorebqpbbpegawrqym",
                "liaivbhcgvjjnxpggrewglalthmzv",
                "choncklguqgnyrcslwztbstmycjzi",
                "fpkdpenxlewyxxgrkmwrmshhzfnor",
                "hhhcaqxbqpthuaafwgrouaxonzocl",
                "ipahojoysepzhpljpaugrghgjimtd",
                "wosrmnouwpstgbrvhtlqcnmqbygbf",
                "nwyskffpxlragrnfffawqtgyfpmzx",
                "bcvvadhnssbvneecglnqxhavhvxpk",
                "hoavxqksjreddpmibbodtbhzfehgl",
                "lazxadnftllhmjslfbrtdlahkgwle",
                "uuukupjmbbvshzxyniaowdjamlfss",
                "tpqtazbphmfoluliznftodyguessh",
                "ychqumiscfkwmqqxunqrfbgqjdwmk",
                "rkdclgzjvqrjofjjvbyfragofeoaz",
                "pphhedxdepgfgrqerpuhgmaawhnhq",
                "cacrsvutylalqrykehjuofisdookj",
                "kyldfriuvjranikluqtjjcoiqffdx",
                "bnwvrwgoskzqkgffpsyhfmxhymqin",
                "uzmlliugckuljfkljoshjhlvvlnyw",
                "abfxqbdqnexvwsvzvcsbrmkbkuzsd",
                "xotbbyvxyovzxgtcyzgqnsvcfhczo",
                "bwtpqcqhvyyssvfknfhxvtodpzipu",
                "nsfbpjqkijvudpriqrfsrdfortimg",
                "tgwyqugeuahpuvvzmgarbsyuutmbx",
                "upnwqzbsazplkyaxqorqsshhlljjl",
                "edfyahijobxyhimebctobsjudkqst",
                "ialhfmgjohzoxvdaxuywfqrgmyahh",
                "jlhcpegmtrelbosyajljvwwedtxbd",
                "tpfppjzowoltyqijfoabgzejerpat",
                "mgogyhzpmsdemugqkspsmoppwbnwa",
                "nubmpwcdqkvhwfuvcahwibniohiqy",
                "ukfadjvdnrievszilfinxbyrvknfi",
                "dgnepdiimmkcxhattwglbkicvsfsw",
                "syqxmarjkshjhxobandwyzggjibjg",
                "bnwxjytnaejivivriamhgqsskqhnq",
                "hzyjdcbyuijjnkqluaczrnrbbwaee",
                "yscnqoohcsxenypyqhfklloudgmkl",
                "habidqszhxorzfypcjcnopzwigmbz",
                "wjdqxdrlsqvsxwxpqkljeyjpulbsw",
                "tytawuuyjrwxboogfessmltwdcssd",
                "pfixglatdvuogdoizdtsgsztsfcih",
                "apkvhvsqojyixaechvuoemmyqdlfk",
                "ouaehwnnxwkdplodpuqxdbemfwahp",
                "ixuckaralemvsnbgooorayceuedto",
                "ymxdjrqikughquwtenyucjdgrmipi",
                "smrwrlkvpnhqrvpdekmtpdfuxzjwp",
                "bhjakgajafgzxpqckmhdbbnqmcszp",
                "beqsmluixgsliatukrecgoldmzfhw",
                "greuevnjssjifvlqlhkllifxrxkdb",
                "yzsqcrdchhdqprtkkjsccowrjtyjj",
                "sviyovhitxeajqahshpejaqtcdkuv",
                "qtwomymjskujjtmxiueopwacrwfuq",
                "mzyjtctvtwgyiesxhynvogxnjdjph",
                "dyfbxcaypyquodcpwxkstbthuvjqg",
                "hfmflesfabvanxlrurjtigkjotftq",
                "mxydechlraajjmoqpcyoqmrjwoium",
                "nabesvshjmdbhyhirfrkqkmfwdguj",
                "bhrfxxemhgbkgmkhjtkzyzdqmxxwq",
                "gziobrjeanlvyukwlscexbkibvdjh",
                "mcwwubbnwenybmfqglaceuyqnoadz",
                "xyzvyblypeongzrttvwqzmrccwkzi",
                "ncfalqenfcswgerbfcqsapzdtscnz",
                "dtqpezboimeuyyujfjxkdmbjpizpq",
                "wmuhplfueqnvnhukgjarxlxvwmriq",
                "qwapdkoqswyclqyvbvpedzyoyedvu",
                "uoqbztnftzgahhxwxbgkilnmzfydy",
                "zsddaahohbszhqxxgripqlwlomjbw",
                "bwadkiavdswyuxdttoqaaykctprkw",
                "eixdbntdfcaeatyyainfpkclbgaaq",
                "nmjnpttflsmjifknezrneedvgzfmn",
                "avlzyhfmeasmgrjawongccgfbgoua",
                "kklimhhjqkmuaifnodtpredhqygme",
                "xzbwenvteifxuuefnimnadwxhruvo",
                "ugmwlmidtxkvqhbuaecevwhmwkfqm",
                "rhpyjfxbjjryslfpqoiphrwfjqqha",
                "eeaipxrokncholathupdetgaktmvm",
                "ltuimrnsphqslmgvmmojawwptghon",
                "azitvyhvlspvoaeipdsjhgyfjbxhi",
                "efrelxezcgikdliyhvpocvvpkvagv",
                "znxforctwzecxyrkwufpdxadrgzcz",
                "kcqgynjcpbylayvgdqfpbqmshksyf",
                "hrljvedsywrlyccpaowjaqyfaqioe",
                "cjmfyvfybxiuqtkdlzqedjxxbvdsf",
                "zeqljuypthkmywaffmcjkickqqsuh",
                "wnfzoyvkiogisdfyjmfomcazigukq",
                "zyaaqxorqxbkenscbveqbaociwmqx",
                "ahnpivdtlcnptnxjyiaafislqavam",
                "edtqirqmjtvsfhadhafktyrmkzmvi",
                "wponuefgdtcrgxswiddygeeflpjee",
                "xozgwhtbhlkvrzismnozqpfthajaf",
                "ptnfnojnlinbfmylhdlijcvcxzjhd",
                "uxekzlgigjpsukjvsdihrjzgovnre",
                "rbohxlytsmoeleqrjvievpjipsgdk",
                "fxtzaxpcfrcovwgrcwqptoekhmgpo",
                "tvxvvgjbyxpgwpganjiaumojpyhhy",
                "vqjjhfaupylefbvbsbhdncsshmrhx",
                "urhedneauccrkyjfiptjfxmpxlssr",
                "ltvgknnlodtbhnbhjkmuhwxvzgmkh",
                "ucztsneqttsuirmjriohhgunzatyf",
                "rbzryfaeuqkfxrbldyusoeoldpbwa",
                "atlgpnkuksuesrduxkodwjzgubpsm",
                "lrdniqbzxrbpcvmzpyqklsskpwctg",
                "qvnvgzkyhistydagsgnujiviyijdn",
                "uzatydzcnktnkeyztoqvogodxxznh",
                "ocbvphmtpwhcgjbnmxgidtlqcnnwt",
                "koudovxrjkusxdazxaawmvoostlvv",
                "ptruqmjtbaapgmkfnbwnlvzlxwdpz",
                "xdxtpbpoemekvxzrrakwjxcxqsdas",
                "gdpclnsguabtgbfwdmrmbvydorfrb",
                "htwxdbarwuxykgduxjlkxppwyruih"
        };
        new Solution().findSubstring(str, words5);

    }

    private void print(Object x) {
        System.out.println(x.toString());
    }

    private void print(Object[] array) {
        System.out.println(Arrays.toString(array));
    }

    private void print(Object[][] array2d) {

        if (array2d == null) {
            return;
        }

        for (int i = 0 ; i < array2d.length; i++) {

            if (array2d[i] == null) {
                continue;
            }

            print(array2d[i]);
        }
        System.out.println();
    }

    private void print(Map map) {

        for (Object key: map.keySet()) {
            Object val = map.get(key);
            if (val instanceof int[]) {
                int[] array = (int[]) val;
                print("Key: " + key + " Value: " + Arrays.toString(array));
            } else {
                print("Key: " + key + " Value: " + val);
            }
        }
    }
}

