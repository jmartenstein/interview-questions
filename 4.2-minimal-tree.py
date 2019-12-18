import unittest
import anytree

class MinimalTreeTest(unittest.TestCase):

  def test_minimaltree_small1(self):
    tree = minimal_tree([1, 2, 3])
    self.assertEqual(tree.root.name, 2)
    self.assertEqual(tree.root.children[0].name, 1)
    self.assertEqual(tree.root.children[1].name, 3)
    print(anytree.RenderTree(tree, style=anytree.render.AsciiStyle()))

  def test_minimaltree_large1(self):
    tree = minimal_tree([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    self.assertEqual(tree.root.name, 16)
    self.assertEqual(tree.root.children[0].name, 13)
    print(anytree.RenderTree(tree, style=anytree.render.AsciiStyle()))

def minimal_tree(node_list):
  
  slice_index = int(len(node_list) / 2)
  
  #print("slice_index: " + str(slice_index))
  #print("list:        " + str(node_list))
  root_node = anytree.Node(node_list[slice_index])
 
  left_list = node_list[0:slice_index]
  right_list = node_list[slice_index+1:len(node_list)]

  if len(left_list) > 0:
    left_node = minimal_tree(left_list)
    left_node.parent = root_node
  if len(right_list) > 0:
    right_node = minimal_tree(right_list)
    right_node.parent = root_node

  return root_node

if __name__ == '__main__':
  unittest.main()
