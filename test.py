# process data
from transfer import run_bulk2, get_default_config

# config = {
#         "alpha": 1, 
#         "content": './examples/content', 
#         'content_segment': None, 
#         "cpu": False, 
#         "image_size": 512, 
#         "option_unpool": 'cat5', 
#         "output": './outputs', 
#         "style": './examples/style', 
#         "style_segment": None, 
#         "transfer_all": False, 
#         "transfer_at_decoder": False, 
#         "transfer_at_encoder": False, 
#         "transfer_at_skip": False, 
#         "verbose": False
#     }

data_root = "./805"
config = get_default_config()
# config["transfer_all"] = True
config["transfer_at_skip"] = True
config["content"] = f"{data_root}/content"
# config["content_segment"] = f"{data_root}/content_segment"
config["style"] = f"{data_root}/style"
# config["style_segment"] = f"{data_root}/style_segment"
config["verbose"] = True
config["output"] = f"{data_root}/output"


run_bulk2(config)
