#include <cmath>
#include <iostream>
#include <vector>
#include <utility>


int find_values(int x_min, int x_max, int y_min, int y_max) {
  std::vector<std::pair<int, int> > valid_combinations;
  
  int y_limit_upper = -(y_min) - 1; //should be positive
  int y_limit_lower = y_min;
  
  int x_limit_lower = std::floor(std::sqrt(x_min * 2));
  int x_limit_upper = x_max;
  std::cout << "x_limits: " << x_limit_lower << " "<< x_limit_upper << std::endl;
  for (int y_init= y_limit_lower; y_init <= y_limit_upper; ++y_init) {
    for (int x_init = x_limit_lower; x_init <= x_limit_upper; ++x_init) {
      int y_delay = 0;
      auto x_vel = x_init;
      auto y_vel = y_init;
      auto x_current = 0;
      auto y_current = 0;
      if (y_init > 0) {
        y_delay = 2 * y_init + 1;
        y_vel = -(y_init) - 1;
      }
      //y_delay = std::min(y_delay, x_vel);
      x_current = (x_vel * (x_vel + 1) / 2);
      if (x_vel > y_delay) {
        x_current -= ((x_vel - y_delay) * ((x_vel - y_delay) + 1) / 2);
        }
      x_vel = std::max(x_vel - y_delay, 0);


      //scenario1: x_vel > delay -> we don't do all steps
      //scenario2: delay > x_vel -> we are stopping after a while, don't change anything
      
      while (y_current >= y_min) {
        // std::cout << "y_current: " << y_current << "\n";
        // std::cout << "y_vel: " << y_vel << "\n";

        if (y_current <= y_max && x_current >= x_min && x_current <= x_max){
          valid_combinations.push_back({x_init, y_init});
          break;
        }
        y_current += y_vel;
        --y_vel;
        if (x_vel > 0)
        {
          x_current += x_vel;
          --x_vel;
        }
        else {
          if (x_current < x_min) {
            break;
            }
          }
      }
    }
  }
  
  // for (auto & element: valid_combinations) {
  //   std::cout << element.first << " " << element.second << "\n";
  //   }
  
  return valid_combinations.size();
}

int main() {
  std::cout << find_values(20, 30, -10, -5) << "\n";
  std::cout << find_values(94, 151, -156, -103)<< '\n';
}
