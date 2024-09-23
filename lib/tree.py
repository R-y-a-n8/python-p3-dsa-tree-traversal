class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, node_id):
        return self._depth_first_search(self.root, node_id)

    def _depth_first_search(self, node, node_id):
        if node['id'] == node_id:
            return node
        for child in node['children']:
            result = self._depth_first_search(child, node_id)
            if result:
                return result
        return None
