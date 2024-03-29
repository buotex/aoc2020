use ndarray::Array1;
use regex::Regex;
use std::collections::HashMap;
use std::collections::HashSet;
const TEST_INPUT: &str =
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce";

const INPUT: &str =
    "cefbd dcg dcfgbae bdeafg gfcaed ecbgd bcag bdacge cg bedag | cebdg egcfda gdacbe badefg
aefgc bcdgef bef bdegca bdeca fdab afcbe fcebgda bf bfaecd | fgdecab gefac fgaec bdaf
cbgedf beda cfgbea cafbed cdb afcbe bd gbaedcf bfacd gfacd | acdefb cdfeab dfcaeb abde
efbag de adcgf fgcdea gfdabc daec fdcgbe edg fgead acbgdfe | de bgfae decafbg gefabcd
bfg gabecd gf facgb cafgbd acebf degcfb bagedfc gdabc gfad | daecbg gabcde cfgdbe bgcfa
gbaf dbfgac dfeacbg fg gcf cdfab cbefad dbcfg faegdc gbdce | aecgfd efadcb bcdeaf cdbaf
dgc gbfde aebdgf gecfd cd gecdbaf cfgedb dbgafc efagc decb | gebdf cd fcage dabcfeg
dbfeg debfcga ecg gfbaec eadfgc ebac gbadfc ce ecfgb acgbf | dabfecg abegfc dcbgaf cfgab
gbadefc dbegac bcadef gabcf gd gfbdc gefd fedbc dgb bedgfc | cbdgf bfacde cdgbafe edfg
edbac fbaedg aedcg acg gdcf fbcedag afedgc acbfeg gc fdaeg | dafge adceg cbeda dcbae
gbcfe fgebdac cefab gdfcb efg aegdfb bgadcf gdec ge gecdfb | aecfb egcd fecab bcfdga
gbd ecbfga gbedcaf bgedca bdgac baegc dg cedbfg dfbca geda | cdbaeg dgaceb gade bfcad
cefab agf faceg agced gf fgabedc gacdbe dabfgc ecgfda edfg | gdeac fgadcb afg agcfdb
bagd ecfagb ag gaebdf acdfeb abefd edfgacb fcegd dgefa eag | afdge egfdc abefd dfaeb
gdcaf ebafdg fdcbeg dbgce aecb adcge adcgbe gea ea afgbdec | efdgbc egacdbf egcbd bedacg
gafcd bedcf ab cfdbeag eafb dfbac decfgb dgbeac cedfab acb | abc cba ebgcad fcdageb
dceagb edfa af bfa acfdbg faegb gbade ecfbg eafdgb cebadgf | degcbfa af bgdecfa aegbf
efcabgd gfbead gbcefa egabf bcgea gc badce fagcbd acg fgce | bfgeca gca bgcae bafcgd
afcgd gafecdb ea befcg egda gbfdac eaf caefbd cadegf faceg | aegd fecbg gdea fcgdab
gcbd cag gbcfae bfdcea cg acgfd bgadcfe aefdg fabcd bdcgfa | dabcf dbgc bcdg gc
cedgbaf ae afe gdfec cdbfa dfaec faebgc bdea bgfdac cfdeab | begcdaf ecfgba ae ae
bfea adcbge feacd bcfeagd af gcfde caebd acbedf afd dfgcab | aebf becad dfa fcegd
dagef acdgf ecad ea gfedb gea cdgafe acegbf dgfacb aecgdbf | cagfd dfabgc gfbed ae
fced bgfcad ecb cafbde afbcegd abdce dcafb ec gadbe cfegab | afgcbe ec cfegab bcdfa
afedbg bda gfbcade ebfdg dbacef badeg fecgdb agfb agecd ba | ecdag gcbedf fdgeb gfdeb
becdfg ac dcgef aegcfd gadc eabfg afegc dgefcba eac adbcef | bcfgde ca facge fbgea
dafg abegfd defgcab df abegcd eafcdb edf gedbf dageb egfbc | agfdbe df agefdcb dfebg
fcea cbe bdfeac edfgba deafb edfgabc adbec efdcgb bagcd ce | bfegda baedf dagbc cbeafd
bfdec abefgc gb gfbd gbced fbdecg gedfbac ecgad cbg bcfaed | fedcb bdecg efdcgb dceagbf
cgabe gafc bcegaf bfcaegd begfda agedcb gf gefbc bcdfe bfg | gcaf bedacg becdga bfg
gebdfac cbga fadebc fcgdab ag gbdfa dbafc agd bdefg egcdfa | abdfc bfadce abcfd abcgfed
caefd fgabed acefdg gbcfe gdac dcfge ecfabd cdebgfa gd gdf | cdga gedfca defagc ebfcg
efagc cdf df cfdae dgbfca egadfc gdfe dabce gacefb cfbdega | cbefag ceadb dabfegc cbdea
edfca eacdgf aefbc ced faedbg gfead dgac fgabdec dfgceb cd | edbafg dcag dec dagc
fgcbade ecfdg efcbad aefdc deabc bgaced gafecb fa bfda efa | eabcgdf af dceabf bdfcea
gfabd abg ab gefdb gfabdce cdebfg dabecg bagfed dacgf fbea | ba bga fdacg dgbeca
ec dcgfa gcdeba efgcd dce dcegbf gbefd bfce dbgafce bgdeaf | cefb agedcb cegdf ecd
cde daecbg dbeafc dacbgf fegcb dfecb ed gbcaefd dacfb dfea | edfbac ed ecd eagbdc
gcbfdae cbdg dbgfe febad befcg dbgfec fcbaeg deg fedcga gd | adfeb ebgcf cedfga gadbcef
fceba dgefac aedb befadc dafcbge fbced gfabec gbfdc ed dfe | gcefba bade bfgdc cebdfa
bef fabg fb feabd cgadbe cgdfbe ecdaf dbfgea adgbe ecbgfad | gcdbae ecadf adgbe eadgbc
fcagb cefbga aebgcd eadgcf bfge gcefa fadebgc gbc afcdb gb | agbedc febcag gfbecda fcabd
dfgeca gfceba gd gcaeb gdc bdga dgbaec ecdgb dgfcbae dbefc | bacgef gcefba afcged cdgefab
edafg feagdb dgacefb dae bfgedc abfedc ad fbedg cgeaf bgda | gfbeda fcaeg dgba abgd
ad cadf dcabe fegbac gfadbe bdecfa gbdaefc dgecb feabc abd | fegdba cadf gdbeaf fcgbea
badfg dfeacg dfeag dbf bfecgd bf dacgb agdbcef gfaebd ebfa | fb gdbca agdbc fdbgae
gcbfda fa faeb efdac bacefd dbcfeag gedfcb fedcb afd gecda | feab gcfdba gaecd abcdef
da acegfdb acfgb gade abgdf cedfba fgbdec gedafb bad bfedg | eabfcd bfcdeg deafcb cbfedg
gcfdb dcea gadef gfdace bdgfeca fcbaeg agbedf ca acf cdfag | cgfad feagbd badgfe egfadc
cdgfba bfeadg gbca fadbg fcaed gdbface dgacf cg cgd dbgefc | gdafb cfeda cgab gbdfa
cbdeg bcda cag ca fegba gfdecb agdcfe cebdgfa cebga gbcead | gecab cdfbage gfeba gcabde
agfbc dage edbcfg dg bgd acedbfg dcagb bcafed edabc degcba | bgd gacdb gabedcf agebdfc
gd gdeb cbafed dgecfab faged fcdgab fgebda cfgae gdf beafd | acefg bdfeag feadgb cgaef
cadbfe acgbd ecfa fagbdec dgfabe cbade eafbd fbedgc ec bec | dbfgcea fcebdg bacde dbeafc
eaf eafdg afgdc cgef abcgdef dfgcae dgabe fe fbcaed dgfcab | bfgcad egfda gcef eaf
cdbgafe efb eagfcd cfgbe cbdefa cfgba dgbe be gcfed befdgc | eb fgdec dcafeb adfebc
gafcd ceba abedg aegdbf cfgedb adcge edc fagdcbe bcegad ec | ceagd dagbfce ce cde
acegdb fe adgcfe efgc gbcedaf dafbc gacde fcdae dgabef aef | geabdc eagdc fdebag bgeafd
fgdba ebfdg gfe gfeacbd fe eafb degacf gecdb bfegad fbgadc | bfcdag cdgbaf afdgbe adfbge
bagdfe edcfgba gbcea ecdgbf ebcfg gef dbfcga fe fced cfgdb | ecfd bcfeg gdcbf cfabged
fgacde egdbf ecf fc dbgefa gdfcbe bgeac cbfd dagcebf cfgbe | degfb gdbef bafcged egdafc
ed eda cgdafe cgdbea efacgdb gdbe eacfb acebd gcabd fdgbca | adbgc bcgad gdabc gacdb
cgbdf bcd cd fcad bfcag cfbdega begdac dbagcf dbgfe aebgcf | cfgba dgcfb cbdgf gcbefa
bd gfbdeac cdegf bdc cgefda gbfd fecdab dgcbe cgeba dcbgef | cbd db db gdecf
dgfcaeb adebcg ecdag fadc afe eagfc bgfce af edgcaf afegbd | gdcaefb fa cdaf eacdg
ebdfa bae be dfecabg fagdcb dfgab aegbfc dbeg cfdea dabfge | fdagb adbgefc bae fgbdac
cefb agfedc ebcfgad fgadbe edgbc be bed dfgce cedfgb dcbag | be faecgd gcbda eb
gaed dbefcga dbgce ag abfce gfacbd adgbec dgfecb gceab agb | debcga gedfcab aged dcbge
dbfceg abcgde gcabd dabfg geabfcd cg egca ecdab dgc abcdef | bdcefg fbgcaed cdg gc
gf bcegd fbg dacfbe afcdb gfda efgacb bgfcda fdcgb fbedacg | bcfda bedcg gbf fdceab
cfgbe gdcebaf fbcdeg bdfga edf fcedab dfgbe de cedg gebfca | abgcdef befgd fed fedbgca
fbdac bafgcd eb cbfged bec cdefab dcefabg deab fbaec fcage | cfeba bgcefd ebc bce
dab ebaf afgde cdfabg debga dcebg fgacde ba bcdafge efdbag | ba bagde dgaef gebcd
dbacf ad dgcfb caefdb daf deab fegcda bafdceg efcab fgacbe | deba egcdfba afd ad
bfega dabegcf egafd becgdf gbaced bgcfe afgbec ab cbfa gba | abegf defga fabcge cabf
bfecg fd abdgc gfbacd afdb dgf cgeabd aebfcgd gdfeac cdbgf | bcfdg agcdb cdgaeb eacdbg
fea dgefca gacbfd dcfae afbedg dbcef dbefgca gafdc ae aegc | afced efa egac ea
aegc gdcaef bfgcda acd cegbfd ac decgf gfecdab efadb fcead | cadef cfgde agcfbd dfeagc
bafcgd ce bdcage fbdeg ebgdc ecba ceg cedgaf edcagfb bdcga | cbae cbgefda gceabfd cafedg
bac ca bfgcda aecfdgb egbfca cdbef abcdf gefadb fbdga agdc | dcbfe cagd dfabc dcag
agdcbe cdagb dec de gbed bfadegc afcbe fagcbd dceab cgedaf | ecd ed gbacd dafgebc
dfgbeca fgdeb dcefga af cgaf eabdgc afgde cedafb adf gacde | edcbfa cadfgbe gdfebac af
fba dcbgeaf agecfb gabde eacf fa cgbdaf aegfb gefcbd ecbfg | fegcba bgeaf gbaed bagfe
bd afgdc gebcf gbeacd cadbgf caefgd afdb bdg fdbcg cadgefb | fbdgc cgebf agbfcd cbgdf
fcgbdea dcbgaf cgfde ebcadf gcfaeb gcfeb ceafb gbea bg cgb | cbg cefgd fgdabc feabdc
ac cefgba gabc fbcea caf bafed bgcfe dbegcf cbaedfg fdacge | ca dcbfeg fbgce bacg
agfbdce gcb gc abdefc badgfc cega egbfd efacb bcafge fbgec | cbefa cabgfd afcebg ebgcf
cbga adcef cbgdfa dab dfbcg ebdgcf aegdfb ba fcbad aegfcbd | eadbfg bcga cafbgd bfdgec
gedfac dfeag gfdb cabgefd gaefdb bfgae fba eacbg deacfb fb | bf afb abgce egbfa
ebdfg gaefcb de dgeacb gafeb bgfdc deb egcbafd edfa gbfdea | bafeg ed fgcbd bfadcge
dagfc ecg cafdgb bdeac cdfgae dfgceab degca gdcebf eg gfea | cgdfabe afecdg decga gcbadf
agf ebfcgd cefgab ga cedfbag fdcbg dcefa cfgad gcbfda gbad | abegcdf agbecf gbad bcgfd
cfabdg da abfd gcaef fdgac dga dbfcg cbeagd bdecfg becdgaf | fbad gdcfa gfdca gcbdf
egad dg ebacg gcfeba adcgfb becgd dfceb ecfbdga gcd egbdca | dg gabce gbecda gacedb
fgbdec eca cabd gfeadc ac afgbe degbc fecbagd gbadce gcabe | eac dabc bcadeg efabg
fd bdegc dcabge dcefga decbfg cdfb degbf egfba edbcgfa dfg | fdg gdf gbecd bdgfce
fcebd efdbgc degabc fegad gb cadbegf bgdfe bfgc eacbdf egb | agdfe afdge bge cbaedg
fdgc bdeac abcgef dfbega daegc gca dafeg gcfbdae gc cfeadg | cag agc begcadf gfbeca
gfabcd edafc acegbd fabdc dacbg badgcfe fb bfgc baf fadbeg | adcbf gafedb fba acbfd
bgdec acfbe cfeagbd efcbd faebgc fbdeca dfc adfb cgfade fd | fdc afegcd ebcgfda fd
gcebf bdfgca de cedbg ecgfad dbcaeg agcdb gbfceda eadb gde | dbgce bade abgdce dbgec
gfbdcae bac ca gfabe cfdbag agec edfgba efdcb acbef gbcefa | gcbfad fcaegb ac fgcbad
gadebfc cedbga bfad dgebaf cfgeb dfeag bgdef acedgf bd bed | degbf eafdgc edb db
bdgca gfbca ebcfdg cdea gafdbe cdb cd agebdc aebcdgf deabg | edbag bdaeg dcefgab adec
cedaf fbdaeg cgaef bceagf dfgeacb cbga agf ga ecfgb dbcgfe | dafbeg ag fegbcd dbgceaf
abgcd aefcdg fab eadfg ecbgfa fgbda aedfbgc bfed bf dgfeba | bfa fgaed bceagf agdef
aecb bfa afgedcb befgdc ba efdbc bgcafd cdfeab aebfd fdeag | fab ba fba efbadc
cbgedf gdebc cebgfda gdeca cdgeab adcb eagdf cea ca bfaecg | dcgea fbegac dabc acefbg
fgc bcag cdbgf gedcaf ebgdaf gbdfa cedfb cg bdagfc fgbcaed | fgcbda gdcfba cdebf gcbfd
cafdgbe fecga cfgdbe gf eafdc gbcea fge gbaf acgbde gcbfea | efdac gfaec agbec bedgfac
bace egdafc eb bdecfag gbcfd daebfg gedca geb edcbg edgcab | gedcb eb fedbga bgcde
bgdcf cfdgabe dafgb gfc bacg bdcef cg cfedga fbegda abgfdc | afgebd fagdb fdaecgb cg
gacde bcgfaed fbcde ebfdgc dfba adecbf gcbaef adcfe caf fa | adfb ebdfc daebfgc fecdba
gbeac dgbaefc caegfd gd cgfd edg aedcg befdac fcade dbagef | daebgf gadcfe ged dg
bcfdg bfecag efcdg fagedb adce dacbgef gcedaf ed efd egfac | aecd abecfg cedgf efgbda
acdfg cfebdag cfegba cga gfbda ac cfbgda cdegf fegdba bcad | acfdg fagdecb fedgc ca
aeb fcbagd gafebd be efcda degbca edfgcab dbaef gfadb bfge | dcabge aeb be adbegc
gbfdaec gafedc gadcfb efdcba acfbe ef caebg cfe dfeb bacfd | afebcd cabef cfbda ef
aegcf dagbe bf fabedg bafd feb fdbceag gafbe edfcgb egcadb | eabfg fgace bgade dbaf
fedbagc afgcb dc fbdcg bdegaf edcb cdf begdf edfgca gfcbed | dbec gbcfa dc cgabf
gcfade dg fbecgda bcdef gbfd gdbec abdefc cgeab gbfcde deg | cdeafbg gd bfgdcea dafbec
fdega cfgab adc cbegad cbfgaed gfaced fdec abdegf agcdf dc | cagbed dgabce dcefga fgcad
bf bfadc bfga gfcda bfc afdgbce cfdbge bgacfd efagcd cdaeb | dcabe fb gacfed edacb
deba badcf gbdcaf bfdce ecdfg bec efcgbda cgebfa be aebcfd | eb adbgcef cfadb dfecg
eadcfgb gf eadcf dagfe gfab bgefdc egdba dfg eagbfd egdbca | aecbdg edfag efadc adegb
cegabd gaedc gceabfd degabf agfceb acdgf adgeb debc ce gec | eagbfc cge ce agcfd
cfdabg fcead agfedb ba fbcgd fcgedb gfbdcea dbfca cgba adb | gefdba bafgdc dceaf ab
degbf bcd agcfbd bgeafc fdca aebdcg cgbfd fagcb dc cfgbeda | fcad adgcfb cd dbegf
dagbc eabcdf abgcefd bdagef faec beafd ebadc gdfcbe cbe ce | cadbg adcgb gbdefc ec
eadf fcbga edgfacb cfbdeg fagdb abgde cgbdae dfb df fgdeba | feadgbc egdba df gecadb
eacf dgecb bcfda fbgdea gbfdac fcdabe dfe cfebd ef bgfcdea | aecfgbd fde cadefb ecgfdba
bdecag cfdaeg cbafg gbafed bedf gabdf fedag db adefgcb dab | fegadc efcgad feadg fedb
fdegca facge dcfe ec eca fagde gafcb egcadb gfdaebc gdaefb | eac acgbf dgafeb fbagc
cbfdea bg gbea egbfcad fdecbg eabcf acbgef fgbca fgb afcdg | ecbdaf cfabe abcgf bega
fegcd cagbe edafcg fgbced dfeabg bd bcdeg bdcf bed agcebdf | ecfgd cgedf gcabe fegdba
ec eafgbd aefdc cgae fadcb bgdefc gbcdfea ced cdfega efagd | ecga ce dfgceb bacfd
decfa efc fgdaecb cbgfad ebca ce cbafd adbcfe afged ebgdfc | cbfgad cfabd bcae cgafdb
cbdgfe egafcdb gbadce fc decgfa bfceg gcf dbfc cgedb febag | cf cfgeb gfbedc gbdefc
gface gabd fdceba cgdfbe bfg cbgdfea fbcagd gb abfgc cbfda | bdcgfe cfgbde abcfd gcbfdea
fadgbe gdafb daef bae bacfgd gecdb gebfca gebda ea eacgdbf | ebdfag bfgda agbde ae
ec bacdegf dbacg cdeb fageb cea abecg bdacfg dacebg dafegc | bgdacef gacefd ebgaf acgdfb
dgbfe gb ebafdc bgd daecfgb aedfb dfegc ageb fadgeb gafdcb | fgaedb dgfce fbegd facdgb
egcfd acdefb fgea fbdagc efacd aefdcg bdfaecg fg fdg ecdgb | aedcbf fgd cedaf gf
fdcbge dfbe cgdea db gbfce gcdbfa agecbdf bgcde abgefc bgd | dagfcb efbdgc ecgfb febd
geadcb afgbdc cfd cedgf ebgfcd bgfaedc dbceg fd bdfe ceagf | fd dagebc edcgb fd
fdeabc eg cedbag fgbadce agefc cbfgae ceg ceabf gdacf fbge | egbf gec ge ge
ebcgd ebc efcagb cbaged fdecgab dgfeab ec dgbcf degab cdae | cgebd gdafecb afcebg cbegd
bcdafg cfdea edg dcefgb egdcfba gbdfc gcbe eg gedcf bagfed | bfadegc fgbdc cefgd cfdgb
edcab gcabefd dg cbagdf gbedc cdg fgecb cadbfe gdea cebadg | aged gcfbe gdc dbgfeac
acgedf cbfadg ebafdg fcged cdg cefbg eadc dgfae cd dbfegac | fgecb bfacgd gbecf fcbdag
ecfda cbgfeda dg ebfcdg aegfbc bcgae egdac abgd gde gadcbe | gcbae efdgbc gabdce dg
gbfecda gbd dg cadg egcfbd eabgf ebcfad gbdcaf fbdga badcf | dbg abfge fcdgbe ebgfa
aegcf dgaefc abdfcg fdce abcdge bfdcgea fcg feabg gaecd fc | fgc cdebag fecd cfde
gbcfae ecgadb ecg edag gbdca decbg eg bfecd cbdagf edcfagb | gbcadf ge afdgbc gecdba
dec caegdbf deacgf dfcea gadc gefcba bedaf dc febcgd gcafe | dcagbef dc eafgdc cfdebg
dafebg gfced fgcdabe bagdec eafbcg ebc dbac agedb cb bcdge | egacfb ecgfd edcbg cb
gcd dfbcag gbaefd agfdb dc abcegd cfega ebcadfg dgcaf cdfb | fabgdc gbedac agdefb bcadfg
dcgaefb dcebg cb bdeag afdcge cfeb cdgef bcd dcgbfa dcbgfe | fecgad befgdc efcb eadgb
agc aefgcd ag dfaebgc edcbfa cbagd gbfa abfdc decgb dcfagb | gabdc cga dgfcba bgadcf
bde beca gcafdb bdecg fdgeabc aedgbc dbcag dfceg gbfade eb | bcae agdcbf fcgde ecdbg
gbacdef bf fab cbdf fdacbg bcdga bdcaeg gfabd fabecg egdfa | bf gcbeaf dcabg becdag
bf ecgbdf cfgdeab dgfb cfedba cbagde feb fceag decbg gbcef | ebdgc fbgd cgedab dacfeb
eabdcg efdgbca abegc bf efab cfged afcdbg fgebc gbf agfcbe | ebcag ecgabd baedcg gbcfea
efcgd afbgec bdfgca adgef eabd ae gfadbe gae fgbda bdafgec | fadgcb bgaecf eag gfdea
cafb dcbage gfecd dafec ac cdgbfae badfeg afecdb cae adefb | ebacfd badgfe ceadf dbgcea
deagb dfebcg deagf dagcbe fcdgeab bafg daecf gdeafb dfg fg | gf fedgba gdbae fgd
gbcfd ecfbdg eadcbg ceb agdfcb fdceb ce ecfg daebf aedgcbf | egcdbf fadbe ec abcdeg
fbgca gadefb egbfd ecdgbf afgeb ea adbe fgdaebc fea agdecf | ae becdgf eaf agefb
gfcabd dabgf gfbcd fegacbd fcab bcd daebfg cgabde fdgce bc | bcfdg efdbga adefgb bgdcfa
dcbagfe ebgdac cabfeg gf egacb aefg cebfd cgbfe cbadgf gcf | aegf ebfdc bdgcfa gf
befcdg bef fcdb gcfae gfecb agdecb fb daegbf bfdgcea begcd | bf fgace cgebd dbgce
acfebg fdceg efcab bcd dabe cbafde gbcdaf db agfbedc cdefb | abde cefgd cdb fecbd
agc ac afged dfbcg fbgedca eacf gdbace dfcga agfdce aegdbf | gcabedf fecgad agfde gdefba
dfc gdce dc bdegfc debfg gceabdf bafged efcdb gbdfca ebcfa | fbcegd bcgdaf fbedc bfcde
cbedf baged adfeb bgeacd gebafd bfa afdg af gcfedba gfacbe | edbaf fabed gbedcfa fadgbe
gabe debfa cgdbfe adfge dfgcea beagfd abcfd be abgfdce dbe | fdacb eb fcegdb egfbcd
dceag dacfbg gcbae bfae becfg gcdbfe bacfedg ecfagb bag ab | bgeac eacfbg efagbc egfbc
ebcdfa dcebg eab bafcedg cadgfb ae fabged bdfca face adceb | bae dabgfe gdbec ae
ecbgaf efdgac edagf cefdg fgbdc gce eadc bfdega acbfedg ce | ce efbgad fbcdg fcdgb
bagf afbde bad gdfebc bdceag bdcagef acefd dgfbea bdfge ba | abd fdbae cafde bfaged
dcfaegb efdbc afecb ba bgcfda bac gbae gbface afecg gacfde | abeg fcdage dgbacf febagc
bafc faced cfagedb bdc bgead aefbcd degfcb bc gfaedc cedab | dbc dcb feadc bdcagef
ebadfc gf afebd gfb gafd ecdbg dcegfba dgabfe degfb abcgef | gbf fdbgae fadbe gf
cbagde bcdae dgcab dg dbeacf gefabd edcgafb acfgb dcge dgb | gbacd debgac acbedf ecdg
aegcf dagecf abegcf facgb fba cdagb bgfecda fb fbeg bdcfea | bfeagc gbafce gcabfe fgeb
dgebc dg ebcdf bfdcga gdc ebcadf baegc bedgcaf cbdegf gfed | edgbc bdfgce dg gd
cebd gbcfae fecgb gadbfc cdf dfceg fedag debfagc bfdecg cd | bcfeg ecgfb acbfeg cegabf
ab cbae dgfbe ebacgd gabed abgcdfe fagbdc abg efdcag decga | bcaefdg fgdacb aceb bdcafeg
ea bafgd cafgeb gae aegdb dbefacg begdac dcegb fbgced eacd | aedc bdgea fbdecg gebacf
afgdce fe gdecbf egfb cbaed bfcdage cef fgadbc dfebc gdcfb | fe fec efdcbg fcdebg
cfbdge fabcg bge eadb fgebda abegf ebgafdc eb dgaef adfecg | gfecdb gacfde afbcg ecgbdf
abecf bgcfad bdcg gfbeadc fbgad bfagc dgbfae fecgad gc cga | fdabge bcfag dgabf acg
gcfdae be decfg gedafcb cbge edb aecfbd agfbd cedfbg bgfde | cdgbfe fgdceb gdcfe becg
agfdce baecgf dgbaef afegc cebgd ad fcad gfcabde ead adegc | ebfgca cfbage cgaebdf gafebd
ea acfgde dfbacg egba cgfba caefb fbced cea egbcaf dabfceg | bgecaf bgefac bfcaged fgbcae
gbcfda cegbf cgd badfcge ceabd dg aedg gcbed bcaefd acedgb | fcabgd dg fbgce gd
bgface eafbcdg bdegfc efcdb dceafb ecdfg fgaed gcf gc dcbg | gfc bcgefd fdceb gbfeac
fdageb gefdbc cagbe fdgba ecadfgb dcfa abgcdf dbc bagcd cd | agefdb bdagf dbc cgadbf
gcfbd gafbcde aedg bfdga ad eacdfb bgcaef adf bgfae gdfeab | bgfcdea aegbf fbdag gafcdeb
dgabe fdace acbfge efdcabg egcda cge gc beadcg febgad gdbc | dgcb gebadc adbge gdace";

fn parse_input(input: &str) -> Vec<[String; 14]> {
    let re = Regex::new(
        r"([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) \| ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+) ([[:alpha:]]+)",
    )
    .unwrap();
    re.captures_iter(input)
        .map(|cap| {
            [
                cap[1].to_string(),
                cap[2].to_string(),
                cap[3].to_string(),
                cap[4].to_string(),
                cap[5].to_string(),
                cap[6].to_string(),
                cap[7].to_string(),
                cap[8].to_string(),
                cap[9].to_string(),
                cap[10].to_string(),
                cap[11].to_string(),
                cap[12].to_string(),
                cap[13].to_string(),
                cap[14].to_string(),
            ]
        })
        .collect()
}
fn count_in_output(group: &[String; 14]) -> Array1<i32> {
    let mut count = Array1::<i32>::zeros(8);
    for entry in group[10..].iter() {
        count[entry.len()] += 1;
    }

    count
}
fn strings_to_number(group: &[String; 14]) {
    let mut mapping = HashMap::new();
    let full_set = HashSet::from(['a', 'b', 'c', 'd', 'e', 'f', 'g']);
    for character in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] {
        mapping.insert(character, full_set.clone());
    }
    for entry in group.iter() {
        let mut cf = HashSet::new();
        if entry.len() == 2 {
            cf = HashSet::from(['c', 'f']);
        } else if entry.len() == 3 {
            cf = HashSet::from(['a', 'c', 'f']);
        } else if entry.len() == 4 {
            cf = HashSet::from(['b', 'c', 'd', 'f']);
        }
        for character in entry.chars() {
            let val: &mut HashSet<_> = mapping.entry(character).or_default();
            let inter: HashSet<_> = val.intersection(&cf).cloned().collect();
            *val = inter;
        }
    }
}

fn count_entries(parsed: Vec<String>) {}
pub fn day8() {
    let parsed_input = parse_input(INPUT);
    println!("{}", parsed_input.len());
    println!("{}", parsed_input[0][0]);
    let counts: Vec<Array1<i32>> = parsed_input
        .iter()
        .map(|group| count_in_output(&group))
        .collect();
    let mut count = Array1::<i32>::zeros(8);
    for group in counts.iter() {
        count += group;
    }
    println!("{}", count);
    println!("{}", count[2] + count[3] + count[4] + count[7]);
}
