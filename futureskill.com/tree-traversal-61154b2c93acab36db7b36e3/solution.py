class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_depth_first_pre_order(self, root_node_id):
        self.api.activate_node(root_node_id)
        children = self.api.get_children(root_node_id)

        if children[0]:
            self.level_1_depth_first_pre_order(children[0])
        if children[1]:
            self.level_1_depth_first_pre_order(children[1])

    def level_2_depth_first_in_order(self, root_node_id):
        children = self.api.get_children(root_node_id)

        if children[0]:
            self.level_2_depth_first_in_order(children[0])

        self.api.activate_node(root_node_id)

        if children[1]:
            self.level_2_depth_first_in_order(children[1])

    def level_3_depth_first_post_order(self, root_node_id):
        children = self.api.get_children(root_node_id)

        if children[0]:
            self.level_3_depth_first_post_order(children[0])

        if children[1]:
            self.level_3_depth_first_post_order(children[1])

        self.api.activate_node(root_node_id)

    def level_4_breadth_first(self, root_node_id):
        current_level_nodes = [root_node_id]

        while len(current_level_nodes) > 0:
            for node_id in current_level_nodes:
                self.api.activate_node(node_id)

            current_level_nodes = [child_node for node_id in current_level_nodes for child_node in
                                   self.api.get_children(node_id) if child_node != '']
