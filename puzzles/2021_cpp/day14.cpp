#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
struct Rule {
  char first;
  char second;
  char inbetween;
};

const Rule puzzle_rules[] = {
    {'K', 'O', 'F'}, {'C', 'V', 'H'}, {'C', 'F', 'P'}, {'F', 'K', 'B'},
    {'B', 'N', 'P'}, {'V', 'N', 'K'}, {'B', 'C', 'H'}, {'O', 'P', 'S'},
    {'H', 'S', 'V'}, {'H', 'K', 'N'}, {'C', 'C', 'F'}, {'C', 'K', 'V'},
    {'O', 'C', 'S'}, {'S', 'N', 'C'}, {'P', 'K', 'H'}, {'B', 'B', 'S'},
    {'P', 'O', 'F'}, {'H', 'F', 'K'}, {'B', 'V', 'P'}, {'H', 'P', 'F'},
    {'V', 'F', 'H'}, {'B', 'P', 'H'}, {'C', 'H', 'C'}, {'K', 'N', 'O'},
    {'N', 'P', 'F'}, {'F', 'S', 'F'}, {'B', 'H', 'B'}, {'V', 'B', 'P'},
    {'O', 'S', 'S'}, {'K', 'K', 'O'}, {'S', 'O', 'P'}, {'N', 'B', 'O'},
    {'P', 'S', 'O'}, {'K', 'V', 'O'}, {'C', 'S', 'P'}, {'P', 'N', 'O'},
    {'H', 'B', 'V'}, {'N', 'F', 'P'}, {'S', 'C', 'S'}, {'N', 'H', 'N'},
    {'H', 'V', 'K'}, {'F', 'N', 'V'}, {'K', 'S', 'P'}, {'B', 'O', 'C'},
    {'K', 'P', 'V'}, {'O', 'K', 'B'}, {'O', 'V', 'P'}, {'C', 'N', 'C'},
    {'S', 'B', 'H'}, {'V', 'P', 'C'}, {'H', 'C', 'P'}, {'F', 'B', 'F'},
    {'V', 'S', 'K'}, {'P', 'H', 'C'}, {'V', 'C', 'H'}, {'K', 'H', 'B'},
    {'S', 'H', 'B'}, {'B', 'K', 'N'}, {'S', 'P', 'P'}, {'S', 'F', 'B'},
    {'O', 'O', 'B'}, {'V', 'H', 'K'}, {'P', 'P', 'C'}, {'F', 'V', 'P'},
    {'K', 'C', 'P'}, {'C', 'O', 'S'}, {'N', 'O', 'O'}, {'F', 'O', 'K'},
    {'S', 'K', 'O'}, {'O', 'N', 'K'}, {'V', 'O', 'H'}, {'V', 'V', 'H'},
    {'C', 'P', 'P'}, {'F', 'C', 'B'}, {'F', 'P', 'N'}, {'F', 'H', 'C'},
    {'K', 'F', 'F'}, {'P', 'B', 'C'}, {'N', 'N', 'K'}, {'S', 'S', 'O'},
    {'C', 'B', 'C'}, {'H', 'H', 'S'}, {'F', 'F', 'S'}, {'K', 'B', 'N'},
    {'H', 'O', 'O'}, {'B', 'F', 'N'}, {'P', 'V', 'K'}, {'O', 'B', 'B'},
    {'O', 'H', 'N'}, {'V', 'K', 'V'}, {'N', 'V', 'H'}, {'S', 'V', 'F'},
    {'N', 'C', 'P'}, {'O', 'F', 'V'}, {'N', 'S', 'V'}, {'P', 'F', 'N'},
    {'H', 'N', 'K'}, {'B', 'S', 'S'}, {'N', 'K', 'H'}, {'P', 'C', 'O'},
};

const Rule test_rules[] = {
    {'C', 'H', 'B'}, {'H', 'H', 'N'}, {'C', 'B', 'H'}, {'N', 'H', 'C'},
    {'H', 'B', 'C'}, {'H', 'C', 'B'}, {'H', 'N', 'C'}, {'N', 'N', 'C'},
    {'B', 'H', 'H'}, {'N', 'C', 'B'}, {'N', 'B', 'B'}, {'B', 'N', 'B'},
    {'B', 'B', 'N'}, {'B', 'C', 'B'}, {'C', 'C', 'N'}, {'C', 'N', 'C'}};

const char *test_input = "NNCB";
const char *puzzle_input = "CFFPOHBCVVNPHCNBKVNV";

auto step(const std::map<std::pair<char, char>, int64_t> pairs,
          std::vector<Rule> rules) -> decltype(pairs) {

  auto newpairs = decltype(pairs){};
  for (const auto [key, val] : pairs) {
    auto [first, second] = key;

    bool rule_triggered = false;
    for (auto rule : rules) {
      if (rule.first == first && rule.second == second) {
        newpairs[{rule.first, rule.inbetween}] += val;
        newpairs[{rule.inbetween, rule.second}] += val;
        rule_triggered = true;
        break;
      }
    }
    if (!rule_triggered) {
      newpairs[{first, second}] += val;
    }
  }

  return newpairs;
}

int main() {
  std::map<std::pair<char, char>, int64_t> pairs;
  auto start_string = std::string{puzzle_input};
  start_string.append(" ");
  for (std::size_t i = 0; i < start_string.size() - 1; ++i) {
    ++pairs[std::pair(start_string[i], start_string[i + 1])];
  }
  auto rules =
      std::vector<Rule>(std::begin(puzzle_rules), std::end(puzzle_rules));
  for (int i = 0; i < 40; ++i) {
    pairs = step(pairs, rules);
  }
  auto count = 0;
  for (auto [key, val] : pairs) {
    auto [first, second] = key;
    std::cout << first << " " << second << " " << val << "\n";
    count += val;
  }
  std::cout << count << std::endl;
  std::map<char, int64_t> char_counts;
  for (auto [key, val] : pairs) {
    auto [first, second] = key;
    char_counts[first] += val;
  }
  const auto [min, max] = std::minmax_element(
      std::cbegin(char_counts), std::cend(char_counts),
      [](auto kv1, auto kv2) { return kv1.second < kv2.second; });
  std::cout << max->second - min->second << std::endl;
}