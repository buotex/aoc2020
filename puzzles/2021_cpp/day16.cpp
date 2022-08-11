#include <algorithm>
#include <bitset>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

std::vector<int32_t> version_numbers;
auto decode_packet(const std::vector<std::bitset<4>> &bitsets) {
  int header;
  int typeID;
}
auto decode_hex(const std::string &input) {

  std::vector<std::bitset<4>> bitsets;
  for (auto hex_char : input) {
    std::stringstream ss;
    ss << std::hex << hex_char;
    //std::cout << ss.str() << std::endl;
    int num;
    ss >> num;
    bitsets.push_back(std::bitset<4>(num));
  }
  std::string output;
  output.resize(4 * bitsets.size());
  int pos = 0;
  for (auto bitset : bitsets) {
    output.replace(pos, 4, bitset.to_string());
    pos += 4;
  }
  return output;
}

int64_t bool2int(const std::vector<int> &binary_num) {

  int64_t sum = 0;
  int64_t multiplier = 1;
  std::cout << "Parsing boolean vector" << std::endl;
  std::cout << "number length: " << binary_num.size() << std::endl;
  for (auto c: binary_num) {
    std::cout << c;
    }
  std::cout << std::endl;
  for (auto digit_ptr = binary_num.crbegin(); digit_ptr != binary_num.crend();
       ++digit_ptr) {
    sum += int64_t{*digit_ptr} * multiplier;
    //std::cout << sum << std::endl;
    multiplier *= 2;
  }
  return sum;
}
int64_t str2int(const std::string &binary_num) {
  std::cout << "Parsing string: " << binary_num << std::endl;
  int64_t sum = 0;
  int multiplier = 1;
  for (auto digit_ptr = binary_num.crbegin(); digit_ptr != binary_num.crend();
       ++digit_ptr) {
    sum += (*digit_ptr == '1') * multiplier;
    multiplier *= 2;
  }
  return sum;
}

int64_t parse_binary_num(const std::string &input, size_t &pos) {

  std::vector<int> binary_num;
  while (input[pos++] != '0') {
    for (int i = 0; i < 4; ++i) {
      binary_num.push_back(input[pos++] == '1');
    }
  }
  for (int i = 0; i < 4; ++i) {
    binary_num.push_back(input[pos++] == '1');
  }
  auto sum = bool2int(binary_num);

  return sum;
}
int64_t parse_packet(const std::string &input, size_t &pos);
int64_t parse_operator(const std::string &input, size_t &pos, int8_t type_id) {

  bool length_type_id = (input[pos++] == '1');
  std::vector<int64_t> values;
  if (length_type_id == 0) {
    // handle num bits case
    int length = str2int(input.substr(pos, 15));
    pos += 15;
    auto original_pos = pos;
    std::cout << "length_subpackets: " << length << std::endl;
    while (pos < original_pos + length) {
      auto val = parse_packet(input, pos);
      std::cout << "Pos after: " << pos << std::endl;
      std::cout << "max pos " << original_pos + length << std::endl;
      values.push_back(val);
    }
  } else {
    int num_subpackets = str2int(input.substr(pos, 11));
    std::cout << "Num_subpackets: " << num_subpackets << std::endl;
    pos += 11;
    for (int i = 0; i < num_subpackets; ++i) {
      auto val = parse_packet(input, pos);
      values.push_back(val);
    }
  }
  int64_t retval = 0;
  switch (type_id) {
    case 0:
      retval = std::accumulate(values.cbegin(), values.cend(), 0LL);
    break;
    case 1:
      retval = std::accumulate(values.cbegin(), values.cend(), 1LL, [](auto a, auto b){return a * b;});
    break;
    case 2:
      retval = std::accumulate(values.cbegin(), values.cend(), std::numeric_limits<int64_t>::max(), [](auto a, auto b){return std::min(a, b);});
    break;
    case 3:
      retval = std::accumulate(values.cbegin(), values.cend(), 0LL, [](auto a, auto b){return std::max(a, b);});
    break;
    case 5:
      std::cout << "greater: " << values[0] << " " << values[1] << std::endl;
      retval = values[0] > values[1];
    break;
    case 6:
      std::cout << "less: " << values[0] << " " << values[1] << std::endl;
      retval = values[0] < values[1];
    break;
    case 7:
      std::cout << "equal: " << values[0] << " " << values[1] << std::endl;
      retval = values[0] == values[1];
    break;
  }
  return retval;
}

int64_t parse_packet(const std::string &input, size_t &pos) {
  if (pos + 6 + 5 > input.size()) {
    std::cout << "pos: " << pos << std::endl;
    pos = input.size();
    return 0;
  }
  std::cout << "Current position of packet: " << pos << std::endl;
  std::cout << "6 bits: " << input.substr(pos, 6) << std::endl;
  auto version = std::bitset<3>(input, pos, 3).to_ulong();
  std::cout << "version: " << version << std::endl;
  version_numbers.push_back(version);
  pos += 3;
  auto type_id = std::bitset<3>(input, pos, 3).to_ulong();
  pos += 3;

  if (type_id == 4) {
    auto binary_num = parse_binary_num(input, pos);
    std::cout << "number: " << binary_num << std::endl;
    return binary_num;
  } else {
    auto binary_num = parse_operator(input, pos, type_id);
    return binary_num;
  }
}
int64_t workflow(const std::string & hex_input) {

  version_numbers.clear();
  auto input = decode_hex(hex_input);
  std::cout << " " << std::endl;
  std::cout << input << std::endl;
  size_t pos = 0;
  //std::cout << "Length of packet: " << input.size() << std::endl;
  auto result = parse_packet(input, pos);
   // std::cout << "version sum: "
   //          << std::accumulate(version_numbers.cbegin(), version_numbers.cend(),
   //                             0LL)
   //          << std::endl;
  return result;
  }

int main() {
  // std::string test_input = "D2FE28";
  // std::string test_input = "38006F45291200";
  std::string test_input = "620080001611562C8802118E34";
  std::string sum_input = "C200B40A82";
  std::string prod_input = "04005AC33890";
  std::string min_input = "880086C3E88112";
  std::string max_input = "CE00C43D881120";
  std::string less_input = "D8005AC2A8F0";
  std::string greater_input = "F600BC2D8F";
  std::string equal_input = "9C005AC2F8F0";
  std::string equal_input2 = "9C0141080250320F1802104A08";
  std::string puzzle_input =
      "005532447836402684AC7AB3801A800021F0961146B1007A1147C89440294D005C12D2A7"
      "BC992D3F4E50C72CDF29EECFD0ACD5CC016962099194002CE31C5D3005F401296CAF4B65"
      "6A46B2DE5588015C913D8653A3A001B9C3C93D7AC672F4FF78C136532E6E0007FCDFA975"
      "A3004B002E69EC4FD2D32CDF3FFDDAF01C91FCA7B41700263818025A00B48DEF3DFB89D2"
      "6C3281A200F4C5AF57582527BC1890042DE00B4B324DBA4FAFCE473EF7CC0802B59DA285"
      "80212B3BD99A78C8004EC300761DC128EE40086C4F8E50F0C01882D0FE29900A01C01C2C"
      "96F38FCBB3E18C96F38FCBB3E1BCC57E2AA0154EDEC45096712A64A2520C6401A9E80213"
      "D98562653D98562612A06C0143CB03C529B5D9FD87CBA64F88CA439EC5BB299718023800"
      "D3CE7A935F9EA884F5EFAE9E10079125AF39E80212330F93EC7DAD7A9D5C4002A24A806A"
      "0062019B6600730173640575A0147C60070011FCA005000F7080385800CBEE006800A30C"
      "023520077A401840004BAC00D7A001FB31AAD10CC016923DA00686769E019DA780D00223"
      "94854167C2A56FB75200D33801F696D5B922F98B68B64E02460054CAE900949401BB8002"
      "1D0562344E00042A16C6B8253000600B78020200E44386B068401E8391661C4E14B804D3"
      "B6B27CFE98E73BCF55B65762C402768803F09620419100661EC2A8CE0008741A83917CC0"
      "24970D9E718DD341640259D80200008444D8F713C401D88310E2EC9F20F3330E05900911"
      "8019A8803F12A0FC6E1006E3744183D27312200D4AC01693F5A131C93F5A131C970D6008"
      "867379CD3221289B13D402492EE377917CACEDB3695AD61C939C7C10082597E3740E8573"
      "96499EA31980293F4FD206B40123CEE27CFB64D5E57B9ACC7F993D9495444001C998E66B"
      "50896B0B90050D34DF3295289128E73070E00A4E7A389224323005E801049351952694C0"
      "00";

  std::cout << "expected_sum: 3, result: " << workflow(sum_input) << std::endl;
  std::cout << "expected_prod: 54, result: " << workflow(prod_input) << std::endl;
  std::cout << "expected_min: 7, result: " << workflow(min_input) << std::endl;
  std::cout << "expected_max: 9, result: " << workflow(max_input) << std::endl;
  std::cout << "expected_less: 1, result: " << workflow(less_input) << std::endl;
  std::cout << "expected_greater: 0, result: " << workflow(greater_input) << std::endl;
  std::cout << "expected_equal: 0, result: " << workflow(equal_input) << std::endl;
  std::cout << "expected_equal2: 1, result: " << workflow(equal_input2) << std::endl;
  std::cout << "result: " << workflow(puzzle_input) << std::endl;

}