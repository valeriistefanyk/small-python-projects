class Tank:
    def get_all_modules_for_tank(self, tank_id):
        pass

    def get_selected_modules_for_tank(self, selected_modules, tank_id):
        pass

    def get_open_modules_for_tank(self, tank_id):
        pass

class Round:
    def save_finished_round_on_tank(self, game_result, tank_id):
        pass

    def save_experience_for_tank(self, calculated_exp_result, tank_id):
        pass

class ModuleRepository:
    def delete_module(self):
        pass
    
    def add_module(self):
        pass

class Render:
    def show_all_modules_by_tank_id(self, tank_id):
        pass

    def render_selected_module(self, selected_modules, tank_id):
        pass

    def render_model_selected_tank(self, tank_id):
        pass