#include <array>
#include <cstdio>
#include <iostream>
#include <utility>
const std::array<std::array<int8_t, 12>, 12> test_data = {{
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 5, 4, 8, 3, 1, 4, 3, 2, 2, 3, 0},
    {0, 2, 7, 4, 5, 8, 5, 4, 7, 1, 1, 0},
    {0, 5, 2, 6, 4, 5, 5, 6, 1, 7, 3, 0},
    {0, 6, 1, 4, 1, 3, 3, 6, 1, 4, 6, 0},
    {0, 6, 3, 5, 7, 3, 8, 5, 4, 7, 8, 0},
    {0, 4, 1, 6, 7, 5, 2, 4, 6, 4, 5, 0},
    {0, 2, 1, 7, 6, 8, 4, 1, 7, 2, 1, 0},
    {0, 6, 8, 8, 2, 8, 8, 1, 1, 3, 4, 0},
    {0, 4, 8, 4, 6, 8, 4, 8, 5, 5, 4, 0},
    {0, 5, 2, 8, 3, 7, 5, 1, 5, 2, 6, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
}};

const std::array<std::array<int8_t, 12>, 12> puzzle_data = {{
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 4, 8, 3, 6, 4, 8, 4, 5, 5, 5, 0},
    {0, 4, 6, 6, 3, 8, 4, 1, 7, 7, 2, 0},
    {0, 3, 5, 1, 2, 4, 8, 4, 5, 5, 6, 0},
    {0, 1, 4, 8, 1, 5, 4, 7, 5, 7, 2, 0},
    {0, 7, 7, 4, 1, 1, 8, 3, 4, 2, 2, 0},
    {0, 8, 6, 8, 3, 2, 2, 2, 8, 8, 2, 0},
    {0, 4, 2, 1, 5, 2, 4, 4, 2, 3, 3, 0},
    {0, 1, 5, 4, 4, 7, 1, 2, 1, 7, 1, 0},
    {0, 5, 7, 2, 5, 8, 5, 5, 7, 8, 6, 0},
    {0, 1, 7, 1, 7, 3, 8, 2, 2, 8, 1, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
}};

template <typename T, size_t N, size_t M>
void printer(const std::array<std::array<T, N>, M> &arr) {
  for (size_t i = 0; i < N; ++i) {
    for (size_t j = 0; j < M; ++j) {
      printf("%d", arr[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}

template <typename T, size_t N, size_t M>
void printer(const std::array<std::array<T, N>, M> &arr,
             const std::array<std::array<bool, N>, M> &do_bold,
             bool skip_border = true) {
  for (size_t i = skip_border; i < N - skip_border; ++i) {
    for (size_t j = skip_border; j < M - skip_border; ++j) {
      if (do_bold[i][j]) {
        printf("\033[1m%d\033[0m", arr[i][j]);
      } else {
        printf("%d", arr[i][j]);
      }
    }
    printf("\n");
  }
  printf("\n");
}

template <typename T, size_t N, size_t M>
std::array<std::array<T, N>, M> step(std::array<std::array<T, N>, M> &arr) {
  for (size_t i = 1; i < N - 1; ++i) {
    for (size_t j = 1; j < M - 1; ++j) {
      arr[i][j] += 1;
    }
  }
  return arr;
}

template <typename T, size_t N, size_t M>
int flash(std::array<std::array<T, N>, M> &arr) {
  std::array<std::array<bool, N>, M> is_flashing = {{{false}}};
  bool new_flash = true;
  while (new_flash) {
    new_flash = false;
    for (size_t i = 1; i < N - 1; ++i) {
      for (size_t j = 1; j < M - 1; ++j) {
        if (arr[i][j] > 9) {
          if (is_flashing[i][j] == false) {
            is_flashing[i][j] = true;
            arr[i - 1][j - 1] += 1;
            arr[i - 1][j] += 1;
            arr[i - 1][j + 1] += 1;
            arr[i][j - 1] += 1;
            arr[i][j + 1] += 1;
            arr[i + 1][j - 1] += 1;
            arr[i + 1][j] += 1;
            arr[i + 1][j + 1] += 1;
            new_flash = true;
          }
        }
      }
    }
  }
  for (size_t i = 1; i < N - 1; ++i) {
    for (size_t j = 1; j < M - 1; ++j) {
      if (is_flashing[i][j]) {
        arr[i][j] = 0;
      }
    }
  }
  for (size_t i = 0; i < N; ++i) {
    arr[i][0] = 0;
    arr[i][M - 1] = 0;
  }
  for (size_t j = 0; j < M; ++j) {
    arr[0][j] = 0;
    arr[N - 1][j] = 0;
  }
  printer(arr, is_flashing);
  int count_flashes = 0;
  for (size_t i = 1; i < N - 1; ++i) {
    for (size_t j = 1; j < M - 1; ++j) {
      count_flashes += (is_flashing[i][j]);
    }
  }
  return count_flashes;
}

int main() {
  auto data = puzzle_data;
  printer(data);

  int count_flashes = 0;
  for (int i = 0; i < 100; ++i) {
    step(data);
    count_flashes += flash(data);
  }
  std::cout << "Part1: " << count_flashes;
  data = puzzle_data;
  for (int i = 1; i < 1000; ++i) {
    step(data);
    auto flashes = flash(data);
    if (flashes == 100) {
      std::cout << "Part2: " << i << std::endl;
      break;
    }
  }
}
