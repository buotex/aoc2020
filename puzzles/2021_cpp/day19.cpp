#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <vector>

const char *puzzle_input = R"(--- scanner 0 ---
-377,550,716
405,-463,594
-612,-603,479
-673,637,-463
536,-465,715
821,322,-697
-676,-693,500
643,432,654
366,-500,-472
708,409,-755
469,-498,555
738,371,759
600,282,729
362,-630,-324
-446,-778,-395
-679,-672,612
-450,654,697
353,-429,-389
-661,719,-393
118,-178,-1
702,313,-718
-540,-676,-341
-716,754,-469
-313,635,722
-546,-749,-540
-46,-64,45

--- scanner 1 ---
-393,569,-783
823,673,744
492,605,-667
568,-702,420
498,-690,338
-442,536,-928
-458,-493,-747
-617,-342,422
-654,709,686
539,-496,-476
540,570,-668
-416,521,-829
756,-480,-461
-387,-515,-848
-549,614,625
-611,-406,507
666,628,-671
-592,-479,403
632,-478,-385
802,792,735
860,679,648
27,17,-91
-624,571,775
-535,-422,-848
574,-745,303

--- scanner 2 ---
558,-741,-564
646,-807,485
464,437,812
-898,-528,468
616,-770,-508
-127,-22,17
351,393,-850
532,-629,-522
-680,-690,-789
600,353,768
-655,-827,-770
593,-678,448
675,-648,590
-808,525,-539
-765,-461,537
335,474,-887
-777,396,-580
241,407,-941
-787,793,667
-973,848,720
-661,-763,-685
-789,519,-676
449,424,815
-815,754,730
-42,81,-107
-877,-464,558

--- scanner 3 ---
-436,572,-578
746,-456,727
-475,513,-649
-451,-549,481
-562,-572,-515
774,-516,696
-704,791,507
768,-722,-551
812,-661,-568
-613,684,551
700,767,716
-303,592,-650
116,21,-89
-408,-507,547
753,-717,750
609,753,-601
-62,-9,37
553,672,-596
836,-673,-599
-467,-404,-483
-660,817,634
-609,-356,-546
602,796,-590
692,646,766
-565,-477,532
702,620,743

--- scanner 4 ---
538,-453,-833
-126,24,29
-352,-473,-587
-444,-449,-740
691,-464,520
626,828,344
-565,-317,406
775,942,-788
-369,-409,417
-708,823,-645
727,935,-697
-746,539,507
-806,434,481
-789,742,-763
-556,-362,404
-690,470,523
593,877,489
405,-436,-796
317,-447,-785
-404,-427,-788
-13,189,-5
-698,727,-823
600,898,-737
561,-551,518
641,854,443
733,-626,469

--- scanner 5 ---
46,10,147
758,-651,532
-527,-618,452
-823,464,-569
690,764,759
-564,-447,-551
764,-302,-267
684,881,802
456,449,-735
435,440,-616
107,94,-30
760,846,747
-677,-709,468
-647,455,-499
-408,-549,-539
398,536,-622
-293,614,774
829,-503,-276
-385,-416,-489
-272,801,808
-563,-622,372
-612,469,-575
613,-622,632
-278,753,780
681,-373,-280
812,-549,626

--- scanner 6 ---
579,574,-541
-505,493,-632
618,658,359
-341,743,774
-322,-636,574
716,580,-522
366,-369,516
-654,544,-722
401,-424,440
-413,-618,481
-785,-692,-593
-785,-599,-445
466,-635,-650
675,451,-553
89,132,-70
-427,825,855
-398,-634,698
570,-708,-669
-60,27,13
522,657,457
-376,606,841
-684,-621,-516
485,-772,-675
475,716,376
-647,496,-573
483,-412,510

--- scanner 7 ---
512,585,-747
807,772,880
733,795,840
-767,-876,-603
-719,662,750
-612,458,-552
570,-882,858
-589,-932,-661
623,-601,-378
-343,-464,739
-589,632,-556
746,-608,-532
494,492,-838
-652,610,660
-554,584,-555
111,-115,-49
589,-757,885
-618,631,899
496,368,-762
618,-644,-539
696,-814,921
-640,-913,-544
737,746,813
-310,-533,587
-23,-193,76
-85,0,-51
-447,-527,622

--- scanner 8 ---
-419,640,-664
-722,-533,531
705,861,595
577,-689,716
-842,-385,512
632,-792,-344
815,768,660
490,-691,586
-502,623,-798
-554,-811,-585
676,809,607
560,496,-785
-943,400,567
415,-740,758
679,-805,-531
732,438,-813
-792,347,621
724,-803,-540
-489,-738,-726
-746,-370,499
-2,59,-33
558,494,-753
-515,574,-768
-486,-634,-564
-122,-93,-71
-872,325,554

--- scanner 9 ---
506,-688,-561
571,721,622
503,-562,-503
-709,-714,-463
-835,437,457
-948,-735,-497
314,-589,962
495,809,-475
-788,360,-772
-612,-499,488
291,-602,907
-580,-584,424
-119,8,40
-636,429,-805
408,627,663
555,634,776
301,-483,836
-799,-766,-396
-671,423,-668
-725,535,411
10,-85,163
554,772,-348
-726,558,457
507,-736,-526
612,828,-526
-444,-607,500

--- scanner 10 ---
-643,-839,-726
-663,-800,-791
-17,49,1
-428,-762,319
-452,-869,434
806,-584,-592
-468,406,-817
118,-97,56
530,403,850
-433,399,-634
521,-484,654
881,-476,-533
954,-520,-545
781,439,-557
609,-463,682
-327,671,688
-542,-771,-726
-328,557,674
661,-458,693
510,298,863
-240,536,611
785,322,-393
-432,416,-779
-475,-744,471
518,305,832
823,411,-365

--- scanner 11 ---
-559,-302,-674
-766,553,760
-687,-322,850
-800,-238,758
370,-773,-566
-851,883,-504
-804,954,-655
-716,-388,-711
17,134,92
884,-743,798
905,900,-296
-681,-359,-759
-84,7,-30
851,833,-390
-756,459,918
479,-816,-448
-848,870,-519
707,-731,809
814,914,-406
503,782,753
544,911,722
767,-719,748
640,788,734
572,-776,-603
-781,-228,812
-703,514,732

--- scanner 12 ---
-593,845,571
-95,162,7
-509,-378,-516
504,-445,343
-400,708,-674
-554,-465,-583
431,-519,471
-473,-359,-516
-592,828,716
-931,-358,491
-906,-487,413
-628,838,754
-487,573,-751
370,841,-913
625,922,330
663,833,302
429,-748,-651
358,939,-895
244,-687,-680
-794,-417,415
621,805,494
350,946,-926
351,-656,-694
-488,687,-737
575,-504,385

--- scanner 13 ---
-540,634,673
764,-806,-384
489,306,-588
141,-5,-53
577,221,-522
-383,-685,663
-575,616,539
-558,-546,-541
-444,-533,-673
-356,-714,588
-603,633,440
791,-862,408
763,728,555
610,-722,-434
758,-918,432
693,-743,468
-611,661,-390
607,-706,-368
-1,-144,-29
-280,-701,796
-706,583,-501
-709,727,-493
764,719,476
763,692,397
643,299,-606
-566,-523,-601

--- scanner 14 ---
-636,680,-483
718,525,642
822,571,-429
534,-636,-655
-464,-684,-415
34,31,141
-600,748,862
-629,673,889
719,758,705
-438,-516,679
-448,-588,801
780,425,-363
-616,881,965
467,-723,-700
-462,-614,-303
806,549,-467
668,-416,539
746,-305,634
-461,-456,687
701,624,670
-795,747,-546
-726,811,-463
-540,-743,-278
-82,-24,3
812,-408,536
467,-742,-736

--- scanner 15 ---
570,716,-401
813,-522,-700
-565,-663,616
577,-384,448
71,-43,-130
-641,-610,619
-731,-539,-421
-448,392,521
563,363,512
-486,-548,601
792,-612,-764
638,513,555
-760,-644,-580
680,-591,-767
533,452,650
-701,454,-458
698,-382,317
-309,433,468
576,631,-465
-18,83,4
-617,468,-599
737,-417,381
-678,-502,-550
-643,510,-487
595,735,-538
-419,340,533

--- scanner 16 ---
-99,-26,105
-171,-173,17
-808,-569,-752
-430,-810,823
276,298,847
-545,545,909
406,-582,-466
797,-624,681
-592,481,-545
-566,579,670
483,-511,-365
283,346,756
390,447,-285
766,-707,633
341,480,-430
-591,-585,-737
814,-646,819
-404,-880,890
-381,-806,850
-544,516,-546
-514,646,760
320,473,796
-718,539,-542
364,432,-384
-684,-567,-828
335,-604,-365

--- scanner 17 ---
-814,515,-501
351,736,-672
-840,-376,629
-809,-483,615
420,355,558
452,-906,-323
-512,341,793
461,-873,-478
534,356,572
-618,422,726
-901,-561,658
-866,536,-417
346,616,-702
-798,-485,-246
-31,-18,-10
-785,-377,-340
786,-490,414
-885,-489,-394
278,697,-583
-163,40,154
-828,605,-546
-531,377,793
555,268,635
793,-482,383
688,-502,396
346,-856,-366

--- scanner 18 ---
-599,-418,-687
485,631,359
-642,-843,277
894,-574,-927
137,-133,-101
-513,528,790
-703,425,-406
623,-464,487
843,-793,-941
616,-512,636
-661,-584,-635
857,650,-567
765,-461,546
-612,-497,-702
-561,611,821
-770,355,-380
485,724,507
929,-711,-860
-699,589,838
948,668,-660
-730,429,-357
-605,-829,293
-24,-73,10
586,653,430
-757,-881,273
872,666,-784

--- scanner 19 ---
805,-688,638
106,-100,35
673,664,467
-736,-787,-834
-702,-600,-813
641,-450,-283
561,430,-721
-708,-739,-828
571,-441,-459
-562,-605,531
-610,479,771
590,617,600
-611,307,692
623,461,-542
-300,636,-543
755,-696,517
-551,-598,488
-557,-549,612
-380,632,-579
-77,14,78
611,563,-698
782,-698,664
-396,723,-429
546,708,493
-539,440,712
647,-455,-494

--- scanner 20 ---
-73,-55,-94
679,574,-740
412,-822,-515
-380,370,-593
587,593,879
-693,453,644
-818,416,667
722,670,792
450,-652,686
608,656,791
-288,297,-533
457,-835,651
-749,-809,456
691,374,-778
-793,-809,-818
421,-914,-678
113,-67,36
-695,-740,-793
467,-797,687
-788,-744,476
538,-900,-564
-579,-816,-811
662,430,-653
-720,-744,577
-333,306,-554
-711,301,691

--- scanner 21 ---
-720,-494,-326
-779,-506,-326
725,743,-671
643,-838,-672
735,624,-742
780,-444,760
635,-395,727
-773,-551,682
523,664,668
712,637,-797
4,104,146
-655,857,-500
-883,800,504
-152,-49,102
-923,-626,725
681,-418,775
-827,-424,-336
601,-802,-556
520,538,726
617,-733,-612
-698,874,-492
-834,-656,587
-892,821,623
519,490,691
-920,866,-491
-796,858,617

--- scanner 22 ---
80,-91,68
564,449,615
694,505,-425
820,-741,761
697,526,-537
-542,-761,600
-615,-889,674
630,595,-404
558,522,416
-23,-171,-90
635,-555,-793
552,-486,-729
-335,769,464
464,420,470
683,-817,702
-344,568,399
-75,6,7
-833,-862,-867
-686,-847,615
-836,-696,-870
615,-645,-662
-348,698,547
-518,733,-640
795,-819,632
-874,-749,-817
-387,735,-519
-451,700,-480

--- scanner 23 ---
-521,536,-591
405,-522,-611
598,-743,933
739,728,856
-767,828,470
553,913,-698
-311,-634,587
808,645,792
-303,-497,588
-36,32,-25
475,888,-569
447,-593,-552
-793,724,594
533,-449,-537
-589,-447,-308
-454,455,-697
649,708,725
477,776,-639
-632,-369,-400
-809,762,616
545,-781,880
105,114,172
-310,-582,457
432,-740,930
-618,-262,-369
-454,491,-678

--- scanner 24 ---
-574,-700,-914
645,309,-801
511,564,648
-735,664,363
464,628,796
703,-469,305
691,-453,440
-552,404,-633
710,348,-821
-763,685,451
496,-926,-724
702,-429,236
-885,-631,405
1,-36,-128
452,672,723
-672,-700,-757
-928,-818,431
-916,-845,434
-515,279,-610
515,-953,-752
645,377,-700
421,-973,-621
-625,-803,-884
-774,690,503
-400,386,-586

--- scanner 25 ---
-660,-612,759
44,-15,-25
-564,539,589
-501,550,610
817,513,-563
412,-387,533
-535,416,-425
-819,-717,730
743,582,558
666,604,559
-690,-754,677
790,542,-488
836,-482,-889
781,-535,-703
-473,-665,-681
-540,-734,-814
-665,512,540
-618,347,-489
742,-472,-731
341,-434,684
425,-390,548
593,616,664
-555,506,-556
-476,-644,-793
893,526,-355

--- scanner 26 ---
283,522,745
-873,247,471
628,-379,499
336,469,783
-605,567,-596
-904,279,268
-675,529,-760
-944,-764,-808
-898,-880,692
286,356,742
-18,5,-170
-93,-106,-29
360,663,-726
622,-869,-722
-946,250,385
759,-386,584
-742,-793,-828
629,-387,636
-776,-774,753
-830,-795,-768
746,-843,-826
600,-885,-760
-654,540,-697
424,732,-643
491,573,-706
-885,-685,732

--- scanner 27 ---
706,-520,-692
-101,126,35
771,564,-698
-480,528,-493
442,456,859
559,502,806
752,-472,-669
514,541,941
-584,455,-474
-875,-543,521
-499,391,-468
-747,589,719
771,471,-550
-763,-660,-431
726,-380,811
-823,-531,550
670,542,-627
-782,-478,411
677,-552,736
675,-422,649
851,-487,-643
-702,-565,-536
-852,-522,-461
-43,-34,179
-761,448,803
-705,477,745

--- scanner 28 ---
573,505,-684
8,-24,126
428,-551,785
857,610,665
-56,144,29
-507,671,603
-723,-628,-438
-717,-596,681
850,592,511
495,394,-589
464,-393,785
-586,488,-809
-697,-643,701
-698,573,-725
429,497,-687
523,-436,-581
-702,-787,657
-789,-593,-508
-533,539,692
935,526,599
540,-535,-553
-778,-650,-426
-354,610,678
116,29,-19
522,-669,-518
-553,559,-659
437,-472,786

--- scanner 29 ---
683,-540,-630
402,-538,-643
-329,-493,653
840,566,429
722,647,510
664,-649,866
28,-140,-104
878,620,-837
-765,-884,-623
732,696,-778
-28,13,9
-454,309,-532
-327,-538,662
948,661,-747
-340,-585,849
817,-625,774
434,-525,-638
865,-603,814
-430,363,472
900,551,520
-446,294,528
-808,-917,-481
-563,315,-597
-510,267,-682
-758,-915,-590
-404,258,412

--- scanner 30 ---
-299,482,-468
753,540,-526
737,658,-630
835,-810,469
-294,373,-321
-718,-593,401
-757,-504,474
-637,-474,469
-294,618,-363
356,-836,-662
-536,-675,-691
680,719,-521
505,718,872
-589,832,666
885,-853,575
-532,795,629
-626,-630,-705
-56,-7,92
385,591,857
-380,769,678
468,-782,-762
517,481,906
464,-930,-675
-557,-759,-743
852,-698,584

--- scanner 31 ---
-504,-722,764
-471,-655,604
620,778,-539
-579,438,-698
-750,-487,-538
-649,474,-531
-41,117,16
305,-582,-421
-635,-502,-459
-524,762,878
-469,-786,725
276,-591,590
365,-453,560
420,460,710
-635,417,-543
372,470,792
-182,-19,99
253,-570,-392
426,-548,665
618,810,-537
-697,-484,-614
346,-635,-282
479,460,722
-606,786,771
-653,734,906
676,838,-365

--- scanner 32 ---
-839,-599,715
351,-528,-912
377,598,754
-751,502,-745
498,820,-545
-631,-549,-889
566,-519,640
-706,-506,-739
-862,-551,669
-524,788,651
332,607,752
-149,64,-129
-455,732,635
-833,512,-793
496,852,-547
324,880,-489
-419,848,677
6,95,-6
-763,502,-686
479,-649,638
380,-540,-860
641,-691,689
424,411,741
241,-593,-819
-601,-411,-800
-813,-584,814
  
)";

const char *test_input = R"(--- scanner 0 ---
0,2,3
4,1,1
3,3,2

--- scanner 1 ---
-1,-1,-2
-5,0,1
-2,1,0
  
)";
const char *large_test_input = R"(--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14

)";
struct Transformation {
  size_t sensor_1;
  size_t sensor_2;
  std::array<std::pair<size_t, size_t>, 3> mapping;
  std::array<int, 3> offsets;
  std::array<bool, 3> flips;
  friend std::ostream &operator<<(std::ostream &os,
                                  const Transformation &transf);
};

std::ostream &operator<<(std::ostream &os, const Transformation &t) {
  os << "Transforming from sensors: " << t.sensor_1 << " " << t.sensor_2
     << '\n';
  for (const auto &m : t.mapping) {
    os << "Mapping: " << m.first << " " << m.second << '\n';
  }
  for (size_t i = 0; i < 3; ++i) {
    os << "offset: " << t.offsets[i] << '\n';
    os << "flips: " << t.flips[i] << '\n';
  }
  return os;
}

template <int N>
std::array<std::vector<std::array<int, 3>>, N> parse(const char *input) {

  std::array<std::vector<std::array<int, 3>>, N> scanners;
  auto iss = std::istringstream(input);
  int scanner = 0;
  std::regex num_regex("(-?[0-9]+)");
  for (std::string line; std::getline(iss, line);) {
    if (line.size() > 3) {
      if (line.substr(0, 3) == std::string("---")) {
        continue;
      }
      // std::cout << line << std::endl;
      auto num_begin = std::sregex_iterator(begin(line), end(line), num_regex);
      auto num_end = std::sregex_iterator();
      // std::cout << "Numbers found: " << std::distance(num_begin, num_end) <<
      // std::endl;
      std::array<int, 3> coordinates;
      int i = 0;
      for (auto itr = num_begin; itr != num_end; ++itr) {
        auto match = *itr;
        coordinates[i++] = std::stoi(match.str());
      }
      scanners[scanner].push_back(coordinates);
    } else {
      ++scanner;
    }
  }
  return scanners;
}

std::array<std::vector<int>, 3>
transpose(const std::vector<std::array<int, 3>> &beacons) {
  std::array<std::vector<int>, 3> dimensions;
  for (const auto &beacon : beacons) {
    auto [x0, x1, x2] = beacon;
    dimensions[0].push_back(x0);
    dimensions[1].push_back(x1);
    dimensions[2].push_back(x2);
  }
  return dimensions;
}

std::vector<std::tuple<int, int, int, bool>>
match(const std::array<std::vector<int>, 3> &set1,
      const std::array<std::vector<int>, 3> &set2, int num_matches = 12) {
  std::vector<std::tuple<int, int, int, bool>> matches;
  for (size_t dim1 = 0; dim1 < 3; ++dim1) {
    const auto &vec1 = set1[dim1];
    bool match_found = false;
    for (size_t dim2 = 0; dim2 < 3; ++dim2) {
      if (match_found)
        break;
      const auto &vec2 = set2[dim2];
      for (int flip = 0; flip < 2; ++flip) {
        if (match_found)
          break;
        auto flipper = [flip](auto &elem) { elem = (flip) ? -elem : elem; };
        auto flipped = vec2;
        std::for_each(begin(flipped), end(flipped), flipper);
        // std::cout << "flipped" << '\n';
        // for (auto elem : flipped) {
        //   std::cout << elem << '\n';
        //   }
        std::map<int, size_t> differences;
        for (auto elem1 : vec1) {
          for (auto elem2 : flipped) {
            differences[elem1 - elem2]++;
          }
        }
        auto iter =
            std::max_element(begin(differences), end(differences),
                             [](const auto &keyval1, const auto &keyval2) {
                               return keyval1.second < keyval2.second;
                             });
        auto [val, count] = *iter;
        if (count >= num_matches) {
          // std::cout << "vec1" << '\n';
          // for (auto elem : vec1) {
          //   std::cout << elem << '\n';
          //   }
          // std::cout << "flipped" << '\n';
          // for (auto elem : flipped) {
          //   std::cout << elem << '\n';
          //   }
          matches.push_back({dim1, dim2, val, flip});
          std::cout << dim1 << "->" << dim2 << " Offset: " << val
                    << " Flip: " << flip << '\n';
          match_found = true;
        }
      }
    }
  }
  return matches;
}

std::optional<Transformation>
find_offsets(const std::array<std::vector<int>, 3> &set1,
             const std::array<std::vector<int>, 3> &set2, size_t n1_sensor,
             size_t n2_sensor) {
  auto matches = match(set1, set2);
  auto transf = Transformation();
  if (matches.size() >= 3) {
    auto [dim0_s, dim0_t, offset0, flip0] = matches[0];
    auto [dim1_s, dim1_t, offset1, flip1] = matches[1];
    auto [dim2_s, dim2_t, offset2, flip2] = matches[2];
    transf.sensor_1 = n1_sensor;
    transf.sensor_2 = n2_sensor;
    transf.mapping[0] = {dim0_s, dim0_t};
    transf.mapping[1] = {dim1_s, dim1_t};
    transf.mapping[2] = {dim2_s, dim2_t};
    transf.offsets = {offset0, offset1, offset2};
    transf.flips = {flip0, flip1, flip2};

    return transf;
  }
  return {};
}

std::array<std::vector<int>, 3>
reverse_transformation(std::array<std::vector<int>, 3> data,
                       const Transformation &transf) {
  auto transformed = decltype(data)();
  for (int i = 0; i < 3; ++i) {
    auto m = transf.mapping[i];
    // transformed[];
    // data[m.second] += offset;
    auto column = data[m.second];
    auto offset = transf.offsets[i];
    auto flip = transf.flips[i];
    std::for_each(begin(column), end(column), [flip, offset](auto &val) {
      if (flip)
        val = -val;
      val += offset;
    });
    transformed[m.first] = column;
    std::cout << "Moving columns: " << m.first << " " << m.second << "\n";
  }

  return transformed;
}

Transformation flip_transformation(Transformation transf) {
  std::swap(transf.sensor_1, transf.sensor_2);
  for (size_t i = 0; i < 3; ++i) {
    transf.mapping[i] = {transf.mapping[i].second, transf.mapping[i].first};
    if (transf.flips[transf.mapping[i].second]) {
      transf.offsets[transf.mapping[i].second] = +transf.offsets[i];

    } else
      transf.offsets[transf.mapping[i].second] = -transf.offsets[i];
    transf.flips[transf.mapping[i].second] = transf.flips[i];
  }
  return transf;
}

Transformation combine_transformations(const Transformation &first,
                                       const Transformation &second) {
  std::cout << "combine transformations" << first << second << "\n";
  auto combined = Transformation();
  combined.sensor_1 = first.sensor_1;
  combined.sensor_2 = second.sensor_2;

  for (int i = 0; i < 3; ++i) {
    auto m1 = first.mapping[i];
    for (int j = 0; j < 3; ++j) {
      auto m2 = second.mapping[j];
      if (m1.second != m2.first)
        continue;

      combined.mapping[i] = {m1.first, m2.second};
      combined.offsets[i] = 0;
      if (first.flips[i])
        combined.offsets[i] -= second.offsets[j];
      else
        combined.offsets[i] += second.offsets[j];
      combined.offsets[i] += first.offsets[i];

      combined.flips[i] = (first.flips[i] != second.flips[j]);
    }
  }

  std::cout << "combined" << combined << "\n";

  return combined;
}
std::map<std::pair<size_t, size_t>, Transformation>
normalize_transformations(const std::vector<Transformation> &transformations) {
  std::map<std::pair<size_t, size_t>, Transformation> transformation_map;
  for (auto transf : transformations) {
    transformation_map[{transf.sensor_1, transf.sensor_2}] = transf;
  }

  std::vector<Transformation> normalized_transformations;
  bool all_mapped = false;
  while (!all_mapped) {
    all_mapped = true;
    for (auto &keyval : transformation_map) {
      auto [mapping, transf] = keyval;
      std::cout << mapping.first << " " << mapping.second << '\n';
      if (mapping.first != 0) {
        all_mapped = false;
        if (transformation_map.contains({0, mapping.first})) {
          auto pre_transf = transformation_map[{0, mapping.first}];
          transformation_map.erase(mapping);
          transformation_map[{0, mapping.second}] =
              combine_transformations(pre_transf, transf);
          break;
        } else if (transformation_map.contains({0, mapping.second})) {
          auto pre_transf = transformation_map[{0, mapping.second}];
          transformation_map.erase(mapping);
          transformation_map[{0, mapping.first}] =
              combine_transformations(pre_transf, flip_transformation(transf));
          break;
        }
      }
    }
  }

  return transformation_map;
}

int main() {
  constexpr int N = 33;
  std::array<std::vector<std::array<int, 3>>, N> scanners =
      parse<N>(puzzle_input);
  std::array<std::array<std::vector<int>, 3>, N> scanners_transposed;
  for (int i = 0; i < N; ++i) {
    scanners_transposed[i] = transpose(scanners[i]);
  }
  std::vector<Transformation> transformations;
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      auto transf =
          find_offsets(scanners_transposed[i], scanners_transposed[j], i, j);
      if (transf) {
        transformations.push_back(transf.value());
        std::cout << transf.value();
      }
    }
  }
  auto normalized_transformations = normalize_transformations(transformations);
  std::set<std::array<int, 3>> beacons;
  std::array<std::array<std::vector<int>, 3>, N> scanners_normalized;
  scanners_normalized[0] = scanners_transposed[0];
  for (auto &[mapping, transf] : normalized_transformations) {
    std::cout << transf;
  }

  for (int scanner_idx = 1; scanner_idx < N; ++scanner_idx) {
    std::cout << "Applying: " << normalized_transformations[{0, scanner_idx}];
    auto transformed =
        reverse_transformation(scanners_transposed[scanner_idx],
                               normalized_transformations[{0, scanner_idx}]);
    scanners_normalized[scanner_idx] = transformed;
    for (size_t j = 0; j < transformed[0].size(); ++j) {
      std::array<int, 3> b{transformed[0][j], transformed[1][j],
                           transformed[2][j]};
      std::cout << b[0] << "," << b[1] << "," << b[2] << "\n";
    }
  }
  for (const auto &transformed : scanners_normalized) {
    for (size_t j = 0; j < transformed[0].size(); ++j) {
      std::array<int, 3> b{transformed[0][j], transformed[1][j],
                           transformed[2][j]};
      // std::cout << b[0] << "," << b[1] << "," << b[2] << "\n";
      std::cout << b[0] << "," << b[1] << "," << b[2] << "\n";
      beacons.insert(b);
    }
  }
  std::cout << beacons.size() << std::endl;
  std::vector<int> manhattan_distances;
  for (auto &[mapping, t] : normalized_transformations) {
    for (auto &[mapping2, t2] : normalized_transformations) {
      if (mapping == mapping2)
        continue;
      auto scanner_distance = (std::abs(t.offsets[0] - t2.offsets[0]) +
                               std::abs(t.offsets[1] - t2.offsets[1]) +
                               std::abs(t.offsets[2] - t2.offsets[2]));
      manhattan_distances.push_back(scanner_distance);
    }
  }
  std::cout << *std::max_element(begin(manhattan_distances), end(manhattan_distances));
}