#include <iostream>
#include <string>
#include <vector>

const char *puzzle_input = R"([[2,[[1,1],9]],[[0,[3,0]],[[1,6],[4,2]]]]
[[8,[0,5]],[[[9,9],0],[[2,9],2]]]
[[[[6,4],[5,8]],[[0,9],[6,5]]],[[5,1],4]]
[[[9,[2,8]],[[0,2],[8,3]]],[[[5,6],[5,8]],[[4,8],2]]]
[[0,[[0,1],[6,0]]],[[[6,4],1],[8,6]]]
[[[[8,5],6],8],[[[9,1],[0,6]],[4,[2,4]]]]
[7,[[4,3],[8,5]]]
[[8,[1,[3,4]]],[[3,8],[0,1]]]
[[[1,1],[[2,1],[0,3]]],[[7,[1,8]],[[3,8],[5,2]]]]
[[2,[[4,6],[6,2]]],[[0,5],[3,7]]]
[[[[9,8],[4,6]],[7,[9,1]]],[[[8,7],[4,7]],[[6,6],[8,1]]]]
[[[2,[5,1]],[[0,4],3]],[[9,7],[[0,2],0]]]
[[[[5,0],2],5],[[3,[5,8]],[5,[8,9]]]]
[[6,[3,6]],[[[2,7],6],[[6,0],4]]]
[[8,8],7]
[[[[7,9],3],8],[[0,[1,7]],[[3,2],[4,5]]]]
[[[1,1],[7,2]],[3,[4,[6,4]]]]
[[[9,[6,6]],[[4,8],[1,3]]],[[[4,7],8],[[5,2],[3,8]]]]
[[[6,[6,7]],[3,4]],5]
[[[[0,0],2],9],[[[2,1],1],[5,[4,7]]]]
[[[2,[9,8]],[5,8]],[[[3,4],6],[5,0]]]
[[[7,[9,4]],[7,[7,2]]],[[1,[9,6]],1]]
[[[[9,1],1],[4,[2,6]]],3]
[[0,[8,[3,4]]],[8,[9,8]]]
[[[1,6],[6,7]],[[[0,4],1],7]]
[[6,[5,[0,0]]],[7,[[5,4],1]]]
[[2,[[9,5],[9,1]]],[[3,0],4]]
[[[5,7],[[1,0],[3,5]]],[4,[5,[4,0]]]]
[[3,3],[2,2]]
[[[[6,2],[1,7]],[1,7]],[[[6,7],6],9]]
[[[[9,8],[8,8]],[2,1]],[[8,4],8]]
[[[[1,4],1],[2,0]],[4,[[0,5],5]]]
[[[7,[6,0]],[[7,3],1]],9]
[[[[2,4],0],[[6,9],8]],[[3,[0,9]],[[4,4],[5,4]]]]
[[7,3],[0,[2,[7,2]]]]
[[[[8,8],5],9],[[8,6],6]]
[[[[9,5],7],9],0]
[[[1,4],8],[[7,[5,3]],[[6,4],6]]]
[[9,[[9,3],[3,7]]],[[[6,9],1],[[2,3],[4,4]]]]
[[4,[9,2]],[3,4]]
[[1,[[0,9],2]],[1,[1,[8,7]]]]
[[[4,1],8],[9,[9,[2,9]]]]
[[[[7,9],[9,7]],8],[[[3,0],5],[[7,8],[3,1]]]]
[[[[9,4],[9,9]],[[9,5],[8,9]]],[[2,[7,4]],[[4,6],6]]]
[[[[8,7],1],[6,8]],[[4,2],5]]
[7,[3,[3,3]]]
[[[4,9],[0,2]],[[[4,2],9],[[5,8],6]]]
[[[[1,3],1],[[7,5],[4,0]]],[[[6,3],4],[[1,2],8]]]
[[[[3,2],2],[4,7]],[[[5,6],[6,3]],3]]
[[[[4,0],6],[4,2]],[7,5]]
[[[[9,5],[2,0]],[[6,8],[0,9]]],[[[7,4],[3,6]],1]]
[[[4,[9,3]],[[9,4],8]],[[6,[1,2]],2]]
[[[[4,1],[1,1]],[[4,8],9]],[[[1,0],[0,3]],2]]
[[[3,[3,8]],[[0,6],7]],[[2,5],9]]
[[[0,[6,8]],[[2,7],[4,1]]],6]
[[6,3],0]
[[[3,[7,1]],[3,[2,0]]],[[[3,5],9],[[5,2],[7,8]]]]
[[7,8],[1,[[7,1],5]]]
[[[9,[8,9]],2],[9,[[8,8],4]]]
[[[8,[5,8]],[[9,1],[6,0]]],[[[9,1],[4,7]],8]]
[5,[[[4,9],7],[[6,0],[9,0]]]]
[[[[8,8],[6,7]],[[1,0],6]],[[5,[2,8]],[[8,0],[3,7]]]]
[[0,[6,6]],[[0,1],[3,[9,2]]]]
[[1,[0,[8,1]]],[[0,[0,0]],[8,[0,0]]]]
[[[4,[1,4]],[8,[9,5]]],7]
[7,[[[0,0],[4,3]],8]]
[[[9,1],[[7,5],[9,2]]],[5,[9,0]]]
[[[[2,0],9],[8,[3,0]]],[[9,8],[4,[0,7]]]]
[4,[5,[5,[0,3]]]]
[[6,[[6,9],8]],[1,[0,[6,0]]]]
[[7,[4,3]],[[0,6],[[5,2],[6,9]]]]
[[[[7,2],[4,6]],[[5,0],9]],6]
[[[0,1],[0,2]],[0,[5,2]]]
[[[[5,0],[5,4]],[[5,9],[9,9]]],[2,[[3,0],[8,1]]]]
[[[[9,2],[2,9]],[[5,5],2]],[[1,3],[[3,6],[1,8]]]]
[[0,[2,4]],[[[6,9],1],[[7,9],[9,8]]]]
[[[[2,1],1],[7,3]],[4,[[1,2],[2,6]]]]
[[[6,[0,1]],[[6,4],[4,2]]],[1,[[0,0],[9,7]]]]
[[[[9,2],3],[9,8]],[[6,5],[7,[1,7]]]]
[[3,9],7]
[[[6,9],[[0,2],0]],[[[8,6],2],9]]
[[[[2,2],2],[[6,7],7]],[[0,3],9]]
[[[7,[2,7]],3],4]
[[[[1,9],6],[0,7]],[[[2,2],1],2]]
[9,9]
[0,[9,[[4,1],1]]]
[[[[7,6],1],2],[[[6,9],[9,1]],0]]
[[[[4,3],[4,2]],3],[[5,[6,5]],[[2,6],0]]]
[[[0,[5,1]],[6,[1,4]]],[5,[[8,1],3]]]
[6,[9,6]]
[[8,[9,[6,8]]],[[4,9],[[2,4],[7,1]]]]
[[5,[[9,9],[3,3]]],[[[9,8],[5,0]],6]]
[[6,7],1]
[1,[4,[[9,6],0]]]
[[[[9,8],[7,8]],[5,[4,6]]],[[[5,9],6],[[4,6],4]]]
[[[2,7],4],[[[0,3],0],[[7,4],[7,4]]]]
[7,[0,4]]
[1,[3,2]]
[[3,0],8]
[[[3,2],5],8]
)";

const char *test_input = R"([1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
)";
const char *large_test_input = R"([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
)";

std::vector<std::string> parse(const char *inp) {
  std::string::size_type pos = 0;
  std::string::size_type prev = 0;

  std::string input = std::string(inp);
  std::string delimiter = "\n";
  std::vector<std::string> lines;
  while ((pos = input.find(delimiter, prev)) != std::string::npos) {

    std::string line = input.substr(prev, pos - prev);
    lines.push_back(line);
    prev = pos + delimiter.size();
  }
  return lines;
}

struct TreeNode {
  int val;
  std::unique_ptr<TreeNode> left;
  std::unique_ptr<TreeNode> right;
  TreeNode * parent;

  TreeNode() : val(0), parent(0) {}
  TreeNode(int _val) : val(_val), parent(0) {}
  static std::unique_ptr<TreeNode> copy(TreeNode * root) {
    if (root == nullptr) return std::unique_ptr<TreeNode>(nullptr);
    auto root_copy = std::make_unique<TreeNode>();
    root_copy->val = root->val;
    root_copy->left = copy(root->left.get());
    if (root_copy->left) root_copy->left->parent = root_copy.get();
    root_copy->right = copy(root->right.get());
    if (root_copy->right) root_copy->right->parent = root_copy.get();
    return root_copy;
    
  }

  friend std::unique_ptr<TreeNode> operator+(TreeNode lhs, const TreeNode &rhs);
  friend void print(TreeNode *root, int depth);
};

void print(TreeNode *root, int depth = 0) {
  if (root->left) {
    std::cout << '[';
    print(root->left.get(), depth + 1);
    if (!root->right) {
      throw std::runtime_error("Missing right node");
    }
    std::cout << ',';
    print(root->right.get(), depth + 1);
    std::cout << ']';

  } else {
    std::cout << root->val;
  }
  if (depth == 0) {
    std::cout << '\n';
  }
}
TreeNode *find_pred(TreeNode *node) {
  //std::cout << "Finding predecessor for: " << node->val << std::endl;
  bool found_parent = false;
  while (node->parent != nullptr) {
    // go upwards, till we're the right child
    if (node->parent->right.get() == node) {
      node = node->parent;
      found_parent = true;
      break;
    }
    node = node->parent;
  }
  if (!found_parent) {
    return nullptr;
  }
  //std::cout << "Found parent" << std::endl;
  node = node->left.get();
  while (node->right != nullptr) {
    node = node->right.get();
  }
  if (node != nullptr) {
    //std::cout << "Found predecessor: " << node->val << std::endl;
  }

  return node;
}
TreeNode *find_succ(TreeNode *node) {
  bool found_parent = false;
  while (node->parent != nullptr) {
    // go upwards, till we're the right child
    if (node->parent->left.get() == node) {
      node = node->parent;
      found_parent = true;
      break;
    }
    node = node->parent;
    //print(node);
  }
  if (!found_parent) {
    return nullptr;
  }
  node = node->right.get();
  while (node->left != nullptr) {
    node = node->left.get();
  }
  if (node != nullptr) {
    //std::cout << "Found successor: " << node->val << std::endl;
  }

  return node;
}

bool explode(const std::unique_ptr<TreeNode> & root, int depth = 0) {
  bool has_changed = false;
  if (root == nullptr) {
    return false;
  }
  if (depth == 4) {
    // we should be able to assume that it isn't any deeper than this.
    if (root->left) { // not terminal
      //print(root.get());
      auto pred = find_pred(root->left.get());
      auto succ = find_succ(root->right.get());
      if (pred) {
        pred->val += root->left->val;
      }
      if (succ) {
        succ->val += root->right->val;
      }
      root->left.reset();
      root->right.reset();
      has_changed = true;
    }
    // explode
  }

  if (!has_changed)
    has_changed |= explode(root->left, depth + 1);
  if (!has_changed)
    has_changed |= explode(root->right, depth + 1);
  return has_changed;
}
bool split(const std::unique_ptr<TreeNode> &root) {
  bool has_changed = false;
  if (root == nullptr)
    return false;
  // std::cout << "val: " << root->val << std::endl;
  if (root->val > 9) {
    auto stored_val = root->val;
    auto left_val = root->val / 2;
    auto right_val = (root->val + 1) / 2;
    root->val = 0;
    root->left = std::make_unique<TreeNode>(left_val);
    root->right = std::make_unique<TreeNode>(right_val);
    root->left->parent = root.get();
    root->right->parent = root.get();
    has_changed = true;
  }

  if (!has_changed)
    has_changed |= split(root->left);

  if (!has_changed)
    has_changed |= split(root->right);

  return has_changed;
}

void fix_tree(const std::unique_ptr<TreeNode> &root) {
  bool has_changed = true;
  while (has_changed) {
    has_changed = false;
    //print(root.get());
    has_changed |= explode(root);
    //std::cout << "After explode" << std::endl;
    //print(root.get());
    if (has_changed)
      continue;
    has_changed |= split(root);
    //std::cout << "After split" << std::endl;
    //print(root.get());
  }
}
std::unique_ptr<TreeNode> operator+(const std::unique_ptr<TreeNode> & lhs,
                                    const std::unique_ptr<TreeNode> & rhs) {
  auto new_tree = std::make_unique<TreeNode>();
  new_tree->left = std::move(TreeNode::copy(lhs.get()));
  new_tree->left->parent = new_tree.get();
  new_tree->right = std::move(TreeNode::copy(rhs.get()));
  new_tree->right->parent = new_tree.get();
  //std::cout << "Before fixing" << std::endl;
  //print(new_tree.get());
  fix_tree(new_tree);
  return new_tree;
}

int64_t get_magnitude(TreeNode *root) {
  int64_t sum = 0;
  if (root->left) {
    sum += 3 * get_magnitude(root->left.get());
  }
  if (root->right) {
    sum += 2 * get_magnitude(root->right.get());
  }
  sum += root->val;
  return sum;
}
std::unique_ptr<TreeNode> handle_line(const std::string &line) {
  std::cout << "Handling line: " << line << std::endl;
  int nested_level = 0;

  auto tree = std::make_unique<TreeNode>();
  auto current_node = tree.get();

  for (auto chr : line) {
    switch (chr) {
    case '[':
      if (!current_node->left) {
        current_node->left = std::make_unique<TreeNode>();
        current_node->left->parent = current_node;
      }
      current_node = current_node->left.get();
      break;

    case ']':
      current_node = current_node->parent;
      break;
    case ',':
      current_node = current_node->parent;
      if (!current_node->right) {
        current_node->right = std::make_unique<TreeNode>();
        current_node->right->parent = current_node;
      }
      current_node = current_node->right.get();
      break;
    default:
      current_node->val = chr - '0';
    }
  }

  return tree;
}
int main() {
  auto lines = parse(puzzle_input);

  std::vector<std::unique_ptr<TreeNode>> trees;
  for (const auto &line : lines) {
    auto tree = handle_line(line);
    trees.push_back(std::move(tree));
    std::cout << get_magnitude(trees.back().get()) << std::endl;
  }
  //auto tree3 = tree1 + tree2;
  //print(tree3.get());

  auto tree = TreeNode::copy(trees[0].get());
  for (std::size_t i = 1; i < trees.size(); ++i) {
    std::cout << "Adding" << std::endl;
    print(trees[i].get());
    auto new_tree = tree + trees[i];
    tree = std::move(new_tree);
    }
  std::cout << "Final tree: " <<std::endl;
  print(tree.get());
  std::cout << get_magnitude(tree.get()) << std::endl;
  std::vector<int> magnitudes;
  for (size_t i = 0; i < trees.size(); ++i) 
  {
    for (size_t j = i+1; j < trees.size(); ++j) {
      auto new_tree = TreeNode::copy(trees[i].get()) + TreeNode::copy(trees[j].get());
      magnitudes.push_back(get_magnitude(new_tree.get()));
    }
  }
  std::cout << *std::max_element(cbegin(magnitudes), cend(magnitudes)) << std::endl;
}